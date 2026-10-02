"""Build a readable, monochrome XLSX and matching self-contained Markdown."""

from __future__ import annotations

import json
import math
from pathlib import Path
import re

from PIL import Image, ImageDraw, ImageFont
import xlsxwriter

from guide_content import (
    AS_OF, TITLE, SUBTITLE, SOURCES, SECTIONS, INTRO, CODE_EXAMPLES,
    CHECKLIST, DIAGRAMS, EXAMPLE_NOTES, HEAP_EXAMPLE, LOAD_EXAMPLE,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
BUILD = ROOT / ".build"
STEM = "AWS_JMeter_EAP81_Observability_Guide"
FONT = "Meiryo UI"
FONT_PATH = Path(r"C:\Windows\Fonts\meiryo.ttc")
FONT_BOLD = Path(r"C:\Windows\Fonts\meiryob.ttc")


def font(size, bold=False):
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_PATH), size, index=2)


MEASURE = font(15)


def wrap(text, width, ft=MEASURE):
    """Measure actual Meiryo UI glyph widths, including Japanese and long URLs."""
    lines = []
    for para in str(text).split("\n"):
        if not para:
            lines.append("")
            continue
        current = ""
        for char in para:
            if current and ft.getlength(current + char) > width:
                lines.append(current)
                current = char
            else:
                current += char
        lines.append(current)
    return lines or [""]


def row_height(values, widths, minimum=44):
    def cell_lines(value, width, ft):
        count = 0
        for paragraph in str(value).split("\n"):
            current = ""
            count += 1
            for token in re.findall(r"[A-Za-z0-9_.:/%=-]+|[^A-Za-z0-9_.:/%=-]", paragraph):
                if current and ft.getlength(current + token) > width:
                    count += 1
                    current = ""
                for char in token:
                    if current and ft.getlength(current + char) > width:
                        count += 1
                        current = ""
                    current += char
        return count

    count = max(cell_lines(value, width * 7 - 15, font(15, i == 0))
                for i, (value, width) in enumerate(zip(values, widths)))
    return min(390, max(minimum, count * 15.4 + 12))


def cite(refs):
    return " / ".join(f"[{key} {SOURCES[key]['title']}]({SOURCES[key]['url']})" for key in refs.split())


def markdown():
    lines = [f"# {TITLE}", "", f"**{SUBTITLE}**", "", f"公式情報確認日：{AS_OF}（日本時間）", "",
             "Excel版と本文・根拠を共通化しています。Markdownは表示アプリがフォントを決めるため、Meiryo UIの指定はExcel版へ適用しています。", "",
             "## まず答えと前提", ""]
    for label, body, refs in INTRO:
        lines += [f"**{label}**：{body}" + (f" {cite(refs)}" if refs else ""), ""]
    lines += ["## 目次", ""]
    order = [("01", "動作の図解")] + [(s["sheet"][:2], s["title"]) for s in SECTIONS]
    order += [("12", "設定・診断・検索の例"), ("18", "数値例と計算"), ("21", "実行チェックリスト"), ("22", "公式資料一覧")]
    for num, title in sorted(order):
        lines.append(f"- [{num} {title}](#chapter-{num})")
    lines += [""]

    sections = {s["sheet"][:2]: s for s in SECTIONS}
    for num, title in sorted(order):
        lines += [f'<a id="chapter-{num}"></a>', "", f"## {num} {title}", ""]
        if num == "01":
            for d in DIAGRAMS:
                lines += [f"### {d['title']}", "", d["summary"], "", "```mermaid", d["mermaid"], "```", "", cite(d["refs"]), ""]
            lines += ["Mermaid非対応の閲覧環境ではコードとして表示されます。Excel版では同じ概念を図として表示しています。", ""]
        elif num == "12":
            lines += ["設定断片と診断例です。全体のデプロイ定義ではなく、この資料作成で実行した設定でもありません。環境名・PID・path・データは例示です。", ""]
            for example in CODE_EXAMPLES:
                lines += [f"### {example['title']}", "", example["note"], "", f"```{example['language']}", example["code"], "```", "", cite(example["refs"]), ""]
        elif num == "18":
            lines += [*EXAMPLE_NOTES, "", "### ヒープの波（架空値、MiB）", "",
                      "| 分 | 安定するヒープ | 底が増えるヒープ |", "| --- | ---: | ---: |"]
            lines += [f"| {t} | {a} | {b} |" for t, a, b in HEAP_EXAMPLE]
            lines += ["", "### 段階負荷（架空値）", "", "| 予定RPS | 成功RPS | p95（ms） |", "| ---: | ---: | ---: |"]
            lines += [f"| {a} | {b} | {c} |" for a, b, c in LOAD_EXAMPLE]
            lines += ["", "### 計算の具体例", "",
                      "- Heap used=1,024MiB、max=2,048MiBなら50%。committed=1,536MiBならused/committedは約66.7%で、意味が違います。",
                      "- 60秒で成功6,000件なら成功RPSは100。試行6,100件・失敗100件なら失敗率は約1.64%。",
                      "- 同一JVMの累積GC時間が60秒で3,000ms増えたら時間率は5%。厳密な停止率とは限りません。",
                      "- task10個×datasource pool上限20接続＋他用途30接続なら、予算上は230接続。DBの許容枠と照合します。",
                      "- 定常状態で平均同時処理数≈到着率×平均処理時間。100件/秒×0.2秒=平均20件。p95を平均時間の代わりに入れません（Littleの法則による設計上の見積り）。", ""]
        elif num == "21":
            for phase, action, evidence, _ in CHECKLIST:
                lines.append(f"- [ ] **{phase}** {action}。証拠：{evidence}。")
            lines += ["", "Excel版には状態・結果・証拠の記入欄があります。初期値の『未確認』は環境試験の未実施を表します。", ""]
        elif num == "22":
            lines += ["すべて公式の一次資料です。登場当時の発表は歴史の根拠として使い、現在の仕様・料金は現行ガイドを優先しました。Web資料は後日変更されることがあります。", ""]
            for key, s in SOURCES.items():
                lines += [f"- **{key}** [{s['title']}]({s['url']}) — {s['confirms']}（確認：{s['checked']}）"]
            lines += ["", "数値例、たとえ、診断仮説、推奨する並べ方・手順は本資料の説明です。採用環境での動作検証や、原因確定を代替するものではありません。", ""]
        else:
            section = sections[num]
            lines += [section["lead"], ""]
            for row in section["rows"]:
                lines += [f"### {row[0]}", ""]
                for header, value in zip(section["headers"][1:-1], row[1:-1]):
                    lines += [f"**{header}**：{value.replace(chr(10), ' / ')}", ""]
                if row[-1]:
                    lines += [cite(row[-1]), ""]
    target = OUT / f"{STEM}.md"
    target.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    return target


def diagram_files():
    files = []

    def canvas(title, subtitle):
        im = Image.new("RGB", (1500, 860), "white")
        d = ImageDraw.Draw(im)
        d.rectangle((0, 0, 1500, 90), fill="#252525")
        d.text((32, 23), title, font=font(29, True), fill="white")
        for i, line in enumerate(wrap(subtitle, 1410, font(21))):
            d.text((35, 113 + i * 31), line, font=font(21), fill="#333333")
        return im, d

    def box(d, rect, text, shade="#eeeeee", size=24, bold=False):
        d.rounded_rectangle(rect, 12, fill=shade, outline="#555555", width=2)
        lines = wrap(text, rect[2] - rect[0] - 28, font(size, bold))
        total = len(lines) * (size + 9)
        top = (rect[1] + rect[3] - total) / 2
        for i, line in enumerate(lines):
            length = font(size, bold).getlength(line)
            d.text(((rect[0] + rect[2] - length) / 2, top + i * (size + 9)), line, font=font(size, bold), fill="#222222")

    def arrow(d, points, dashed=False):
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            distance = math.hypot(x2 - x1, y2 - y1)
            if dashed:
                for k in range(0, int(distance), 16):
                    end = min(k + 9, distance)
                    d.line((x1 + (x2 - x1) * k / distance, y1 + (y2 - y1) * k / distance,
                            x1 + (x2 - x1) * end / distance, y1 + (y2 - y1) * end / distance), fill="#777777", width=3)
            else:
                d.line((x1, y1, x2, y2), fill="#333333", width=4)
        x, y = points[-1]
        px, py = points[-2]
        angle = math.atan2(y - py, x - px)
        triangle = [(x, y), (x - 15 * math.cos(angle - .45), y - 15 * math.sin(angle - .45)),
                    (x - 15 * math.cos(angle + .45), y - 15 * math.sin(angle + .45))]
        d.polygon(triangle, fill="#555555")

    im, d = canvas("① APIの道と、監視データの道", "実線＝業務のHTTP/DB呼出し　　破線＝監視データの転送　　ALB・DBは代表構成の例")
    box(d, (35, 210, 270, 350), "JMeter\n利用者側の時計", bold=True)
    box(d, (325, 210, 550, 350), "ALB\n入口の時計", bold=True)
    box(d, (605, 190, 1030, 375), "ECS Fargate task\nEAP 8.1 / Red Hat JDK 21\nJVM内：ADOT Java agent", bold=True)
    box(d, (1090, 210, 1460, 350), "DB\nSQL・CPU・待機", bold=True)
    for x1, x2 in [(270, 325), (550, 605), (1030, 1090)]:
        arrow(d, [(x1, 280), (x2, 280)])
    box(d, (40, 545, 370, 680), "Container Insights\nCPU・外側のメモリ")
    box(d, (435, 475, 905, 570), "同じtaskのCloudWatch agent sidecar")
    box(d, (430, 670, 705, 805), "Application Signals\nAPI・heap・GC")
    box(d, (745, 670, 1030, 805), "X-Ray /\nTransaction Search")
    box(d, (1100, 545, 1460, 680), "Database Insights\nDB内部を分解")
    arrow(d, [(650, 375), (650, 415), (205, 415), (205, 545)], True)
    arrow(d, [(805, 375), (805, 475)], True)
    arrow(d, [(570, 570), (570, 670)], True)
    arrow(d, [(830, 570), (887, 670)], True)
    arrow(d, [(1275, 350), (1275, 545)], True)
    d.text((42, 740), "EAP/GCのstdout →", font=font(20), fill="#444444")
    d.text((42, 775), "CloudWatch Logs（別経路）", font=font(20), fill="#444444")
    files.append(BUILD / "diagram_architecture.png")
    im.save(files[-1])

    im, d = canvas("② ヒープは、taskメモリの一部分", "同じ『メモリ』でも数えている境界が違う。ヒープが減っても、外側が同じ割合で減るとは限らない。")
    d.rounded_rectangle((35, 195, 1465, 730), 20, fill="#f6f6f6", outline="#333333", width=3)
    d.text((60, 215), "Fargate task：ECS / Container Insightsで外側を観測", font=font(27, True), fill="#222222")
    d.rounded_rectangle((60, 278, 1070, 690), 16, fill="white", outline="#777777", width=2)
    d.text((83, 297), "EAPコンテナ内のJVM process", font=font(26, True), fill="#222222")
    box(d, (85, 370, 595, 650), "Heap（オブジェクトの机）\nused：いま使用中\ncommitted：確保済み\nmax：最大まで広げる上限", size=27)
    box(d, (625, 370, 1038, 487), "Non-heap\nMetaspace / Code Cache等", size=24)
    box(d, (625, 517, 1038, 650), "その他のnative領域\nstack / direct buffer等", size=24)
    box(d, (1110, 332, 1420, 644), "監視sidecar\n\n収集・加工・送信\n\nここにも\nCPUとRAMが必要", size=25)
    d.text((45, 766), "heap used → Application Signals　｜　max / committed / EAP内部 → JMX等で補完", font=font(26, True), fill="#222222")
    d.text((45, 814), "図は概念図。RSS・予約・cacheの扱いが違うため、各数字を単純に足し引きして原因を断定しない。", font=font(21), fill="#444444")
    files.append(BUILD / "diagram_memory.png")
    im.save(files[-1])

    im, d = canvas("③ 時計の範囲と、親子spanの重なり", "すべて架空の数値。直列に進む1件を単純化した例。Elapsedの内訳にEAP spanとJDBC spanが含まれる。")
    x0, scale = 325, 1.78
    rows = [
        ("JMeter Elapsed", 0, 600, 225, "全体 600ms", "#363636", "white"),
        ("EAP server span", 50, 590, 350, "EAP内 540ms", "#7b7b7b", "white"),
        ("接続pool待ち", 90, 190, 475, "100ms", "#b5b5b5", "#111111"),
        ("JDBC client span", 190, 550, 585, "360ms", "#d6d6d6", "#111111"),
    ]
    for label, start, end, y, caption, fill, fg in rows:
        d.text((30, y + 15), label, font=font(25, True), fill="#222222")
        rect = (x0 + start * scale, y, x0 + end * scale, y + 70)
        d.rectangle(rect, fill=fill, outline="#444444", width=2)
        d.text(((rect[0] + rect[2] - font(24).getlength(caption)) / 2, y + 17), caption, font=font(24), fill=fg)
    for t in range(0, 601, 100):
        x = x0 + t * scale
        d.line((x, 190, x, 205), fill="#555555", width=2)
        d.text((x - 16, 155), str(t), font=font(20), fill="#444444")
    d.text((1350, 190), "ms", font=font(21), fill="#444444")
    d.text((42, 715), "600 + 540 + 360 と足すと二重計上。親spanの中に子spanが入っている。", font=font(27, True), fill="#222222")
    d.text((42, 770), "JDBCが長い → Database InsightsでDB内の待ちへ。pool待ちはEAPの統計で補う。", font=font(25), fill="#333333")
    d.text((42, 816), "ALB TargetResponseTimeは応答ヘッダー開始まで。JMeter Elapsedは本文完了まで。", font=font(23), fill="#444444")
    files.append(BUILD / "diagram_trace.png")
    im.save(files[-1])
    return files


def build_xlsx(diagrams):
    target = OUT / f"{STEM}.xlsx"
    book = xlsxwriter.Workbook(target, {"strings_to_urls": False, "strings_to_formulas": False})
    book.formats[0].set_font_name(FONT)
    book.formats[0].set_font_size(11)
    book.set_properties({"title": TITLE, "subject": SUBTITLE, "author": "Technical Documentation",
                         "comments": f"Official sources checked {AS_OF}. Illustrative values are not test results."})
    base = dict(font_name=FONT, font_size=11, font_color="#222222", valign="top", text_wrap=True)
    f_title = book.add_format({**base, "bold": True, "font_size": 22, "bg_color": "#252525", "font_color": "#FFFFFF", "valign": "vcenter"})
    f_sub = book.add_format({**base, "font_size": 10, "bg_color": "#EEEEEE", "valign": "vcenter"})
    f_lead = book.add_format({**base, "font_size": 11, "bg_color": "#F6F6F6"})
    f_head = book.add_format({**base, "bg_color": "#4B4B4B", "font_color": "#FFFFFF", "bold": True, "valign": "vcenter", "border": 1, "border_color": "#DDDDDD"})
    f_link = book.add_format({**base, "underline": 1, "font_color": "#333333", "font_size": 10})
    body_formats = {}
    for alternate in (0, 1):
        for bold in (False, True):
            body_formats[alternate, bold] = book.add_format({**base, "bold": bold, "bg_color": "#FFFFFF" if alternate == 0 else "#F1F1F1", "border": 1, "border_color": "#D8D8D8"})
    f_code = book.add_format({**base, "font_size": 10, "bg_color": "#F3F3F3", "border": 1, "border_color": "#D8D8D8"})
    f_input = book.add_format({**base, "font_size": 12, "bg_color": "#E0E0E0", "border": 2, "border_color": "#555555", "align": "right", "num_format": "0.0"})
    f_number = book.add_format({**base, "num_format": "0.0", "align": "right", "border": 1, "border_color": "#DDDDDD"})
    f_percent = book.add_format({**base, "num_format": "0.0%", "align": "right", "bold": True, "border": 1, "border_color": "#BBBBBB"})
    f_out = book.add_format({**base, "num_format": "0.0", "align": "right", "bold": True, "border": 1, "border_color": "#BBBBBB"})

    all_titles = {s["sheet"]: s["title"] for s in SECTIONS}
    all_titles.update({"00_案内": "最初の答え・前提・目次", "01_図解": "動作を図で理解する", "12_設定例": "設定・診断・検索の例", "18_例と計算": "架空のグラフと計算", "21_実行チェック": "実行チェックリスト", "22_出典": "公式資料一覧"})
    sheets = {name: book.add_worksheet(name) for name in sorted(all_titles)}
    source_rows = {key: 5 + i for i, key in enumerate(SOURCES)}
    layout = {}

    def init(ws, title, lead, widths):
        ws.hide_gridlines(2)
        ws.set_zoom(85)
        ws.set_tab_color("#777777")
        for col, width in enumerate(widths):
            ws.set_column(col, col, width, body_formats[0, False])
        ws.set_default_row(22)
        ws.merge_range(0, 0, 0, len(widths)-1, title, f_title)
        ws.set_row(0, 47)
        ws.merge_range(1, 0, 1, len(widths)-1, f"{SUBTITLE}  |  公式情報確認 {AS_OF}  |  数値例は架空", f_sub)
        ws.set_row(1, 25)
        ws.merge_range(2, 0, 2, len(widths)-1, lead, f_lead)
        ws.set_row(2, max(48, row_height([lead], [sum(widths)], 48)))
        ws.write_url(3, 0, "internal:'00_案内'!A1", f_link, "← 目次")
        ws.set_row(3, 23)
        ws.freeze_panes(5, 1)
        ws.set_landscape()
        ws.set_paper(8)  # A3: dense technical tables remain readable in print.
        ws.fit_to_pages(1, 0)
        ws.set_margins(.28, .28, .40, .40)
        ws.repeat_rows(0, 4)
        ws.set_header(f'&L&"{FONT},Regular"&9 AWS / JMeter / EAP 8.1 &R{AS_OF}')
        ws.set_footer(f'&L&"{FONT},Regular"&8 公式資料の確認日を基準に記述　&R&P / &N')

    def references(ws, row, col, refs, style):
        if not refs:
            ws.write_string(row, col, "説明・設計例", style)
            return
        first = refs.split()[0]
        ws.write_url(row, col, f"internal:'22_出典'!A{source_rows[first] + 1}", style, refs)
        ws.write_comment(row, col, "\n\n".join(f"{key} {SOURCES[key]['title']}\n{SOURCES[key]['url']}" for key in refs.split()), {"font_name": FONT, "font_size": 10, "width": 480, "height": 220, "author": "公式資料"})

    def table(section):
        ws = sheets[section["sheet"]]
        widths = section["widths"]
        init(ws, section["title"], section["lead"], widths)
        for c, header in enumerate(section["headers"]):
            ws.write_string(4, c, header, f_head)
        ws.set_row(4, 35)
        for r, values in enumerate(section["rows"], 5):
            ws.set_row(r, row_height(values, widths))
            for c, value in enumerate(values):
                style = body_formats[(r-5) % 2, c == 0]
                if c == len(values)-1:
                    references(ws, r, c, value, style)
                else:
                    ws.write_string(r, c, value, style)
        last = 4 + len(section["rows"])
        ws.autofilter(4, 0, last, len(widths)-1)
        ws.print_area(0, 0, last, len(widths)-1)
        layout[section["sheet"]] = {"rows": last + 1, "cols": len(widths), "kind": "table"}

    for section in SECTIONS:
        table(section)

    ws = sheets["00_案内"]
    widths = [30, 102, 15]
    init(ws, TITLE, "JMeterで結果を測り、AWSで理由を探す。とくに『container全体のメモリ』と『JVMのheap』の違いを、図と手順から理解する。", widths)
    ws.freeze_panes(5, 0)
    ws.set_row(0, 58)
    for c, h in enumerate(["読み始める場所", "結論・対象・使い方", "根拠"]):
        ws.write(4, c, h, f_head)
    for r, (label, body, refs) in enumerate(INTRO, 5):
        ws.set_row(r, row_height([label, body, refs], widths, 60))
        ws.write(r, 0, label, body_formats[(r-5) % 2, True])
        ws.write(r, 1, body, body_formats[(r-5) % 2, False])
        references(ws, r, 2, refs, body_formats[(r-5) % 2, False])
    r = 6 + len(INTRO)
    ws.merge_range(r, 0, r, 2, "クリックして移動する目次", f_head)
    r += 1
    for name, title in sorted(all_titles.items()):
        if name == "00_案内":
            continue
        ws.set_row(r, 33)
        ws.write_url(r, 0, f"internal:'{name}'!A1", f_link, name)
        ws.write(r, 1, title, body_formats[r % 2, False])
        ws.write(r, 2, "クリック", body_formats[r % 2, False])
        r += 1
    ws.print_area(0, 0, r-1, 2)
    ws.set_first_sheet()
    ws.activate()

    ws = sheets["01_図解"]
    widths = [26] * 6
    init(ws, "API・JVM・監視の動作イメージ", "3枚の図を上から読む。実環境の構成や実測結果ではなく、理解のための概念図。用語の正確な意味は各章で説明する。", widths)
    ws.freeze_panes(4, 0)
    for i, (path, dg) in enumerate(zip(diagrams, DIAGRAMS)):
        r = 5 + i * 35
        for rr in range(r, r+29):
            ws.set_row(rr, 18)
        ws.insert_image(r, 0, str(path), {"x_scale": .72, "y_scale": .72, "description": dg["summary"], "object_position": 1})
        ws.merge_range(r+30, 0, r+32, 4, dg["summary"], f_lead)
        references(ws, r+30, 5, dg["refs"], f_link)
    ws.set_h_pagebreaks([40, 75])
    ws.print_area(0, 0, 107, 5)

    ws = sheets["12_設定例"]
    widths = [30, 31, 31, 31, 30]
    init(ws, "設定・診断・検索の例", "以下は説明用の断片であり、デプロイ用の完成定義ではない。読み取り・設定変更・診断採取を区別する。実際のAWS環境では未実行。", widths)
    ws.freeze_panes(4, 0)
    r = 5
    for ex in CODE_EXAMPLES:
        ws.merge_range(r, 0, r, 4, ex["title"], f_head)
        ws.set_row(r, 32)
        r += 1
        ws.merge_range(r, 0, r, 4, ex["note"], f_lead)
        ws.set_row(r, row_height([ex["note"]], [sum(widths)], 55))
        r += 1
        for line in ex["code"].split("\n"):
            ws.merge_range(r, 0, r, 4, line or " ", f_code)
            ws.set_row(r, row_height([line], [sum(widths)], 23))
            r += 1
        references(ws, r, 0, ex["refs"], f_link)
        ws.set_row(r, 33)
        r += 2
    ws.print_area(0, 0, r-1, 4)

    ws = sheets["18_例と計算"]
    widths = [25, 19, 20, 22, 26, 21, 23]
    init(ws, "架空の数値でグラフと計算を学ぶ", EXAMPLE_NOTES[0], widths)
    ws.freeze_panes(5, 0)
    ws.merge_range(4, 0, 4, 6, "入力欄＝グレー＋太枠　計算結果＝白　／　比率は同一JVM・同一時刻で計算", f_head)
    entries = [
        (5, "Heap Used（MiB）", 1024, "Heap Max（MiB）", 2048, "heap used / max", "=IF(AND(D6>0,B6>=0,B6<=D6),B6/D6,NA())", .5, True),
        (6, "Heap Used（MiB）", 1024, "Committed（MiB）", 1536, "used / committed", "=IF(AND(D7>0,B7>=0,B7<=D7),B7/D7,NA())", 2/3, True),
        (7, "GC累積の増分（ms）", 3000, "期間（秒）", 60, "GC時間率（STWとは別）", "=IF(AND(D8>0,B8>=0),B8/(D8*1000),NA())", .05, True),
        (8, "成功件数", 6000, "期間（秒）", 60, "成功RPS", "=IF(AND(D9>0,B9>=0),B9/D9,NA())", 100, False),
        (9, "失敗件数", 100, "試行件数", 6100, "失敗率", "=IF(AND(D10>0,B10>=0,B10<=D10),B10/D10,NA())", 100/6100, True),
        (10, "最大task数", 10, "1taskのpool上限", 20, "EAPの最大接続予算", "=IF(AND(B11>=0,D11>=0),B11*D11,NA())", 200, False),
        (11, "到着率（件/秒）", 100, "平均時間（秒）", .2, "平均同時処理（定常）", "=IF(AND(B12>=0,D12>=0),B12*D12,NA())", 20, False),
    ]
    for rr, a, av, b, bv, caption, formula, result, pct in entries:
        ws.set_row(rr, 49)
        ws.write(rr, 0, a, body_formats[rr % 2, True])
        ws.write_number(rr, 1, av, f_input)
        ws.write(rr, 2, b, body_formats[rr % 2, True])
        ws.write_number(rr, 3, bv, f_input)
        ws.write(rr, 4, caption, body_formats[rr % 2, True])
        ws.write_formula(rr, 5, formula, f_percent if pct else f_out, result)
        ws.write(rr, 6, "架空の入力例", body_formats[rr % 2, False])
        for cc in (1, 3):
            ws.data_validation(rr, cc, rr, cc, {"validate": "decimal", "criteria": ">=", "value": 0, "input_title": "説明用の入力", "input_message": "同一範囲・同一単位の値を入力してください。", "error_title": "0以上の数値", "error_message": "0以上の数値を入力してください。", "error_type": "stop"})
    ws.merge_range(13, 0, 13, 6, "接続予算の例：EAP 200接続 ＋ 他用途30接続 ＝ 230接続。DBの許容枠と比較。Littleの法則は平均値・定常状態の見積りで、p95からは計算しない。", f_lead)
    ws.set_row(13, 53)
    ws.merge_range(15, 0, 15, 6, "A. heapの鋸歯状と、回収後の底上がり（すべて架空値）", f_head)
    ws.set_row(15, 33)
    for c, h in enumerate(["時刻（分）", "安定（MiB）", "底上がり（MiB）"]):
        ws.write(16, c, h, f_head)
    for r, values in enumerate(HEAP_EXAMPLE, 17):
        ws.set_row(r, 25)
        for c, value in enumerate(values):
            ws.write_number(r, c, value, f_number)
    chart = book.add_chart({"type": "line"})
    for c, color, dash in [(1, "#222222", "solid"), (2, "#858585", "dash")]:
        chart.add_series({"name": [ws.name, 16, c], "categories": [ws.name, 17, 0, 32, 0], "values": [ws.name, 17, c, 32, c], "line": {"color": color, "width": 2.2, "dash_type": dash}})
    chart.set_title({"name": "heapの波：架空例", "name_font": {"name": FONT, "size": 13}})
    chart.set_x_axis({"name": "経過（分）", "num_font": {"name": FONT}, "name_font": {"name": FONT}})
    chart.set_y_axis({"name": "Heap Used（MiB）", "min": 0, "num_font": {"name": FONT}, "name_font": {"name": FONT}, "major_gridlines": {"visible": True, "line": {"color": "#DDDDDD"}}})
    chart.set_legend({"position": "bottom", "font": {"name": FONT, "size": 10}})
    chart.set_chartarea({"border": {"none": True}, "fill": {"color": "#FFFFFF"}})
    chart.set_size({"width": 630, "height": 390})
    ws.insert_chart(16, 3, chart)
    ws.merge_range(34, 0, 34, 6, EXAMPLE_NOTES[1], f_lead)
    ws.set_row(34, 48)
    ws.merge_range(36, 0, 36, 6, "B. 負荷を増やしたときの遅延（すべて架空値）", f_head)
    for c, h in enumerate(["予定RPS", "成功RPS", "p95（ms）"]):
        ws.write(37, c, h, f_head)
    for r, values in enumerate(LOAD_EXAMPLE, 38):
        ws.set_row(r, 38)
        for c, value in enumerate(values):
            ws.write_number(r, c, value, f_number)
    chart = book.add_chart({"type": "scatter", "subtype": "straight_with_markers"})
    chart.add_series({"name": "p95（架空例）", "categories": [ws.name, 38, 0, 44, 0], "values": [ws.name, 38, 2, 44, 2], "line": {"color": "#333333", "width": 2}, "marker": {"type": "circle", "size": 5, "fill": {"color": "#333333"}, "border": {"color": "#333333"}}})
    chart.set_title({"name": "負荷とp95：架空例", "name_font": {"name": FONT, "size": 13}})
    chart.set_x_axis({"name": "予定RPS", "min": 0, "num_font": {"name": FONT}, "name_font": {"name": FONT}})
    chart.set_y_axis({"name": "p95（ms）", "min": 0, "num_font": {"name": FONT}, "name_font": {"name": FONT}, "major_gridlines": {"visible": True, "line": {"color": "#DDDDDD"}}})
    chart.set_legend({"none": True})
    chart.set_chartarea({"border": {"none": True}, "fill": {"color": "#FFFFFF"}})
    chart.set_size({"width": 630, "height": 360})
    ws.insert_chart(37, 3, chart)
    ws.merge_range(49, 0, 49, 6, EXAMPLE_NOTES[2], f_lead)
    ws.set_row(49, 50)
    ws.set_h_pagebreaks([15, 36])
    ws.print_area(0, 0, 49, 6)

    ws = sheets["21_実行チェック"]
    widths = [15, 50, 39, 15, 52]
    init(ws, "実行前後の確認・結果記入", "資料に記載した設定例は未実行。各行の状態と、実際の結果・証拠を記入して使用する。ドロップダウンは色だけに頼らず状態名で区別する。", widths)
    for c, h in enumerate(["区分", "確認項目", "証拠の例", "状態（入力）", "結果・証拠・担当（入力）"]):
        ws.write(4, c, h, f_head)
    for r, (phase, action, evidence, _) in enumerate(CHECKLIST, 5):
        ws.set_row(r, row_height([phase, action, evidence, "未確認", ""], widths, 65))
        for c, value in enumerate([phase, action, evidence, "未確認", ""]):
            ws.write(r, c, value, body_formats[(r-5) % 2, c == 0])
        ws.data_validation(r, 3, r, 3, {"validate": "list", "source": ["未確認", "確認済", "要対応", "対象外"], "error_type": "stop"})
    ws.autofilter(4, 0, len(CHECKLIST)+4, 4)
    ws.print_area(0, 0, len(CHECKLIST)+4, 4)

    ws = sheets["22_出典"]
    widths = [10, 37, 48, 63, 16]
    init(ws, "公式資料と確認対象", "一次資料83件。各行のURLから原文へ移動する。現在仕様には現行ガイド、登場年月には当時の公式発表を使用。Web資料は確認後に変更される場合がある。", widths)
    for c, h in enumerate(["ID", "公式資料", "確認した事項", "公式URL", "確認日"]):
        ws.write(4, c, h, f_head)
    for r, (key, s) in enumerate(SOURCES.items(), 5):
        values = [key, s["title"], s["confirms"], s["url"], s["checked"]]
        ws.set_row(r, row_height(values, widths, 64))
        for c, value in enumerate(values):
            style = body_formats[(r-5) % 2, c == 0]
            if c == 3:
                ws.write_url(r, c, value, style, value)
            else:
                ws.write_string(r, c, value, style)
    ws.autofilter(4, 0, len(SOURCES)+4, 4)
    ws.print_area(0, 0, len(SOURCES)+4, 4)
    book.close()
    (BUILD / "layout.json").write_text(json.dumps(layout, ensure_ascii=False, indent=2), encoding="utf-8")
    return target


def main():
    OUT.mkdir(exist_ok=True)
    BUILD.mkdir(exist_ok=True)
    used = set()
    for section in SECTIONS:
        for row in section["rows"]:
            used.update(row[-1].split())
    for _, _, refs in INTRO:
        used.update(refs.split())
    for ex in CODE_EXAMPLES:
        used.update(ex["refs"].split())
        if ex["language"] == "json":
            json.loads(ex["code"])
    assert used <= SOURCES.keys(), used - SOURCES.keys()
    md = markdown()
    xlsx = build_xlsx(diagram_files())
    print(json.dumps({"markdown": str(md), "xlsx": str(xlsx), "source_count": len(SOURCES),
                      "content_rows": sum(len(s["rows"]) for s in SECTIONS), "code_examples": len(CODE_EXAMPLES),
                      "md_characters": len(md.read_text(encoding="utf-8"))}, ensure_ascii=False))


if __name__ == "__main__":
    main()

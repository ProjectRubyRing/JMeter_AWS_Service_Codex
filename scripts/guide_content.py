"""Source-backed Japanese content shared by the XLSX and Markdown deliverables."""

AS_OF = "2026-10-02"
TITLE = "JMeter × AWS 全体パフォーマンステスト 監視・分析ガイド"
SUBTITLE = "ECS Fargate / JBoss EAP 8.1 / Red Hat build of OpenJDK 21"
CW = "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/"
ECS = "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/"
ALB = "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/"
RDS = "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/"
EAP = "https://docs.redhat.com/en/documentation/red_hat_jboss_enterprise_application_platform/8.1/html/"
JDK = "https://docs.oracle.com/en/java/javase/21/"
WHATS = "https://aws.amazon.com/about-aws/whats-new/"
SOURCES = {}


def source(key, title, url, confirms):
    SOURCES[key] = dict(title=title, url=url, confirms=confirms, checked=AS_OF)


source("S01", "Application Signalsの収集指標", CW + "AppSignals-MetricsCollected.html", "JVM指標の正式名・単位・次元、既知問題、Fault/Errorの定義")
source("S02", "Application SignalsをECSで有効化", CW + "CloudWatch-Application-Signals-Enable-ECSMain.html", "Fargateはsidecar方式。ECSではサービス名を設定")
source("S03", "Application Signalsのsidecar設定", CW + "CloudWatch-Application-Signals-ECS-Sidecar.html", "Java agent、CloudWatch agent、環境変数、IAM、4316の経路")
source("S04", "Application Signals対応システム", CW + "CloudWatch-Application-Signals-supportmatrix.html", "Java対応はADOTと対応ライブラリに依存")
source("S05", "ECS Enhanced Container Insights指標", CW + "Container-Insights-enhanced-observability-metrics-ECS.html", "タスク・コンテナ指標、TaskId次元、RestartCountの条件")
source("S06", "ECSのCloudWatch監視", ECS + "cloudwatch-metrics.html", "Fargateサービスの標準CPU・メモリ指標")
source("S07", "ECSサービス使用率と高解像度指標", ECS + "service_utilization.html", "使用率の母数、標準60秒、選択可能な20秒")
source("S08", "Container Insightsの設定", CW + "deploy-container-insights-ECS-cluster.html", "クラスター設定enabled/enhanced")
source("S09", "Container InsightsのECS概要", ECS + "cloudwatch-container-insights.html", "2024年12月2日の拡張版、性能ログからの集計")
source("S10", "ALBのCloudWatch指標", ALB + "load-balancer-cloudwatch-metrics.html", "ALB指標名、集計、TargetResponseTimeの計測区間")
source("S11", "ALBアクセスログ", ALB + "load-balancer-access-logs.html", "処理時間の3区間、WAF/POSTの扱い、best effortの性質")
source("S12", "ALBのリクエスト追跡", ALB + "load-balancer-request-tracing.html", "X-Amzn-Trace-Idの付与・更新")
source("S13", "ALBのCloudWatch Logs連携", ALB + "load-balancer-cloudwatch-logs.html", "access/connection/health checkログの配信経路")
source("S14", "REST API Gateway指標", "https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html", "Latency/IntegrationLatency、4XXError/5XXError、Countの統計")
source("S15", "HTTP API Gateway指標", "https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-metrics.html", "HTTP APIの4xx/5xxと詳細指標")
source("S16", "API Gateway REST APIのX-Ray", "https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-xray.html", "REST APIのactive tracing")
source("S17", "RDSのCloudWatch指標", RDS + "rds-metrics.html", "CPU、接続、メモリ、I/O、クレジットの定義")
source("S18", "AuroraのCloudWatch指標", "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html", "Auroraのレプリカ遅延・Serverless指標")
source("S19", "CloudWatch Database Insights", CW + "Database-Insights.html", "2026年のPerformance Insights移行、現行モード・保持期間")
source("S20", "Database Insightsインスタンス画面", CW + "Database-Insights-Database-Instance-Dashboard.html", "DB Load、SQL、待機の診断")
source("S21", "RDS Enhanced Monitoring", RDS + "USER_Monitoring.OS.html", "DBのOS内部を監視。ECS上のJavaとは別")
source("S22", "Database Insightsと従来API", RDS + "USER_PerfInsights.html", "DB待機分類とPerformance Insights API文書の継続")
source("S23", "RDS Proxyの指標", RDS + "rds-proxy.monitoring.html", "接続借用待ちとDB接続の指標")
source("S24", "ElastiCache Valkey/Redis OSS指標", "https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.Redis.html", "ノード型キャッシュのエンジンCPU、メモリ、退避")
source("S25", "CloudFrontの指標", "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/programming-cloudwatch-metrics.html", "us-east-1、追加指標、OriginLatency")
source("S26", "WAFの指標", "https://docs.aws.amazon.com/waf/latest/developerguide/waf-metrics.html", "AWS/WAFV2、許可・遮断の件数")
source("S27", "NAT Gatewayの指標", "https://docs.aws.amazon.com/vpc/latest/userguide/metrics-dimensions-nat-gateway.html", "ポート割当失敗、接続、破棄")
source("S28", "SQSの指標", "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html", "最古メッセージ経過時間、近似キュー件数")
source("S29", "Lambdaの指標", "https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html", "Duration、Errors、Throttles、同時実行")
source("S30", "DynamoDBの指標", "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html", "成功時遅延、容量、スロットリング")
source("S31", "S3の指標", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/metrics-dimensions.html", "有効化が必要なリクエスト指標")
source("S32", "EFSの指標", "https://docs.aws.amazon.com/efs/latest/ug/efs-metrics.html", "PercentIOLimit、スループット、適用条件")
source("S33", "CloudWatchのメトリクス概念", CW + "cloudwatch_concepts.html", "名前空間・次元・統計・期間・保持")
source("S34", "CloudWatch Logs Insights", "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html", "ログ検索の役割・費用の考え方")
source("S35", "Logs Insightsのstats", "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Stats.html", "bin、avg、pct等の集計構文")
source("S36", "CloudWatch Transaction Search", CW + "CloudWatch-Transaction-Search.html", "受信spanのログ保存、aws/spans、トレース索引")
source("S37", "Transaction Searchの有効化", CW + "Enable-TransactionSearch.html", "保存先設定・権限・索引割合")
source("S38", "X-Ray SDK/daemonのサポート日程", "https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html", "2026-02-25からメンテナンスモード。現行表の終了日はN/A")
source("S39", "X-RayからOpenTelemetryへの移行", "https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-migration.html", "計装をOpenTelemetryへ移行する推奨")
source("S40", "OpenTelemetry Java対応ライブラリ", "https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md", "WildFly/OpenJDK21、JDBC、既定無効のjdbc-datasource等")
source("S41", "CloudWatch agentのJMX収集", CW + "CloudWatch-Agent-JMX-metrics.html", "jvm.memory.heap.*。公式手順はEC2/EKS向け")
source("S42", "ECSのPrometheus収集", CW + "ContainerInsights-Prometheus-Setup-ECS.html", "Fargate awsvpcでのPrometheus収集経路")
source("S43", "ECSからAMPへのアプリ指標送信", ECS + "application-metrics-prometheus.html", "ADOT Collector、remote_write、タスクロール")
source("S44", "Prometheus JMX Exporter Java agent", "https://prometheus.github.io/jmx_exporter/deployment/java-agent/", "同一JVM内のMBean収集、bindアドレス指定")
source("S45", "EAP 8のサポート構成", "https://access.redhat.com/articles/6961381", "EAP 8.1とRed Hat build of OpenJDK 21。OS等の条件も必要")
source("S46", "EAP 8.1の対応構成・コンテナ", EAP + "release_notes_for_red_hat_jboss_enterprise_application_platform_8.1/supported-configurations-rn_assembly-release-notes", "OpenJDK21/RHEL9イメージ。Fargateの認定を意味しない")
source("S47", "EAP 8.1の性能監視", EAP + "performance_tuning_for_red_hat_jboss_enterprise_application_platform/assembly-monitoring-performance_performance-tuning-guide", "JMX、JConsole等のJVM監視")
source("S48", "EAP 8.1のJVMチューニング", EAP + "performance_tuning_for_red_hat_jboss_enterprise_application_platform/assembly-jvm-tuning_performance-tuning-guide", "ヒープ、GCログ、heap dump")
source("S49", "EAP 8.1の接続プール", EAP + "performance_tuning_for_red_hat_jboss_enterprise_application_platform/assembly-datasource-resource-adapter-tuning_performance-tuning-guide", "統計の事前有効化とプール容量設計")
source("S50", "EAP 8.1の管理属性リファレンス", EAP + "configuration_guide/reference_material", "InUseCount、ActiveCount、worker queue等の定義")
source("S51", "EAP 8.1のdatasource管理", EAP + "configuration_guide/datasource_management", "管理CLIの読み取りとstatistics-enabled")
source("S52", "EAP XP 6のMicroProfile", EAP + "using_jboss_eap_xp_6.0/understand_microprofile", "XPの条件、MicroProfile Metricsをそのまま前提にしない")
source("S53", "Java 21 MemoryUsage", JDK + "docs/api/java.management/java/lang/management/MemoryUsage.html", "used/committed/max/init、max=-1")
source("S54", "Java 21 MemoryMXBean", JDK + "docs/api/java.management/java/lang/management/MemoryMXBean.html", "ヒープとnon-heapの境界")
source("S55", "Java 21 ThreadMXBean", JDK + "docs/api/java.management/java/lang/management/ThreadMXBean.html", "platform threadとvirtual threadの監視範囲")
source("S56", "Java 21 jcmd", JDK + "docs/specs/man/jcmd.html", "VM.flags、GC.heap_info、JFR、thread dump、heap dump")
source("S57", "Java 21 Native Memory Tracking", JDK + "vm/native-memory-tracking.html", "起動時設定、対象範囲、負荷")
source("S58", "Red Hat build of OpenJDK 21の配布", "https://docs.redhat.com/en/documentation/red_hat_build_of_openjdk/21/html/getting_started_with_red_hat_build_of_openjdk_21/openjdk-distribution-selection", "JFR/JMCによる診断")
source("S59", "JMeter用語集", "https://jmeter.apache.org/usermanual/glossary.html", "Elapsed/Latency/Connect Time/Throughputの境界")
source("S60", "JMeter Best Practices", "https://jmeter.apache.org/usermanual/best-practices.html", "非GUI実行、Listener負荷、計測器側の制約")
source("S61", "ECS Exec", ECS + "ecs-exec.html", "診断コマンドの実行条件、IAM、SSM、コンテナ")
source("S62", "ECSのawslogs", ECS + "using_awslogs.html", "stdout/stderrをCloudWatch Logsへ送信")
source("S63", "CloudWatch Embedded Metric Format", CW + "CloudWatch_Embedded_Metric_Format.html", "ログからカスタム指標を抽出。高cardinalityと重複への注意")
source("S64", "CloudWatch料金", "https://aws.amazon.com/cloudwatch/pricing/", "地域・使用量別料金。資料では単価を固定しない")
source("S65", "CloudWatch登場の公式発表", "https://aws.amazon.com/blogs/aws/new-aws-load-balancing-automatic-scaling-and-cloud-monitoring-services/", "2009年5月の登場背景のみ参照")
source("S66", "CloudWatch Logsの登場", WHATS + "2014/07/10/introducing-amazon-cloudwatch-logs/", "2014-07-10")
source("S67", "X-Ray一般提供", WHATS + "2017/04/aws-x-ray-now-generally-available/", "2017-04-19")
source("S68", "Fargateの登場", WHATS + "2017/11/introducing-aws-fargate-a-technology-to-run-containers-without-managing-infrastructure/", "2017-11-29")
source("S69", "統合CloudWatch agentの登場", WHATS + "2017/12/amazon-cloudwatch-introduces-a-new-cloudwatch-agent-with-aws-systems-manager-integration-for-unified-metrics-and-logs-collection/", "2017-12-14")
source("S70", "Logs Insights一般提供", WHATS + "2018/11/announcing-amazon-cloudwatch-logs-insights-fast-interactive-log-analytics/", "2018-11-27")
source("S71", "Container Insights一般提供", WHATS + "2019/08/container-monitoring-for-amazon-ecs-eks-and-kubernetes-is-now-available-in-amazon-cloudwatch/", "2019-08-30")
source("S72", "OpenTelemetryの誕生", "https://www.cncf.io/blog/2019/05/21/a-brief-history-of-opentelemetry-so-far/", "2019年のOpenTracingとOpenCensus統合")
source("S73", "Synthetics一般提供", WHATS + "2020/04/amazon-cloudwatch-synthetics-generally-available/", "2020-04-23")
source("S74", "ADOTプレビュー", WHATS + "2020/10/announcing-aws-distro-for-opentelemetry-in-preview/", "2020-10-21")
source("S75", "Managed Grafana一般提供", "https://aws.amazon.com/blogs/aws/amazon-managed-grafana-is-now-generally-available-with-many-new-features/", "2021-08-31")
source("S76", "AMP一般提供", "https://press.aboutamazon.com/2021/9/aws-announces-general-availability-of-amazon-managed-service-for-prometheus", "2021-09-29")
source("S77", "CloudWatch RUMの登場", "https://aws.amazon.com/blogs/aws/cloudwatch-rum/", "2021-11-29")
source("S78", "Application Signals一般提供", WHATS + "2024/06/amazon-cloudwatch-application-signals-application-monitoring/", "2024-06-10")
source("S79", "Transaction Search一般提供", WHATS + "2024/11/amazon-cloudwatch-visibility-application-transactions/", "2024-11-21")
source("S80", "Database Insights一般提供", WHATS + "2024/12/amazon-cloudwatch-database-insights/", "2024-12-01")
source("S81", "ECSの20秒指標の発表", WHATS + "2026/06/amazon-ecs-faster-autoscaling/", "2026-06-18。従来60秒との違い")
source("S82", "ALBログのCloudWatch連携の発表", WHATS + "2026/07/amazon-cloudwatch-logs/", "2026-07-23。S3限定という旧説明を更新")
source("S83", "OpenTelemetryのCNCF Graduation", "https://www.cncf.io/announcements/2026/05/21/cloud-native-computing-foundation-announces-opentelemetrys-graduation-solidifying-status-as-the-de-facto-observability-standard/", "2026-05-21。歴史の補足")

SECTIONS = []


def chapter(sheet, title, lead, headers, widths, rows, kind="cards"):
    assert len(headers) == len(widths)
    assert all(len(row) == len(headers) for row in rows), sheet
    SECTIONS.append(dict(sheet=sheet, title=title, lead=lead, headers=headers,
                         widths=widths, rows=rows, kind=kind))


CARD_HEADERS = ["テーマ", "やさしく理解", "動作原理・正確な意味", "テストでの使い方・注意", "根拠"]
CARD_WIDTHS = [25, 37, 49, 47, 12]
METRIC_HEADERS = ["対象・優先度", "名前空間 / 正式指標名", "単位・統計の選び方", "何がわかるか", "読み方・収集条件", "根拠"]
METRIC_WIDTHS = [21, 39, 25, 39, 45, 12]

INTRO = [
    ("今回の前提", "ユーザー指定：JBoss EAP 8.1、Red Hat build of OpenJDK 21、ECS Fargate。Linuxコンテナを説明例にする。ALB・DB・キャッシュ等の採用状況は未指定なので、利用時のみ読む項目とする。", "S45 S46"),
    ("最初の答え", "コンテナ全体はCloudWatchのAWS/ECSとECS/ContainerInsights。JVMヒープ・GC・スレッドは、計装を追加したApplication Signals（ApplicationSignals名前空間）が第一候補。Xmx・committed・EAPの接続プールなど不足する指標はJMX等で補う。", "S01 S05 S06 S53"),
    ("大切な区別", "FargateのMemoryUtilizationはJVMヒープ使用率ではない。部屋全体の荷物の量と、その部屋に置かれた机の上の量は違う。JVM外・ヒープ外・監視用コンテナにもメモリが必要。", "S05 S53 S54"),
    ("何を組み合わせるか", "JMeterで利用者の待ち時間、AWS標準指標で入口と土台、Application SignalsでAPIとJVM、X-Ray/Transaction Searchで1件の道のり、Logs Insightsで理由、Database InsightsでDBの待ちを調べる。", "S01 S19 S34 S36 S59"),
    ("資料の性質", "2026-10-02に公式Web資料を確認した設計・学習資料。AWSアカウントへの接続、環境変更、実負荷試験は行っていない。図・数値例・閾値案は学習用であり、実測値やAWSの保証値ではない。", ""),
    ("互換性の境界", "EAPとJDKの対応、Fargateでのコンテナ実行、ADOTのライブラリ計装、Red Hatのサポート契約は別々に確認する。WildFlyの対応表だけでEAP 8.1の個別イメージや業務アプリの完全動作を保証しない。", "S04 S40 S45 S46"),
    ("読む順番", "初めての方：図解→基礎→メモリ深掘り。担当者：サービス比較→指標一覧→収集設定→設定例→テスト手順。問題が起きたら障害切分とFAQへ。各行の根拠IDから公式資料へ進める。", ""),
]

chapter("02_基礎", "数字・記録・道のりを区別する", "学校の給食をAPIにたとえる。JMeterは注文を出す人、ALBは受付、EAPは調理場、DBは食材倉庫。たとえの後で正式な用語を説明する。", CARD_HEADERS, CARD_WIDTHS, [
    ("API", "『カレーを1つください』という決められた注文口。", "HTTPリクエストを受けて処理し、ステータスと本文を返す入口。1回のAPI内でDBや別サービスを何度も呼ぶ場合がある。", "同じURLでも検索条件・件数・本文サイズで負荷は変わる。API名とシナリオを対応付ける。", ""),
    ("メトリクス", "1分ごとの注文数や、調理場の混み具合を数字にした記録。", "時間に沿って蓄積する数値。どの範囲の何を何秒ごとに測ったかが必須。数字だけでは個別の注文の事情を特定できない。", "CPU高騰とAPI遅延が同時に起きたら手掛かり。ただし同時発生だけで因果関係は決まらない。", "S33"),
    ("ログ", "『10時3分、食材が届かず注文17が失敗』という日記。", "アプリやサービスが出した出来事の記録。記録していない情報は検索しても出ない。GCログとアクセスログは目的が違う。", "時刻、API、task ID、trace ID、例外の種類を結び付ける。機密の本文・認証情報は出力しない。", "S34 S62"),
    ("トレース / span", "1枚の注文票に、受付・調理・倉庫でかかった時間を書く。", "traceは1つの処理のつながり、spanはその一部分。親子関係とIDでHTTPやJDBCの呼出しを関連付ける。", "遅い1件を選び、DB・外部API・アプリ内部のどこが長いかを見る。計装していない区間は空白になる。", "S36 S40"),
    ("プロファイル", "料理人がどの作業に手を動かしていたかを、細かく観察する。", "コードの実行・割当・ロック等を調べる。トレースが示す『このspanが遅い』を、JFR等でメソッドや待機へ絞る。", "遅延を見つけた後の深掘り。すべての負荷試験で重いダンプを取る必要はない。", "S56 S58"),
    ("レイテンシと完了時間", "最初の返事までと、お皿を全部受け取るまでの時間は違う。", "JMeter Latencyは最初の応答まで、Elapsedはサンプル完了まで。ALBのTargetResponseTimeは応答ヘッダー開始までの別区間。", "同じ『Latency』という名前でも区間が違う。単位をmsへ揃えてから比べる。差分はあくまで調査の入口。", "S10 S59"),
    ("RPS / スループット", "1秒に何人へ給食を渡せたか。", "処理量を時間で割った値。要求の開始件数、完了件数、成功件数は別。再試行や非同期受付によって件数も違う。", "成功RPS・全RPS・失敗率を同時に見る。早いエラーが増えると平均時間だけは改善することがある。", "S59"),
    ("p50・p95・p99", "100人を待ち時間順に並べ、真ん中・95番目・99番目を見る。", "分位点。平均に隠れる少数の遅い処理を見るために使う。厳密な補間方法はツールに依存する。", "標本数も保存する。各分のp95を平均しても全期間のp95にはならない。API別・負荷段階別に元データから集計。", "S33"),
    ("飽和と待ち行列", "料理人が全員働いていると、新しい注文は列に並ぶ。", "使用率が上限に近付くと待ち時間が急増し得る。CPUだけでなく接続プール・worker・外部サービスにも上限がある。", "低CPUでもプール待ちやロック待ちなら遅い。CPU使用率だけを合否条件にしない。", "S49 S50"),
    ("名前空間", "数字のノートに付いた『受付』『調理場』という分類名。", "CloudWatchのNamespace。同名のCPUUtilizationでもAWS/ECSとAWS/RDSでは測る対象が違う。", "資料の正式名を名前空間とセットで使う。カスタム指標は例としてPerfTest/JBossEAPを使う。", "S17 S33"),
    ("ディメンション", "同じ注文数でも『1組』『2組』の札で分ける。", "ClusterName、ServiceName、TaskId等の組合せが時系列を識別する。フィルター対象を変えると別の集計になる。", "サービス平均で正常でも1タスクだけ異常な場合がある。タスク交代前後を分けて比較する。", "S05 S33"),
    ("Sum / Average / Maximum", "今日の注文数は足し算、机の混み具合は平均や最大で見る。", "イベント件数はSum、使用量の瞬間値はAverage/Maximumが基本。既に秒当たりの指標をSumすると意味が変わる。", "指標固有の例外を優先。ALB RequestCountPerTargetはSumが有効だが、その値はターゲット当たり平均。", "S10 S33"),
    ("ゲージとカウンター", "体温計と、スタートしてからの歩数計の違い。", "使用メモリはゲージ。JMXのGC回数は累積カウンター。累積値は差分を期間で割り、再起動によるゼロ復帰を考慮する。", "GC累積時間の生値をSumしない。Application SignalsとJMXで送信形式・単位が同じとは限らない。", "S01 S41"),
    ("収集間隔 / 表示期間", "1分に1回写真を撮っても、間に起きた1秒の出来事は写らない。", "測定頻度とグラフの集約幅は別。送信遅延もある。Maximumでも未観測のピークは復元できない。", "1分指標で短いGC停止を否定しない。GCログ・トレースと、必要時の細かなカスタム計測で補う。", "S07 S33"),
    ("欠測", "記録用紙が空欄なら、注文ゼロなのか、記録係が不在なのかを調べる。", "No dataは0ではない。停止タスク、送信障害、次元違い、権限不足、有効化前等で指標がなくなる。", "低負荷時の疎なエラー件数と監視停止を区別する。アラームの欠測扱いも指標ごとに決める。", "S06 S33"),
    ("SLOと合否", "『ほとんどの人へ5分以内に配る』という約束。", "要求から決めるサービス目標。例：成功RPS、API別p95/p99、エラー率、継続時間、回復時間。", "CPU80%やヒープ70%は万人共通の合格基準ではない。業務の締切と容量余裕から決める。", "S78"),
])

chapter("03_歴史", "なぜ監視の道具が増えたのか", "登場年月は公式発表で確認。『必要になった理由』は発表内容とシステム構造を基にした解説。昔の発表ページにある当時の制限・料金を現在仕様として扱わない。", ["時期", "登場・変化", "その前に困っていたこと", "今回へのつながり", "根拠"], [17, 37, 52, 52, 12], [
    ("2009年5月", "Amazon CloudWatch", "借りた仮想サーバーが忙しいかを共通の仕組みで測り、自動増減へ結び付けたかった。", "CPU等の数字を集める土台。ただしアプリ内部の事情は追加計装が必要。", "S65"),
    ("2014-07-10", "CloudWatch Logs", "サーバーごとに日記が散らばり、交換・停止後に原因の記録を追いにくかった。", "EAPとGCログをタスク外へ残す。ログを持ち出して初めて停止後も分析できる。", "S66"),
    ("2017-04-19", "AWS X-Ray一般提供", "1つの要求が複数サービスを通り、別々のログだけではどこが遅いかつなぎにくかった。", "HTTP・JDBC等の道のりをtraceとして見る。メモリの中身を見る機能とは役割が違う。", "S67"),
    ("2017-11-29", "AWS Fargate", "コンテナを動かす前に、土台のサーバー確保・保守・容量調整が必要だった。", "ホスト管理はAWSに任せる。その結果、利用者の観察対象はサービス・タスク・コンテナ・アプリになる。", "S68"),
    ("2017-12-14", "統合CloudWatch agent", "OS内部の数値とログを集める道具が分かれ、運用が複雑だった。", "収集係の統合。現在のFargate向けAPMではsidecarとして使う構成がある。", "S69 S03"),
    ("2018-11-27", "Logs Insights一般提供", "大量の日記を目で読むだけでは、失敗数や遅いAPIの傾向をすぐに探せなかった。", "時刻と条件で検索し、その場で集計する。", "S70"),
    ("2019年", "OpenTelemetry誕生", "製品ごとに計装方式が分かれ、送信先を変えるたびにアプリの変更が増えた。", "OpenTracingとOpenCensusを統合。計測・伝送の共通言語を作り、収集先を選びやすくした。", "S72"),
    ("2019-08-30", "Container Insights一般提供", "短命なコンテナが増え、個々のCPUやメモリを名前と結び付けるのが大変だった。", "ECSの構造に沿った画面・集計を用意。標準機能だけではJVM内部まではわからない。", "S71"),
    ("2020-04-23", "CloudWatch Synthetics一般提供", "利用者がいない時間も、注文口が本当に使えるか確かめたかった。", "少量の定期的な試し注文。JMeterの大量負荷と組み合わせる補助役。", "S73"),
    ("2020-10-21", "ADOTプレビュー", "OpenTelemetryをAWS環境で収集・送信しやすくし、AWSリソースと関連付けたかった。", "Java agentとCollectorの役割を分けて理解する。ADOT自体はデータを見るWebサービスではない。", "S74"),
    ("2021年8・9月", "Managed Grafana / AMP一般提供", "見やすい画面やPrometheus保存基盤のために、別途サーバーを保守していた。", "Grafanaは画面、AMPはPrometheus互換保存基盤。JVMの詳細指標を扱う選択肢が広がった。", "S75 S76"),
    ("2021-11-29", "CloudWatch RUM", "サーバーが速くても、利用者のブラウザーでは遅いことがあった。", "実利用者の画面側を観察。通常のJMeter HTTP SamplerはブラウザーのJavaScriptを実行しない。", "S77 S60"),
    ("2024-06-10", "Application Signals一般提供", "CPUとログとtraceを人がつなぐだけでは、API単位の健康状態とSLOを管理しにくかった。", "API・依存先・ランタイムの数字を同じ文脈で見るAPMへ。", "S78"),
    ("2024-11-21", "Transaction Search一般提供", "少数の遅い処理や業務属性を、柔軟に検索する必要が増えた。", "spanを検索可能な構造化ログとして扱う。未送信のspanを後から取り戻す機能ではない。", "S79 S36"),
    ("2024-12-01", "Database Insights一般提供", "DBごとの画面だけでは、アプリ全体とDB群の問題を関連付けにくかった。", "DB Load・SQL・待機・ログをまとめ、アプリ依存先から掘り下げる。", "S80"),
    ("2024-12-02", "ECS向けContainer Insights拡張", "平均だけでは、特定タスク・特定コンテナの異常を見落としやすかった。", "enhancedでTaskIdやContainerNameを使って調べる。", "S09"),
    ("2026-02-25", "X-Ray SDK/daemonがメンテナンスモード", "新規の計装をOpenTelemetryへ集約する方向へ変化。", "新規構成ではOTel/ADOTを優先。X-Rayサービスの終了ではない。現行の公式日程の終了欄はN/Aであり、古い記事の2027年終了を確定事項にしない。", "S38 S39"),
    ("2026-05-21", "OpenTelemetryがCNCF Graduatedへ", "共通計装が多数の利用者・提供者に使われ、プロジェクトの成熟が評価された。", "個別agentの動作保証とは別だが、標準化を選ぶ背景になる。", "S83"),
    ("2026-06-18", "ECSサービスの20秒指標", "急な増加に対し、従来の1分指標ではスケール判断が遅れやすかった。", "CPU/メモリの高解像度を選択可能。自動で全指標が20秒になるわけではない。", "S81 S07"),
    ("2026-07-23", "ALBログのCloudWatch Logs配信", "入口のログを他のCloudWatchログと同じ場所で検索したかった。", "S3経由だけでなく、ALBのIntegrationsからCloudWatch Logs等への配信を選べる。", "S82 S13"),
    ("2026-07-31", "RDS Performance Insightsの移行日", "DB監視をDatabase Insightsにまとめる変更。", "現行ガイドは移行済みと案内。PI API文書は継続。Standardは7日無料＋有償1～24か月、Advancedは1～24か月をモード料金に含む。古い保持期間表を流用しない。", "S19 S22"),
])

chapter("04_サービス", "どのAWSサービス・機能で何を見るか", "CloudWatchはサービス名、Container InsightsやApplication Signalsはその機能名。収集するソフト、保存する場所、見る画面を混同しない。優先度は本資料の提案。", CARD_HEADERS, CARD_WIDTHS, [
    ("最優先：CloudWatch Metrics / Dashboard / Alarm", "全体の温度計と掲示板とベル。", "AWS各サービスの指標とカスタム指標を時系列で保存し、比較・数式・通知に使う。AWS標準指標と追加有効化が必要な指標がある。", "JMeter、ALB、ECS、JVM、DBを同じ時間範囲で並べる。アラームは合否判定のすべてを代行しない。", "S33"),
    ("最優先：Container Insights（enhanced）", "建物→教室→机という順で、どこが混んでいるか見る。", "ECSのサービス・タスク・コンテナ別にCPU、メモリ、ネットワーク、状態を扱う。通常はECS/ContainerInsightsを参照。", "クラスターのenhancedを事前有効化。タスク単位の偏りを発見する。標準のインフラ収集だけではヒープ/GCは出ない。", "S05 S08"),
    ("最優先：Application Signals", "注文口ごとの混み具合と調理場の状態を一緒に見る。", "計装したアプリのAPI・依存先のAPM指標を扱い、Javaランタイム情報も同じサービス文脈で見られる。", "EAPへADOT Java agent、同一タスクへCloudWatch agentを設定するのが基本候補。JVMの全属性を自動収集するわけではない。", "S01 S02 S03"),
    ("最優先：AWS X-Ray", "遅かった1枚の注文票の経路図。", "計装済みspan/segmentを集め、親子関係・時間・エラーを分析。サンプリングされる場合がある。", "Servlet/JAX-RS、JDBC、HTTP client等が採用agentで計装されるか確認。SQLのDB内部待機はDatabase Insightsで補う。", "S36 S39 S40"),
    ("深掘り：Transaction Search", "たくさんの注文票を、時間や条件で検索する索引。", "CloudWatchへ受信したspanをaws/spansに保存して検索。X-Rayのtrace summaryの索引割合と、アプリでspanを作る割合は別。", "短期診断で詳細なspanを送る場合に有用。100%の取り込み能力と、実際に100%送信・計装できていることは区別する。", "S36 S37"),
    ("最優先：CloudWatch Logs / Logs Insights", "エラーや出来事の日記をまとめて読み、数える。", "EAPログ、GCログ、アクセスログ、Collectorログを蓄積・検索。メトリクスへ変換するにはEMF/metric filter等が必要。", "awslogsはstdout/stderr用。コンテナ内のserver.logを置くだけでは転送されない。GCログの時刻をAPIと揃える。", "S34 S62 S63"),
    ("DB使用時：Database Insights", "倉庫係が実際に働いているのか、鍵待ちなのかを調べる。", "DB LoadをCPU・I/O・ロック等の待機とSQLへ分解する。機能はエンジン・リージョン・モードに依存。", "アプリのJDBC spanが長い時に使用。EAPのJavaヒープはここでは見られない。", "S19 S20"),
    ("補助：RDS Enhanced Monitoring", "倉庫の建物の中にあるOSの計器。", "RDS側のOS・プロセスを細かく確認。CloudWatch Logsへ送る仕組みで、通常のAWS/RDS指標とは由来が違う。", "DBのCPUやメモリを深掘り。ECSタスクのJVM監視と取り違えない。", "S21"),
    ("詳細指標の保存：AMP", "細かな数字を札付きでしまう、大きなノート。", "Amazon Managed Service for Prometheus。Prometheus互換の時系列保存・PromQL。JMX ExporterからCollectorがscrapeしremote_writeする。", "task ID、pool名、GC名などを用いた独自分析に向く。AMPの数字は自動でCloudWatch名前空間へ現れるわけではない。", "S43"),
    ("統合表示：Amazon Managed Grafana", "複数のノートを1枚の掲示板に並べる。", "AMPやCloudWatch等のデータソースを可視化する。GrafanaそのものがEAP内部を計測するわけではない。", "既存のGrafana運用がある場合の選択肢。データソース、IAM、ワークスペース利用料を確認する。", "S75"),
    ("収集係：ADOT Java agent", "調理場の作業に小さな時計を付ける係。", "-javaagentでJVM起動時にロードし、対応ライブラリを計装する。AWS向けOpenTelemetry配布物の1つ。", "既存agentと二重計装しない。クラスローダー、JDBC driver、log contextの組合せを少量負荷で確認。", "S03 S40 S74"),
    ("収集係：CloudWatch agent / ADOT Collector", "時計から記録を受け取り、ノートへ運ぶ係。", "受信・加工・バッチ化・送信を行う。選んだ構成に応じてCloudWatch/AMP/X-Rayへ流す。Java agentとは別プロセスになることが多い。", "FargateではsidecarのCPU・メモリもタスク予算へ入れる。標準APM経路と独自Prometheus経路を設計せず混在させない。", "S02 S03 S42 S43"),
    ("補助：CloudWatch Synthetics", "人が少ない時間も、定期的に小さな試し注文をする。", "CanaryがAPIや画面の成功率・所要時間を確認。合成監視の機能。", "負荷試験中も通常利用の代表経路を少量観察できる。大規模な負荷生成はJMeter側で設計する。", "S73"),
    ("画面も対象なら：CloudWatch RUM", "本当に使っている人の端末で待ち時間を記録。", "WebクライアントのJavaScriptによって実利用者の性能・エラーを送信する。", "APIだけのJMeter試験ではRUMイベントが自動発生しない。ブラウザー試験を別に定義する。", "S77 S60"),
    ("補助：イベント / 操作記録", "教室の入替えや設定変更を記録した日程表。", "ECSの停止理由・デプロイ・スケーリングイベントを保存。構成変更の監査記録も時系列に重ねる。", "Task stoppedとcontainer restartは違う。CloudTrailの操作記録を業務APIの性能traceと混同しない。", "S09 S61"),
])

chapter("05_入口指標", "JMeterからEAPに入るまでの指標", "該当サービスを使う場合に確認する。統計の選択は分析目的に応じた提案であり、公式に指定された例外を優先する。ALBはLoadBalancer/TargetGroup、API GatewayはAPI/Stage等の正しい次元を選ぶ。", METRIC_HEADERS, METRIC_WIDTHS, [
    ("ALB / 必須", "AWS/ApplicationELB\nRequestCount", "Count / Sum\nRPS=件数÷期間秒", "ターゲットを選べた要求の量。", "入口で先に拒否された要求は含まれない場合がある。JMeterの件数と一致しないときはWAF、再試行、redirect等を確認。", "S10"),
    ("ALB / 必須", "AWS/ApplicationELB\nTargetResponseTime", "Seconds / p95・p99・Average", "ALBから送り、ターゲットが応答ヘッダーを返し始めるまで。", "JMeter Elapsedと同一ではない。EAPやDBの遅延を探す入口。比較時は×1000してmsへ。", "S10"),
    ("ALB / 必須", "AWS/ApplicationELB\nHTTPCode_Target_5XX_Count", "Count / Sum", "ターゲットが返したサーバーエラー件数。", "同時刻のEAP例外・依存先失敗を見る。HTTP200でも業務的失敗なら、この値には出ない。", "S10"),
    ("ALB / 必須", "AWS/ApplicationELB\nHTTPCode_ELB_5XX_Count", "Count / Sum", "ALB自身が返す5XX件数。", "ターゲット接続失敗、応答待ち、healthy数等を確認。Target側5XXと分ける。個別コードの内訳も使う。", "S10"),
    ("ALB / 必須", "AWS/ApplicationELB\nHealthyHostCount\nUnHealthyHostCount", "Count / Minimum・Maximum", "正常に配送できるターゲット数。", "最小healthyと最大unhealthyを見る。停止や登録解除で減ったこととヘルスチェック失敗を区別する。", "S10"),
    ("ALB / 推奨", "AWS/ApplicationELB\nTargetConnectionErrorCount\nRejectedConnectionCount", "Count / Sum", "接続が成立しない・受付側で接続を拒否する兆候。", "接続数、EAPのworker状態、セキュリティグループ、スケール時刻と照合する。", "S10"),
    ("ALB / 推奨", "AWS/ApplicationELB\nRequestCountPerTarget", "Count / Sum（値は平均）", "ターゲット1台当たりの要求量。", "Sumという統計名でも意味はターゲット当たり平均。タスク別の真の偏りはログ等で確認する。", "S10"),
    ("ALB / 補助", "AWS/ApplicationELB\nActiveConnectionCount\nNewConnectionCount\nProcessedBytes", "接続数・Bytes / Sumを確認", "接続再利用と転送量の変化。", "Keep-Aliveの条件を本番に合わせる。接続数とAPI件数は1対1ではない。", "S10"),
    ("ALB / ログ", "request_processing_time\ntarget_processing_time\nresponse_processing_time", "Seconds / 要求ごとのログ値", "ALBの前処理・ターゲット応答開始・返送開始までを分ける。", "ログ項目であって標準メトリクス名ではない。POST本文の時間の配分はWAF有無等に依存。3項目を足してもJMeter全時間とは一致しない。", "S11"),
    ("REST API Gateway / 必須", "AWS/ApiGateway\nLatency\nIntegrationLatency", "Milliseconds / p95・p99・Average", "入口全体とバックエンド往復の違い。", "同じAPI/Stageで比較。p95同士の差は入口のp95追加時間にはならない。個別ログで裏付ける。", "S14"),
    ("REST API Gateway / 必須", "AWS/ApiGateway\nCount\n4XXError\n5XXError", "Count: SampleCount\nエラー: Sum、率はAverage", "受信量と入口が認識したエラー。", "Method/Resourceまでの詳細指標は追加設定・料金。401/403/429等はアクセスログで分ける。", "S14"),
    ("HTTP API Gateway / 必須", "AWS/ApiGateway\nLatency / IntegrationLatency\n4xx / 5xx / Count", "遅延: ms / 分位点\nエラー件数: Sum", "HTTP APIの遅延と件数。", "RESTの4XXError/5XXErrorという名前を使わない。Route単位は詳細指標を有効化。X-Ray active tracingのREST向け手順を流用しない。", "S15 S16"),
    ("WAF / 利用時", "AWS/WAFV2\nAllowedRequests\nBlockedRequests\nCountedRequests", "Count / Sum / 通常1分", "負荷がアプリへ届く前に止められていないか。", "WebACL/Rule等で確認。負荷を1IPに集中するとrate-based ruleへ影響し得る。試験の目的に合わせ、実設定を記録する。", "S26"),
    ("CloudFront / 利用時", "AWS/CloudFront\nRequests\n5xxErrorRate\nCacheHitRate", "Requests: Sum\n率: Average (%)", "エッジで処理した数とキャッシュの効き方。", "us-east-1で確認、Region次元はGlobal。CacheHitRateは追加指標。ヒットが多いとEAPへ到達する負荷は小さくなる。", "S25"),
    ("CloudFront / 利用時", "AWS/CloudFront\nOriginLatency", "Milliseconds / Percentile", "オリジン取得が必要だった処理の初期応答まで。", "追加指標。キャッシュヒットを含む全利用者の待ち時間とは違う。冷えた/温まったcacheを別シナリオにする。", "S25"),
    ("NAT Gateway / 通過時", "AWS/NATGateway\nErrorPortAllocation\nPacketsDropCount\nActiveConnectionCount", "失敗/破棄: Sum\n接続: Maximum等", "外部API呼出し等で接続や通信が詰まる手掛かり。", "その通信がNATを本当に通るかを経路で確認。ALB→Fargateや同一VPCのDB通信を無条件でNAT原因にしない。", "S27"),
])

chapter("06_ECS指標", "Fargateの外側とコンテナの指標", "標準サービス指標と追加のContainer Insightsを分ける。Fargateの土台のEC2へ自分でホストagentを入れる設計にはしない。詳細の画面ではClusterName・ServiceName・TaskId・ContainerNameを揃える。", METRIC_HEADERS, METRIC_WIDTHS, [
    ("サービス / 必須", "AWS/ECS\nCPUUtilization", "% / Average・Maximum", "サービスが割り当てられたCPUに対して使った割合。", "Fargateサービスで標準提供。平均でCPUの偏りが隠れるのでtask単位も併用。分母はEC2ホスト全体ではない。", "S06 S07"),
    ("サービス / 必須", "AWS/ECS\nMemoryUtilization", "% / Average・Maximum", "サービスのメモリ使用割合。", "予約値/制限の設定と分母を確認。soft limitを分母にすると100%超もあり得るため、hard limitによる終了条件とは別に解釈。ヒープ率ではない。", "S07"),
    ("標準 / 2026年追加", "AWS/ECS\nCPUUtilization / MemoryUtilization\nresolutionSeconds=20", "既定60秒、選択時20秒", "急な利用率変化を細かく観測する選択肢。", "サービス側のmonitoring設定が必要。Container InsightsやJVM指標まで自動的に20秒化されない。課金も確認。", "S07 S81"),
    ("タスク / 必須", "ECS/ContainerInsights\nCpuUtilized / CpuReserved", "CPU units / Average・Maximum", "タスクごとの使用量と割当量。", "enhancedのTaskId次元で外れ値を探す。1024 CPU unitsが1 vCPUの目安。再配置によるID変化を記録。", "S05"),
    ("コンテナ / 必須", "ECS/ContainerInsights\nContainerCpuUtilization\nContainerCpuUtilized", "% / CPU units\nAverage・Maximum", "EAPと監視sidecarのCPUを区別。", "EAP CPU高騰とCollector CPU高騰では対処が違う。メトリクスの集計範囲を確認する。", "S05"),
    ("タスク / 必須", "ECS/ContainerInsights\nMemoryUtilized\nMemoryReserved", "公式単位: Megabytes\nAverage・Maximum", "タスク全体のメモリ余裕。", "独自のBytes計測と比べる時は単位・算出方法を揃える。task合計とEAPのみを混ぜない。", "S05"),
    ("コンテナ / 必須", "ECS/ContainerInsights\nContainerMemoryUtilized\nContainerMemoryUtilization", "Megabytes / %\nAverage・Maximum", "EAPコンテナとsidecarの使用メモリ。", "JVMヒープ、native領域、計測方式によるcache等を含む外側の観測。JMXのHeapMemoryUsageとは境界が違う。", "S05 S54"),
    ("容量 / 必須", "ECS/ContainerInsights\nDesiredTaskCount\nRunningTaskCount\nPendingTaskCount", "Count / 時系列を比較", "欲しい台数、稼働台数、起動待ち。", "台数が増えてもEAP起動・JIT・接続プール準備が終わるまで処理能力が十分でない場合がある。ALB healthy数も重ねる。", "S05"),
    ("状態 / 必須", "ECS/ContainerInsights\nRestartCount", "Count / 発行方式を確認して増加を見る", "restart policyによるコンテナ再起動。", "restart policy有効のコンテナのみ。タスク入替えの総数ではない。Task STOPPED理由とイベントを別保存する。", "S05 S09"),
    ("状態 / 推奨", "ECS/ContainerInsights\nUnHealthyContainerHealthStatus", "Count / Maximum等", "コンテナのhealth check異常。", "ALB health checkとは別。CPU高負荷、GC停止、起動途中、チェック先の依存障害を切り分ける。", "S05"),
    ("通信 / 推奨", "ECS/ContainerInsights\nNetworkRxBytes / NetworkTxBytes\nContainerNetworkRxBytes / ContainerNetworkTxBytes", "Bytes/Second / Average・Maximum", "受信・送信の転送量。", "名前にBytesがあっても公表単位は毎秒。Sumをそのまま転送総量と扱わない。同一taskの共有network集計を二重加算しない。", "S05"),
    ("一時領域 / 推奨", "ECS/ContainerInsights\nEphemeralStorageUtilized\nEphemeralStorageReserved", "Gigabytes / Maximum等", "ログ・一時ファイル・heap dumpの保存先の余裕。", "Fargate Linux platform 1.4.0以降等の条件。RAMではない。容量不足でダンプ保存が失敗すると原因の証拠が失われる。", "S05"),
    ("EBS / 使用時", "ECS/ContainerInsights\nTaskEBSFilesystemUtilization", "% / Maximum", "タスクに接続したEBSのfilesystem使用率。", "EBS使用構成のみ。すべてのFargateタスクで存在する指標としない。", "S05"),
    ("CPU待ち / 深掘り", "標準指標だけで確定しない\nCPU quota / schedulingの追加観測", "JFR・実行待ち・利用率で照合", "CPUが足りず順番を待つ可能性。", "k8sのcontainer_cpu_cfs_throttled_seconds_total等がFargateの標準CloudWatch指標だと決め付けない。利用可能な追加収集を実環境で確認する。", "S05 S56"),
])

chapter("07_DB依存指標", "DB・キャッシュ・非同期・ストレージの指標", "EAPのCPUが低くても、依存先待ちならAPIは遅くなる。採用されているサービスだけを対象にする。DBエンジン、ノード型/Serverless、ストレージ方式により指標の有無・単位が違う。", METRIC_HEADERS, METRIC_WIDTHS, [
    ("RDS / 必須", "AWS/RDS\nCPUUtilization", "% / Average・Maximum", "DB処理のCPU負荷。", "高負荷時はDatabase InsightsのCPU待ちとSQLを確認。低CPUでもロックやI/O待ちは起こる。", "S17 S20"),
    ("RDS / 必須", "AWS/RDS\nDatabaseConnections", "Count / Average・Maximum", "DBへのクライアント接続。", "EAPのInUseCountと同じではない。アイドル接続もある。task数×各pool上限がDB接続枠を圧迫しないか確認。", "S17 S50"),
    ("RDS / 必須", "AWS/RDS\nFreeableMemory\nSwapUsage", "Bytes / Minimum（空き）・Maximum", "DBのメモリ余裕とswapの兆候。", "ここはDBサーバーのメモリ。EAP JVMのヒープとは無関係。DB cacheで使用率が高いこと自体は異常とは限らない。", "S17"),
    ("RDS / 推奨", "AWS/RDS\nReadLatency / WriteLatency\nReadIOPS / WriteIOPS\nDiskQueueDepth", "遅延: Seconds\nIOPS: Count/Second\nqueue: Count", "ディスク読み書きの待ちと処理量。", "IOPSだけで速い/遅いを決めない。遅延と待ち行列が増えているかを見る。SQL実行時間そのものではない。", "S17"),
    ("RDS / 条件付き", "AWS/RDS\nCPUCreditBalance\nBurstBalance\nEBSIOBalance%", "Credits / %\nMinimumを確認", "バーストの残り能力。", "t系、gp2、対応instance等の条件がある。短時間だけ通り、長時間で遅くなる原因候補。非対応構成の欠測を障害扱いしない。", "S17"),
    ("DB / 最優先の深掘り", "Database Insights\nDB Load（Average Active Sessions）", "平均実行中/待機中セッション数", "DBの仕事量と、CPU・I/O・ロック待ちの内訳。", "CPU成分をvCPUと比較し、wait/SQLを絞る。AAS全体がvCPUを超えただけでCPU不足と断定しない。接続数とも別。", "S19 S20"),
    ("Aurora / 利用時", "AWS/RDS\nAuroraReplicaLag\nBufferCacheHitRatio", "lag: Milliseconds\nhit: Percent", "読み取り側の遅れとcache効率。", "writer/readerを分ける。RDSのReplicaLagはSecondsなので混ぜない。エンジン対応を確認。", "S17 S18"),
    ("Aurora Serverless v2 / 利用時", "AWS/RDS\nServerlessDatabaseCapacity\nACUUtilization", "ACU / Percent", "伸縮したDB容量と、設定上限に対する利用。", "最小/最大ACU、変化の時刻、SQLの遅延を並べる。ECSの伸縮とDBの伸縮は別。", "S18"),
    ("RDS Proxy / 利用時", "AWS/RDS\nDatabaseConnectionsBorrowLatency\nDatabaseConnections\nClientConnections", "借用遅延: Microseconds\n接続: Count", "Proxyの先でDB接続を借りる待ち。", "EAP pool待ちとProxy待ちは別段階。pinningや上限も確認。microsecondsをmsへ直す時は÷1000。", "S23"),
    ("ElastiCacheノード型 / 利用時", "AWS/ElastiCache\nEngineCPUUtilization\nCPUUtilization", "% / Average・Maximum", "エンジンのCPUとノード全体のCPU。", "片方だけ正常でも安心しない。ノード/シャード別の偏りを見る。Serverlessへ同じ表をそのまま適用しない。", "S24"),
    ("ElastiCacheノード型 / 利用時", "AWS/ElastiCache\nDatabaseMemoryUsagePercentage\nEvictions", "%: Maximum\nCount: Sum", "cacheの容量と上限によるkey追い出し。", "追い出し→cache miss→DB呼出し増という連鎖を調べる。EAPのheapとは別のメモリ。", "S24"),
    ("ElastiCacheノード型 / 利用時", "AWS/ElastiCache\nCacheHits / CacheMisses\nCurrConnections / NewConnections\nReplicationLag", "件数: Sum\n接続: Maximum\nlag: Seconds", "cacheの効き、接続再利用、複製遅延。", "同じcache keyばかりの試験では本番より軽くなる。値のサイズ・分布・TTLを再現する。", "S24"),
    ("SQS / 利用時", "AWS/SQS\nApproximateAgeOfOldestMessage", "Seconds / Maximum", "列の先頭が何秒待っているか。", "APIが202を速く返しても後段が終わっているとは限らない。再試行やDLQを含めて業務完了時間を測る。", "S28"),
    ("SQS / 利用時", "AWS/SQS\nApproximateNumberOfMessagesVisible\nApproximateNumberOfMessagesNotVisible", "Count / Average・Maximum", "未処理の待ちと処理中の量。", "近似値。NumberOfMessagesSent/Deleted等と照合するが、再配信があるので単純な一意件数の台帳にはしない。", "S28"),
    ("Lambda / 利用時", "AWS/Lambda\nDuration / Errors / Throttles\nConcurrentExecutions", "Duration: ms / 分位点\n件数: Sum\n同時実行: Maximum", "関数の遅延、失敗、制限、同時実行。", "Durationだけで利用者の全時間やcold start全体を説明しない。init情報はログ/traceで補う。", "S29"),
    ("DynamoDB / 利用時", "AWS/DynamoDB\nSuccessfulRequestLatency\nReadThrottleEvents\nWriteThrottleEvents", "遅延: ms\n制限: Count / Sum", "成功した処理の遅延と容量制限。", "クライアントでの再試行やnetwork時間は成功時サーバー遅延だけには出ない。table/index/operationを分ける。", "S30"),
    ("S3 / 利用時", "AWS/S3\nFirstByteLatency\nTotalRequestLatency\n5xxErrors", "遅延: ms\n失敗: Count / Sum", "オブジェクト転送の初期応答と全体。", "リクエストメトリクスは事前有効化。日次のBucketSizeBytesだけではAPI性能を診断できない。", "S31"),
    ("EFS / 利用時", "AWS/EFS\nPercentIOLimit\nBurstCreditBalance\nPermittedThroughput", "% / Bytes / Bytes/Second", "共有filesystemの処理枠と余裕。", "スループットモード等で適用が変わる。EAPログを同期書込みする構成ではI/O待ちと照合。", "S32"),
])

chapter("08_JVM指標", "JBoss EAPのJVMはどの指標で見るか", "上段はApplication Signalsの正式メトリクス。名前空間はApplicationSignals、標準のランタイム次元はServiceとEnvironment。ここではタスク別ヒープ最大値やXmxが自動で揃うとは扱わない。下段の『補完』は追加計測。", METRIC_HEADERS, METRIC_WIDTHS, [
    ("ヒープ / 必須", "ApplicationSignals\nJVMMemoryHeapUsed", "Bytes / Average・Maximum", "ヒープで現在使っている量。", "EAPのオブジェクト置場の量。GCで上下する波と、負荷停止後の落ち方を見る。サービス集計と単一JVMを混同しない。", "S01 S54"),
    ("GC後 / 必須", "ApplicationSignals\nJVMMemoryUsedAfterLastGC", "Bytes / Average・Maximum", "直近GC後に観測したメモリ量。", "poolとGC方式に依存。heap全体の厳密な生存object量と同一と決め付けず、長時間の底上がりの手掛かりにする。", "S01"),
    ("世代 / 推奨", "ApplicationSignals\nJVMMemoryOldGenUsed", "Bytes / Average・Maximum", "長く生きるobject側の使用量。", "cacheの成長と漏れを見分けるため、安定負荷・GC後・無負荷回復を比較する。GC方式で領域構成が変わる。", "S01 S48"),
    ("若い領域 / 補助", "ApplicationSignals\nJVMMemoryEdenSpaceUsed\nJVMMemorySurvivorSpaceUsed", "Bytes / Average・Maximum", "新しいobjectと生き残り側の領域。", "短命objectを大量に作る処理の仮説に使う。割当速度そのものはJFR等で追加確認。", "S01 S56"),
    ("非ヒープ / 必須", "ApplicationSignals\nJVMMemoryNonHeapUsed", "Bytes / Average・Maximum", "クラス情報・コード等の非ヒープ領域。", "JVMのnative memory全部を表すわけではない。direct buffer、thread stack、native library等は別途考える。", "S01 S54 S57"),
    ("GC時間 / 必須", "ApplicationSignals\nJVMGCDuration", "Milliseconds / Sum・Maximum等", "GC処理時間の集計。", "収集方式を確認し、同じJVMのログと照合。GC総時間をそのまま利用者の停止時間や厳密なSTW率にしない。", "S01 S48"),
    ("GC回数 / 必須", "ApplicationSignals\nJVMGCCount", "None（回数）/ Sum等", "GC発生の頻度。", "頻度だけで悪いと断定しない。1回当たりの長さ、CPU、APIの裾の遅延を組み合わせる。", "S01"),
    ("G1の内訳 / 補助", "ApplicationSignals\nJVMGCYoungGenDuration\nJVMGCYoungGenCount", "ms / 回数", "若い世代に関するGCの時間と回数。", "公式にはG1のみ。Red Hat JDK21でShenandoah等を選んだ環境に同じ指標の存在を期待しない。", "S01"),
    ("G1の内訳 / 補助", "ApplicationSignals\nJVMGCOldGenDuration\nJVMGCOldGenCount", "ms / 回数", "古い世代に関するGCの時間と回数。", "G1のみ。メトリクス名だけでFull GCの回数と同一視しない。GCログのpause/cycle分類を確認。", "S01 S48"),
    ("スレッド / 必須", "ApplicationSignals\nJVMThreadCount", "None（本数）/ Average・Maximum", "JVM内のthread量の変化。", "EAP workerのbusy数とは別。Java21のvirtual threadを含むすべての仕事数と断定しない。", "S01 S55"),
    ("クラス / 推奨", "ApplicationSignals\nJVMClassLoaded", "None（クラス数）/ Average・Maximum", "ロードされたクラス量。", "初回アクセス時の増加はあり得る。デプロイ後も増え続ける時はclassloaderとMetaspaceを調べる。", "S01 S54"),
    ("JVM CPU / 推奨", "ApplicationSignals\nJVMCpuRecentUtilization\nJVMCpuTime", "utilization: None\ntime: ns（単位表示None）", "JVM processから見たCPU利用。", "ECSの%と分母・表現を確認。CPU時間の累積性/送信集計を確認し、JVM間の時間をそのまま待ち時間へ変換しない。", "S01"),
    ("ヒープ上限 / 補完必須", "JMX MemoryMXBean\nHeapMemoryUsage.max\nカスタム例: HeapMaxBytes", "Bytes / JVMごとの値", "JVMに設定されたヒープの最大量。", "Application Signals標準表にHeapMax指標はない。Xmx/MaxRAMPercentageの実効結果をJMX/jcmdで確認し、必要なら独自送信。", "S01 S53 S56"),
    ("確保済み / 補完推奨", "JMX MemoryMXBean\nHeapMemoryUsage.committed\nカスタム例: HeapCommittedBytes", "Bytes / Average・Maximum", "ヒープへ確保している量。", "usedとの余白と拡張を見る。committedをRSSと同一視しない。max=-1等の未定義値は率の計算から除外。", "S53"),
    ("pool別 / 補完", "JMX MemoryPoolMXBean\nUsage / CollectionUsage", "Bytes / pool別ゲージ", "Metaspace・Code Cache等を分解。", "名前はGC/JDKに依存。pool名を固定して全collectorに適用しない。", "S47 S54"),
    ("native側 / 補完", "BufferPoolMXBean\nMemoryUsed / TotalCapacity / Count\nNMT / JFR", "Bytes・個数・診断イベント", "direct/mapped bufferやnative領域の候補。", "HeapUsedが平らでも外側だけ増える場合に使用。NMTも全native libraryの確保を完全追跡するわけではない。", "S56 S57"),
    ("thread状態 / 補完", "ThreadMXBean / thread dump\nRUNNABLE / BLOCKED / WAITING", "本数・stack trace", "仕事中か、ロック・I/O・pool待ちか。", "1回のsnapshotで結論を出さず間隔を空けて複数回。採取そのものの負荷と権限を考慮する。", "S55 S56"),
    ("EC2/EKS向け別経路", "CloudWatch agent JMX\njvm.memory.heap.used\njvm.memory.heap.committed\njvm.memory.heap.max", "Bytes / CWAgent等の設定先", "CloudWatch agentにもJMX収集機能はある。", "公式手順の対象はEC2/EKS。Fargateへそのまま対応済みと断定しない。本資料ではFargate向けに明示されたPrometheus/EMF経路を補完候補にする。", "S41 S42"),
])

chapter("09_メモリ深掘り", "部屋・机・引き出しで理解するJVMメモリ", "ここが今回の中心。『どのAWSサービスを見るか』に加え、『その数字は何を数えているか』まで理解すると、誤った増強を避けられる。数値例は説明用。", CARD_HEADERS, CARD_WIDTHS, [
    ("入れ子の構造", "Fargate taskは部屋、EAPコンテナは作業区画、JVMは料理人、heapは机。", "taskはEAPと監視sidecar等を含む。JVM processはheapに加えnon-heap/nativeを使う。コンテナ側のメモリ観測はその外側。", "task→container→process→heapの順に境界を確認。数値が異なることは直ちに矛盾ではない。図解も参照。", "S05 S53 S54"),
    ("used", "机の上に今置いてある材料の量。", "ヒープ使用中の量。まだGCに回収されていない不要objectも含み得る。『業務で必要なデータだけ』ではない。", "JVMMemoryHeapUsedをまず見る。増加の傾き、GCで下がる幅、負荷終了後の状態を記録する。", "S01 S53"),
    ("committed", "料理人のために確保した机の広さ。空き部分も含む。", "JVMがヒープ用に確保した容量。used以上で、定義済みのmax以下。OSの物理メモリ消費と単純な同義ではない。", "heap拡張が続くかを見る。usedが小さくてもcommittedが大きいと、外側のメモリがすぐ小さくなるとは限らない。", "S53"),
    ("max / Xmx", "これ以上広げないという机の最大サイズ。", "-Xmxはheap上限。Java process全体やFargate taskの上限ではない。明示Xmxがなければcontainer認識や他の起動設定の影響を受ける。", "タスク定義だけではXmxの実効値は確定しない。起動スクリプト・イメージの計算・jcmd/JMXの結果を照合。", "S48 S53 S56"),
    ("init / Xms", "最初に用意する机の大きさ。", "初期heap設定。Xms=Xmxは拡張を抑えやすいが、メモリ予算や初期化時間との交換条件がある。", "一律に同値へ変更しない。起動時間、常駐量、スケールアウト時の立上がりを測って判断。", "S48 S53"),
    ("ヒープ率の分母", "机の使用率は『使った机÷最大の机』。部屋の広さでは割らない。", "同一JVM・同時刻のheap used/max。used/committedは『今確保しているheapの密度』という別の指標。", "サービス集計のHeapUsedを1taskのXmxで割らない。taskごとに計算して最大値や分布を集約する。", "S01 S53"),
    ("GCの基本", "使い終わった材料の容器を片付けて机を空ける。", "GCは不要になったobjectを回収する。使っているうちに上がり、回収後に下がる鋸歯状の波は普通に起こる。", "1回の高い使用率でメモリ漏れと呼ばない。必要量と回収能力が釣り合っているかを見る。", "S48"),
    ("GC後の底が上がる", "片付けても机に残る荷物が増え続ける。", "長寿命object、cache成長、滞留要求、漏れなど複数候補がある。ウォームアップだけでも初期に増える。", "同じ負荷を長く継続し、安定後の傾向と無負荷回復を確認。残るobjectの参照はJFR/heap dumpで調べる。", "S48 S56"),
    ("短いGCが多い", "小さな片付けを何度もしている。", "短命objectを多く作るとyoung GCが増える。1回のpauseが小さくてもCPU消費やtail latencyへ影響し得る。", "GC回数・GC時間・CPU・p99を同時に見る。JSON変換、巨大配列、一時文字列などの仮説はJFRで確認。", "S01 S56"),
    ("STWと並行GC", "全員の作業を止めて片付ける時間と、仕事を続けながら片付ける時間。", "GCのすべての時間がStop-The-Worldではない。G1には並行処理とpauseがある。Young/Mixed/Fullを分ける。", "厳密な停止時間はGCログのpauseとsafepointを確認。GCメトリクス合計をAPI停止時間と同一にしない。", "S48"),
    ("大きなobject", "机に一度に大きな鍋を置くと、ほかの作業場所が減る。", "大きい応答・バッチ・byte配列は割当とGCに影響。G1の大object扱いはregionサイズ等に依存。", "平均payloadだけでなく最大payloadを試す。JMeter自身も応答保存でメモリ不足になり得る。", "S48 S60"),
    ("Metaspace / Code Cache", "レシピ帳と、すぐ使える手順カード。", "クラスmetadataとJITコンパイル済みcode等。heapとは別の領域。クラスロードや再デプロイで変化する。", "NonHeapUsed、ClassLoaded、pool別JMXを照合。heapだけ増やす対処では直らない場合がある。", "S01 S54"),
    ("thread stack", "料理人1人ごとに必要な手元の作業メモ。", "platform threadにはstackがある。threadを増やすとnative側の予算も必要。予約量と物理使用量は同じではない。", "thread数が増える設定変更時は、heap以外の余白と切替コストも測る。Java21だからEAPの全処理がvirtual threadになるわけではない。", "S55 S57"),
    ("direct buffer / native", "机の外に置く配送用の箱。", "NIO bufferやnative libraryの確保はheapの外。JVM NonHeapUsedですべてを説明できるわけでもない。", "heapが安定してcontainerだけ増えるならBufferPool、NMT、JFR、ログ書込み等を順に調べる。", "S54 S57"),
    ("Java OutOfMemoryError", "料理人が『自分の机や道具の置場が足りない』と報告する。", "Java heap space、Metaspace、direct buffer、native thread等で原因が異なる。例外文字列とdump条件を確認する。", "HeapDumpOnOutOfMemoryErrorは主にheapの証拠取得に有用。どのOOMでも必ず完全なdumpが得られると期待しない。", "S48 S56"),
    ("コンテナOOM kill", "部屋全体が満杯になり、外の管理者が作業を止める。", "メモリ制限によりprocessが外側から終了すると、Java例外やheap dumpを残す機会がない場合がある。", "ECS停止理由、container exit code、直前のtask/containerメモリを見る。exit 137だけでOOMと断定しない。", "S05 S09 S61"),
    ("監視sidecarの予算", "記録係にも椅子と机が必要。", "Collectorは受信・圧縮・queue・送信にCPUとメモリを使う。spanが多いほど負担が増え、送信先不調でqueueが膨らむこともある。", "taskの全RAMをXmxにしない。EAPとsidecarを別に監視し、計装ありの状態を本番相当として試す。", "S03 S05"),
    ("4GiB taskの設計例", "部屋を机だけで埋めず、通路と記録係の場所も残す。", "例：task4096MiB、EAP上限3584MiB、監視384MiB、調整余地128MiB。EAP内heap上限2048MiBとし、残りはnative等と余裕へ配分。", "数値は推奨設定ではない。JVMの予約/確保/実使用が混ざるため厳密なRSSの足し算にしない。実負荷のピークと長時間試験で見直す。", "S03 S53 S57"),
    ("診断ファイルの置場", "部屋が片付けられる前に、写真を安全な場所へ移す。", "taskの一時filesystemはtask終了後の保管場所にならない。heap dumpやJFRには業務データが含まれ得る。", "書込み権限・空き容量・暗号化した永続保存先・回収手順・保管期限を事前に決める。巨大dump採取中の性能値は別扱い。", "S05 S56 S61"),
])

chapter("10_EAP内部", "JVMの中で動くJBoss EAPの待ちを調べる", "JVMの健康とEAPの処理能力は同じではない。ここにある管理属性はAWS標準メトリクスではなく、管理CLI・JMX・exporter等で取得して送信する。subsystem名とresource名は実環境で確認する。", CARD_HEADERS, CARD_WIDTHS, [
    ("Undertow → worker → 業務処理", "受付が仕事を料理人へ渡し、料理人が倉庫へ材料を取りに行く。", "EAPのHTTP処理はUndertow等を通り、I/O workerや業務thread、datasourceを利用。入口が空いていても途中の資源で待つ。", "API traceとworker queue、DB poolを一緒に見る。CPU・heapだけでは待ち場所が見えない。", "S40 S50"),
    ("busy-task-thread-count", "今仕事中の料理人の推定人数。", "/subsystem=io/worker=<名前> の実行時属性。JVMThreadCountとは違い、workerの忙しさを見る。", "max-pool-sizeやqueue-sizeと照合。待機でthreadが埋まっているなら、thread数の増加だけで解決しない。", "S50"),
    ("queue-size / max-pool-size", "料理人の前に並ぶ注文と、増員できる上限。", "worker queueの推定待ち件数とpool上限。値は瞬間の観測であり、短いピークを取り逃がし得る。", "p99上昇の時間にqueueも伸びるか調べる。DBや外部API待ちによる二次的な混雑の可能性も検討。", "S50"),
    ("InUseCount / MaxUsedCount", "貸し出し中の倉庫の鍵と、過去の最大貸出数。", "datasource poolの現在使用中接続と最大使用数。単なる接続総数とは違う。", "InUseCountが上限に張り付く時、SQLが遅い・返却漏れ・小さ過ぎるpoolなどを比較する。", "S49 S50"),
    ("ActiveCount / AvailableCount", "用意されている鍵と、利用できる余地。", "ActiveCountには使用中だけでなく利用可能な接続も含む。AvailableCountの意味はpool実装・管理定義に合わせて読む。", "ActiveCountを使用中接続数として扱わない。IdleCountやInUseCount、設定上限と並べて解釈。", "S50"),
    ("AverageGetTime / AverageBlockingTime", "鍵を借りるまでの時間と、poolの排他制御で待つ時間。", "接続取得とpool lock待ちに関する統計。SQLを実行する時間そのものではない。長期間の累積平均では直近の悪化が薄まる。", "試験前の値を保存し、取得時刻やリセット条件も記録。平均だけでなく待ち件数・timeoutと組み合わせる。", "S50 S51"),
    ("WaitCount / MaxWaitCount / TimedOut", "鍵待ちになった回数や最大待ち人数と、期限切れになった接続は別に数える。", "WaitCount/MaxWaitCountは接続取得待ちの統計。TimedOutはタイムアウトした接続数で、業務要求の接続取得タイムアウト件数と同一視しない。", "待ち失敗はBlockingFailureCountや例外ログと照合。counterは試験前後の差分を使い、採用poolの管理属性説明で定義を確認する。", "S50"),
    ("統計を事前に有効化", "記録係を試験が終わってから呼んでも、過去は書けない。", "datasourceのstatistics-enabledは既定で無効。反映にreloadが必要になる場合がある。", "本試験より前に有効化・再デプロイして少量負荷で値を確認。計測途中のreloadで結果を混ぜない。", "S49 S51"),
    ("DB接続数の掛け算", "1教室20本の鍵でも、10教室なら最大200本。", "複数task×各datasource最大接続に加え、バッチ・管理・他サービスの接続がDBへ集まる。", "scale-out最大task数でDB接続予算を計算。task追加がDB過負荷を悪化させる場合がある。", "S17 S49"),
    ("HTTP client pool・外部依存", "倉庫ではなく配送業者の受付が詰まっている場合もある。", "下流HTTP clientの接続pool、timeout、retryも待ちの原因。自動計装の対応はclient libraryに依存。", "接続取得待ち・connect・read timeout・retry回数を分ける。外部APIの規約に合わせて負荷を制御する。", "S40"),
    ("EJB / transaction / session", "食事1セットを完成させるまで、複数の道具を借りたままにする。", "利用しているsubsystemに応じてEJB pool、transaction timeout、HTTP session、cacheが影響する。", "本当に使っている機能だけ追加監視。すべてのMBeanを無差別に送らず、仮説に必要なものを選ぶ。", "S47 S50"),
    ("EAP8.1と過去の設定例", "前の学校の鍵が、新しい学校で同じとは限らない。", "EAP7.4のMicroProfile Metrics設定や/metricsの存在をEAP8.1へそのまま仮定しない。XP6は追加構成であり、今回導入済みとは限らない。", "本資料は標準JMX/管理モデルと外付けagentを軸にする。Tomcat専用のCatalina MBean例をUndertowへ流用しない。", "S41 S50 S52"),
])

chapter("11_収集設定", "FargateからJVM情報を届ける仕組み", "推奨する入口はA：Application Signals。個別JVMの上限やEAP内部統計が必要な時にB/Cで補完する。これは構成の提案で、既存環境へ変更を実施した結果ではない。", CARD_HEADERS, CARD_WIDTHS, [
    ("A：標準APMの経路", "時計→記録係→掲示板。", "EAP JVM内ADOT Java agent → 同じtaskのCloudWatch agent → Application SignalsとX-Ray。メトリクスとtraceは別の種類のデータとして送る。", "まずこの経路でAPI遅延・依存先・基本JVM指標を揃える。Fargateはawsvpcのsidecar方式で、EC2向けdaemon方式を使わない。", "S02 S03"),
    ("A1：バージョンを記録", "『同じ時計』と言っても型番が違うと動きが違う。", "EAP8.1のupdate、Red Hat JDK21のpatch/build、image digest、ADOT Java agent、CloudWatch agentを固定して記録。", "公式最低条件はJava SDK1.32.5/CloudWatch agent1.300049.1。JBoss/WildFly既知問題は1.32.6で修正。これは最新推奨版という意味ではなく、現行の検証済み版を選ぶための下限情報。", "S01 S04 S45"),
    ("A2：agentの配置", "調理が始まる前に時計を取り付ける。", "-javaagentでサーバーJVM起動時に読み込む。公式ECS例はinit containerが共有volumeへjarを置き、成功後にEAPを起動する構成。", "イメージへの組込みも設計候補。既存JAVA_TOOL_OPTIONS/JAVA_OPTSを消さずに統合。Java agentのjarが存在し読めることを確認。", "S03"),
    ("A3：sidecar設定", "記録係が隣に座り、localhostで受け取る。", "CloudWatch agent設定でapplication_signalsのtraceとmetric受信を有効化。taskのawsvpcでは同一task内通信にlocalhostを使える。", "APM例の4316と一般OTLPの4317/4318を混同しない。受信設定・protocol・pathを送信側と一致させる。", "S03"),
    ("A4：サービス名・環境名", "同じ名前の教室の数字を混ぜないために札を付ける。", "service.nameとdeployment.environmentを設定する。ECS Application Signalsではサービス名を明示する。", "本番と性能試験の値を混ぜない。taskごとの識別は別のresource属性やログ/カスタム指標で補う。", "S02 S03"),
    ("A5：IAMを分ける", "記録係の権限と、荷物を運び込む係の権限は別。", "task roleはコンテナ内agentのAWS送信に使う。execution roleはimage取得、awslogs、task定義で参照するSSM/Secrets等に使う。", "公式のCloudWatchAgentServerPolicyを出発点に必要操作を確認。読み取り者にもMetrics/Logs/Traceの必要範囲を付与し、無制限な権限で代用しない。", "S03 S43 S62"),
    ("A6：private subnet", "記録先へ道がなければ、時計が正しくてもノートは空白。", "Logs、監視、X-Ray、ECR等の必要通信をNATまたは適切なVPC endpointで確保。構成次第でSSM等も必要。", "Collectorの送信失敗、DNS、SG、endpoint policyを確認。APIの外向き経路と監視の送信経路を区別する。", "S03 S61"),
    ("A7：画面での確認", "数字がノートまで届いたことを確かめる。", "CloudWatch → Application Signals → 対象Service/Environment → runtime表示。Metrics → ApplicationSignalsでも正式名を選んで確認する。", "低負荷でHeapUsed/GC/threadの値をEAP側と照合。GC未発生による欠測と送信失敗を区別。画面名はconsole更新で変わり得る。", "S01 S03"),
    ("B：JMX → Prometheus", "JVMが持っている計器を、決まった形式の数字へ翻訳する。", "同一JVMのJMX Exporter → HTTP /metrics → CloudWatch agentまたはADOT Collector → CloudWatchのカスタム指標、またはAMP。", "heap used/max/committed、GC、thread、必要なEAP属性を補完。Prometheus endpointを用意しただけではAWSへの保存は始まらない。", "S42 S43 S44"),
    ("B1：公開範囲と取得対象", "机の横で読む計器を、道路へ公開する必要はない。", "同一taskのscrapeならJMX Exporterを127.0.0.1の専用portへbindする設計が可能。別task収集ならprivate到達経路と認証等を設計。", "remote JMX/RMIを無認証で外部公開しない。管理MBeanには値の取得以外の機能もある。JVM標準とEAP固有のMBean登録先を確認。", "S44 S47"),
    ("B2：指標の宣言と次元", "必要な項目だけ転記し、どのtaskの値かを残す。", "CloudWatch Prometheus収集ではscrape設定とmetric declaration/EMF変換を設計。AMPではlabelとremote_writeを設計。", "metric名はexporter/collector版で変わり得る。実際の/metricsを確認して表と合わせる。本資料の独自名をAWS組込み名として検索しない。", "S42 S43 S63"),
    ("C：管理API/JMX → EMF", "定期的に机と鍵の数を読み、決まったJSON用紙へ書く。", "軽量な収集処理がEAP管理情報を読み、EMFを標準出力へ出す。awslogsがCloudWatch Logsへ送り、指定のcustom namespaceへ指標化。", "管理CLIを毎秒起動する構成は計測負荷が大きくなり得る。再利用する軽量clientやexporterを選び、10～30秒等の間隔案を検証する。", "S51 S62 S63"),
    ("補完経路の選び方", "大きな掲示板と詳しいノートを、目的に応じて使い分ける。", "CloudWatch中心ならA＋不足するcustom指標。Prometheus中心ならB→AMP→Grafana。JMX直接収集のEC2/EKS手順は別枠。", "同じ指標を複数経路で送ると二重計上や課金増の原因。名前空間・識別ラベル・集計の責任を決める。", "S41 S42 S43"),
    ("EAP特有の起動・logging", "料理人の時計を付けたつもりで、管理係にも二重に付けない。", "JAVA_TOOL_OPTIONSはサーバー以外のJava起動にも影響し得る。JBoss Modules・log manager・別agentとの組合せが計装に影響する。", "jboss-cliを同じ環境で起動する場合も注意。trace_idのMDC連携は採用logging実装で実出力を確認し、自動で入ると仮定しない。", "S03 S40 S47"),
    ("有効化の完了条件", "時計が付いた、数字が届いた、正しい教室名になった、の3つ。", "アプリ起動だけでは計装成功とは言えない。HTTP server/clientとJDBC span、JVM値、エラーログ、実行IDのつながりを検証する。", "本試験前に正常APIと意図した失敗を少数送信し、各信号が見えることを確認。Collectorのqueue/drop/送信失敗も確認する。", "S01 S03 S40"),
])

CODE_EXAMPLES = [
    dict(title="A. CloudWatch agentのApplication Signals受信設定", language="json", refs="S03", note="公式方式を基にした最小の設定断片。Fargateのtask定義全体ではない。image・role・log group・CPU/RAM・起動依存を別途設定する。JSON中のlogs.metrics_collectedは誤記ではなく、この方式の設定構造。", code='''{
  "traces": {"traces_collected": {"application_signals": {}}},
  "logs": {"metrics_collected": {"application_signals": {}}}
}'''),
    dict(title="B. EAPアプリコンテナの環境変数断片", language="json", refs="S01 S03", note="例示のservice/environment名を実環境へ変更する。既存のJAVA_TOOL_OPTIONSへ追記し、agent用jarを事前配置する。OTEL_METRICS_EXPORTER=noneでも、このAWS専用Application Signals経路は有効。一般OTelの設定へ無条件で流用しない。", code='''{
  "JAVA_TOOL_OPTIONS": "-javaagent:/otel-auto-instrumentation/javaagent.jar",
  "OTEL_RESOURCE_ATTRIBUTES": "service.name=eap-api,deployment.environment=perf-test",
  "OTEL_AWS_APPLICATION_SIGNALS_ENABLED": "true",
  "OTEL_AWS_APPLICATION_SIGNALS_RUNTIME_ENABLED": "true",
  "OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT": "http://localhost:4316/v1/metrics",
  "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT": "http://localhost:4316/v1/traces",
  "OTEL_EXPORTER_OTLP_PROTOCOL": "http/protobuf",
  "OTEL_TRACES_SAMPLER": "xray",
  "OTEL_PROPAGATORS": "tracecontext,baggage,b3,xray",
  "OTEL_METRICS_EXPORTER": "none",
  "OTEL_LOGS_EXPORTER": "none"
}'''),
    dict(title="C. EAP管理CLIで現在値を読む", language="text", refs="S47 S50 S51", note="EAPへ認証済みの管理CLIに入力するコマンド例。Windows PowerShellのコマンドではない。standaloneを想定し、AppDSとworker名は置換。domainの場合はhost/serverのaddressを付ける。実装差はread-resource-descriptionで確認する。", code='''/core-service=platform-mbean/type=memory:read-attribute(name=heap-memory-usage)
/core-service=platform-mbean/type=memory:read-attribute(name=non-heap-memory-usage)
/core-service=platform-mbean/type=threading:read-resource(include-runtime=true)
/subsystem=datasources/data-source=AppDS/statistics=pool:read-resource(include-runtime=true)
/subsystem=io/worker=default:read-resource(include-runtime=true,recursive=true)'''),
    dict(title="D. datasource統計の有効化（設定変更）", language="text", refs="S49 S51", note="読み取り操作ではない。テスト前の設定変更手順へ組み込む例。reload/再デプロイの要否とタイミングを事前調整する。この資料作成では実行していない。", code='''/subsystem=datasources/data-source=AppDS:write-attribute(name=statistics-enabled,value=true)
/subsystem=datasources/data-source=AppDS:read-attribute(name=statistics-enabled)'''),
    dict(title="E. Java21のGCログを標準出力へ", language="text", refs="S48 S62", note="EAPサーバーJVMの起動optionへ追加する例。stdoutはawslogs等で転送。既存のGCログ設定と競合しないよう統合し、出力量を確認。wall clockとuptimeを両方残す。", code='''-Xlog:gc*,safepoint:stdout:time,uptime,level,tags'''),
    dict(title="F. コンテナ内でJVM状態を読む", language="text", refs="S56 S61", note="Linuxの対象コンテナ内で、JDKのjcmdが存在し、対象Javaと同じ利用者等のattach条件を満たす場合。ECS Execは事前有効化と権限が必要。123は例示PIDであり、1に固定しない。", code='''jcmd -l
jcmd 123 VM.version
jcmd 123 VM.flags
jcmd 123 GC.heap_info
jcmd 123 Thread.print -l'''),
    dict(title="G. 詳細診断（採取負荷・保存先を事前検証）", language="text", refs="S56 S57 S58", note="Linuxコンテナ内の例。/diagnosticsは書込み可能で空き容量のある例示path。NMTは起動時に-XX:NativeMemoryTracking=summaryが必要。heap dumpは高負荷/停止を伴い得るので通常計測区間と分ける。", code='''jcmd 123 VM.native_memory summary scale=MB
jcmd 123 JFR.start name=perf settings=profile duration=60s filename=/diagnostics/perf.jfr
jcmd 123 GC.heap_dump /diagnostics/heap.hprof'''),
    dict(title="H. EMFで独自JVM指標を送るデータ構造", language="json", refs="S33 S63", note="値も時刻も架空。実装では観測時刻のepoch millisecondsと実測値へ置換し、1イベントをJSON1行でstdoutへ出す。StorageResolution=1は高解像度で保存する指定で、毎秒の測定を開始する設定ではない。収集間隔は別途設計する。TaskIdによりtask別に見られる一方、task入替えごとに時系列が増える。", code='''{
  "_aws": {
    "Timestamp": 1790895600000,
    "CloudWatchMetrics": [{
      "Namespace": "PerfTest/JBossEAP",
      "Dimensions": [["Service", "Environment", "TaskId"]],
      "Metrics": [
        {"Name": "HeapUsedBytes", "Unit": "Bytes", "StorageResolution": 1},
        {"Name": "HeapMaxBytes", "Unit": "Bytes", "StorageResolution": 1},
        {"Name": "HeapCommittedBytes", "Unit": "Bytes", "StorageResolution": 1}
      ]
    }]
  },
  "Service": "eap-api", "Environment": "perf-test", "TaskId": "example-task",
  "HeapUsedBytes": 1073741824,
  "HeapMaxBytes": 2147483648,
  "HeapCommittedBytes": 1610612736
}'''),
    dict(title="I. アプリログの構造例とLogs Insights", language="text", refs="S34 S35", note="このJSON構造は本資料の設計例。EAPの既定ログ形式ではない。アプリで実装/設定してから検索する。queryで本文やtokenを表示しない。errorの集計は別queryでstatus>=500をfilterする等、定義を明示。", code='''{"event":"api_completed","test_run_id":"perf-20261002-01","request_id":"example-id","trace_id":"example-trace","operation":"GET /orders/{id}","duration_ms":120,"status":200,"task_id":"example-task"}

fields @timestamp, operation, duration_ms, status
| filter event = "api_completed" and test_run_id = "perf-20261002-01"
| stats count(*) as requests, avg(duration_ms) as avg_ms,
        pct(duration_ms, 95) as p95_ms, pct(duration_ms, 99) as p99_ms
  by bin(1m), operation'''),
    dict(title="J. JMeterで実行IDと要求IDを保存", language="groovy", refs="S60", note="各API Samplerに作用するJSR223 PreProcessor（Groovy）の設計例。生成は要求につき1回。HTTP Header ManagerへX-Test-Run-Id=${testRunId}とX-Request-Id=${requestId}を設定。アプリも同じ値を構造化ログへ保存する設定が必要。", code='''vars.put('testRunId', props.getProperty('runId', 'perf-example'))
vars.put('requestId', java.util.UUID.randomUUID().toString())'''),
    dict(title="K. WindowsでのJMeter非GUI実行", language="powershell", refs="S60", note="JMeterインストールdirectoryから実行する例。api-test.jmxは別途用意し、出力先は実行ごとに新しい名前にする。今回の資料作成では負荷を発生させていない。", code='''.\u005cbin\u005cjmeter.bat -n -t api-test.jmx -JrunId=perf-20261002-01 -Jsample_variables=testRunId,requestId -l results-20261002-01.jtl -e -o report-20261002-01'''),
    dict(title="L. 同一JVMのヒープ率とGC率の計算", language="text", refs="S53 S41", note="上はメモリゲージ、下はJMX累積GC時間からの期間差分。GC時間率はSTW率と必ずしも等しくない。再起動・未定義max・欠測を除外し、service平均と単一JVMの値を混ぜない。", code='''heap_used_ratio = 100 * heap_used_bytes / heap_max_bytes
  条件: 同一JVM、同時刻、heap_max_bytes > 0

gc_time_ratio = 100 * (gc_time_ms_end - gc_time_ms_start) / interval_ms
  条件: 同一JVM、同一collector、再起動なし、単調な累積値

例: 60秒間で累積GC時間が3000ms増加 → 5%
  この5%をAPI停止率と断定しない。pauseはGCログで確認。'''),
]

chapter("13_トレース", "1回のAPIの旅を追う", "計測した処理と、まだ見えていない処理を区別する。JMeterのHTTP測定、ALBのヘッダー追跡、アプリのOpenTelemetry計装はそれぞれ別の役割を持つ。", CARD_HEADERS, CARD_WIDTHS, [
    ("始まりから終わり", "1枚の注文票に番号を付け、受付から倉庫まで運ぶ。", "trace IDで処理全体を識別し、span IDと親IDで個々の処理を結ぶ。HTTP header等でcontextを次のサービスへ渡す。", "同じ要求をアプリ→JDBC→DBの順で追えるか事前確認。contextが途切れると別traceになる。", "S36 S40"),
    ("JMeterは自動ではtraceしない", "ストップウォッチを押すだけでは、調理場の各作業は見えない。", "通常のHTTP Samplerは外部時間を測る。EAP内部のspanはアプリ側agent/SDKが作る。必要に応じてclient側も別途計装する。", "JMeter結果とログを実行ID・要求IDでつなぎ、ログにあるtrace IDへ進む方法がわかりやすい。任意の文字列をtraceparentへ入れない。", "S59 S60 S40"),
    ("ALBのX-Amzn-Trace-Id", "受付が注文票へ追跡番号を付ける。", "ALBはheaderを付与/更新できる。しかし、その設定だけでEAP内部やDB内部の詳細spanが生まれるわけではない。", "ALBアクセスログのtrace_idとアプリで採用するpropagatorを確認。W3C tracecontextとX-Ray形式の表記差も考慮。", "S12 S03"),
    ("入口の対応差", "すべての受付が同じ種類の注文票を作るとは限らない。", "API GatewayのX-Ray active tracingはREST API向けの手順。HTTP APIには同じ機能を当然に適用しない。", "REST/HTTP API、ALB、独自proxyごとにcontext伝搬を実測する。未計装の入口区間はアクセスログで補う。", "S15 S16"),
    ("JDBC spanの境界", "倉庫へ問い合わせた往復時間と、倉庫内の棚探し時間は別。", "JDBC client spanはアプリ側から見たDB呼出し。network、driver処理、DB側の待ちが含まれ得る。", "DB内のSQL/lock/I/OへはDatabase Insightsで進む。connection取得待ちは通常のJDBC実行spanに含まれない場合がある。", "S20 S40"),
    ("接続取得の計装", "倉庫に入る鍵を借りる前に待っていると、入室後だけ測っても見つからない。", "上流OTelのjdbc-datasource計装は既定無効と案内されている。対応agent版と対象poolの動作確認が必要。", "必要なら限定的に有効化し負荷を比較。EAP pool統計も収集し、spanだけへ依存しない。", "S40 S50"),
    ("親子spanの二重加算", "給食全体の10分に、調理の7分は含まれている。", "親spanの時間に子spanが入るため、単純合計は実時間を超える。並列呼出しは同時に進む。", "クリティカルパス（完了を決める最長の道筋）を見る。排他的な時間区間だけが足し算できる。", "S36"),
    ("sampling", "すべての注文票を詳しく保管するか、一部だけ保管するか決める。", "生成時・収集時・保存/索引で選別があり得る。低頻度の遅延は標本から抜けることがある。", "採用samplerと割合を試験計画へ記録。診断区間だけ増やす場合は監視CPU/メモリ、費用、欠落数も見る。", "S03 S37"),
    ("Transaction Searchの100%", "届いた注文票は全部保管できても、初めから書かなかった注文票は増えない。", "受信spanの取り込みとtrace summaryの索引は別。アプリやCollectorが落としたspanは後で復元できない。", "件数が少ない時に検索画面だけを疑わず、計装、sampling、送信、保存、索引の順に確認。", "S36 S37"),
    ("非同期処理", "受付が『受け付けた』と言った後、別の係が配達を続ける。", "SQS等ではAPI完了と業務完了が分かれる。messageにcontext/関連IDを適切に伝える。trace linkを使う場合もある。", "JMeterの202応答時間に加え、注文受付から業務完了イベントまでの時間と失敗/DLQを測る。", "S28 S40"),
    ("taskとtraceの関連", "同じ教室名でも、どの机で処理したかを追う。", "service.nameは論理サービス名。task ID、image version、instance識別をresource属性やログへ残す。", "遅いtraceのtaskだけのCPU・heapを見る。ApplicationSignalsのService/Environment集計をそのtaskの値だと思い込まない。", "S01 S05"),
    ("業務失敗とHTTP失敗", "注文票の受取りは成功でも、肝心の食事が違えば目的は達成していない。", "Application SignalsのFault、ErrorとJMeter assertionの失敗は定義が違う。4XXはサービス可用性では故障扱いしない。", "HTTP200内の業務errorもassertion等で判定。availabilityだけで試験合格にしない。", "S01 S60"),
])

chapter("14_JMeter", "JMeterの数字を正しくAWSへつなぐ", "負荷を出す側もJavaアプリ。測定器が先に苦しくなると、AWSの能力を正しく測れない。テスト対象と負荷生成器のJVMを別々に観測する。", CARD_HEADERS, CARD_WIDTHS, [
    ("Elapsed / Latency / Connect", "全部受け取るまで、最初の返事まで、接続するまでの3つの時計。", "JMeterの指標は重なる区間を持つため、Elapsed=Latency+Connectではない。connection再利用時のConnectの意味も変わる。", "サンプラーとHTTP client設定を記録。DNS/TLS/network/本文転送を含む実際の区間を確認する。", "S59"),
    ("Throughputと成功RPS", "たくさん配っていても、間違った食事ばかりなら成功とは言えない。", "成功した要求の数/秒と、すべての完了数/秒を区別する。再試行を含めたサーバー到達数も別。", "API labelを安定させ、成功率と時間を両方集計。Transaction Controllerの親子sampleを二重計上しない。", "S59 S60"),
    ("thread数とRPS", "同じ人数でも、料理が遅くなると次の注文は遅れる。", "一般的なclosed modelでは各利用者が応答を待って次を送る。100threadは100RPSではない。", "到着率を保ちたい試験ではarrival modelを明示し、生成器が予定の到着数を出せたか測る。", "S60"),
    ("負荷が弱まる見落とし", "遅くなったため注文が減ると、列の長さが意外に小さく見える。", "応答待ちの間に新規要求を出さないモデルは、一定到着率の現実と違う結果になり得る。coordinated omissionの問題として考える。", "計画RPS・開始RPS・完了RPSを分ける。thread追加で解消したつもりになる前に生成器容量を確認。", ""),
    ("ウォームアップ", "最初に道具を出す時間と、作業に慣れた後は別。", "JIT、class loading、DB接続、cacheが温まる。初回アクセスと定常負荷を混ぜると解釈しづらい。", "起動直後の性能試験と定常性能試験を分ける。cold startを測る要件なら温めて除外しない。", "S48 S49"),
    ("非GUI実行", "測る係が毎回大きな図を描いて疲れないようにする。", "大量負荷ではGUIと重いListenerを減らす。応答bodyの大量保存はCPU・heap・diskを圧迫する。", "非GUI実行と必要なJTL保存を基本にする。試験後にHTML reportを作る。", "S60"),
    ("生成器の監視", "走る人だけでなく、ストップウォッチを持つ人の体力も見る。", "JMeter hostのCPU・heap・GC・network・file descriptor/port等が負荷上限になる。", "AWS側に余裕があるのにRPSが増えない時は最初に確認。分散生成時は各nodeを個別監視。", "S60"),
    ("clockと時間帯", "別の時計が5分ずれていると、同じ事件を別の時刻だと思う。", "端末・生成器・サーバー・DBの時刻同期とUTC/JSTの変換を揃える。durationの時計とwall clockの役割も違う。", "実行ID、開始/終了UTC、JST表示、負荷段階の境界を保存。到着遅延を出来事の時刻と混ぜない。", "S33"),
    ("相関ID", "注文票の番号をレシートと日記にも書く。", "test_run_idは試験全体、request_idはAPI1回、trace_idは分散処理の関連付け。目的が違う。", "実行ID・要求IDをJTLとアプリログへ記録。unique IDをCloudWatch metricのdimensionにはしない。", "S63"),
    ("データの現実性", "全員が同じ簡単な注文だと、本当の給食時間にならない。", "API比率、payload、DB件数、検索selectivity、cache key、認証、session、read/write比が性能を左右する。", "正常・最大payload・cache miss・更新競合を含める。秘密情報のない試験データを用意する。", ""),
    ("タイムアウト・再試行", "待ち切れず再注文すると、厨房では仕事が重なることがある。", "JMeter、ALB、EAP、DB、外部clientのtimeoutとretryは別。client timeout後もserverが処理を続ける場合がある。", "失敗を除外して平均だけ見ない。retryの有無と回数を固定し、二重処理や非同期滞留も確認。", "S11 S40"),
    ("ネットワーク条件", "学校の隣から注文するか、遠くの町から注文するかで時間が違う。", "負荷生成region、AZ、internet/VPN、TLS、Keep-Alive、圧縮、DNS cache、protocolで変わる。", "AWS内部の最大能力試験と実利用者相当のend-to-end試験を分けて設計し、結果へ条件を添える。", "S59"),
    ("分位点の母集団", "全員の列と、1組だけの列の95番目は別の人。", "JMeterとAWSで成功/失敗、開始/完了時刻、API分類、sampling等が違う。p95の差はnetworkのp95ではない。", "同じ時間帯・API・成功条件・標本数を確認。違いが残る場合は同じrequestの個別ログで説明する。", "S01 S10 S59"),
])

chapter("15_テスト手順", "準備から報告までの具体的な手順", "時間・負荷量・閾値は業務要件から決める。以下の分数は手順を理解するための例であり、必須時間ではない。実行結果を書けるチェックリストをExcelの別シートに用意する。", ["段階", "やること", "残す証拠", "判断するポイント", "根拠"], [22, 50, 44, 42, 12], [
    ("1. 要件", "API別の成功RPS・p95/p99・許容error率・継続時間・非同期完了期限を決める。", "合否表、API定義、負荷モデル、データ規模。", "CPUの値だけでは合否を決めない。ピーク時と定常時を分ける。", ""),
    ("2. 構成", "ALB/API Gateway/CDN/WAF、ECS、DB等の実際の経路を図にする。", "region/AZ、task definition、image digest、EAP/JDK/agent版。", "未使用サービスへ監視作業を広げない。", "S02 S45"),
    ("3. 資源", "task CPU/RAM、EAP container制限、Xms/Xmx、GC、worker、各pool上限を記録。", "設定とJMX/jcmdで確認した実効値。", "同じtaskサイズでもJVMやpool設定が違えば別条件。", "S48 S49 S56"),
    ("4. 監視有効化", "Container Insights、Application Signals、ログ、DB監視、必要なcustom指標を事前に用意。", "名前空間/次元とテスト要求に対する値の変化。", "収集できていることを確認してから本試験へ。", "S01 S08 S19"),
    ("5. clock/ID", "時刻同期、UTC範囲、実行ID、要求ID、trace IDの連携を確認。", "JTLからアプリログとtraceへ辿れる1件。", "個別相関ができない場合も時系列相関と区別して記録。", "S36 S59"),
    ("6. 基準", "無負荷または低負荷を例として5～10分観測。", "idle CPU/heap、task数、DB接続、sidecarの使用量。", "既にあるノイズと負荷で増えた値を分ける。", ""),
    ("7. ウォームアップ", "代表APIを流し、JIT/cache/poolが安定した区間を判断。", "class数、heap、応答時間、cache hit、connection数。", "時間だけで機械的に終了せず、安定した根拠を見る。", "S48 S49"),
    ("8. 段階負荷", "目標の25→50→75→100%等へ段階的に増やす。各段階に安定観測区間を設ける。", "段階ごとの開始RPS/成功RPS/p95/p99/error、全監視値。", "RPS増加に対し、どこで遅延やqueueが急増するか。", ""),
    ("9. 定常負荷", "目標負荷を例として30～60分継続。", "SLO達成率、GC後heap、DB待ち、queue、task安定性。", "短いピークだけでなく、継続して目標を守れるか。", ""),
    ("10. 長時間", "業務周期に応じて数時間以上のsoak試験を計画。", "heap底、thread数、cache、DB接続、file/disk、credit。", "漏れ・蓄積・バースト枯渇・周期batchの影響。", "S17 S48"),
    ("11. 急増", "急な到着率増加とスケール動作を測る。", "監視→alarm→起動→healthy→応答回復の時刻。", "20秒指標を使ってもEAPの起動完了を短縮する保証はない。", "S07 S81"),
    ("12. 限界", "要件に含まれる場合だけ、停止基準のあるstress試験をする。", "初めに飽和した資源、timeout/拒否、回復時刻。", "限界を超えた挙動と、通常の合否を混同しない。", ""),
    ("13. 回復", "負荷を下げた後も観測を続ける。", "RPS/遅延、heap、queue、connectionが戻る曲線。", "要求の残留、GC後の底、scale-in後の安定性。", ""),
    ("14. 1件を深掘り", "同じAPIの正常・遅延・失敗例をそれぞれ選ぶ。", "request/trace ID、該当task指標、GC/DB待ち。", "相関だけの説明を、個別の証拠で補強する。", "S20 S36"),
    ("15. 改善比較", "ボトルネックに対応する設定/実装を1条件ずつ変える。", "変更前後で同じデータ・負荷・監視条件の結果。", "CPU、Xmx、poolを同時変更して原因を見失わない。", ""),
    ("16. 報告", "合否、capacity、原因の確度、改善、未検証条件をまとめる。", "元JTL、統計、dashboard設定、ログquery、構成、図。", "推測/確認済みを明記。スクリーンショットだけに依存しない。", ""),
])

chapter("16_障害切分", "症状から次に見る証拠を選ぶ", "下記は診断仮説であり、症状だけで原因を断定する表ではない。原則は利用者→入口→task→JVM/EAP→依存先の順で絞り、共通時刻と個別要求で裏付ける。", ["見えた症状", "考えられる原因", "次に照合する証拠", "確定前に注意すること", "根拠"], [29, 40, 51, 38, 12], [
    ("JMeterだけ遅い", "生成器飽和、network、DNS/TLS、本文転送。", "JMeter CPU/GC、Connect/Latency/Elapsed、ALBログ、payload。", "計測区間と母集団が違う。p95の引き算で場所を確定しない。", "S10 S59 S60"),
    ("ALBもAPIも遅くCPU高", "アプリCPU飽和、GC過多、重い変換処理。", "task別CPU、GCログ、JFR、traceのself側の時間。", "CPUの平均で1taskの偏りを見落とさない。", "S01 S05 S56"),
    ("CPU低いが遅い", "DB/外部待ち、pool待ち、lock、worker queue。", "JDBC/client span、EAP pool、thread dump、DB wait。", "CPUを増やすだけでは待ち先が改善しない可能性。", "S20 S40 S50"),
    ("heapが増えGCで下がる", "通常の割当と回収、または高頻度割当。", "GC後の底、pause、成功RPS、p99。", "鋸歯状だけを漏れと診断しない。", "S48"),
    ("GC後heapが上がり続ける", "cache/滞留の増大、object参照の保持、漏れ。", "同一taskの長時間傾向、無負荷回復、JFR、heap dump。", "warm-upと恒久増加を分ける。heap dumpで参照元を確認。", "S48 S56"),
    ("heap安定、containerだけ増加", "native、direct buffer、thread stack、page cache等。", "NonHeapUsed、BufferPool、NMT、thread数、ログI/O。", "container値からheapを引いただけではnative実使用と断定できない。", "S05 S54 S57"),
    ("GC例外なくtaskが終了", "OOM kill、health failure、デプロイ/scale、外部停止。", "ECS stopped reason、exit code、直前メモリ、deploymentイベント。", "exit137単独やRestartCountだけではOOM確定できない。", "S05 S09 S61"),
    ("JDBC長くDB CPU低い", "lock/I/O/network、Proxy待ち、client側待機。", "Database Insightsのwait/SQL、RDS I/O、Proxy借用遅延。", "JDBC spanの境界を確認。DB CPU低いからDB正常とは言えない。", "S17 S20 S23"),
    ("pool上限、DB処理は短い", "接続返却漏れ、長いtransaction、アプリ側pool不足。", "InUseCount、待ち、TimedOut、transaction/threadのstack。", "pool拡大はDBの同時負荷も増やす。DB接続予算を計算する。", "S49 S50"),
    ("負荷を上げてもRPS頭打ち", "生成器不足、closed model、入口制限、server飽和。", "開始/完了RPS、active threads、WAF/429、CPU、queue。", "平均応答が短いままエラーだけ増えていないか。", "S14 S26 S60"),
    ("scale-out後も遅い", "EAP初期化、cache/JIT、DB全体の上限、偏り。", "Running/Healthy差、startupログ、DB接続/Load、task別負荷。", "タスク数が増えた時刻と有効capacity増加の時刻を分ける。", "S05 S10 S49"),
    ("監視の値が出ない", "設定漏れ、agent失敗、IAM/network、次元違い。", "Collectorログ、export失敗、namespace/region、GC実行有無。", "空欄をゼロとして性能良好と報告しない。", "S01 S03 S33"),
    ("API速いが業務完了が遅い", "非同期consumer不足、再試行、DLQ、後段DB。", "SQS age/visible、完了イベント、consumer trace、DB待ち。", "202受付のp95で業務全体のp95を代用しない。", "S28 S36"),
    ("監視導入後に性能悪化", "agent重複、過剰span、scrape頻度、log同期書込み。", "sidecar CPU/RAM、export量、log量、計装前後比較。", "本番で同じ監視を使うなら監視込みの能力で評価。機能を闇雲に止めない。", "S03 S05 S63"),
])

chapter("17_ダッシュボード", "試験中に並べるグラフと見る順番", "同じ実行ID・UTC範囲・負荷段階で比較する。複数taskがある時はサービス全体の段とtask別の段を設ける。名前空間や単位の異なる線を無説明で同じ軸に重ねない。", ["配置", "表示する指標", "集計・見せ方", "この組合せで答える問い", "根拠"], [23, 49, 46, 40, 12], [
    ("1段目：利用者", "JMeter 成功RPS、全RPS、error率、p50/p95/p99、標本数。", "API別、定常/増加/回復別。JTLからの集計値はcustom指標等の追加送信が必要。", "要求の量と品質を両立できたか。", "S59 S60"),
    ("2段目：入口", "ALB RequestCount、TargetResponseTime、ELB/Target別5XX、healthy数。", "同じTargetGroup。p95/p99、件数Sum、healthyのMinimum。", "入口まで届いたか、受付かアプリか、どこで異常が起きたか。", "S10"),
    ("3段目：APM", "ApplicationSignals / Latency、Fault、Error。", "Service/Environment/OperationでAPI別に見る。Latencyはms、Fault/Errorは件数集計。", "どのAPI・依存先が遅いか。", "S01"),
    ("3段目：APMの率", "呼出量=SampleCount(Latency)、availability=(1−Fault/総数)×100。", "分母ゼロと欠測を処理。4XXのErrorを別表示。JMeterの業務成功率も並べる。", "可用性が良くても、認証失敗や業務エラーが増えていないか。", "S01"),
    ("4段目：容量", "ECS CPU/Memory、Desired/Running/Pending、ALB healthy。", "task数と利用率は軸を分ける。スケールとデプロイ時刻に注記。", "増員が間に合い、利用可能な処理能力になったか。", "S05 S07"),
    ("5段目：偏り", "Container InsightsのTaskId/ContainerName別CPU・メモリ。", "上位のtask、全task分布、EAPとsidecarを分ける。", "平均に隠れている1台の異常がないか。", "S05"),
    ("6段目：heap", "HeapUsed、GC後使用量、補完したHeapMax/Committed。", "Bytes→MiBを明示変換。個別JVMとサービス集計を別panelにする。", "heapの量・回収・余裕がどう変わったか。", "S01 S53"),
    ("7段目：GCとthread", "GC duration/count、GC pauseログ、thread、non-heap。", "GC時刻にp99を重ねて照合。pauseはms、countは期間当たり。", "少数の遅いAPIがGCやthread待ちに関係するか。", "S01 S48"),
    ("8段目：EAP内部", "worker busy/queue、InUseCount、pool待ち・timeout。", "custom指標のtask・worker・datasource次元を固定。", "CPU以外の『貸出枠』で仕事が止まっていないか。", "S50"),
    ("9段目：DB", "DB Load内訳、Top SQL、CPU、接続、I/O、Proxy待ち。", "Database Insightsへリンクし、writer/readerを区別。", "下流の待ちがアプリへ跳ね返っていないか。", "S17 S20 S23"),
    ("10段目：補助経路", "cache hit/miss、SQS age、WAF、NAT、S3/EFS等。", "実際に使う資源を選択。未使用サービスの空panelを増やさない。", "主経路の外側に原因がないか。", "S24 S26 S27 S28"),
    ("11段目：証拠", "slow/error trace、EAP/GCログquery、stopped taskイベント。", "時刻から詳細へ移れるlinkを保存。traceがない時のlog検索経路も用意。", "グラフの山を、具体的な原因と結び付けられるか。", "S09 S34 S36"),
    ("最下段：監視自身", "Collector CPU/RAM、送信失敗、drop、ログ件数、生成器資源。", "採用agentが出す内部ログ/指標で確認。一般に固定の共通AWSメトリクス名はない。", "観察の仕組みが壊れて、良く見えていないか。", "S03 S05 S60"),
])

chapter("19_注意と費用", "正しく測り続けるための設定", "性能値の信頼性に直接関係する項目をまとめる。具体的な料金単価・利用可能regionは変更されるため、導入時に公式表を参照する。", CARD_HEADERS, CARD_WIDTHS, [
    ("費用の分類", "時計、日記の量、保存棚、掲示板に別々の費用がかかる。", "追加metrics、高解像度、Container Insights、Application Signals、span、ログ取込/保存/query、AMP、Grafana等を見積もる。", "対象region、継続時間、task数、API数、span/request、sampling率、保持期間を入力条件として残す。", "S64"),
    ("cardinality", "注文番号ごとに新しいノートを作ると、棚がすぐ埋まる。", "metricの次元の組合せごとに時系列が増える。URLへ実IDを入れる場合やTaskIdが大量に入れ替わる場合は増加が大きい。", "request_idはlog/traceへ。metricはGET /orders/{id}等の安定operation名。task別指標は診断目的と期間を決めて採用。", "S33 S63"),
    ("保持期間と解像度", "古い記録は細かい1秒の値ではなく、まとめた表で残ることがある。", "CloudWatch標準の保持では、1分未満の高解像度は3時間、1分は15日、5分は63日、1時間は455日という段階がある。", "試験直後に必要な粒度で取得・保管する。logとtraceの保持は別設定。DB監視の保持も別表で管理する。", "S33 S19"),
    ("観測のオーバーヘッド", "見張る人が通路をふさぐと、作業の速さ自体が変わる。", "自動計装・JMX scrape・GCログ・JFR・dump・詳細traceには処理負荷がある。影響はアプリと設定に依存。", "監視なし/標準監視/詳細診断を比較して影響を記録。本番相当監視を付けた結果を最終capacityとする。", "S56 S57 S60"),
    ("送信とバッファ", "配達先が混むと、記録係の手元に紙がたまる。", "Collector/ログdriverのbuffer、再試行、batch、queueに上限がある。ドロップかアプリのブロックかは設定に依存。", "監視経路の遅延・欠落時の挙動を確認。計測終了後もflushと遅延到着を待って集計する。", "S03 S62"),
    ("機密情報", "注文票に名前や支払情報を何でも書かない。", "URL/query、SQL、例外、heap dump、JFR、HTTP headerには機密が入り得る。高cardinality対策と機密対策は両方必要。", "SQL bind値・token・bodyを原則収集対象から外し、診断ファイルのアクセス/暗号化/保存期限を定める。", "S36 S56"),
    ("計測portと管理port", "記録の窓口と、教室の設備を変える鍵は別。", "管理API/JMXと公開APIを分離。localhostで足りる収集をpublicへ開かない。外部接続が必要なら適切に認証・TLS・SGを使う。", "Fargate taskの境界を理解し、同じtask内の他containerも信頼境界に含める。", "S41 S42 S44"),
    ("再現できる版管理", "同じ条件で測ったつもりでも、時計の版が変わると比較できない。", "latest tagだけでは再現できない。EAP/JDK/agent/Collector/exporter、GC、アプリ、task定義を記録。", "この資料の最低版を最新の推奨版として固定しない。採用版でサポート表とrelease noteを再確認。", "S01 S40 S45"),
    ("Application Signalsの名前違い", "似た名前の教科書でも、扱う科目が違う。", "Application SignalsとCloudWatch Application Insightsは別機能。本資料のJVM名はApplicationSignalsのランタイム指標。", "console検索で似た機能へ迷い込まない。名前空間とsourceを手掛かりにする。", "S01 S78"),
    ("2026年の変更を扱う", "古い地図の道順が、今の町では変わっていることがある。", "ECS20秒、ALB→CloudWatch Logs、Database Insightsの保持/移行、X-Ray SDK日程を現行公式資料で確認した。", "現行機能は現行ガイド、登場日は当時の公式発表を使い分ける。region・画面・料金の変化は導入時に確認。", "S07 S13 S19 S38"),
])

chapter("20_FAQ", "よくある疑問に明確に答える", "迷ったときの確認表。ここでの『見える』は、必要な計装・送信・権限・保持期間を満たしている場合を意味する。", ["質問", "答え", "理由・例", "次の行動", "根拠"], [37, 34, 48, 39, 12], [
    ("FargateのMemoryUtilizationでheapがわかる？", "heapの使用量や使用率は直接わからない。", "containerにはheap以外も含まれる。taskにはsidecarもある。", "Application SignalsのHeapUsedとJMXのmaxを別に取得する。", "S01 S05 S53"),
    ("Container InsightsをONにすればGCも出る？", "標準インフラ収集だけでは出ない。", "同じCloudWatchで見ても、JVM指標を作るのはアプリ内の計装/JMX収集。", "AのApplication SignalsかB/Cの補完経路を設定する。", "S01 S05 S42"),
    ("JVM heapを見るAWSサービスは結局どれ？", "第一候補はCloudWatch Application Signals。", "正式名はJVMMemoryHeapUsed。詳細が必要ならCloudWatch custom metricsやAMPへJMX値を送る。", "08_JVM指標と11_収集設定を参照。", "S01 S42 S43"),
    ("X-Rayでheap dumpを見られる？", "X-Rayは要求の道のりを調べる。heap dump解析の代わりにはならない。", "objectの参照関係はdump等で分析し、遅いspanとの関連を調べる。", "GCログ/JFR/heap dumpを目的に応じて採取。", "S36 S56"),
    ("RDS Enhanced MonitoringでEAPのJVMが見える？", "見えない。対象はDB側のOS。", "DB serverとEAP taskは別の実行場所。", "EAPはApplication Signals/JMX、DBはDatabase Insights/Enhanced Monitoring。", "S01 S19 S21"),
    ("EAP8.1とJDK21なら自動計装は保証される？", "実際の組合せで確認が必要。", "Red Hat対応、OTel対応ライブラリ、agent版、classloaderや業務実装の条件は別。", "採用image/digestとagent版を固定して少量負荷で確認。", "S04 S40 S45"),
    ("heapが80%なら失敗？", "一律には決まらない。", "GCで十分戻るか、pause・p99・OOM・回復性がどうかで評価する。", "業務SLO、GC後の底、native余裕を組み合わせる。", "S48 S53"),
    ("CPUが低ければ余裕がある？", "待ちがある場合は遅くなる。", "DB lock、pool、外部API、worker queueなど。", "thread・pool・trace・DB waitsを見る。", "S20 S50"),
    ("heap maxとcontainer上限を同じにしてよい？", "通常はheap外の余白が必要。", "Metaspace、code、thread、buffer、監視agentにもメモリを使う。", "実測と長時間試験で予算を決める。4GiBの例は保証値ではない。", "S53 S54 S57"),
    ("1分グラフでGCとp99が重ならないのは正常？", "解像度とsamplingを確かめるまで結論を出さない。", "短いpauseは1分平均へ埋もれ、traceから抜けることもある。", "GCログの時刻と同一requestのdurationで照合。", "S33 S36 S48"),
    ("Application Signalsのavailabilityが良ければ合格？", "業務成功率も別に必要。", "4XXやHTTP200の業務errorはJMeterの失敗定義と違う。", "assertion、4XX、Fault、成功RPSを併記する。", "S01 S60"),
    ("ALBログは必ずS3でしか見られない？", "2026年の現行機能ではCloudWatch Logsへの配信も選べる。", "2026-07-23の統合によりaccess/connection/health checkログを扱える。", "ALB Integrationsと配信先/権限を設定する。従来S3方式も利用可能。", "S13 S82"),
    ("X-Ray自体が終了する？", "SDK/daemonのメンテナンス化とサービスの終了は別。", "現行公式日程は2026-02-25からmaintenance、終了欄N/A。", "新規計装はOpenTelemetry/ADOTを検討し、最新日程を確認。", "S38 S39"),
    ("Performance Insightsの旧資料を使える？", "概念は参考になるが画面・移行日・保持期間を現行に合わせる。", "現行Database Insights文書は2026-07-31移行を案内し、保持期間も旧表から変わっている。", "S19のモード表を参照。PI APIがすべてなくなるとは解釈しない。", "S19 S22"),
    ("監視を入れてから負荷が変わったら？", "監視込みの性能と、追加診断の負荷を分けて記録する。", "計測は無料の処理ではない。本番で使う監視を含めた能力が運用上の容量。", "同条件で計装前後とsampling設定を比較する。", "S03 S57 S60"),
])

CHECKLIST = [
    ("前提", "EAP 8.1のupdateとRed Hat JDK21のpatch/buildを記録", "実行中JVMの版、image digest", ""),
    ("前提", "対象AWS経路と利用region/AZを確定", "構成図、resource識別一覧", ""),
    ("前提", "API別のRPS・p95/p99・error率・業務完了条件を合意", "SLO/合否表", ""),
    ("資源", "task/container CPU・RAMと実効heap上限を照合", "task定義、JMX/jcmd", ""),
    ("資源", "最大task数を含むDB接続予算を確認", "task数×pool上限＋他接続", ""),
    ("収集", "Container Insights enhancedでtask別値が出る", "TaskId/ContainerNameのグラフ", ""),
    ("収集", "Application SignalsのAPI/JVM値が出る", "HeapUsed、GC、thread、API指標", ""),
    ("収集", "heap max/committedとEAP poolの補完を確認", "独自namespace/AMPと管理値の一致", ""),
    ("収集", "EAP/GC/Collectorログをtask停止後も読める", "log groupと保持設定", ""),
    ("収集", "正常・遅延・失敗のtrace経路を確認", "HTTP/JDBC spanと対応task", ""),
    ("収集", "DB監視のエンジン/モード/保持を確認", "DB Loadのwait/SQL画面", ""),
    ("相関", "JTL→request ID→log→traceを1件追跡", "対応するIDと時刻", ""),
    ("相関", "UTC/JSTと負荷段階の境界を揃える", "実行ID、開始・終了、段階表", ""),
    ("負荷", "生成器自身のCPU/heap/GC/networkに余裕", "生成器別の監視値", ""),
    ("負荷", "代表的なデータ量・cache状態・API比率を再現", "データ条件とseed等", ""),
    ("負荷", "予定の到着量と実際の開始/成功RPSを照合", "計画・開始・完了件数", ""),
    ("実行", "warm-upと定常と回復を分けて保存", "各区間の統計とグラフ", ""),
    ("実行", "long runでheap底や接続等の蓄積を確認", "同一taskの長時間曲線", ""),
    ("実行", "scale-outの起動からhealthyまでを記録", "時刻付きイベント", ""),
    ("品質", "欠測とゼロ、task入替えを識別", "欠測理由とstopped reason", ""),
    ("品質", "span/log/metricのdropや重複経路を確認", "Collectorログ、送信量", ""),
    ("報告", "母集団・単位・統計・samplingを結果へ記載", "分析条件一覧", ""),
    ("報告", "原因を確認済みと仮説に分けて報告", "根拠trace/log、追加確認項目", ""),
    ("保管", "JTL/監視値/設定を必要な粒度で保管", "保存先と保持期限", ""),
]

DIAGRAMS = [
    dict(title="① 注文の道と、監視データの道", summary="実線のHTTP経路と監視データの転送は別。図のALB・DBは代表例であり、採用済みという意味ではない。", refs="S02 S03 S05 S19 S36", mermaid='''flowchart LR
  J[JMeter：全体の待ち時間] --> A[ALB：入口と応答開始]
  A --> E[ECS Fargate：EAP 8.1 / JDK 21]
  E --> D[DB：SQLと待機]
  E -. インフラ .-> C[Container Insights]
  E -. Java agent .-> W[CloudWatch agent sidecar]
  W -. JVMとAPI .-> S[Application Signals]
  W -. span .-> X[X-Ray / Transaction Search]
  E -. stdout / GC .-> L[CloudWatch Logs]
  D -. DB内部 .-> I[Database Insights]'''),
    dict(title="② メモリは入れ子。ただし計測の合計は単純ではない", summary="task、container、JVM、heapは異なる境界。committed、RSS、予約量、cacheの扱いが違うので、単純な引き算だけでnative memoryを確定しない。", refs="S05 S53 S54 S57", mermaid='''flowchart TB
  subgraph T[Fargate taskの予算]
    subgraph E[EAPコンテナ]
      subgraph V[JVM process]
        H[Heap：used / committed / max]
        N[Non-heap：Metaspace / Code Cache等]
        O[その他：stack / direct buffer / native等]
      end
    end
    C[監視sidecar：別のCPU・メモリ]
  end
  H -.-> A[Application Signals + JMX補完]
  T -.-> B[Container Insightsで外側を観測]'''),
    dict(title="③ 同じ要求でも時計の区間が違う", summary="架空例：client接続等30ms＋入口/配送20ms＋EAP540ms＋本文受信10ms＝Elapsed600ms。EAP540msの内訳は自処理80ms＋pool待ち100ms＋JDBC360ms。実際には区間の重なりや並行処理を考慮する。", refs="S10 S11 S36 S59", mermaid='''sequenceDiagram
  participant J as JMeter
  participant A as ALB
  participant E as EAP
  participant D as DB
  J->>A: 接続・要求送信
  A->>E: ターゲットへ配送
  Note over E: 前処理・pool待ち
  E->>D: JDBC実行
  D-->>E: 結果
  E-->>A: 応答ヘッダー開始
  A-->>J: 応答開始 → 本文受信完了
  Note over J: LatencyとElapsedは終了点が違う'''),
]

EXAMPLE_NOTES = [
    "このシートの全数値は説明用の架空値。実環境の測定結果・推奨閾値ではない。入力欄の数値を変えると計算結果とグラフが変わる。",
    "ヒープ例：正常な波と、GC後に残る量が徐々に増える波を比較。後者だけで漏れは確定せず、cacheや滞留も調査する。",
    "負荷例：RPSを増やすとp95が急に悪化し、最終段階では成功RPSも伸びなくなる。限界の手前で必要なSLOを守れる容量を探す。",
    "比率計算は同一JVM・同時刻・同一単位を前提。サービス平均のheapと1taskのXmxの組合せでは使わない。",
]

HEAP_EXAMPLE = [(i, [650, 850, 1100, 700][i % 4], [650, 920, 1200, 780][i % 4] + (i // 4) * 130) for i in range(16)]
LOAD_EXAMPLE = [(50, 50, 110), (100, 100, 125), (150, 150, 145), (200, 200, 190), (250, 248, 330), (300, 275, 800), (350, 277, 1500)]

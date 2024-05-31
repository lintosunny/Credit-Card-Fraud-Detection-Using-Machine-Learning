# Fraud-Detection-Using-Machine-Learning

```mermaid
flowchart LR
    A["`API Gateway
    _Azure API Gateway_`"] --> B["`Data Ingestion
    _Kafka_`"]
    B --> C["`Data Storage
    _Azure blob_`"]
    C --> D["`Data Processing
    _pyspark_`"]
    D --> E["`EDA
    _Jupyter lab_`"]
    D --> F["`Model Training
    _AutoML_`"]
    F --> G["`Model Evaluation
    _Custom Scripts_`"]
    G --> H["`Model Registry
    _MLFlow_`"]
    H --> I["`Model Deployment
    _Docker, BentoML, Azure, Kubernetes_`"]
    I --> J["`Monitoring & Logging
    _Grafana, Prometheus_`"]
    J --> K["`Visualization
    _Power BI_`"]


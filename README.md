# Fraud-Detection-Using-Machine-Learning

```mermaid
graph LR
  A[API Gateway (Kong/AWS API Gateway)] --> B[Data Ingestion Service (Kafka, Kafka Streams)]
  B --> C{Data Storage (HDFS/S3, Redshift/BigQuery)}
  C --> D{Data Processing Service (PySpark, Delta Lake, Dask)}
  C --> E{EDA Service (JupyterHub)}
  D & E --> F[Model Training Service (AutoML, H2O.ai, AutoKeras)]
  F --> G[Model Evaluation Service (SHAP, Custom Scripts)]
  G --> H[Model Registry Service (MLflow, Seldon)]
  H --> I[Model Deployment Service (Docker, Kubernetes, Azure)]
  I --> J[Monitoring & Logging (Prometheus, Grafana)]
  J --> K[Visualization Service (Power BI)]

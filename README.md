# Fraud-Detection-Using-Machine-Learning

```mermaid
graph TD
  API_Gateway(API Gateway(Kong/AWS API Gateway)) --> Data_Ingestion(Data Ingestion Service(Kafka, Kafka Streams))
  Data_Ingestion --> Data_Storage(Data Storage(HDFS/S3, Redshift/BigQuery))
  Data_Storage --> Data_Processing(Data Processing Service(PySpark, Delta Lake, Dask))
  Data_Processing --> EDA(EDA Service(JupyterHub))
  Data_Processing --> Model_Training(Model Training Service(AutoML, H2O.ai, AutoKeras))
  EDA --> Model_Training
  Model_Training --> Model_Evaluation(Model Evaluation Service(SHAP, Custom Scripts))
  Model_Evaluation --> Model_Registry(Model Registry Service(MLflow, Seldon))
  Model_Registry --> Model_Deployment(Model Deployment Service(Docker, Kubernetes, Azure))
  Model_Deployment --> Monitoring(Monitoring & Logging(Prometheus, Grafana))
  Monitoring --> Visualization(Visualization Service(Power BI))

  style API_Gateway fill:#f9f,stroke:#333,stroke-width:2px;
  style Data_Ingestion fill:#f9f,stroke:#333,stroke-width:2px;
  style Data_Storage fill:#f9f,stroke:#333,stroke-width:2px;
  style Data_Processing fill:#f9f,stroke:#333,stroke-width:2px;
  style EDA fill:#f9f,stroke:#333,stroke-width:2px;
  style Model_Training fill:#f9f,stroke:#333,stroke-width:2px;
  style Model_Evaluation fill:#f9f,stroke:#333,stroke-width:2px;
  style Model_Registry fill:#f9f,stroke:#333,stroke-width:2px;
  style Model_Deployment fill:#f9f,stroke:#333,stroke-width:2px;
  style Monitoring fill:#f9f,stroke:#333,stroke-width:2px;
  style Visualization fill:#f9f,stroke:#333,stroke-width:2px;

  classDef service fill:#f9f,stroke:#333,stroke-width:2px;
  class API_Gateway, Data_Ingestion, Data_Storage, Data_Processing, EDA, Model_Training, Model_Evaluation, Model_Registry, Model_Deployment, Monitoring, Visualization service;

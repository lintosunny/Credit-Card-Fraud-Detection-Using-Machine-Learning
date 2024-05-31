# Fraud-Detection-Using-Machine-Learning

flowchart TB
    subgraph "API Gateway\n(Kong/AWS API Gateway)"
        API_Gateway
    end

    subgraph "Data Ingestion Service\n(Kafka, Kafka Streams)"
        Data_Ingestion_Service
    end

    subgraph "Data Storage\n(HDFS/S3, Redshift/BigQuery)"
        Data_Storage
    end

    subgraph "Data Processing Service\n(PySpark, Delta Lake, Dask)"
        Data_Processing_Service
    end

    subgraph "EDA Service\n(JupyterHub)"
        EDA_Service
    end

    subgraph "Model Training Service\n(AutoML, H2O.ai, AutoKeras)"
        Model_Training_Service
    end

    subgraph "Model Evaluation Service\n(SHAP, Custom Scripts)"
        Model_Evaluation_Service
    end

    subgraph "Model Registry Service\n(MLflow, Seldon)"
        Model_Registry_Service
    end

    subgraph "Model Deployment Service\n(Docker, Kubernetes, Azure)"
        Model_Deployment_Service
    end

    subgraph "Monitoring & Logging\n(Prometheus, Grafana)"
        Monitoring_Logging
    end

    subgraph "Visualization Service\n(Power BI)"
        Visualization_Service
    end

    API_Gateway --> Data_Ingestion_Service
    Data_Ingestion_Service --> Data_Storage
    Data_Storage --> Data_Processing_Service
    Data_Processing_Service --> EDA_Service
    EDA_Service --> Model_Training_Service
    Model_Training_Service --> Model_Evaluation_Service
    Model_Evaluation_Service --> Model_Registry_Service
    Model_Registry_Service --> Model_Deployment_Service
    Model_Deployment_Service --> Monitoring_Logging
    Monitoring_Logging --> Visualization_Service

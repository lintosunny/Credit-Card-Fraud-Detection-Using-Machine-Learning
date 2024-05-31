# Fraud Detection Using Machine Learning

## Architecture Overview ## High-Level Design (HLD)
1. **API Gateway**: Entry point for all client requests.
2. **Data Ingestion Service**: Handles data ingestion using Kafka.
3. **Data Storage**: Stores raw data in a data lake (e.g., HDFS or S3).
4. **Data Processing Service**: Uses PySpark for data preprocessing and Redis/Apache Ignite for in-memory data handling.
5. **EDA Service**: Jupyter Notebooks for exploratory data analysis.
6. **Model Training Service**: Incorporates AutoML for automated model selection and training.
7. **Model Evaluation Service**: Evaluates models based on recall, precision, F1-score, and AUPRC.
8. **Model Registry Service**: Manages model versions using MLflow.
9. **Model Deployment Service**: Deploys models using Docker, BentoML/FastAPI, and integrates with CI/CD tools like CircleCI and Azure.
10. **Monitoring and Logging Service**: Monitors the system using Grafana and Prometheus.
11. **Visualization Service**: Uses Power BI for visualization of results and insights.

## Process
```mermaid
flowchart LR
    A[(Transactions)] --> B[[model]]
    B --> C{Fraud Score}
    C -- >= threshold --> D[Analyst]
    C -- < threshold --> E[End]
    D -- check --> F((Feedback))
    F --> B
```

## Architecture Diagram
```mermaid
flowchart TD
    A[(MongoDB)] --> B["`Data Ingestion
    _Kafka_`"]
    B --> C["`Data Storage
    _Azure blob_`"]
    C --> D["`Data Processing
    _pyspark_`"]
    D --> E["`EDA
    _Jupyter lab_`"]
    D --> F["`Model Training
    _Scikit-Learn_`"]
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
```




## Low-Level Design (LLD)

### API Gateway

- **Endpoints**: Define REST endpoints for data submission, model predictions.
- **Security**: Implement JWT for authentication, API rate limiting policies.

### Data Ingestion Service

- **Producer Configuration**: Set up Kafka producers to stream data.
- **Topic Management**: Define Kafka topics for different data streams.

### Data Storage

- **Bucket Management**: Create S3 buckets or HDFS directories for storing raw data.
- **Data Partitioning**: Implement partitioning strategies for efficient storage and retrieval.

### Data Processing Service

- **Spark Jobs**: Write PySpark jobs for data cleaning, transformation, and feature engineering.
- **Caching**: Use Redis/Apache Ignite for intermediate data caching.

### EDA Service

- **Notebook Configuration**: Set up Jupyter notebooks with necessary libraries.
- **Data Access**: Provide secure access to processed data for analysis.

### Model Training Service

- **AutoML Pipeline**: Implement AutoML pipelines for automated model selection and hyperparameter tuning.
- **Hyperparameter Optimization**: Utilize AutoML tools to automate the optimization process.

### Model Evaluation Service

- **Evaluation Scripts**: Write scripts to compute recall, precision, F1-score, AUPRC.
- **Visualization**: Plot performance metrics using matplotlib/seaborn.

### Model Registry Service

- **MLflow Setup**: Configure MLflow for model tracking.
- **Versioning**: Implement version control for models.

### Model Deployment Service

- **Dockerization**: Create Docker images for model services.
- **CI/CD Pipelines**: Set up CircleCI pipelines for continuous deployment to Azure.

### Monitoring and Logging Service

- **Prometheus Config**: Configure Prometheus to scrape metrics.
- **Grafana Dashboards**: Create dashboards for monitoring key metrics.

### Visualization Service

- **Data Pipelines**: Set up ETL pipelines to feed data into Power BI.
- **Dashboard Design**: Design interactive dashboards for data visualization.


## Repository Structure

```
Fraud-Detection-Using-Machine-Learning/
│
├── data/                          
│   ├── raw/                        
│   ├── processed/                 
│   ├── models/                     
│   └── ...
│
├── notebooks/                      
│   ├── eda.ipynb  
│   ├── preprocessing.ipynb    
│
├── src/                           
│   ├── fraud_prediction/                        
│       ├── entity/
│       |   ├── config_entity.py
│       |   ├── ...
|       |
│       ├── artifacts/
│       |   ├── model.pkl
│       |   ├── preprocessing.pkl
│       |   ├── ...
|       |
│       ├── component/
│       |   ├── data_ingestion.py
│       |   ├── data_validation.py
│       |   ├── data_transformation.py
│       |   ├── model_trainer.py
│       |   ├── model_evaluation.py
│       |   ├── model_pusher.py
|       |
│       ├── config/
│       |   ├── azure_connection.py
│       |   ├── kafka_connection.py
│       |   ├── pyspark_manager.py
│       |   ├── mongo_client.py
│       |   ├── ...
|       |           
│       ├── constant/
│       |   ├── database/
│       |   ├── environment/
│       |   ├── model/
│       |   ├── prediction_pipeline_config/
│       |   ├── training_pipeline_config/
│       |   ├── ...
|       |
│       ├── templates/
│       |   ├── index.html
│       |   ├── ...
│       |  
│       ├── utils/
│       |   ├── utils.py
│       |  
│       ├── app.py
│       ├── exception.py
│       ├── logger.py                  
│       └── ...
│
├── tests/                         
│   ├── test_data_processing.py     
│   ├── test_model_training.py      
│   ├── test_api.py                
│   └── ...
│
├── config/                        
│   ├── config.yaml                
│   ├── mlflow.yaml                 
│   ├── dockerfile                  
│   └── ...
│
├── docs/                           
│   ├── architecture.md            
│   ├── api_reference.md            
│   ├── data_dictionary.md          
│
├── flowcharts/
│   ├── data_ingestion.md     
│   ├── data_validation.md         
│   ├── data_transformation.md         
│   ├── model_trainer.md
│   ├── model_evaluation.md         
│   ├── model_pusher.md
│   ├── training_pipeline.md
│   ├── prediction_pipeline.md
|
├── setup.py
├── start.sh
├── Dockerfile
├── Docker-compose.yaml
├── .dockerignore
├── requirements.txt               
├── README.md                      
├── LICENSE                        
└── .gitignore                     
```

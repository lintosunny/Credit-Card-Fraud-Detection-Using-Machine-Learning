# Fraud-Detection-Using-Machine-Learning

```mermaid
flowchart TD
    A[API GATEWAY] --> B[Data Ingestion]
    B --> C[Data Storage]
    C --> D[Data Processing]
    D --> E[EDA]
    D --> F[Model Training]
    F --> G[Model Evaluation]
    G --> H[Model Registry]
    H --> I[Model Deployment]
    I --> J[Monitoring & Logging]
    J --> K[Visualization]


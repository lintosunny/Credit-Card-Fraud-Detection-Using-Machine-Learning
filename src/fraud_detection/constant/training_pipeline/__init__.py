import os
from fraud_detection.constant.blob_container import TRAINING_BUCKET_NAME

SAVED_MODEL_DIR = os.path.join("saved_models")

# defining coommon constant variable for training pipeline
TARGET_COLUMN = "isFraud"
PIPELINE_NAME: str = "fraud_detection"
ARTIFACT_DIR: str = "artifact"
FILE_NAME: str = "transactions.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "transactions"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

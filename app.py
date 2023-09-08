import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomExceptions
from src.ml_project.components.data_ingestion import DataIngestion
from src.ml_project.components.data_ingestion import DataIngestionConfig


if __name__ == '__main__':
    logging.info("The executaion has been created")

    try:
        #data_ingestion = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomExceptions(e, sys)
        
import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomEceptions

if __name__ == '__main__':
    logging.info("The executaion has been created")

    try:
        a = 1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomEceptions(e, sys)
        
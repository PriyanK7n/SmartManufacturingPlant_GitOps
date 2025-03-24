from src.data_processing import DataProcessing # src.data_processing becomes a package which can be imported
from src.model_training import ModelTraining  # src.model_training becomes a package which can be imported

from src.logger import get_logger
logger = get_logger(__name__)


# This File Acts as Training Pipeline involving all necessayr methods at once sequentially
if __name__ == "__main__":

    logger.info(" Training Pipeline Started")

    processor = DataProcessing("artefacts/raw/data.csv" , "artefacts/processed")
    processor.run() # it will data loading for processing and will perform preprocessing and then split, scale and save data into artefacts folder

    trainer = ModelTraining("artefacts/processed/" , "artefacts/models/")
    trainer.run() # It will perform data loading, model training and model evaluation

    logger.info(" Training Pipeline Finished")

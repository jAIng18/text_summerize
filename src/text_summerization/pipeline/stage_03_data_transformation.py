from text_summerization.config.configuration import ConfigurationManager
from text_summerization.components.data_transformation import DataTransformation
from text_summerization.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
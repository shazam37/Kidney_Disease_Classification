from src.cnn_classifier.config.configuration import ConfigurationManager
from src.cnn_classifier.components.model_evaluation import Evaluation
from src.cnn_classifier import logger

STAGE_NAME = "Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()



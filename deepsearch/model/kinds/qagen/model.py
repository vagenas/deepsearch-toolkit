from abc import abstractmethod
from typing import List, Tuple

from deepsearch.model.base.model import BaseDSModel
from deepsearch.model.base.types import BaseModelConfig
from deepsearch.model.kinds.qagen.types import GenerateAnswersOutput, QAGenConfig


class BaseQAGenerator(BaseDSModel):
    @abstractmethod
    def generate_answers(
        self, texts: List[Tuple[List[str], str]]
    ) -> GenerateAnswersOutput:
        raise NotImplementedError()

    @abstractmethod
    def get_qagen_config(self) -> QAGenConfig:
        raise NotImplementedError()

    def get_config(self) -> BaseModelConfig:
        return self.get_qagen_config()

from abc import ABC, abstractmethod
from typing import List


class IFileTransformer(ABC):

    @property
    @abstractmethod
    def source_file_extension(self) -> str:
        pass

    @property
    @abstractmethod
    def target_file_extension(self) -> str:
        pass

    @abstractmethod
    def transform(self, source_path: str, target_path: str) -> None:
        pass


class ISubstitutionRule(ABC):

    @property
    @abstractmethod
    def match_pattern(self) -> str:
        pass

    @property
    @abstractmethod
    def substitution_pattern(self) -> str:
        pass

    @property
    @abstractmethod
    def maximum_repeat_count(self) -> int:
        pass


class ITransformer(ABC):

    @property
    @abstractmethod
    def rules(self) -> List[ISubstitutionRule]:
        pass


class ITextTransformer(ABC, ITransformer):

    @abstractmethod
    def transform(self, source_text: str) -> str:
        pass

    @abstractmethod
    def generate_transformers_for_each_rule(self) -> List["ITextTransformer"]:
        pass

    @abstractmethod
    def get_steps(self, source_text: str) -> List[str]:
        pass

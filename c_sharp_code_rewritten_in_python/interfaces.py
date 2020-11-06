from abc import ABC, abstractmethod


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


class ITextTransformer(ABC):

    @abstractmethod
    def transform(self, source_text: str) -> str:
        pass

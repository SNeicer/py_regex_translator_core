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

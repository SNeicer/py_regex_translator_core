from typing import List

from c_sharp_code_rewritten_in_python import interfaces


class TextTransformer(interfaces.ITextTransformer):

    def __init__(self, substitution_rules: List[interfaces.ISubstitutionRule]):
        self.__rules = substitution_rules

    @property
    def rules(self) -> List[interfaces.ISubstitutionRule]:
        return self.__rules

    @rules.setter
    def rules(self, rules: List[interfaces.ISubstitutionRule]) -> None:
        raise NotImplementedError("You can't set this field")

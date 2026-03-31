from typing import List

from pydantic import BaseModel, RootModel


class Element(BaseModel):
    english: str
    chinese: str
    japanese: str
    effective: List[str]
    ineffective: List[str]
    noeffect: List[str]


class Types(RootModel):
    root: list[Element]

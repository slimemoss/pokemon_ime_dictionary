from pydantic import BaseModel, RootModel


class Name(BaseModel):
    english: str
    japanese: str
    chinese: str
    french: str


class Element(BaseModel):
    id: int
    name: Name
    type: str
    category: str
    pp: str
    power: str
    accuracy: str


class Moves(RootModel):
    root: list[Element]

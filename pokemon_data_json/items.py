from pydantic import BaseModel, RootModel


class Name(BaseModel):
    japanese: str
    english: str
    chinese: str


class Element(BaseModel):
    id: int
    type: str
    description: str
    name: Name


class Items(RootModel):
    root: list[Element]

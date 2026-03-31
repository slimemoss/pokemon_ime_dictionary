from typing import List, Optional

from pydantic import BaseModel, RootModel


class Base(BaseModel):
    HP: int
    Attack: int
    Defense: int
    SpAttack: int
    SpDefense: int
    Speed: int


class Evolution(BaseModel):
    next: Optional[List[List[str]]] = None
    prev: Optional[List[str]] = None


class Image(BaseModel):
    sprite: str
    thumbnail: str
    hires: Optional[str] = None


class Name(BaseModel):
    english: str
    japanese: str
    chinese: str
    french: str


class Profile(BaseModel):
    height: str
    weight: str
    egg: List[str]
    ability: List[List[str]]
    gender: str


class Element(BaseModel):
    name: Name


class Pokedex(RootModel):
    root: list[Element]

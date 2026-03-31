from datetime import timedelta
from enum import Enum
from typing import Type, TypeVar

import requests_cache
from pydantic import BaseModel


class DataType(str, Enum):
    ITEMS = "items"
    MOVES = "moves"
    POKEDEX = "pokedex"
    TYPES = "types"


def download_json(datatype: DataType):
    url_base = 'https://raw.githubusercontent.com/Purukitto/pokemon-data.json/refs/heads/master'
    url = f'{url_base}/{datatype.value}.json'

    session = requests_cache.CachedSession(expire_after=timedelta(days=20))
    return session.get(url).json()


T = TypeVar("T", bound=BaseModel)


def download(datatype: DataType, cls: Type[T]) -> T:
    data = download_json(datatype)
    return cls.model_validate(data)

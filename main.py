import re

import jaconv

from pokemon_data_json import DataType, download
from pokemon_data_json.moves import Moves
from pokemon_data_json.pokedex import Pokedex


def yomi(tango: str):
    s = jaconv.kata2hira(tango)
    s = re.sub(r"[^ぁ-んーa-zA-Z]", "", s)
    return s


def has_kanji(s: str) -> bool:
    return bool(re.search(r"[一-龯]", s))


def from_pokemon():
    data = download(DataType.POKEDEX, Pokedex)
    return [e.name.japanese for e in data.root]


def from_moves():
    data = download(DataType.MOVES, Moves)
    return [e.name.japanese for e in data.root]


tangos = from_pokemon() + from_moves()
tangos = [t for t in tangos if not has_kanji(t)]

elem = [(yomi(t), t) for t in tangos]
elem = [(y, t) for y, t in elem if len(y) > 2]

for y, t in elem:
    print(f'{y}\t{t}\t固有名詞')

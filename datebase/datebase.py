import pickle
from dataclasses import dataclass, field

_BD = 'bd.pickle'


@dataclass
class UserBD:
    page: int = 1
    bookmarks: set[int] = field(default_factory=set)


def write_to_bd(dir: str) -> None:
    with open(dir, 'ab') as file:
        pickle.dump(users_db, file)


def read_from_db(dir: str) -> set[dict]:
    with open(dir, 'rb') as file:
        res = pickle.load(file)
    return res


# Инициализируем "базу данных"
users_db: set[UserBD] = read_from_db(_BD)
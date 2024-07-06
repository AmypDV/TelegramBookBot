import pickle


_BD = 'bd.pickle'

# Создаем шаблон заполнения словаря с пользователями
user_dict_template = {
    'page': 1,
    'bookmarks': set()
}


def write_to_bd(dir: str) -> None:
    with open(dir, 'ab') as file:
        pickle.dump(users_db, file)


def read_from_db(dir: str) -> set[dict]:
    with open(dir, 'rb') as file:
        res = pickle.load(file)
    return res


# Инициализируем "базу данных"
users_db = read_from_db(_BD)
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

LOAD_CAPACITY = 60

things = {
    'Одеяло': 60,
    'Спальник': 100,
    'Ботинки': 40,
    'Кружка': 10,
    'Ложка': 7,
    'Кастрю': 50,
}


def sort_things(things):
    amount = 0
    things_lst = list(things.items())
    things_lst.sort(key=lambda x: x[1])

    for thing in things_lst:
        if thing[1] + amount <= LOAD_CAPACITY:
            amount += thing[1]
        else:
            things.pop(thing[0])

    return things


if __name__ == '__main__':
    print(sort_things(things))
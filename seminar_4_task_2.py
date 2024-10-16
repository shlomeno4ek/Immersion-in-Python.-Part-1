# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.


# добавлена для примешивания глобальной переменной
GLOBAL_VALUE = 23


def my_func(**kwargs) -> dict:
    """Функция подготовки словаря из переданных аргументов и их значений"""
    result = dict()
    for k, v in kwargs.items():
        try:
            _ = hash(v)
            result[v] = k
        except TypeError:
            result[str(v)] = k

    return result


def main():
    print("Исх. параметры: first=\"one\", second=2, third=3, fourth=\"four\", fifth=[2, 3]")
    print(my_func(first="one", second=2, third=3, fourth="four", fifth=[2, 3]))


if __name__ == "__main__":
    main()
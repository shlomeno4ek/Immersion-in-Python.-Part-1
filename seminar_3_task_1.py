# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


# список для обработки
LIST_1 = [1, 2, 2, 2, "A", "B", "C", 3, "c", "B", 0]
LIST_2 = [1, 2, 3, 4, "D", "E", "F", "F", "G", 5, 8]


# обработка списка
def double_items(work_list: list) -> list:
    return list(set([i for i in work_list if work_list.count(i) > 1]))


def main():
    print(f"{LIST_1} - {double_items(LIST_1)}")
    print(f"{LIST_2} - {double_items(LIST_2)}")


if __name__ == "__main__":
    main()

# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


# Pin код
PIN = "1456"
# Процент за снятие
PERCENT_PULL = 0.015
# Кол-во последовательных операция для начисления %
OPERATION_ADDED = 3
# Процент пополнения карты
PERCENT_ADD = 0.03
# Минимум удержания
MIN_PERCENTAGE = 30
# Максимум удержания
MAX_PERCENTAGE = 600
# Минимальная купюра
MIN_BANKNOTE = 50
# Налогооблагаемая сумма
MIN_TAX = 5_000_000
# Ставка налогообложения
PERCENT_TAX = 0.1

# лог операций
operation_log = []


def logging(operation: str):
    """Логирование"""
    operation_log.append(operation)


def show_log():
    """Отображение лога операций"""
    print("-- ЛОГ ОПЕРАЦИЙ --")
    for o in operation_log:
        print(o)


def tax_pay(summ: float) -> float:
    """Удержание налога"""
    tax = summ * PERCENT_TAX
    print(f"Налог: {tax:.2f}")
    summ -= tax
    return summ


def push_cash(balance: float) -> (bool, float):
    """Положить деньги на счет, запрашивает сумму

    :balance: сумма баланса карты на начало операции
    :(bool, float): результат выполнения операции, новый баланс
    """
    summ = float(input("Сумма для пополнения: "))
    result = False

    # Налог
    if balance > MIN_TAX:
        balance = tax_pay(balance)

    # проверить сумму
    if summ % 50 == 0:
        balance += summ
        print(f"Баланс пополнен: {summ:.2f}")
        result = True
    else:
        print("Недоступная сумма!")

    show_balance(balance)
    return result, balance


def pull_cash(balance: float) -> (bool, float):
    """Снять деньги со счета, запрашивает снимаемую сумму

    :balance: сумма баланса карты на начало операции
    :(bool, float): результат выполнения операции, новый баланс
    """
    result = False
    show_balance(balance)
    summ = float(input("Сумма для снятия: "))

    # Налог
    if balance > MIN_TAX:
        balance = tax_pay(balance)

    # проверить сумму
    if summ % 50 == 0:
        percent_summ = summ * PERCENT_PULL

        if percent_summ > MAX_PERCENTAGE:
            percent_summ = MAX_PERCENTAGE
        if percent_summ < MIN_PERCENTAGE:
            percent_summ = MIN_PERCENTAGE

        if balance - summ - percent_summ < 0:
            print("Недостаточно средств!")
        else:
            balance -= (summ + percent_summ)
            print(f"Выдано {summ:.2f}, комиссия {percent_summ:.2f}")
            result = True
    else:
        print("Недоступная сумма!")

    return result, balance


def show_balance(summ: float):
    """Отображение баланса"""
    print(f"Баланс счета: {summ:.2f}")


def show_menu(menu: dict[int, str]) -> int:
    """Отображение меню, возвращает ключ выбранного пункта или 0, если выбор вне диапазона ключей"""
    for k, v in menu.items():
        print(f"{k} - {v}")
    result = int(input("> "))
    return result if result in menu.keys() else 0


def main():
    # начальный баланс
    balance: float = 0
    # счетчик операций
    operation_counter = 0
    # меню банкомата
    menu_bank: dict = {
        1: "снять",
        2: "пополнить",
        3: "баланс",
        0: "выход",
    }

    # авторизация клиента
    authorized = PIN == (input("Введите PIN: "))

    while authorized:
        action = show_menu(menu_bank)
        match action:
            # Снятие средств.
            case 1:
                success, balance = pull_cash(balance)
                if success:
                    operation_counter += 1
                logging(f"СНЯТИЕ - {'Ok' if success else 'ERROR'}")
            # Пополнение карты.
            case 2:
                success, balance = push_cash(balance)
                if success:
                    operation_counter += 1
                logging(f"ПОПОЛНЕНИЕ - {'Ok' if success else 'ERROR'}")
            # Отображение баланса
            case 3:
                show_balance(balance)
            # Выход
            case _:
                break

        if operation_counter == OPERATION_ADDED:
            operation_counter = 0
            summ_add = balance * PERCENT_ADD
            print(f"Начисление %: {summ_add:.2f}")
            balance += summ_add
            show_balance(balance)
    else:
        print("Неверный пин-код!")
    show_log()


if __name__ == "__main__":
    main()

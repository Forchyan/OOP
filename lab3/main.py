import abc
from math import gcd, lcm


class Operation(abc.ABC):
    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_sign(self) -> str:
        pass

    @abc.abstractmethod
    def calculation(self, a: int, b: int) -> int:
        pass


class DIV(Operation):
    def get_name(self) -> str:
        return "Целочисленное деление"

    def get_sign(self) -> str:
        return "//"

    def calculation(self, a: int, b: int) -> int:
        if b == 0:
            raise ZeroDivisionError("Деление на ноль")
        return a // b


class MOD(Operation):
    def get_name(self) -> str:
        return "Остаток от деления"

    def get_sign(self) -> str:
        return "%"

    def calculation(self, a: int, b: int) -> int:
        if b == 0:
            raise ZeroDivisionError("Деление на ноль")
        return a % b


class NOD(Operation):
    def get_name(self) -> str:
        return "Наибольший общий делитель"

    def get_sign(self) -> str:
        return "НОД"

    def calculation(self, a: int, b: int) -> int:
        return gcd(a, b)


class NOK(Operation):
    def get_name(self) -> str:
        return "Наименьшее общее кратное"

    def get_sign(self) -> str:
        return "НОК"

    def calculation(self, a: int, b: int) -> int:
        return lcm(a, b)


def get_two_numbers():
    while True:
        try:
            values = input('Введите 2 целых числа через пробел: ').strip().split()

            if len(values) != 2:
                print("Пожалуйста, введите ровно 2 числа")
                continue

            a, b = map(int, values)

            if a < 0 or b < 0:
                print("Пожалуйста, введите неотрицательные числа")
                continue

            return a, b

        except ValueError:
            print("Пожалуйста, введите целые числа")


def main():
    operations = [DIV(), MOD(), NOD(), NOK()]

    a, b = get_two_numbers()

    print(f"\nРезультаты для чисел {a} и {b}:")
    print("-" * 30)

    for operation in operations:
        try:
            result = operation.calculation(a, b)
            print(f"{operation.get_name()}: {a} {operation.get_sign():} {b} = {result}")
        except ZeroDivisionError:
            print(f"{operation.get_name()}: {a} {operation.get_sign()} {b} = Ошибка (деление на 0)")
        except Exception as e:
            print(f"{operation.get_name()}: {a} {operation.get_sign()} {b} = Ошибка: {e}")


if __name__ == '__main__':
    main()
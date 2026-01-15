import tkinter as tk
from tkinter import ttk, messagebox
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


class SimpleCalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор операций")
        self.window.geometry("300x300")

        self.operations = [DIV(), MOD(), NOD(), NOK()]

        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        # Заголовок
        tk.Label(self.window, text="Калькулятор операций",
                 font=("Arial", 14, "bold")).pack(pady=10)

        # Поля ввода
        tk.Label(self.window, text="Введите два числа:").pack(pady=5)

        input_frame = tk.Frame(self.window)
        input_frame.pack(pady=5)

        self.a_var = tk.StringVar(value="12")
        self.b_var = tk.StringVar(value="8")

        tk.Entry(input_frame, textvariable=self.a_var, width=10).pack(side="left", padx=5)
        tk.Label(input_frame, text="и").pack(side="left", padx=5)
        tk.Entry(input_frame, textvariable=self.b_var, width=10).pack(side="left", padx=5)


        # Фрейм для кнопок отдельных операций
        ops_frame = tk.Frame(self.window)
        ops_frame.pack(pady=5)

        for i, op in enumerate(self.operations):
            btn = tk.Button(ops_frame, text=op.get_name(),
                            command=lambda o=op: self.calculate(o),
                            width=30)
            btn.pack(pady=2)


    def calculate(self, operation):
        try:
            a = int(self.a_var.get())
            b = int(self.b_var.get())

            try:
                result = operation.calculation(a, b)
                messagebox.showinfo("Результат",
                                    f"{operation.get_name()}\n{a} {operation.get_sign()} {b} = {result}")
            except ZeroDivisionError:
                messagebox.showerror("Ошибка", f"{operation.get_name()}\nДеление на ноль!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"{operation.get_name()}\nОшибка: {e}")

        except ValueError:
            messagebox.showerror("Ошибка", "Введите целые числа!")


# Запуск приложения
if __name__ == '__main__':
    app = SimpleCalculatorGUI()
    app.run()


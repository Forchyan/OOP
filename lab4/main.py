import tkinter as tk
import tkinter.ttk as ttk


class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GUI")
        self.window.geometry("400x500")

        self.create_widgets()
        self.window.mainloop()

    def on_text_change(self, event=None):
        name = self.name_entry.get()
        greeting = f"Здравствуйте, {name}" if name else "Введите имя"
        self.greeting_label.config(text=greeting)

    def on_combobox_change(self, event=None):
        formula = self.func_combo.get()
        self.formula_label.config(text=self.names_and_functions[formula])

    def on_checkbox_change(self):
        state = self.enabled.get()
        self.login_entry.delete(0, tk.END)
        self.login_entry.insert(0, "admin")
        self.pass_entry.delete(0, tk.END)
        self.pass_entry.insert(0, "admin")

        if state:  # Если галочка установлена
            # Отключаем поля логина и пароля
            self.login_entry.config(state='disabled', bg='light gray')
            self.pass_entry.config(state='disabled', bg='light gray')
            self.auth_label.config(text="")


        else:  # Если галочка снята
            # Включаем поля обратно
            self.login_entry.config(state='normal', bg='white')
            self.pass_entry.config(state='normal', bg='white')

            # Очищаем поля
            self.login_entry.delete(0, tk.END)
            self.pass_entry.delete(0, tk.END)

            # Убираем сообщение
            self.auth_label.config(text="Введите свои данные")


    def create_widgets(self):
        # Блок с именем
        tk.Label(self.window, text="Введите своё имя:").pack(pady=5)
        self.name_entry = tk.Entry(self.window, width=20)
        self.name_entry.pack(pady=5)
        self.name_entry.bind("<KeyRelease>", self.on_text_change)

        # Метка для отображения приветствия
        self.greeting_label = tk.Label(self.window, text="")
        self.greeting_label.pack(pady=10)

        # Разделитель
        ttk.Separator(self.window, orient='horizontal').pack(fill='x', pady=10)

        # Блок с функциями
        tk.Label(self.window, text="Выберите функцию:").pack(pady=5)
        self.func_var = tk.StringVar(value='Линейная')
        self.names_and_functions = {
            'Линейная': 'y=kx+b',
            'Квадратичная': 'y=x^2',
            'Модуль': 'y=|x|',
            'Обратная пропорциональность': 'y=k/x',
            'Показательная': 'y=a^x',
            'Степенная': 'y=x^n',
            'Логарифмическая': 'y=log_a(x)'
        }
        self.func_combo = ttk.Combobox(
            self.window,
            textvariable=self.func_var,
            values=list(self.names_and_functions.keys()),
            state='readonly',
            width=25
        )
        self.func_combo.pack(pady=5)
        self.func_combo.bind("<<ComboboxSelected>>", self.on_combobox_change)

        self.formula_label = tk.Label(self.window, text='y=kx+b', font=('Arial', 10))
        self.formula_label.pack(pady=5)

        # Разделитель
        ttk.Separator(self.window, orient='horizontal').pack(fill='x', pady=10)

        # Блок авторизации
        auth_frame = tk.LabelFrame(self.window, text="Регистрация", padx=10, pady=10)
        auth_frame.pack(padx=10, pady=10, fill='x')

        # Чекбокс для использования данных по умолчанию
        self.enabled = tk.BooleanVar(value=True)  # По умолчанию включено
        self.enabled_checkbutton = ttk.Checkbutton(
            auth_frame,
            text="Использовать данные по умолчанию",
            variable=self.enabled,
            command=self.on_checkbox_change
        )
        self.enabled_checkbutton.pack(anchor='w', pady=5)

        # Поля логина и пароля
        tk.Label(auth_frame, text="Логин:").pack(anchor='w', pady=2)
        self.login_entry = tk.Entry(auth_frame, width=20)
        self.login_entry.pack(anchor='w', pady=2)

        tk.Label(auth_frame, text="Пароль:").pack(anchor='w', pady=2)
        self.pass_entry = tk.Entry(auth_frame, width=20, show="*")
        self.pass_entry.pack(anchor='w', pady=2)


        # Метка статуса авторизации
        self.auth_label = tk.Label(auth_frame, text="")
        self.auth_label.pack(pady=5)

        # Инициализируем состояние (вызываем обработчик чекбокса)
        self.on_checkbox_change()


def main():
    app = App()


if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import ttk, messagebox


class ListSelectorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Список профессий")
        self.window.geometry("700x400")

        self.available_items = [
            "Программист", "Врач", "Учитель", "Инженер", "Дизайнер",
            "Бухгалтер", "Юрист", "Архитектор", "Психолог", "Маркетолог",
            "Повар", "Пилот", "Строитель", "Фармацевт", "Электрик",
            "Переводчик", "Журналист", "Фотограф", "Музыкант", "Спортсмен"
        ]

        self.selected_items = []

        self.setup_ui()
        self.window.mainloop()

    def setup_ui(self):
        title_label = tk.Label(self.window, text="Выбор элементов между списками", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Основной фрейм с двумя списками
        main_frame = tk.Frame(self.window)
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Левый список
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=5)

        tk.Label(left_frame, text="Доступные элементы:", font=("Arial", 11)).pack(pady=5)

        # Создаем Listbox для доступных элементов
        self.available_listbox = tk.Listbox(left_frame, selectmode=tk.EXTENDED, height=12, font=("Arial", 10))
        self.available_listbox.pack(fill="both", expand=True)

        # Прокрутка
        left_scrollbar = tk.Scrollbar(self.available_listbox)
        left_scrollbar.pack(side="right", fill="y")
        self.available_listbox.config(yscrollcommand=left_scrollbar.set)
        left_scrollbar.config(command=self.available_listbox.yview)

        # Заполняем список доступными элементами
        for item in sorted(self.available_items):
            self.available_listbox.insert(tk.END, item)

        # Фрейм для кнопок между списками
        buttons_frame = tk.Frame(main_frame)
        buttons_frame.pack(side="left", padx=10, pady=40)

        # Кнопки для перемещения элементов
        tk.Button(buttons_frame, text="→", width=5, command=self.move_to_selected, bg="green").pack(pady=5)
        tk.Button(buttons_frame, text="←", width=5, command=self.move_to_available, bg="coral").pack(pady=5)
        tk.Button(buttons_frame, text="→→", width=5, command=self.move_all_to_selected, bg="blue").pack(pady=5)
        tk.Button(buttons_frame, text="←←", width=5, command=self.move_all_to_available, bg="pink").pack(pady=5)

        # Правый список
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side="left", fill="both", expand=True, padx=5)

        tk.Label(right_frame, text="Выбранные элементы:", font=("Arial", 11)).pack(pady=5)

        # Создаем Listbox для выбранных элементов
        self.selected_listbox = tk.Listbox(right_frame, selectmode=tk.EXTENDED, height=12, font=("Arial", 10))
        self.selected_listbox.pack(fill="both", expand=True)

        # Прокрутка
        right_scrollbar = tk.Scrollbar(self.selected_listbox)
        right_scrollbar.pack(side="right", fill="y")
        self.selected_listbox.config(yscrollcommand=right_scrollbar.set)
        right_scrollbar.config(command=self.selected_listbox.yview)

        # Кнопки управления внизу
        control_frame = tk.Frame(self.window)
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="Очистить выбранные", command=self.clear_selected, bg="orange").pack(side="left", padx=5)
        tk.Button(control_frame, text="Сохранить выбор", command=self.save_selection, bg="magenta").pack(side="left", padx=5)

    def move_to_selected(self):
        """Переместить выбранные элементы в правый список"""
        selected_indices = self.available_listbox.curselection()

        if not selected_indices:
            messagebox.showinfo("Информация", "Выберите элементы для перемещения")
            return

        selected_items = [self.available_listbox.get(i) for i in selected_indices]

        for item in selected_items:
            if item not in self.selected_items:
                self.selected_listbox.insert(tk.END, item)
                self.selected_items.append(item)

        for i in reversed(selected_indices):
            item = self.available_listbox.get(i)
            self.available_listbox.delete(i)
            if item in self.available_items:
                self.available_items.remove(item)

    def move_to_available(self):
        """Переместить выбранные элементы обратно в левый список"""
        selected_indices = self.selected_listbox.curselection()

        if not selected_indices:
            messagebox.showinfo("Информация", "Выберите элементы для возврата")
            return

        selected_items = [self.selected_listbox.get(i) for i in selected_indices]

        for item in selected_items:
            if item not in self.available_items:
                self.available_listbox.insert(tk.END, item)
                self.available_items.append(item)

        for i in reversed(selected_indices):
            item = self.selected_listbox.get(i)
            self.selected_listbox.delete(i)
            if item in self.selected_items:
                self.selected_items.remove(item)

        self.sort_available_list()

    def move_all_to_selected(self):
        """Переместить все элементы в правый список"""
        if not self.available_items:
            messagebox.showinfo("Информация", "Нет доступных элементов для перемещения")
            return

        for item in self.available_items[:]:  # Копируем список
            self.selected_listbox.insert(tk.END, item)
            self.selected_items.append(item)
            self.available_items.remove(item)

        self.available_listbox.delete(0, tk.END)

    def move_all_to_available(self):
        """Переместить все элементы обратно в левый список"""
        if not self.selected_items:
            messagebox.showinfo("Информация", "Нет выбранных элементов для возврата")
            return

        for item in self.selected_items[:]:  # Копируем список
            self.available_items.append(item)
            self.selected_items.remove(item)

        self.selected_listbox.delete(0, tk.END)
        self.sort_available_list()

        self.available_listbox.delete(0, tk.END)
        for item in sorted(self.available_items):
            self.available_listbox.insert(tk.END, item)

    def sort_available_list(self):
        """Сортировка доступных элементов"""
        self.available_items.sort()

    def clear_selected(self):
        """Очистить все выбранные элементы"""
        if not self.selected_items:
            return

        if not messagebox.askyesno("Подтверждение","Очистить все выбранные элементы?"):
            return

        self.move_all_to_available()

    def save_selection(self):
        """Сохранить текущий выбор"""
        if not self.selected_items:
            messagebox.showinfo("Информация", "Нет выбранных элементов для сохранения")
            return

        filename = "мой_выбор.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Выбранные элементы:\n")
            for item in self.selected_items:
                f.write(f"{item}\n")

        messagebox.showinfo("Сохранение", f"Выбрано {len(self.selected_items)} элементов:\n" + "\n".join(self.selected_items) + f"\n\nСохранено в {filename}")


def main():
    app = ListSelectorApp()

# Запуск приложения
if __name__ == "__main__":
    main()
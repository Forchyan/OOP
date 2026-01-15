import tkinter as tk
from tkinter import ttk


class DepositCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор вклада с капитализацией")
        self.window.geometry("400x450")

        # Ставки по вкладам (номинальные годовые ставки)
        self.rates = {
            "1 месяц": {"до 100 тыс.": 10.0, "100-500 тыс.": 10.5, "500 тыс.-1 млн": 11.0, "свыше 1 млн": 11.5},
            "2 месяца": {"до 100 тыс.": 10.2, "100-500 тыс.": 11.0, "500 тыс.-1 млн": 11.5, "свыше 1 млн": 12.0},
            "3 месяца": {"до 100 тыс.": 10.5, "100-500 тыс.": 11.5, "500 тыс.-1 млн": 12.0, "свыше 1 млн": 12.5},
            "6 месяцев": {"до 100 тыс.": 11.0, "100-500 тыс.": 12.0, "500 тыс.-1 млн": 12.5, "свыше 1 млн": 13.0},
            "9 месяцев": {"до 100 тыс.": 11.5, "100-500 тыс.": 12.5, "500 тыс.-1 млн": 13.0, "свыше 1 млн": 13.5},
            "1 год": {"до 100 тыс.": 12.0, "100-500 тыс.": 13.0, "500 тыс.-1 млн": 13.5, "свыше 1 млн": 14.0},
            "2 года": {"до 100 тыс.": 12.0, "100-500 тыс.": 13.5, "500 тыс.-1 млн": 14.0, "свыше 1 млн": 14.5}
        }

        # Периоды капитализации (в месяцах для перевода в годы)
        self.periods_in_months = {
            "1 месяц": 1 / 12,
            "2 месяца": 2 / 12,
            "3 месяца": 3 / 12,
            "6 месяцев": 6 / 12,
            "9 месяцев": 9 / 12,
            "1 год": 1,
            "2 года": 2
        }

        self.create_widgets()

    def create_widgets(self):
        # Сумма вклада
        tk.Label(self.window, text="Сумма вклада (руб):").pack(pady=5)
        self.amount_entry = tk.Entry(self.window, width=25)
        self.amount_entry.pack(pady=5)
        self.amount_entry.insert(0, "30000")

        # Срок вклада
        tk.Label(self.window, text="Срок вклада:").pack(pady=5)
        self.period_var = tk.StringVar(value="1 год")
        periods = list(self.rates.keys())
        self.period_combo = ttk.Combobox(self.window, textvariable=self.period_var, values=periods, state="readonly", width=18)
        self.period_combo.pack(pady=5)

        # Период капитализации
        tk.Label(self.window, text="Период капитализации:").pack(pady=5)
        self.capitalization_freq_var = tk.StringVar(value="Ежемесячно")
        self.capitalization_combo = ttk.Combobox(self.window,
            textvariable=self.capitalization_freq_var,
            values=["Без капитализации", "Ежегодно", "Ежеквартально", "Ежемесячно", "Ежедневно"],
            state="readonly",
            width=18)
        self.capitalization_combo.pack(pady=5)

        # Кнопка расчета
        tk.Button(self.window,
            text="Рассчитать доход",
            command=self.calculate,
            bg="lightblue",
            width=15).pack(pady=15)

        # Результат
        self.result_frame = tk.Frame(self.window, relief="solid", borderwidth=1)
        self.result_frame.pack(pady=10, padx=10, fill="x")

        self.result_label = tk.Label(self.result_frame, text="", justify="left")
        self.result_label.pack(pady=10, padx=10)

    def calculate(self):
        try:
            amount = float(self.amount_entry.get().replace(" ", "").replace(",", "."))
            period = self.period_var.get()
            capitalization_type = self.capitalization_freq_var.get()

            if amount < 30000:
                self.result_label.config(text="Ошибка: сумма должна быть >= 30000", fg="red")
                return

            # Определяем категорию суммы
            if amount < 100000:
                category = "до 100 тыс."
            elif amount <= 500000:
                category = "100-500 тыс."
            elif amount <= 1000000:
                category = "500 тыс.-1 млн"
            else:
                category = "свыше 1 млн"

            # Получаем номинальную ставку C (в %)
            C = self.rates[period][category]  # номинальная годовая ставка в %

            # Длительность депозита в годах (Д)
            D = self.periods_in_months[period]  # уже в годах

            # Определяем П (количество периодов капитализации в год)
            if capitalization_type == "Без капитализации":
                P = 1  # проценты начисляются один раз в конце срока
            elif capitalization_type == "Ежегодно":
                P = 1
            elif capitalization_type == "Ежеквартально":
                P = 4
            elif capitalization_type == "Ежемесячно":
                P = 12
            elif capitalization_type == "Ежедневно":
                P = 365
            else:
                P = 1

            # Эффективная ставка = ((1 + C/(100×P))^(P×D) - 1) × 100/D

            if capitalization_type == "Без капитализации":
                # Простой процент
                total_amount = amount * (1 + C / 100 * D)
                income = total_amount - amount
                effective_rate = C  # для простого процента эффективная = номинальной
            else:
                # Сложный процент с капитализацией
                total_amount = amount * (1 + C / (100 * P)) ** (P * D)
                income = total_amount - amount

                # Расчет эффективной процентной ставки (годовой)
                effective_rate = ((1 + C / (100 * P)) ** (P * D) - 1) * 100 / D

            result_text = f"Номинальная ставка: {C:.2f}%\n"
            result_text += f"Эффективная ставка: {effective_rate:.2f}%\n"
            result_text += f"Категория: {category}\n"
            result_text += f"Срок: {period}\n"
            result_text += f"Капитализация: {capitalization_type}\n"
            result_text += f"Периодов в год (П): {P}\n"
            result_text += "─" * 30 + "\n"
            result_text += f"Начальная сумма: {amount:,.0f} руб.\n"
            result_text += f"Доход: {income:,.0f} руб.\n"
            result_text += f"Итоговая сумма: {total_amount:,.0f} руб."

            self.result_label.config(text=result_text, fg="darkblue")

        except ValueError:
            self.result_label.config(text="Ошибка: введите корректную сумму", fg="red")
        except Exception as e:
            self.result_label.config(text=f"Ошибка: {str(e)}", fg="red")

    def run(self):
        self.window.mainloop()


# Запуск приложения
if __name__ == "__main__":
    app = DepositCalculator()
    app.run()
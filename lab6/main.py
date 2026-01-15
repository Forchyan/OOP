import tkinter as tk
import threading
import time
import random


class MovingShapes:
    def __init__(self):
        self.windows = tk.Tk()
        self.windows.title("3 потока - 3 фигуры")

        self.canvas = tk.Canvas(self.windows, width=400, height=400, bg="white")
        self.canvas.pack()

        self.circle_pos = [random.randrange(50, 351, 25), random.randrange(50, 351, 25)]
        self.square_pos = [random.randrange(50, 351, 25), random.randrange(50, 351, 25)]
        self.triangle_pos = [random.randrange(50, 351, 25), random.randrange(50, 351, 25)]

        self.circle = self.canvas.create_oval(
            self.circle_pos[0] - 25, self.circle_pos[1] - 25,
            self.circle_pos[0] + 25, self.circle_pos[1] + 25,
            fill="red"
        )
        self.square = self.canvas.create_rectangle(
            self.square_pos[0] - 25, self.square_pos[1] - 25,
            self.square_pos[0] + 25, self.square_pos[1] + 25,
            fill="blue"
        )
        self.triangle = self.canvas.create_polygon(
            self.triangle_pos[0], self.triangle_pos[1] - 25,
            self.triangle_pos[0] - 25, self.triangle_pos[1] + 25,
            self.triangle_pos[0] + 25, self.triangle_pos[1] + 25,
            fill="green"
        )

        self.circle_speed = [2, 3]
        self.square_speed = [-3, 2]
        self.triangle_speed = [1, -2]

        # Флаг для потоков
        self.running = True

        # Запускаем потоки
        self.start_threads()

        self.windows.mainloop()

    def move_circle(self):
        """Поток для круга"""
        while self.running:
            # Обновляем позицию
            self.circle_pos[0] += self.circle_speed[0]
            self.circle_pos[1] += self.circle_speed[1]

            # Отскок от границ
            if self.circle_pos[0] <= 25 or self.circle_pos[0] >= 375:
                self.circle_speed[0] = -self.circle_speed[0]
            if self.circle_pos[1] <= 25 or self.circle_pos[1] >= 375:
                self.circle_speed[1] = -self.circle_speed[1]

            # Обновление на канвасе
            self.canvas.coords(self.circle,
                               self.circle_pos[0] - 25, self.circle_pos[1] - 25,
                               self.circle_pos[0] + 25, self.circle_pos[1] + 25)

            time.sleep(0.03)

    def move_square(self):
        """Поток для квадрата"""
        while self.running:
            self.square_pos[0] += self.square_speed[0]
            self.square_pos[1] += self.square_speed[1]

            # Отскок от границ
            if self.square_pos[0] <= 25 or self.square_pos[0] >= 375:
                self.square_speed[0] = -self.square_speed[0]
            if self.square_pos[1] <= 25 or self.square_pos[1] >= 375:
                self.square_speed[1] = -self.square_speed[1]

            # Обновление на канвасе
            self.canvas.coords(self.square,
                               self.square_pos[0] - 25, self.square_pos[1] - 25,
                               self.square_pos[0] + 25, self.square_pos[1] + 25)

            time.sleep(0.04)

    def move_triangle(self):
        """Поток для треугольника"""
        while self.running:
            self.triangle_pos[0] += self.triangle_speed[0]
            self.triangle_pos[1] += self.triangle_speed[1]

            # Отскок от границ
            if self.triangle_pos[0] <= 25 or self.triangle_pos[0] >= 375:
                self.triangle_speed[0] = -self.triangle_speed[0]
            if self.triangle_pos[1] <= 25 or self.triangle_pos[1] >= 375:
                self.triangle_speed[1] = -self.triangle_speed[1]

            # Обновление на канвасе
            self.canvas.coords(self.triangle,
                               self.triangle_pos[0], self.triangle_pos[1] - 25,
                               self.triangle_pos[0] - 25, self.triangle_pos[1] + 25,
                               self.triangle_pos[0] + 25, self.triangle_pos[1] + 25)

            time.sleep(0.01)

    def on_closing(self):
        """Остановка потоков при закрытии"""
        self.running = False
        self.windows.destroy()

    def start_threads(self):
        """Запуск потоков"""
        thread1 = threading.Thread(target=self.move_circle, daemon=True)
        thread2 = threading.Thread(target=self.move_square, daemon=True)
        thread3 = threading.Thread(target=self.move_triangle, daemon=True)

        thread1.start()
        thread2.start()
        thread3.start()

        # Обработка закрытия окна
        self.windows.protocol("WM_DELETE_WINDOW", self.on_closing)


def main():
    app = MovingShapes()

if __name__ == '__main__':
    main()
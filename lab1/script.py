import json
from typing import List, Dict, Any


class Film:
    def __init__(self, title: str, director: str, year: int):
        self.title = title
        self.director = director
        self.year = year

    def to_dict(self) -> Dict[str, Any]:
        """Конвертирует объект в словарь для JSON"""
        return {
            'title': self.title,
            'director': self.director,
            'year': self.year
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Film':
        """Создает объект из словаря"""
        return cls(data['title'], data['director'], data['year'])

    def __str__(self):
        return f"{self.title} ({self.year}), реж. {self.director}"


class FilmManager:
    def __init__(self):
        self.films: List[Film] = []

    def add_film(self, title: str, director: str, year: int):
        """Добавляет фильм в коллекцию"""
        self.films.append(Film(title, director, year))

    def add_film_manually(self):
        """Ручное добавление фильма через консоль"""
        print("\n--- Добавление нового фильма ---")
        title = input("Название фильма: ").strip()
        director = input("Режиссер: ").strip()
        year = input("Год выпуска: ").strip()

        if not year.isdigit():
            print("Ошибка: год должен быть числом!")
            return

        self.add_film(title, director, int(year))
        print(f"Фильм '{title}' успешно добавлен!")

    def sort_by(self, field: str):
        """Сортировка фильмов по указанному полю"""
        if field == 'title':
            self.films.sort(key=lambda film: film.title.lower())
        elif field == 'director':
            self.films.sort(key=lambda film: film.director.lower())
        elif field == 'year':
            self.films.sort(key=lambda film: film.year)

    def display_table(self):
        """Вывод фильмов в виде таблицы"""
        if not self.films:
            print("\nСписок фильмов пуст!")
            return

        print("\n" + "=" * 60)
        print(f"{'№':<3} | {'Название':<20} | {'Режиссер':<15} | {'Год':<6}")
        print("-" * 60)

        for i, film in enumerate(self.films, 1):
            print(f"{i:<3} | {film.title:<20} | {film.director:<15} | {film.year:<6}")
        print("=" * 60)

    def save_to_json(self, filename: str):
        """Сохранение фильмов в JSON"""
        try:
            data = [film.to_dict() for film in self.films]
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"\nДанные успешно сохранены в файл: {filename}")
        except Exception as e:
            print(f"\nОшибка при сохранении: {e}")

    def load_from_json(self, filename: str):
        """Загрузка фильмов из JSON файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            loaded_films = [Film.from_dict(item) for item in data]
            self.films.extend(loaded_films)

            print(f"\nЗагружено {len(loaded_films)} фильмов из файла: {filename}")
            print(f"Всего фильмов в списке: {len(self.films)}")

        except FileNotFoundError:
            print(f"\nФайл '{filename}' не найден!")
        except Exception as e:
            print(f"\nОшибка при загрузке: {e}")


def main():
    manager = FilmManager()

    while True:
        print("\n" + "=" * 40)
        print("МЕНЮ УПРАВЛЕНИЯ ФИЛЬМАМИ")
        print("=" * 40)
        print("1. Показать все фильмы (таблица)")
        print("2. Добавить фильм вручную")
        print("3. Сортировать по названию")
        print("4. Сортировать по режиссеру")
        print("5. Сортировать по году")
        print("6. Сохранить в JSON файл")
        print("7. Загрузить из JSON файла")
        print("8. Выход")
        print("-" * 40)

        choice = input("Выберите действие (1-8): ").strip()

        if choice == '1':
            manager.display_table()

        elif choice == '2':
            manager.add_film_manually()

        elif choice == '3':
            manager.sort_by('title')
            print("\nФильмы отсортированы по названию!")
            manager.display_table()

        elif choice == '4':
            manager.sort_by('director')
            print("\nФильмы отсортированы по режиссеру!")
            manager.display_table()

        elif choice == '5':
            manager.sort_by('year')
            print("\nФильмы отсортированы по году!")
            manager.display_table()

        elif choice == '6':
            filename = input("Введите имя файла для сохранения (например: films.json): ").strip()
            if not filename.endswith('.json'):
                filename += '.json'
            manager.save_to_json(filename)

        elif choice == '7':
            filename = input("Введите имя файла для загрузки (например: films.json): ").strip()
            if not filename.endswith('.json'):
                filename += '.json'
            manager.load_from_json(filename)
            manager.display_table()

        elif choice == '8':
            print("\nДо свидания!")
            break

        else:
            print("\nНеверный выбор! Пожалуйста, выберите от 1 до 8.")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    # Можно добавить аргумент командной строки для запуска тестов
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        # Импортируем и запускаем тесты
        import unittest

        # Здесь вставьте тестовые классы (TestFilm, TestFilmManager и т.д.)
        # ...

        unittest.main(argv=[sys.argv[0]])
    else:
        main()

# if __name__ == "__main__":
#     main()
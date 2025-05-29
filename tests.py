from main import BooksCollector
from qa_python.conftest import b_collector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # 1 f 1 test
    def test_add_new_book_add_two_books(self):

        # добавляем две книги
        b_collector.add_new_book('Гордость и предубеждение и зомби')
        b_collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод add_new_books, имеет длину 2
        assert len(b_collector.books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1 f 2 test проверка невалидного имени книги (граничные значения: 0 символов и 41 символ)
    @pytest.mark.parametrize("name", ["", "abcdi fghij klmno pqrst uvwxy zabcd ifghi"])
    def test_add_new_book_less_more_len_name(self, b_collector, name):
        assert name not in b_collector.books_genre

    # 2 f 1 test
    def test_set_book_genre_add_genre(self, b_collector):
        b_collector.add_new_book("Красная шапочка")  # добавляем книгу
        b_collector.set_book_genre("Красная шапочка", "Мультфильмы")  # устанавливаем жанр
        assert b_collector.books_genre["Красная шапочка"] == "Мультфильмы"  # проверяем, что жанр добавился

    # 3 f 1 test
    def test_get_book_genre_show_genre(self, name):
        b_collector.add_new_book("Ого")    # добавляем книгу
        b_collector.set_book_genre("Ого", "Ужасы")   # устанавливаем жанр
        assert b_collector.books_genre.get("Ого") == "Ужасы"   # получаем жанр книги по названию

    # 4 f 1 test
    def test_get_books_with_specific_genre_show_list_books(self, b_collector):
        b_collector.add_new_book("Ого")  # добавляем книгу
        b_collector.set_book_genre("Ого", "Ужасы")   # устанавливаем жанр
        b_collector.add_new_book("Огров")  # добавляем книгу
        b_collector.set_book_genre("Огров", "Фантастика")   # устанавливаем жанр
        b_collector.add_new_book("Ву-ву")  # добавляем книгу
        b_collector.set_book_genre("Ву-ву", "Ужасы")   # устанавливаем жанр
        assert b_collector.get_books_with_specific_genre("Ужасы") == "Ого", "Ву-ву"

        # получаем словарь books_genre
        def get_books_genre(self):
            return self.books_genre
    # 5 f 1 test
    def test_get_books_genre_show_list(self):
        b_collector.add_new_book("Ого")  # добавляем книгу
        b_collector.set_book_genre("Ого", "Ужасы")  # устанавливаем жанр
        b_collector.add_new_book("Огров")  # добавляем книгу
        b_collector.set_book_genre("Огров", "Фантастика")  # устанавливаем жанр
        assert b_collector.get_books_genre == {"Ого" : "Ужасы", "Огров" : "Фантастика"}

    # 6 f 1 test
    def test_get_books_for_children_show_books(self, b_collector):
        b_collector.add_new_book("Ого")  # добавляем книгу
        b_collector.set_book_genre("Ого", "Ужасы")  # устанавливаем жанр
        b_collector.add_new_book("Огров")  # добавляем книгу
        b_collector.set_book_genre("Огров", "Фантастика")  # устанавливаем жанр
        b_collector.add_new_book("Гарри Поттер")  # добавляем книгу
        b_collector.set_book_genre("Гарри Поттер", "Мультфильмы")  # устанавливаем жанр
        assert b_collector.get_books_for_children() == ["Огров", "Гарри Поттер"]

    # 7 f 1 test
    def test_add_book_in_favorites_show_books(self, b_collector):
        b_collector.add_new_book("Огров")  # добавляем книгу
        b_collector.add_new_book_in_favorites ("Огров") #
        assert "Огров" in b_collector.favorites #

    # 8 f 1 test
    def test_delete_book_from_favorites_delete_book(self, b_collector):
        b_collector.add_new_book("Огров")  # добавляем книгу
        b_collector.add_new_book_in_favorites("Огров") #
        b_collector.delete_book_from_favorites("Огров")
        assert "Огров" not in b_collector.favorites

    # 9 f 1 test
    def test_get_list_of_favorites_books(self, b_collector):
        b_collector.add_new_book("Ого")  # добавляем книгу
        b_collector.add_new_book_in_favorites("Ого")  # в избранные
        b_collector.add_new_book("Огров")  # добавляем книгу
        b_collector.add_new_book_in_favorites("Огров")  # в избранные
        b_collector.add_new_book("Гарри Поттер")  # добавляем книгу
        b_collector.add_new_book_in_favorites("Гарри Поттер")  # в избранные
        assert b_collector.favorites == ["Ого", "Огров", "Гарри Поттер"]


from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_with_name_more_40_symbols(self):
        collector = BooksCollector()
        collector.add_new_book('Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче и о прекрасной Царевне Лебеди')
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        "book_name, genre",
        [
        ('Гордость и предубеждение и зомби', 'Фантастика'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
        ('Убийство по алфавиту', 'Детективы'),
        ('Снежная королева', 'Мультфильмы'),
        ('Недоросль', 'Комедии')
        ]
    )
    def test_set_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book('Идиот')
        collector.set_book_genre('Идиот', 'Комедия')
        assert collector.get_book_genre(book_name) == 'Комедия'

    def test_get_book_genre_nonexistent(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Вий')
        collector.set_book_genre('Вий', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Вий']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Философский камень')
        collector.set_book_genre('Гарри Поттер и Философский камень', 'Фантастика')
        assert collector.get_books_genre() == {'Гарри Поттер и Философский камень': 'Фантастика'}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Тома Сойера')
        collector.set_book_genre('Приключения Тома Сойера', 'Комедии')
        assert collector.get_books_for_children() == ['Приключения Тома Сойера']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Граф Монте-Кристо')
        collector.add_book_in_favorites('Граф Монте-Кристо')
        assert collector.get_list_of_favorites_books() == ['Граф Монте-Кристо']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Евгений Онегин')
        collector.add_book_in_favorites('Евгений Онегин')
        collector.delete_book_from_favorites('Евгений Онегин')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Золушка')
        collector.add_book_in_favorites('Золушка')
        assert collector.get_list_of_favorites_books() == ['Золушка']
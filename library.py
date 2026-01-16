from book import Book

class Library:
    def __init__(self, name, books_lst=None):
        if books_lst is None:
            books_lst = []
        self.name = name
        self.books_lst = books_lst

    def add_book(self, book: Book):
        self.books_lst.append(book)


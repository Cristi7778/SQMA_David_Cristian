class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        if not title:
            raise ValueError("Title cannot be empty")
        self.books.append(title)

    def remove_book(self, title):
        if title not in self.books:
            raise KeyError("Book not found")
        self.books.remove(title)

    def get_count(self):
        return len(self.books)
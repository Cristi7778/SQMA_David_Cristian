import pytest
from library import Library

@pytest.mark.parametrize("book_titles, expected_count", [
    (["Book 1", "Book 2"], 2),
    (["A", "B", "C", "D"], 4),
    ([], 0),
    (["Duplicate", "Duplicate"], 2)
])
def test_multiple_book_additions(book_titles, expected_count):
    lib = Library()
    for title in book_titles:
        lib.add_book(title)
    assert lib.get_count() == expected_count

def test_bulk_removal():
    lib = Library()
    list_of_books = ["Python 101", "Docker Pro", "Jenkins Expert"]
    for b in list_of_books:
        lib.add_book(b)
    
    lib.remove_book("Docker Pro")
    assert "Docker Pro" not in lib.books
    assert lib.get_count() == 2
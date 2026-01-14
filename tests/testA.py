import pytest
from library import Library

@pytest.fixture
def empty_lib():
    return Library()

def test_add_book_success(empty_lib):
    empty_lib.add_book("The Great Gatsby")
    assert empty_lib.get_count() == 1
    assert "The Great Gatsby" in empty_lib.books

def test_add_empty_title_raises_error(empty_lib):
    with pytest.raises(ValueError, match="Title cannot be empty"):
        empty_lib.add_book("")

def test_remove_nonexistent_book(empty_lib):
    with pytest.raises(KeyError):
        empty_lib.remove_book("Unknown Book")
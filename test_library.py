import pytest
from library import Library


def make_library():
    library = Library()
    library.add_book("Python Basics", 2)
    return library


def test_add_book():
    library = make_library()
    assert library.add_book("Python Basics", 3) == 5


def test_check_availability():
    library = make_library()
    assert library.check_availability("Python Basics") is True


def test_issue_book():
    library = make_library()
    assert library.issue_book("Python Basics") is True
    assert library.get_copies("Python Basics") == 1


def test_return_book():
    library = make_library()
    library.issue_book("Python Basics")
    assert library.return_book("Python Basics") == 2


def test_issue_unavailable_book():
    library = Library()
    library.add_book("Data Structures", 1)
    library.issue_book("Data Structures")
    assert library.issue_book("Data Structures") is False
    assert library.check_availability("Data Structures") is False


def test_book_not_found():
    library = Library()
    with pytest.raises(KeyError):
        library.check_availability("Unknown Book")

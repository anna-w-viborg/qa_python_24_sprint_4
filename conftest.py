import pytest

from main import BooksCollector

@pytest.fixture
def b_collector():
    b_collector = BooksCollector()
    return b_collector
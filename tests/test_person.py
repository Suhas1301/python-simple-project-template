import pytest

from person import Person

@pytest.fixture
def get_john_smith():
    print("Setting up John Smith ...")
    person = Person("John", "Smith")
    yield person.fullname()

    print("Tearing down John Smith")

def test_john_smith(get_john_smith):
    fullname = get_john_smith
    assert fullname is not None
    assert fullname == "John Smith"

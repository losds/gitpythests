import pytest
@pytest.fixture
def set_up():
    print("You are login!")
    yield
    print("Exit from system!")


@pytest.fixture
def some(scope = 'module'):
    print("Start!")
    yield
    print("End!")
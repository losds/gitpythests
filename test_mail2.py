import pytest

#deistvie do
@pytest.fixture
def set_up():
    print("You are login!")
    yield
    print("Exit from system!")
#parametr kotoryi peredaem
def test_sending_mail1(set_up):
    print("The letter sended")

def test_sending_mail2(set_up):
    print("The letter sended")


#pytest -s -v
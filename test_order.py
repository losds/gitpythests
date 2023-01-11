import pytest
@pytest.mark.run(order =2)
def test_method_1(set_up):
    print("Method1")
@pytest.mark.run(order =1)
def test_method_2(set_up):
    print("Method2")

def test_method_3(set_up):
    print("Method3")

def test_method_4(set_up):
    print("Method4")

def test_method_5(set_up):
    print("Method5")

def test_method_7(set_up):
    print("Method7")

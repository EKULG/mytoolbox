from mytoolbox.lib import factorial

def test_factorial():
    assert factorial(5) == 120

def test_factorial2():
    assert factorial(1) == 1

def test_factorial3():
    assert type(factorial(3)) == int or float

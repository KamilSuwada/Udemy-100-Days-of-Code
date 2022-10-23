
# specification of default values.
from os import access


def function1(a:int=1, b:int=2, c:int=3):
    print(f"{a} {b} {c}")


function1()



# *args = multiple positional arguments as tuple
def add(*args):
    x = 0

    for n in args:
        x += n
    
    return x


print(add(1,2,3,4,5,6,7,8,9,10))



# **kwargs = multiple keyword arguments as dictionary
def calculate(n:int = 0, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(1, add=3, multiply=5)
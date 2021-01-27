from random import *

def grader1_3_1(function):
    if hasattr(function,"__call__") == False:
        print("You didn't pass me a function :'(")
        return None
    errors = 0
    for i in range(50):
        foo = randint(1,100)
        bar = randint(1,100)
        if function(foo,bar) != foo + bar:
            errors += 1
    if errors == 0:
        print("Great job! Your function passed all tests")
        return None
    if errors != 0:
        print("Uh-oh! Your function didn't quite work right. Check the docstring and make sure everythings written properly!")
        return None

def grader1_3_2(function):
    if hasattr(function,"__call__") == False:
        print("You didn't pass me a function :'(")
        return None
    errors = 0
    for i in range(50):
        array = [[randint(1,100) for y in range(randint(2,100))] for x in range(randint(2,100))]
        if function(array) != [array[0][0],array[-1][0],array[0][-1],array[-1][-1]]:
            errors += 1
    if errors == 0:
        print("Great job! Your function passed all tests")
        return None
    if errors != 0:
        print("Uh-oh! Your function didn't quite work right. Check the docstring and make sure everythings written properly!")
        return None
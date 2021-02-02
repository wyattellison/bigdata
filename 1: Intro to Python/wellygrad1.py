from random import *
import numpy as np

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

def grader1_4_1(function):
    """
    Create a matrix full of zeros of the same shape as an input matrix
    
    Input: input_matrix type: numpy matrix of variable shape M x N
    
    Output: numpy matrix of only 0s (in integer form, not floats) of shape M x N
    
    hint: numpy array's shape method and np.zeros (check the docstrings!)
    """
    if hasattr(function,"__call__") == False:
        print("You didn't pass me a function :'(")
        return None
    errors = 0
    for i in range(50):
        array = np.random.randint(0,100,size=(randint(1,50),randint(1,50)))
        if function(array).all() != np.zeros(array.shape).all():
            errors += 1
    if errors == 0:
        print("Great job! Your function passed all tests")
        return None
    if errors != 0:
        print("Uh-oh! Your function didn't quite work right. Check the docstring and make sure everythings written properly!")
        return None

def grader1_4_2(function):
    """
    Create a matrix full of a specified number of the same shape as an input matrix
    
    Input: input_matrix type: numpy matrix of variable shape M x N
           input_filler type: integer or float 
    
    Output: numpy matrix of only input_fillers (in integer form, not floats) of shape M x N
    
    hint: if you don't know the numpy function to use, google it!
    """
    if hasattr(function,"__call__") == False:
        print("You didn't pass me a function :'(")
        return None
    errors = 0
    for i in range(50):
        array = np.random.randint(0,100,size=(randint(1,50),randint(1,50)))
        filler = randint(1,100)
        if function(array).all() != np.full(array.shape,filler).all():
            errors += 1
    if errors == 0:
        print("Great job! Your function passed all tests")
        return None
    if errors != 0:
        print("Uh-oh! Your function didn't quite work right. Check the docstring and make sure everythings written properly!")
        return None

def grader1_4_3(function):
    """
    input: input_matrix of type numpy.ndarray of shape (M,N)
    output: python list of each column in input_matrix
    returns a list of each column in the input_matrix
    """
    if hasattr(function,"__call__") == False:
        print("You didn't pass me a function :'(")
        return None
    errors = 0
    for i in range(50):
        array = np.random.randint(0,100,size=(randint(2,50),randint(2,50)))
        if np.array(function(array)).all() !=  array.T.all():
            errors += 1
    if errors == 0:
        print("Great job! Your function passed all tests")
        return None
    if errors != 0:
        print("Uh-oh! Your function didn't quite work right. Check the docstring and make sure everythings written properly!")
        return None

def grader1_4_4(function):
    """
    input: input_matrix of type numpy.ndarray of shape (M,N)
           index of type np.ndarray of shape (2,) where the cell will never be on the edge of input_matrix
    output: np.ndarray of shape (8,)
    returns a list of the value of each Moore neighbor of radius = 1 surrounding the given index starting from the top left and going counter-clockwise
    example:
    input_matrix = np.array([[1 ,2 ,3 ,4 ,5 ],
                             [6 ,7 ,8 ,9 ,10],
                             [11,12,13,14,15],
                             [16,17,18,19,20],
                             [21,22,23,24,25]])
    index = [2,3] #corresponds to 14 in input_matrix
    
    moore_neighbors(input_matrix,index) #should return [8,13,18,19,20,15,10,9]
    """
    if hasattr(function,"__call__") == False:
        print("You didn't pass me a function :'(")
        return None
    errors = 0
    for i in range(50):
        size = (randint(4,50),randint(4,50))
        array = np.random.randint(0,100,size=size)
        index = (randint(1,size[0]-2),randint(1,size[1]-2))
        indices = ([index[0]-1,index[0],index[0]+1,index[0]+1,index[0]+1,index[0],index[0]-1,index[0]-1],
                    [index[1]-1,index[1]-1,index[1]-1,index[1],index[1]+1,index[1]+1,index[1]+1,index[1]])
        
        if function(array,index).all() !=  array[indices].all():
            errors += 1
    if errors == 0:
        print("Great job! Your function passed all tests")
        return None
    if errors != 0:
        print("Uh-oh! Your function didn't quite work right. Check the docstring and make sure everythings written properly!")
        return None
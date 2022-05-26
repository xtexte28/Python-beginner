# -*- coding: utf-8 -*-
"""
Created on Sat May  7 12:18:54 2022

@author: Rock
"""

def decorator_1(func):
    def new_function(*args,**kwargs):
        print('Running function:',func.__name__)
        print('Positional arguments',args)
        print('Keyword argument:',kwargs)
        result = func(*args,**kwargs)
        print('Result:',result)
        return result
    return new_function

@decorator_1
def add_ints(a,b):
    return a+b

add_ints(3,7)


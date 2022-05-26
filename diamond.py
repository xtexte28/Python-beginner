# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 19:55:34 2021

@author: Rock
"""


def diamond2(n):
    for i in range(n):
        print(' '*(n-i)+'*'*(2*i-1))

    for i in range(n,0,-1):
        print(' '*(n-i)+'*'*(2*i-1))

n = int(input("layer:"))
diamond2(n)


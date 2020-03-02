# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:01:01 2020

@author: Mohammad Shahnawaz
"""
# User Define Function

# Create Simple Function
# create Function
def func():
    print('Hello! Python')

# Function has been called
func()

# Function has the prameter
def func_para(var): # mandatory paramete
    print('Value is passed',var)

func_para()
func_para(10)

def func_para1(var,var1,var2):
    print('First Argument values is',var)
    print('Second Argument values is',var1)
    print('Third Argument values is',var2)
    
# function calling
func_para1(10)
func_para1(10,20)
func_para1(10,20,30)

x=100
print(x)
x=200
print(x)

def func_with_return():
    x=float(input('Enter a number'))
    y=float(input('Enter a number'))
    res=x+y
    return res
func_with_return()
result=func_with_return()
print(result)


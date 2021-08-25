import numpy as np
import math

def func(x):
    return 2-(x**2)

a = 0.0
b = 50.0
while abs(func((a+b)/2)) >= (10**(-6)) and abs(a-b) >= (10**(-6)):

    if func((a+b)/2) < 0:
        b = (a+b)/2

    if func((a+b)/2) > 0:
        a = (a+b)/2        
        
print((a+b)/2)

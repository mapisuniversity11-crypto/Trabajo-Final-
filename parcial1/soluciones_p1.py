import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def f1(func, a, b):
    ResultadoFinal = 0
    for i in range(a, b + 1):
        ResultadoFinal += func(i) * i
    return ResultadoFinal

def f2(L):
    def f(x):
        Result = 0
        for i in range(len(L)):
            Result += L[i] * (x ** i)
        return Result
    return f

def f3(x0, y0):
    def recta(x):
        return 2 * (x - x0) + y0  
    def paralela(x):
        return 2 * (x - 1) + 1 
    return recta, paralela

def f4(L):
    L = [x for x in L if x > 10 and (int(str(x)[0]) + int(str(x)[-1])) % 2 == 0]
    return sum(L)
import numpy as np
from scipy.optimize import minimize

import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet('Sheet 1')
sheet1.write(0,0,'Метод внешних штрафов')
sheet1.write(1, 0, 'Номер итерации')
sheet1.write(1, 1,'x' )
sheet1.write(1, 2,'y' )
sheet1.write(1, 3,'Значение x^2+y^2-1' )
sheet1.write(1, 4, 'Значение x-y')
sheet1.write(1, 5, 'Значение функции')
sheet1.write(1, 6, 'Значение штрафной функции')
sheet1.write(1, 7, "Коэффиецент")
sheet1.write(1, 8, "Количество вызовов функции")
a = complex(8, 5)
b = complex(5, 8)
li = complex(0, 1)
EPS = 1e-8
P = np.array([1, a, b])
def Horner(z, poly):
    ans = complex(0, 0)
    for i in range(len(poly)):
        ans = ans*z+poly[i]
    return ans
def f(x):
    global counter
    counter+=1
    return x[0]**4 + 16* x[0]**3 + 2 * x[0]**2 * x[1]**2 + 10* x[0]**2 * x[1]
    +99 * x[0]**2 + 16 * x[0] * x[1]**2 + 32 * x[0] * x[1] + 160 * x[0] + x[1] ** 4
    + 10 * x[1]**3 + 79 * x[1]**2 + 78 *x[1] + 89
counter = 0
def penalty_method():
    cons1 = lambda x: (x[0] ** 2 + x[1] ** 2 - 1)
    cons2 = lambda x: (x[1] - x[0])

    x_c = (1, 2)
    r = 1
    b = 10
    iters = 0
    eps = 0.000000001

    while cons1(x_c)>eps or cons2(x_c)>eps:
        curr_func = lambda x: f(x) + r*(max(0,cons1(x))**2) + r*(max(0,cons2(x))**2)
        x_c = minimize(curr_func, x_c).x
        r *= b
        iters += 1
        sheet1.write(iters+2, 0, iters)
        sheet1.write(iters+2, 1, x_c[0])
        sheet1.write(iters + 2, 2, x_c[1])
        sheet1.write(iters+2, 3, cons1(x_c))
        sheet1.write(iters+2, 4, cons2(x_c))
        sheet1.write(iters+2, 5, f(x_c))
        sheet1.write(iters+2, 6, curr_func(x_c))
        sheet1.write(iters+2, 7, r)
        sheet1.write(iters+2, 8, round(counter/3))
    return x_c, counter
print(penalty_method())
book.save("3.xls")
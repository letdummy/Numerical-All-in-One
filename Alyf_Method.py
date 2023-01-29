import math
import numpy as np
# Online Python - IDE, Editor, Compiler, Interpreter
x0 = 1.1
y0 = 0.4
#function
fx1 = y0 + x0*2 - 1- x0
fx2 = x0**2 - 2*y0**2 - y0
#derivative
fx1x = 2*x0 - 1
fx1y = 1
fx2x = 2*x0
fx2y = -4*y0 - 1
#matrics
xm = np.array([[x0],[y0]])
x1m = np.array([[fx1x, fx1y], [fx2x, fx2y]])
x1mt = np.linalg.inv(x1m)
fxm = np.array([[fx1], [fx2]])
#matric calculation
x2mt = np.matmul(x1mt, fxm)
xr = np.subtract(xm, x2mt)
#repeater
x0 = np.array(xr)[0,0]
y0 = np.array(xr)[1,0]
print(f'{xr}')
print(f'{x1mt}')
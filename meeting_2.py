# ========== True Error ========== #
# initial values
e = 2.7183
x = 3.9
delx = 0.019
xdelx = round(x + delx, 3)

# fx = 3 * (x ** 2) + 5 * (e ** (2 * x)) + 1
# f_x = 6 * x + 10 * (e ** (2 * x))
# fxdelx = 3 * (xdelx ** 2) + 5 * (e ** (2 * xdelx)) + 1

# calculations
fx = round(3 * (round(x ** 2, 4)), 5) + round(5 * (round(e ** (2 * x), 4)), 5) + 1
f_x = round(round(6 * x, 5) + round(10 * round(e ** (2 * x), 4), 5), 5)
fxdelx = round(3 * (round(xdelx ** 2, 4)), 5) + round(5 * (round(e ** (2 * xdelx), 4)), 5) + 1
approx_derivative = round(round(fxdelx - fx, 5) / delx, 4)


print(f_x)
print(approx_derivative)

true_error = round(f_x - approx_derivative, 4)
print(true_error)






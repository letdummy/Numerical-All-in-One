# Newton Raphson method for finding roots of a function

# fx = x^3 - 2x^2 + x - 3
# f_x = 3x^2 - 4x + 1
# initial values
iteration = 1
x = 4


while iteration <= 4:
    print("=========================")
    print("{Iteration number: ", iteration, "}")
    print("=========================")

    # fx = x^3 - 2x^2 + x - 3
    fx = x ** 3 - 2 * x ** 2 + x - 3
    print("fx = ", x, "^ 3 - 2 *", x, "^ 2 +", x, "- 3")
    print("fx = ", x ** 3, "-", 2 * x ** 2, "+", x - 3)
    print("fx = ", fx, "\n")
    fx = round(fx, 4)

    # f_x = 3x^2 - 4x + 1
    f_x = 3 * x ** 2 - 4 * x + 1
    print("f_x = 3 *", x, "^ 2 - 4 *", x, "+ 1")
    print("f_x = ", 3 * x ** 2, "-", 4 * x, "+", 1)
    print("f_x = ", f_x, "\n")

    # x1 = x0 - fx/f_x
    print("x", iteration, " = ", x, "- (", fx, "/", f_x, ")")
    print("x", iteration, " = ", x, "- (", round(fx / f_x, 4), ")")
    print("x", iteration, " = ", round(x - (fx / f_x), 4), "\n")
    x = round(x - (fx / f_x), 4)

    iteration += 1

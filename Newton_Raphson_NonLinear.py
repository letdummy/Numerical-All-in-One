# Newton Raphson Non-Linear Method

# Initial guesses
x = 1.3
y = 0.4
x0 = [x, y]
iteration = 1
# function

while iteration <= 4:
    i = y + x ** 2 - 1 - x
    i = round(i, 4)
    j = x ** 2 - 2 * y ** 2 - y
    j = round(j, 4)

    i1x = 2 * x - 1
    i1y = 1
    j1x = 2 * x
    j1y = -4 * y - 1

    f = [[i], [j]]
    f1 = [[i1x, i1y], [j1x, j1y]]

    f_1 = 1 / (i1x * j1y - i1y * j1x)
    f_1 = round(f_1, 4)

    f_1_i1x = f_1 * f1[0][0]
    f_1_i1x = round(f_1_i1x, 4)
    f_1_i1y = f_1 * f1[0][1]
    f_1_i1y = round(f_1_i1y, 4)
    f_1_j1x = f_1 * f1[1][0]
    f_1_j1x = round(f_1_j1x, 4)
    f_1_j1y = f_1 * f1[1][1]
    f_1_j1y = round(f_1_j1y, 4)

    f_1 = [[f_1_i1x, f_1_i1y], [f_1_j1x, f_1_j1y]]

    x1_0 = x0[0] - (f_1[0][0] * f[0][0] + f_1[0][1] * f[1][0])
    x1_0 = round(x1_0, 4)
    x1_1 = x0[1] - (f_1[1][0] * f[0][0] + f_1[1][1] * f[1][0])
    x1_1 = round(x1_1, 4)

    print("x0 = ", x0)

    x0 = [x1_0, x1_1]

    print("f = ",f)
    print("f1 = ", f1)
    print("f_1 = ", f_1)
    print("x", iteration, "=", x0, "\n")

    iteration += 1

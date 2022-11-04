from matplotlib import pyplot as plt

# false position method
# initial value
e = 2.7183
change_xl = True
change_xu = True

# only change this value
iteration = 1
xl = 1
xu = 2

print("given xl =", xl, "xu =", xu, "\n")

while iteration <= 4:
    print("=========================")
    print("{Iteration number: ", iteration, "}")
    if iteration > 1:
        print("from iteration", iteration - 1, "we got xl =", xl, "and xu =", xu)
    print("=========================")
    if change_xl:
        print("fxl = 3 *", xl, "- 2*e^( 0.5 *", xl, ")")
        print("fxl = ", round(3 * xl, 4), "-", round(2 * e ** (0.5 * xl), 4))
    fxl = round(round(3 * xl, 4) - round(2 * round(e ** round(0.5 * xl, 4), 4), 4), 4)
    print("fxl = ", fxl, "\n")

    if change_xu:
        print("fxu = 3 *", xu, "- 2*e^( 0.5 *", xu, ")")
        print("fxu = ", round(3 * xu, 4), "-", round(2 * e ** (0.5 * xu), 4))
    fxu = round(round(3 * xu, 4) - round(2 * round(e ** round(0.5 * xu, 4), 4), 4), 4)
    print("fxu = ", fxu, "\n")

    print("xr = xu - (fxu * (xu - xl)) / (fxu - fxl)")
    print("xr = ", xu, "- (", fxu, "*", "(", xu, "-", xl, ")) / (", fxu, "-", fxl, ")")
    print("xr = ", xu, "- (", round(fxu * (xu - xl), 4), ") / (", round(fxu - fxl, 4), ")")
    xr = round(xu - round((fxu * round((xu - xl), 4)), 4) / round((fxu - fxl), 4), 4)
    print("xr = ", xr, "\n")

    print("fxr = 3 * xr - 2*e^( 0.5 * xr)")
    print("fxr = 3 *", xr, "- 2*e^( 0.5 *", xr, ")")
    print("fxr =", round(3 * xr, 4), "-", round(2 * e ** (0.5 * xr), 4))
    fxr = round(round(3 * xr, 4) - round(2 * round(e ** round(0.5 * xr, 4), 4), 4), 4)
    print("fxr =", fxr, "\n")

    if fxl * fxr < 0:
        print("due to fxl * fxr < 0, xu = xr")
        xu = xr
        change_xu = True
        change_xl = False
    elif fxl * fxr > 0:
        print("due to fxl * fxr > 0, xl = xr")
        xl = xr
        change_xl = True
        change_xu = False

    print("xl = ", xl)
    print("xu = ", xu, "\n")

    iteration += 1

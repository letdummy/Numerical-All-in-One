import matplotlib.pyplot as plt

# ========== Numerical Method ========== #
# initial values
g = 9.8
e = 2.7183
vt = 0
itr = 0
x = []
y = []

# only change this value
m = 9.7
c = 11.7
t = 0
t1 = 0.485

# specific equations
print("========== Specific Numerical Method ==========\n")
print("vt+1 = vt + (g - (c/m) * vt) * (t+1 - t)")
print("vt+1 = vt + (", g, "-", "(", c, "/", m, "* vt) * (t+1 - t)")
print("vt+1 = vt + (", g, "- (", round(c/m, 2), "* vt )) * (t+1 - t)\n")


# calculations
while itr < 20:
    # calculate speed and time
    vt1 = vt + (g - (round(c / m, 2) * vt)) * round((t1 - t), 3)
    t = round(t1, 3)
    t1 = round(t1 + 0.485, 3)
    itr = itr + 1
    # show current speed and time
    print("=========================")
    print("{Iteration number: ", itr, "}")

    print("vt", t, " = ", vt, "+", "(", g, "-", "(", c, "/", m, "*", vt, ")", ")",
          "*", "(", t1, "-", t, ")")

    print("vt", t, " = ", vt, "+", "(", g, "-", "(", round(c / m, 2), "*", vt, ")",
          "*", "(", t1, "-", t, ")")

    print("vt", t, " = ", vt, "+", "(", g, "-", round(round(c / m, 2) * vt, 6), ")",
          "*", "(", round(t1 - t, 3), ")")

    print("vt", t, " = ", vt, "+", "(", round(g - round(round(c / m, 2) * vt, 6), 6), ")",
          "*", "(", round(t1 - t, 3), ")")

    print("vt", t, " = ", round(vt1, 4))

    # update speed
    vt = round(vt1, 4)

    # append speed and time to list
    x.append(t)
    y.append(vt)
print("=========================")

# # plot the graph
# plt.title("speed progress of dropping mass")
# plt.xlabel("time (sec)")
# plt.ylabel("speed (m/s)")
# plt.plot(x, y)
# plt.show()


# # ========== Calculus Method ==========#
# g = 9.8
# e = 2.7183
# vt = 0
# x = []
# y = []
#
# # only change this value
# m = 9.9
# t = 10.9
# c = 12.7
#
# # specific equation
# print("# ========== Specific Calculus Method ==========#\n")
# print("vt = g*m/c * (1-e^(-c/m)*t)")
# print("vt = ", g, "*", m, "/", c, "*", "(1 - e^(-", c, "/", m, ") * t)")
# print("vt = ", round(g*m/c, 4), "*", "(1 - e^(-", round(c/m, 2), ") * t)\n")
#
# print("# ========== Calculation ==========#\n")
# print("vt(10.9) = ", round(g*m/c, 4), "*", "(1 - e^(-", round(c/m, 2), ") *", t, ")")
# print("vt(10.9) = ", round(g * m / c * (1 - e ** ((-c / m) * 10.9)), 4))


# # currently unnecessary
# while t < 15:
#     vt = g * m / c * (1 - e ** ((-c / m) * t))
#     t = t + 1
#     x.append(t)
#     y.append(vt)
# # plot the graph
# plt.title("speed progress of dropping mass")
# plt.xlabel("time (sec)")
# plt.ylabel("speed (m/s)")
# plt.plot(x, y)
# plt.show()

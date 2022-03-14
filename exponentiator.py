


def exponentiator(x, y):
    return x ** y


def raise_to_fourth_power(z):
    return exponentiator(z, 4)


square = lambda a: exponentiator(a, 2)
cube = lambda b: exponentiator(b, 3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))

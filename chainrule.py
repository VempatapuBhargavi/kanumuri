from scipy.misc import derivative

import numpy as np
# Define the functions
def g(x):
    return x ** 2


def h(x):
    return 3 * x + 1


# Sum function
def sum_func(x):
    return g(x) + h(x)


# Compute the derivative of the sum at a point, say x=1
x_val = 1
sum_derivative = derivative(sum_func, x_val, dx=1)

print("Sum Function: g(x) + h(x) = x**2 + 3*x + 1")
print(f"Sum Derivative at x = {x_val}: (g + h)'(x) =", sum_derivative)


# Product function
def product_func(x):
    return g(x) * h(x)


# Compute the derivative of the product at a point, say x=1
x_val = 1
product_derivative = derivative(product_func, x_val, dx=1)

print("Product Function: g(x) * h(x) = (x**2) * (3*x + 1)")
print(f"Product Derivative at x = {x_val}: (g * h)'(x) =", product_derivative)


# Quotient function
def quotient_func(x):
    return g(x) / h(x)


# Compute the derivative of the quotient at a point, say x=1
x_val = 1
quotient_derivative = derivative(quotient_func, x_val, dx=1)

print("Quotient Function: g(x) / h(x) = (x**2) / (3*x + 1)")
print(f"Quotient Derivative at x = {x_val}: (g / h)'(x) =", quotient_derivative)


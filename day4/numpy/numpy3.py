import numpy as np
'''
Built-in Functions
arange: Similar to Python's range() but returns a NumPy array.
linspace: Creates an array of evenly spaced values over a specified range.
ones: Creates an array filled with ones.
zeros: Creates an array filled with zeros.
'''
array_arange = np.arange(0, 10, 2)
print("Array with arange:", array_arange)
array_linspace = np.linspace(10, 100, 5)
print("Array with linspace:", array_linspace)
array_ones = np.ones((2, 3))
print("Array of ones:\n", array_ones)
array_zeros = np.zeros((2, 3))
print("Array of zeros:\n", array_zeros)

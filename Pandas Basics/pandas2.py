'''
Data Structures in Pandas
Series
A Series is a one-dimensional labeled array capable of holding data of
any type (integer, string, float, python objects, etc.).
The axis labels are collectively referred to as the index.
Creating Series from Lists, Dictionaries, and Arrays
'''
import pandas as pd

data_list = [1, 2, 3, 4, 5]
series_from_list = pd.Series(data_list)
print(series_from_list)
data_dict = {'a': 1, 'b': 2, 'c': 3}
series_from_dict = pd.Series(data_dict)
print(series_from_dict)
import numpy as np

data_array = np.array([1, 2, 3, 4, 5])
series_from_array = pd.Series(data_array)
print(series_from_array)
'''
Series Attributes and Methods
Attributes, Methods
'''
print(series_from_list.index)  # RangeIndex(start=0, stop=5, step=1)
print(series_from_list.values)  # array([1, 2, 3, 4, 5])
print(series_from_list.dtype)  # dtype('int64')
print(series_from_list.head(3))  # First 3 elements
print(series_from_list.tail(2))  # Last 2 elements
print(series_from_list.mean())  # Mean value
print(series_from_list.sum())  # Sum of all values
print(series_from_list.describe())  # Statistical summary

# Indexing and Slicing Series
print(series_from_list[2])
print(series_from_dict['b'])
print(series_from_list[1:4])
print(series_from_list[:3])
print(series_from_list[3:])
# Operations on Series
print(series_from_list + 2)  # Adding 2 to each element
print(series_from_list * 2)  # Multiplying each element by 2
other_series = pd.Series([10, 20, 30, 40, 50])
print(series_from_list + other_series)


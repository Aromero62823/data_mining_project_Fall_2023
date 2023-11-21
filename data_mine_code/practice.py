import numpy as np

lst = np.array([1, 2, 3, 4, np.nan])

print(f'Before: {lst}')

lst[np.isnan(lst)] = 0

print(f'After: {lst}')


import numpy as np
  
n_array = np.array([0, 3, 11, 2, 0, 0, 1, 0, 4, 5, 7, 8, 0, 9, 0])
  
print("Original array:", n_array)

res = np.where(n_array == 0)[0]

print("\nIndices of elements equal to zero of the \
given 1-D array:", res)
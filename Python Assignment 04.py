#NumPy Array
import numpy as np
arr = np.array([1, 2, 3])
print(arr)

#Vectorized Operations
import numpy as np
arr = np.array([1, 2, 3])
print(arr * 2)  

# Example Multidimensional Arrays
import numpy as np

mat = np.array([[1, 2], [3, 4]])
print(mat)


   
#Python Program Using NumPy to Create 1D and 2D Arrays
import numpy as np

# Create one-dimensional array
arr1 = np.array([10, 20, 30, 40])

# Create two-dimensional array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

# Display arrays
print("1D Array:")
print(arr1)
print("\n2D Array:")
print(arr2)

# Display shape, dimensions, and data type
print("\nArray Properties:")
print("Shape of arr1:", arr1.shape)
print("Dimensions of arr1:", arr1.ndim)
print("Data type of arr1:", arr1.dtype)

print("\nShape of arr2:", arr2.shape)
print("Dimensions of arr2:", arr2.ndim)
print("Data type of arr2:", arr2.dtype)


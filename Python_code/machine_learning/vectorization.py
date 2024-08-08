import numpy as np

w = np.array([1, 2, 3])
x = np.array([4, 5, 6])

# Dot product
dot_product = np.dot(w, x)
print(dot_product)

# Element-wise multiplication
element_wise_multiplication = np.multiply(w, x)
print(element_wise_multiplication)  

# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])


# Using dot() function
C = np.dot(A, B)
print(C)




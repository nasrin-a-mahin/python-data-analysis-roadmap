# Different Ways to Create Numpy Arrays in Python


import numpy as np

a1 = np.array([1, 2, 3])    # 1D array
a2 = np.array([[1, 2], [3, 4]]) # 2D array
a3 = np.array([[[1, 2], [3, 4]],    # 3D array
               [[5, 6], [7, 8]]])

print(a1)
print(a2)
print(a3)


a0 = np.zeros((3, 3))
a1  = np.ones((2, 2))
ar  = np.arange(0, 10, 2)

print(a0)
print(a1)
print(ar)




a1 = np.array([10, 20, 30, 40, 50])
print(a1[2])      # single element
print(a1[-1])     # last element

a2 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
print(a2[1, 0])   # row 1, column 0


import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a[1:4])      # row slice
print(a[:, 1])     # all rows, column 1
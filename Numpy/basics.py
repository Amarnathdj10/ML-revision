import numpy as np

a = np.array([2,3])
b = np.array([[1,2],[3,4]])
print(a)

#get dimension
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape)
print(b.shape)

#get size
print(a.itemsize)
print(a.size)

#get data type
print(a.dtype)

#get total size
print(a.nbytes)
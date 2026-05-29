import numpy as np

#all 0's matrix
a = np.zeros((2,3))
print(a)

#all 1's matrix
b = np.ones((4,1))
print(b)

#any other number matrix
c = np.full((2,2),99)
print(c)

#random decimal numbers
print(np.random.rand(4,2))
print(np.random.random_sample(a.shape))

#random integer values

print(np.random.randint(2,7,size=(3,3)))

#identity matrix
print(np.identity(3))

#repeat array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)


import numpy as np

'''
a = np.array([1,2,3,4])
print(a)

#print(a+2)
#print(a-2)
#print(a*2)
#print(a//2)

b = np.array([1,0,1,0])
print(b)

print(a+b)

#take sine
print(np.sin(a))

'''

#LINEAR ALGEBRA

a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)

print(np.matmul(a,b))

c = np.identity(3)
print(np.linalg.det(c))

#STATISTICS

stats = np.array([[1,2,3],[4,5,6]])
print(stats)
print(np.min(stats))
print(np.max(stats))
print(np.sum(stats))


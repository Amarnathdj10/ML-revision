'''
GOAL:

1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1

'''

import numpy as np

a = np.ones((5,5))
print(a)

b = np.zeros((3,3))
b[1,1] = 9
print(b)

a[1:-1,1:-1] = b
print(a)


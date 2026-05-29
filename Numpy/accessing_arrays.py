import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print(a.shape)

#get specific element
print(a[1,5])

#get specific row/column
print(a[0,:])
print(a[:,2])

#a bit fancier [startindex:endindex:stepsize]
print(a[0,1:6:2])

#changing values
a[1,5] = 20
print(a)

a[:,2] = [1,2]
print(a)


#3d example
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b[0,1,1])
print(b[:,1,:])

#replace
b[:,1,:] = [[9,9],[8,8]]
print(b)
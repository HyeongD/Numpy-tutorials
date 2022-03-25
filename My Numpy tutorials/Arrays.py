import os
import sys
import numpy as np
from numpy import pi 
##########################
#### CREATING ARRAYS #####
##########################
a= np.array([2, 3, 4])
print(a)
print(a.dtype)
b = np.array([1.2, 3.5, 5.1])
print(b)
print(b.dtype)
b = np.array([(1.5, 2, 3),(4, 5, 6)]) # transforming a sequences int two dimensional array
print(b)
c= np.array([[1,2],[3,4]], dtype=complex) # specifying the type of the array at creation time
print(c)
print(np.zeros((3,4))) #creating an array full of zeros
print(np.ones((2, 3, 4), dtype=np.int16)) #creating an array full of ones
print(np.empty((2, 3))) #creating an array whose initial content is random and depens on the state of the memory
print(np.arange(10, 30, 5)) # creating a sequence of numbers from 10 to number < 30 incrementing value is 5
print(np.arange(0, 2, 0.3))

##########################
#### PRINTING ARRAYS #####
##########################
a= np.arange(6)
print(a)
b=  np.arange(12).reshape(4, 3) #2d array
print(b)
c= np.arange(24).reshape(2, 3, 4) # 3d array
print(c)
print(np.arange(10000)) # (1) this is a large array, Numpy will automatically skip the central part of the array and on;y prints the corners of the array
print(np.arange(10000).reshape(100, 100)) # 
np.set_printoptions(threshold=sys.maxsize) # to resolve issue at (1)
print(np.arange(10000)) 
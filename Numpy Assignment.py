# Numpy Assignment :
import numpy as np
# Q1 Numpy stands for ?
# --> Numpy stands for the Numerical Python.

# Q2 The most important object defined in Numpy is an N-Dimentional array type called ?
# --> ndarry called as the N-Dimensional array.



#Q3 What will be the output of the following code ?

import numpy as np
# a = np.array([1, 2, 3], dtype =complex)
# print(a)
#--->  The output of the following code is Complex Number
    # Output --> [1.+0.j 2.+0.j 3.+0.j]

# a=np.array([1,2,3])
#  print(a)
#---> Output of this code is list --> [1 2 3]


# a=np.array([1,2,3], dtype='float')
# print(a)
# output of the following code is Float numeric list --> [1. 2. 3.]


# a=np.dtype('i4')
# print(a)
# Output of the above code is showing the data type of the element ---> int32


# a = np.array([1, 2, 3,4,5], ndmin = 2)  # ndmin specifies the minimum dimensions of resultant array is ---> [[1 2 3 4 5]]
# print(a)

#output of the following code is ---> [[1 2 3 4 5]]

# dt = np.dtype([('age',np.int8)])
# a=np.array(([(10,),(20,),(30,)]), dtype = dt)
# print(a['age'])
# Output of the above code is ---> [10, 20, 30]


# a = np.array([1,2,3,5,8])
# b = np.array([0,3,4,2,1])
# c = a + b
# c = c*a
# print(c[2])
# The Output of the following code is ----> 21



# a=np.array([1,2,3,5,8])
# a=a+1
# print(a[1])
# ---> The Output of the obove code is --->3

# a=np.array([[1,2,3],[0,1,4]])
# print(a.size)  # a.size funtion used to show the how many element is there in array.
# Output of the obove code is ----> 6


# a = np.array([1,2,3,5,8])
# print(a.ndim)
# #print(a.ndim.describe())
# print(a.describe)
# # print(a.shape())
# #print(a.shape)


# a = np.array([[1,2,3],[0,1,4]])
# b = np.zeros((2,3), dtype=np.int16  # here creation of the 2D array using Zero (0) values.
# c = np.ones((2,3), dtype=np.int16)
# d = a + b + c
# print(d[1,2])
# print(d.size)
# print(d.attributes)
# print(a.zeroes())


# Q4  You have a matrix defined as below:

# A = np.array([[6, 1, 1],
#              [4, -2, 5],
#              [2, 8, 7]])
# rank = np.linalg.matrix_rank(A)
#
# print('Matrix rank is  : ', rank)
#
# det = np.linalg.det(A)
#
# print("\nDeterminant of given 3X3 matrix : ",det)
#
# print('The trace of the this matrix is : ', A.trace())
#
# print("Inverse of the following matris is : ",np.linalg.inv(A))
#
# print("Transpose of matrix is : ", np.transpose(A))



# Q5.  Type this line of code and check the output for each of them .

# list1 =[1,2,3,4,5,6]
# list2 =[10,9,8,7,6,5]
# print(list1*list2)
# print(list1+list2)
# print(list1%list2)
# print(list1/list2)
# print(list1-list2)
# print(list1^list2)

#res=[(a[i]+b[i]) for i in range(len(a))]

# print('Multipication of the above list are: ',[(list1[i]*list2[i]) for i in range(len(list1))])
# print('Addition of above list are : ',[(list1[i]+list2[i]) for i in range(len(list1))])
# print('remainder of the above lists are: ',[(list1[i]%list2[i]) for i in range(len(list1))])
# print('Division of above lists are : ',[(list1[i]/list2[i]) for i in range(len(list1))])
# print('Subtraction of the above list are :',[(list1[i]-list2[i]) for i in range(len(list1))])


#Q6.  The result of the Above code is : -->

# Multipication of the above list are:  [10, 18, 24, 28, 30, 30]
# Addition of above list are :  [11, 11, 11, 11, 11, 11]
# remainder of the above lists are:  [1, 2, 3, 4, 5, 1]
# Division of above lists are :  [0.1, 0.2222222222222222, 0.375, 0.5714285714285714, 0.8333333333333334, 1.2]
# Subtraction of the above list are : [-9, -7, -5, -3, -1, 1]





# list1 = np.array([1, 2, 3, 4 ,5, 6])
# list2 = np.array([10, 9, 8, 7, 6, 5])
#
# print('Multiplication of following array is : ',list1*list2)
# print('Addition of following array is : ',list1+list2)
# print('Division of following array is : ',list1/list2)
# print('Subtraction of following array is : ',list1-list2)
# print('Remainder of following array is : ',list1%list2)

# Output of the following code is :

# Multiplication of following array is :  [10 18 24 28 30 30]
# Addition of following array is :  [11 11 11 11 11 11]
# Division of following array is :  [0.1        0.22222222 0.375      0.57142857 0.83333333 1.2       ]
# Subtraction of following array is :  [-9 -7 -5 -3 -1  1]
# Remainder of following array is :  [1 2 3 4 5 1]






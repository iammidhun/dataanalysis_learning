import numpy  as np
my_list = [1,2,3,4,5] #first create a list
my_array = np.array(my_list) #this will return array

#multi dimension 
mylist2 = [11,22,33,44,55]
my_list2 = [my_list,mylist2] #combining 2  lists of my_list and mylist2   
my_array =  np.array(my_list2)

array([[ 1,  2,  3,  4,  5],
      [11, 22, 33, 44, 55]]) #this will be the output

np.zeros(4) #this will return array of elements with zero and shape of (1,4)
array([0., 0., 0., 0.]) #output .dtype of the output will be float

#elements with one
np.ones([5,5])

#identity matrix
np.eye(5)

#for a specific values in between to ranges
#np.arange(start,end,step)
np.arange(40,50,1) #i/p
array([40, 41, 42, 43, 44, 45, 46, 47, 48, 49]) #o/p



#indexing arrays
arr =  np.arange(0,11) #arr will list value from 0  to 10 just like list

#and array have features like indexing and listing values between particular arrays
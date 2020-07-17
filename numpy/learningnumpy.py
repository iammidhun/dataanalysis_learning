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

arr[0:5] = 100 #what will happen ?  the value indexing from zero to 4 will be 100


slicing an array and changing it value will also affect the original array
for eg  : 
	arr =  np.arange(0,11)
	slice_arr  =  arr[0:5]
	slice_arr [:] = 5
	so now all the value of slice_arr will be 5
	and value of arr from index 0  to 4  will also be 5
#to solve this issue you can use .copy()


#2d array
arr  =  np.array(([1,2,3],[4,5,6],[7,8,9]))
#arr will be
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

arr[0] 
#o/p will be
array([1, 2, 3])

simillary other raws

arr[0][1] will return  2nd element  in 1st raw(0th position)

#slicing 
arr2 =  arr[:2,1:] #[:raw , :coulmn]
array([[2, 3],
       [5, 6]])

#fancy indexing

arr2[[0,2]]
this will return 1st and 3rd raws



#arraytransposition
np.arange(50).reshape(10,5)
#o/p will be 
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24],
       [25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34],
       [35, 36, 37, 38, 39],
       [40, 41, 42, 43, 44],
       [45, 46, 47, 48, 49]])
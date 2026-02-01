#this is the method to import numpy
import numpy as np
from time import process_time


# #lkst vs numpy array time complexity or whichis faster proof
# #list 
# listt=[i for i in range(100000000)]
# start_time=process_time()
# summ=[i+5 for i in listt]
# stop_time=process_time()

# print(f"the time taken by the list is {stop_time-start_time} seconds")

# #numpy array

# numpyy=np.array([i for i in range(100000000)])
# start_time_1=process_time()
# numpyy +=5
# stop_time_1=process_time()

# print(f"the time taken by the list is {stop_time_1-start_time_1} seconds")

#prints all values zeros
a=np.zeros((2,3))
print(a)

#prints the identity matrix
b=np.eye(5,4)
print(b)
listt=[1,2,3,4]
c=np.array(listt)
print(c,c.dtype,type(c))
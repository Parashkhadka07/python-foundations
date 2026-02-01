#this is the method to import numpy
import numpy as np
from time import process_time
#this is the method to create a numpy array


listt=[i for i in range(10000000)]
start_time=process_time()
summ=[i+5 for i in range(10000000)]
stop_time=process_time()
print(f"the time taken by the list is {stop_time-start_time} seconds")
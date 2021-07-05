import matplotlib.pyplot as plt 
import numpy as np
from scipy import signal
import random

def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    return [random.randint(start, stop) for _ in range(length)]

list1=random_int_list(10, 20, 10)
list2=random_int_list(10, 20, 10) 

a = np.append(list1,list2)
print("序列拼接:\n",a) 

b= np.array(list1)+np.array(list2)
print("序列对应元素相加:\n",b) 

print("\n",np.append(a,b))
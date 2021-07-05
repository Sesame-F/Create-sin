import matplotlib.pyplot as plt 
import numpy as np
from scipy import signal
#import random

list1=np.random.randint(0,10,(7,7))
list2=np.random.randint(0,10,(7,7))
sum=np.array(list1)+np.array(list2)
print("矩阵1:\n",list1)
print("矩阵2:\n",list2)
print("矩阵相乘:\n",np.dot(list1,list2))
print("矩阵对应相加:\n",sum)
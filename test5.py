import matplotlib.pyplot as plt 
import numpy as np
from scipy import signal

t=np.arange(-10*np.pi,10*np.pi,0.1)
#plt.xticks([-2*np.pi,-(3/2)*np.pi,-np.pi,-np.pi/2,0,np.pi/2,np.pi,(3/2)*np.pi,2*np.pi],
          # [r'$-\pi*2$',r'$-\pi*3/2$',r'$-\pi$',r'$-\pi/2$',r'$0$',r'$\pi/2$',r'$\pi$',r'$\pi*2$',r'$\pi*3/2$'])
def x(t):
    y=np.sin(np.pi*t)/(np.pi*t)
    return y

y=x(t)
y1=x(t-7)
y2=x(t+7)

plt.subplot(111)
plt.plot(t,y,color='red',label='x(t)')
plt.legend(loc='upper left')
plt.plot(t,y1,color='blue',label='y1(t)')
plt.legend(loc='upper left')
plt.plot(t,y2,color='black',label='y2(t)')
plt.legend(loc='upper left')

plt.show()


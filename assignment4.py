import numpy as np
import matplotlib.pyplot as plt

from math import *
from random import *

# Define inverse CDF function for x|y
def CDF_xy(y, B = 5.0):
    P = uniform(0,1)
    x = -1/y*log(1 - P*(1-exp(-y*B)))
    return(x)

def myGibbs(T, B = 5.0):
    # Initialize a matrix of 2 columns for x and y
    chain = np.zeros((T,2))
    chain[0,0] = uniform(0,B)
    chain[0,1] = uniform(0,B)

    for ii in range(0,T-1):
        chain[ii+1,0] = CDF_xy(chain[ii,1], B)
        chain[ii+1,1] = CDF_xy(chain[ii,0], B)

    return(chain)

myB = 5.0
mychain = myGibbs(500, myB)

myx1 = mychain[:,0]
plt.hist(myx1, bins = np.linspace(0,myB,20))
plt.title("Gibbs sampling")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.ion()
plt.show()

print uniform(0,5)

mychain = myGibbs(5000, myB)
myx2 = mychain[:,0]


mychain = myGibbs(50000, myB)
myx3 = mychain[:,0]

##### Expectation of x
print "Expectation from 500 samples", np.mean(myx1)
print "Expectation from 5000 samples", np.mean(myx2)
print "Expectation from 50000 samples", np.mean(myx3)
plt.ioff()
print 1

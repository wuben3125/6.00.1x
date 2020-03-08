# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 20:46:11 2018

@author: Ben
"""

import pylab as plt
import time

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

def plotExponential():
    plt.plot(mySamples, myExponential)
    
print("Here's a plot in the script.")
# plot all graphs at same time
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

print("Now you try it - run plotExponential() in the Python console.")
print("(Also, for some reason the plot is shown last regardless of the \
        order of the print statements. That's annoying...")
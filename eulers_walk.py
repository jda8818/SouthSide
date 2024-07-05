# eulers_walk.py -- to pi. importing cmath seems to allow complex elements in a list without warning
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

data = [] # purposed as global List of elements of partial sums, each element consisting of real and imag

def partial_sum_elements_exp(x):
    data.append(0 + 0.0j) # start at zero/zero
    z = 0 
    for n in range(0, 50):
        z += x**n / math.factorial(n)
        data.append(z) # feeds list of partial sum elements 
    return(z) # and returns the convergent total value

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim(-5, 2 )
ax.set_ylim(-3, 4)
ax.grid(True, which = 'both')
ax.set_aspect("equal")
ax.title.set_text("exp(pi*j) = -1 --> plot of partial sums")
plt.ylabel('imaginary')
plt.xlabel('real')

print(partial_sum_elements_exp((np.pi)*(1.0j))) # check and load the list
x = [ele.real for ele in data] 
y = [ele.imag for ele in data]
plt.plot(x,y)

plt.show()






# Eulers_Convergence.py
import math
import numpy as np
import matplotlib.pyplot as plt
pi = 3.14159265359

q = pi/12

def plot_it(p):
    ax.scatter(np.real(p), np.imag(p))

def exp(x):
    z = 0
    for n in range(0, 100):
        z += x**n / math.factorial(n)
    return z    

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

for n in range(0, 25):    
   p = exp((q*n)*(1.0j))
   plot_it(p)
   
ax.title.set_text("EXP(jx): Complex Exponentials - Convergence")
circ = plt.Circle((0, 0), radius=1, edgecolor='b', facecolor='None')
ax.add_patch(circ)
plt.xlabel('Real')
plt.ylabel('Imaginary')
ax.grid(True, which='both')    
ax.set_aspect("equal")
plt.show()
               



#Magnetization of a paramagnet

import matplotlib.pyplot as plt
import numpy as np

N = 10
mu = 9.27*10**-24
kb = 1.38*10**-23
V = 1
x = range(-100, 100)

def Magnetization(T):
    M_vals = []
    for B in x:
        M = ((N*mu)/V)*np.tanh((mu*B)/(kb*T))
        M_vals.append(M)
    stringy = 'T = ' + str(T) + 'K'
    plt.plot(x, M_vals, label = stringy)

Magnetization(10)
Magnetization(20)
Magnetization(50)
Magnetization(100)

plt.xlabel('Magnetic Field (Tesla)')
plt.ylabel('Magnetization (a.u.)')
plt.title('Magnetization of a Paramagnet')

plt.legend()

plt.show()
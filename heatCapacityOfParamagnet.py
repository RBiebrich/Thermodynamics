#Heat capacity of a paramagnet

import matplotlib.pyplot as plt
import numpy as np

N = 10
mu = 9.27*10**-24
kb = 1.38*10**-23
V = 1
T = np.arange(0, 10, 0.001)

def HeatCapacity(B):
    Cv = N*kb*(((mu*B)/(kb*T))**2)*(1/(np.cosh((mu*B)/(kb*T))))**2
    stringy = 'B = ' + str(B) + 'Tesla'
    plt.plot(T, Cv, label = stringy)

HeatCapacity(1)
HeatCapacity(2)
HeatCapacity(3)
HeatCapacity(5)

plt.xlabel('Temperature (K)')
plt.ylabel('Specific Heat (a.u.)')
plt.title('Heat Capacity of a Paramagnet')

plt.legend()

plt.show()
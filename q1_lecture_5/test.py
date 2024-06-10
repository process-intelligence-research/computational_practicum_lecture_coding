import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

# time domain
t_start = 0.0
t_end = 30.0
n = 500
t = np.linspace(t_start, t_end, n)
dt = t[1]-t[0]

# reaction system
def dC(t, c):
    cA, _ = c
    k = 0.2
    Vdot = 0.1
    V_0 = 10
    cA_in = 0.5
    dcA = Vdot/(V_0+Vdot*t)*(cA_in-cA)-k*cA
    dcB = k*cA
    return np.array([dcA, dcB])

def forward_euler(func: Callable, yi: float, ti: float, dt: float) -> float:
    return yi+dt*func(ti, yi)

c = np.zeros((2,len(t)))
# initial condition
c[:,0] = [1, 0]
for i in range(1,len(t)):
    c[:,i] = forward_euler(dC, c[:,i-1], t[i-1], dt)

fig, ax = plt.subplots()
ax.plot(t, c[0,:], label = "cA")
ax.plot(t, c[1,:], label = "cB")
ax.set_xlabel("time /s")
ax.set_ylabel("concentration [mol/L]")
ax.set_title("The Forward Euler method")
ax.legend()
ax.grid()
fig.show()
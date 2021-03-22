import math
from scipy.integrate import quadrature

v_t = 54.0
g = 9.8
x = 1400

def velocity(t, v_t):
    return v_t*(1-math.e**(-2*g*t/v_t))/(1+math.e**(-2*g*t/v_t))

dt = 0.001
i = 0
t = 0

outFile = open("JumpData.txt", "w")
while (x > 1200):
    h = 4000
    t = i*dt
    i += 1
    dx, err = quadrature(velocity, 0, t, args = v_t)
    x = h - dx
    outFile.write(str(t) + " " + str(x) + "\n")

while (v_t > 7.6):
    #go from 54.0 to 7.6 in 3 sec in steps of 10e-6 m/s <4.64e6 steps >6.5e-7 dt?
    dt = 6.5e-7
    t = t + dt
    i += 1
    a = 46.4/3
    v_t = v_t - a*dt
    dx, err = quadrature(velocity, t, t+dt, args = v_t)
    x = x - dx
    outFile.write(str(t) + " " + str(x) + "\n")

while (x >= 0):
    dt = 0.001
    t = t + dt
    v_t = 7.6
    dx, err = quadrature(velocity, t, t+dt, args = v_t)
    x = x - dx
    outFile.write(str(t) + " " + str(x) + "\n")
outFile.close()
print(t)
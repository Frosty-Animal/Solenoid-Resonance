
""" 
This RLC circuit uses Euler's Method to numerically calculate
the Solution to Kirchoff's Differential equation



"""
import numpy as np
from matplotlib import pyplot as plt 

#circuit param.
V_amp = 9 #voltage amplitude of the AC gen.
AC_frequency = 50 #in hertz
w = (2 * np.pi) #Angular Frequency
R = 1 #Ohms
L = 1 #Henrys
C = 0.8 #Capacitance

#Time Param. 
t_0 = 0.0
t_f = 500.0 #seconds
sample_size = 1000
dt = (t_f - t_0) / sample_size

#Inital Value (This is an Inital value problem...)
q = 0.0 #initial charge across the capacitor
I = 0.0 #Initial Current ( = dq_dt)

#Storage Bins for Graphing DO NOT TOUCH <<<<
time_x = np.linspace(t_0, t_f, sample_size)
Vc_y = []


####Numerical Solution (Euler's Method)####

for time in time_x:
    Vin = V_amp* np.cos(w * time)

    dI_dt = (Vin - q / C - R * I) / L
    I += dI_dt * dt
    q += I * dt

    Vc_y.append(q)

plt.plot(time_x, Vc_y, label='Numerical')


######Analytical Solution######
#Note: Don't ask me to explain this part, I can't. Just trust me
Vc_y = []

omega = w
A = V_amp / (np.sqrt((1 / L - C * omega ** 2) ** 2 + (R * C * omega) ** 2))
phi = np.arctan2(R * C * omega, (1 / L - C * omega ** 2))
q_steady = V_amp/ (omega * L)
Vc_y = q_steady + A * np.cos(omega * time_x + phi)

plt.plot(time_x, Vc_y, label='Analytical')


#####Graph#######
plt.legend()
plt.grid(True)
plt.show()
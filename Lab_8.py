import numpy as np
import matplotlib.pyplot as plt
with open("/home/gr101/Desktop/Scripts/bogdanova-repo/settings.txt","r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
    data_array = np.loadtxt("/home/gr101/Desktop/Scripts/bogdanova-repo/data.txt", dtype = int)
    data_array = data_array* 3.3
    data_array = data_array / 256
fig, ax = plt.subplots(figsize = (16, 25))
ax.plot(data_array)
ax.minorticks_on()
ax.set_title("График зависимости U(B) от t(с)")
ax.set_xlabel('t(с)')
ax.set_ylabel('U(B)')
N = data_array.size
dt = tmp[0]
k = np.linspace(0, N*dt, N)
ax.grid(which = "major",linewidth = 1.5, color = 'grey')
ax.grid(which = "minor", color = 'grey', linewidth = 0.5,linestyle = '--') 
ax.tick_params(axis='both', which='major', labelsize=16)
ax.tick_params(axis='both', which='minor', labelsize=8)
ax.plot(Label = "Напряжение от времени")
max_index = k[np.argmax(data_array)]
box1 = {'facecolor':'red', 'boxstyle':'square'}
box2 = {'facecolor':'blue', 'boxstyle':'square'}
ax.text(600, 3,'Время разрядки ={:3f}'.format(max_index), bbox = box1, color = 'grey', fontsize = 10)
ax.text(600, 2.8,'Время разрядки ={:3f}'.format(N*dt - max_index), bbox = box2, color = 'grey', fontsize = 10)
fig.set_figwidth(12)
fig.savefig("/home/gr101/Desktop/Scripts/bogdanova-repo/Lab8.svg")
plt.show()

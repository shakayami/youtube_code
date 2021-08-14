import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import math
fig = plt.figure(figsize=(10, 10))
ax1 = plt.subplot2grid((1,1),(0,0))
ims = []
dt = 0.1
#S = 0
n=10
m=1000
Kabuka=[np.full(n,1)]
t = 0
#K = 5
#h = 0.25
ymax=2
def update(flame, Kabuka):
    global ymax
    if flame != 0:
        ax1.cla()
    ax1.grid(True)
    ax1.set_xlim(0,m)
    ymax=max(ymax,1.5*np.max(Kabuka[-1]))
    ax1.set_ylim(0, ymax)
    ax1.set_title("black_scholes_model")
    for j in range(n):
        tmp=np.zeros(flame+1)
        for i in range(flame+1):
            tmp[i]=Kabuka[i][j]
        ax1.plot(tmp, "r-")
    random_vector=math.sqrt(dt)*np.sqrt(-2*np.log(np.random.rand(n)))*np.cos(2*math.pi*np.random.rand(n))
    Kabuka.append(Kabuka[-1]*(1+0.005*dt+0.1*random_vector))
    print(flame)
 
 
ani = anm.FuncAnimation(fig, update, fargs=(Kabuka,), interval=10, frames=m)
ani.save("matplotlib/analysis/black_scholes/000.mp4", writer="ffmpeg", fps=25)
#plt.show()

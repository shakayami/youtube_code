import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import math
from scipy.spatial import KDTree
fig = plt.figure(figsize=(10, 10))
ax1 = plt.subplot2grid((2,2),(0,0))
ax2 = plt.subplot2grid((2,2),(0,1))
ax3 = plt.subplot2grid((2,2),(1,0))
ax4 = plt.subplot2grid((2,2),(1,1))
 
ims = []
dt = 0.1
n = 1000
a, b = (0, 1)
c, d = (0, 1)
e = 0.1
r = 0.001
#S = 0
x = (b - a) * np.random.rand(n) + a
y = (d - c) * np.random.rand(n) + c
t = 0
#K = 5
#h = 0.25
X = np.random.rand(n)
Y = np.random.rand(n)
vx = 0.5*np.sqrt(-2*np.log(X))*np.cos(2*math.pi*Y)
vy = 0.5*np.sqrt(-2*np.log(X))*np.sin(2*math.pi*Y)
E = (sum(vx ** 2 + vy ** 2) / 2)
collisions = 0
M = 1200
Energy = np.array([-1 for i in range(M)])
F = np.arange(0, M*dt, dt)
E0 = 300
CollEnd=20000
Coll = np.array([-1 for i in range(M)]) 
def update(flame, x, y):
    global collisions,CollEnd
    if flame != 0:
        ax1.cla()
        ax2.cla()
        ax3.cla()
        ax4.cla()
    kd_tree = KDTree([[xi,yi] for xi,yi in zip(x,y)])
    for i in range(n):
        for j in kd_tree.query_ball_point([x[i],y[i]], r):
            if i==j:
                continue
            vx[i], vx[j] = ((1 - e) * vx[i] + (1 + e) * vx[j]) / 2, ((1 + e) * vx[i] + (1 - e) * vx[j]) / 2
            vy[i], vy[j] = ((1 - e) * vy[i] + (1 + e) * vy[j]) / 2, ((1 + e) * vy[i] + (1 - e) * vy[j]) / 2
            collisions += 1
    for i in range(n):
        if not(a < x[i] + vx[i] * dt < b):
            vx[i] = -vx[i]
        if not(c < y[i] + vy[i] * dt < d):
            vy[i] = -vy[i]
    x += vx * dt
    y += vy * dt
    E = (sum(vx ** 2 + vy ** 2) / 2)
    Energy[flame] = E
    Coll[flame] = collisions
    CollEnd=max(collisions,CollEnd)
    ax1.grid(True)
    ax1.set_xlim(a, b)
    ax1.set_ylim(c, d)
    ax1.set_title("Position Distribution")
    ax1.plot(x, y, "ro")
    ax2.grid(True)
    ax2.set_xlim(-1,1)
    ax2.set_ylim(-1,1)
    ax2.set_title("Velocity Distribution")
    ax2.plot(vx, vy, "go")
    ax3.grid(True)
    ax3.set_xlim(0, M*dt)
    ax3.set_ylim(0,E0)
    ax3.set_title("Kinetic Energy")
    ax3.plot(F, Energy, "b", linewidth=2)
    ax4.grid(True)
    ax4.set_xlim(0,M*dt)
    ax4.set_ylim(0,CollEnd)
    ax4.set_title("Number of Collision")
    ax4.plot(F, Coll, "y", linewidth=2)
    print(flame, E, collisions)
 
 
ani = anm.FuncAnimation(fig, update, fargs=(x, y), interval=10, frames=M)
ani.save("SMA.mp4", writer="ffmpeg", fps=25)
#plt.show()

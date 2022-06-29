import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import random
fig=plt.figure(figsize=(10,10))
ims=[]
dt=0.1
a=1
b=1
c=1
d=1
####################
#n=100
#x=np.random.rand(n)
#y=np.random.rand(n)
####################
x=random.random()
y=random.random()
####################
t=0
def f(p,q):
    return a*p-b*p*q
def g(p,q):
    return c*p*q-d*q
for flame in range(1000):
    ###################################
    #px=[np.zeros(n) for i in range(4)]
    #py=[np.zeros(n) for i in range(4)]
    ###################################
    px=[0 for i in range(4)]
    py=[0 for i in range(4)]
    ###################################
    px[0] = f(x,y)
    py[0] = g(x,y)
    px[1] = f(x + (px[0] * dt) / 2, y + (py[0] * dt) / 2)
    py[1] = g(x + (px[0] * dt) / 2, y + (py[0] * dt) / 2)
    px[2] = f(x + (px[1] * dt) / 2, y + (py[1] * dt) / 2)
    py[2] = g(x + (px[1] * dt) / 2, y + (py[1] * dt) / 2)
    px[3] = f(x + (px[2] * dt), y + (py[2] * dt))
    py[3] = g(x + (px[2] * dt), y + (py[2] * dt))
    dx=(px[0]+2*px[1]+2*px[2]+px[3])*dt/6
    dy=(py[0]+2*py[1]+2*py[2]+py[3])*dt/6
    x+=dx
    y+=dy
    plt.grid()
    plt.xlim(0,3)
    plt.ylim(0,3)
    im1,=plt.plot(x,y,"ro")
    im2,=plt.plot(d/c,a/b,"bo")
    ims.append([im1,im2])
ani=anm.ArtistAnimation(fig,ims,interval=10)
ani.save("LVE.mp4", writer = "ffmpeg", fps = 25)
plt.show()

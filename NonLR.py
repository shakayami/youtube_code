import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import random
fig=plt.figure(figsize=(10,10))
ims=[]
dt=0.02
####################
n=1000
x=4*np.random.rand(n)-2
y=4*np.random.rand(n)-2
####################
#x=random.random()
#y=random.random()
####################
xzero=np.arange(-2,2,0.01)
yzero=xzero**3-xzero
xone=np.zeros(10)
yone=np.linspace(-2,2,10)
t=0
def f(p,q):
    return q-p**3+p
def g(p,q):
    return -p
for flame in range(1200):
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
    plt.xlim(-2,2)
    plt.ylim(-2,2)
    im1,=plt.plot(x,y,"ro")
    im2,=plt.plot(xzero,yzero,color="b",ls="-")
    im3,=plt.plot(xone,yone,color="b",ls="-")
    ims.append([im1,im2,im3])
    print(flame)
ani=anm.ArtistAnimation(fig,ims,interval=10)
ani.save("NonLR.mp4", writer = "ffmpeg", fps = 25)
#plt.show()

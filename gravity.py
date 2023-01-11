import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.animation as anm
n=100
x=np.random.rand(n)*2-1
y=np.random.rand(n)*2-1
vx=np.zeros(n)
vy=np.zeros(n)
m=np.ones(n)*0.1
G=1000
dt=0.0001
fig=plt.figure(figsize=(10,10))
ims=[]
rmin=0.01#0.03
 
 
def Vx(mm, xx, yy, vvx, vvy):
    return vvx
 
 
def Vy(mm, xx, yy, vvx, vvy):
    return vvy
 
 
def Ax(mm, xx, yy, vvx, vvy):
    result = np.zeros(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                r = math.sqrt((xx[j] - xx[i]) ** 2 + (yy[j] - yy[i]) ** 2)
                result[i] += G*mm[j] * (xx[j] - xx[i]) / (max([r, rmin])) ** 3
    return result
 
 
def Ay(mm, xx, yy, vvx, vvy):
    Result = np.zeros(n)
    for i in range(n):
        for j in range(n):
            if i!=j:
                r=math.sqrt((xx[j]-xx[i])**2+(yy[j]-yy[i])**2)
                Result[i]+=G*mm[j]*(yy[j]-yy[i])/(max([r,rmin]))**3
    return Result
#dx/dt=vx
#dy/dt=vy
#dvx/dt=dot(Ax,x)
#dvy/dt=dot(Ay,y)
for fr in range(700):
    kx1 = Vx(m, x, y, vx, vy) * dt
    ky1 = Vy(m, x, y, vx, vy) * dt
    vx1 = Ax(m, x, y, vx, vy) * dt
    vy1 = Ay(m, x, y, vx, vy) * dt
    kx2 = Vx(m, x + kx1 * 0.5, y + ky1 * 0.5, vx + vx1 * 0.5, vy + vy1 * 0.5) * dt
    ky2 = Vy(m, x + kx1 * 0.5, y + ky1 * 0.5, vx + vx1 * 0.5, vy + vy1 * 0.5) * dt
    vx2 = Ax(m, x + kx1 * 0.5, y + ky1 * 0.5, vx + vx1 * 0.5, vy + vy1 * 0.5) * dt
    vy2 = Ay(m, x + kx1 * 0.5, y + ky1 * 0.5, vx + vx1 * 0.5, vy + vy1 * 0.5) * dt
    kx3 = Vx(m, x + kx2 * 0.5, y + ky2 * 0.5, vx + vx2 * 0.5, vy + vy2 * 0.5) * dt
    ky3 = Vy(m, x + kx2 * 0.5, y + ky2 * 0.5, vx + vx2 * 0.5, vy + vy2 * 0.5) * dt
    vx3 = Ax(m, x + kx2 * 0.5, y + ky2 * 0.5, vx + vx2 * 0.5, vy + vy2 * 0.5) * dt
    vy3 = Ay(m, x + kx2 * 0.5, y + ky2 * 0.5, vx + vx2 * 0.5, vy + vy2 * 0.5) * dt
    kx4 = Vx(m, x + kx3, y + ky3, vx + vx3, vy + vy3) * dt
    ky4 = Vy(m, x + kx3, y + ky3, vx + vx3, vy + vy3) * dt
    vx4 = Ax(m, x + kx3, y + ky3, vx + vx3, vy + vy3) * dt
    vy4 = Ay(m, x + kx3, y + ky3, vx + vx3, vy + vy3) * dt
    dx=(kx1+2*kx2+2*kx3+kx4)/6
    dy=(ky1+2*ky2+2*ky3+ky4)/6
    dvx=(vx1+2*vx2+2*vx3+vx4)/6
    dvy=(vy1+2*vy2+2*vy3+vy4)/6
    x=x+dx
    y=y+dy
    vx=vx+dvx
    vy=vy+dvy
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    im,=plt.plot(x,y,"ro")
    ims.append([im])
ani=anm.ArtistAnimation(fig,ims,interval=10)
ani.save('gravity.mp4',writer="ffmpeg",fps=30)
plt.show()

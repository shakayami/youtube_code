from PIL import Image
import numpy as np
from collections import deque
import cv2
#注意：実行時間はとても長い
#H,Wは共に奇数でなくてはいけない
H=51
W=51

cellsize=8
#配色をRGBで表しています。
red=(219,68,85)
blue=(75,137,220)
black=(38,42,48)
white=(246,247,251)
yellow=(255,206,85)
gray=(170,178,189)
images=[]
image=Image.new('RGB',(H*cellsize,W*cellsize))
numbersofimages=1
def changecell(i,j,color):
    for x in range(cellsize*i,cellsize*(i+1)):
        for y in range(cellsize*j,cellsize*(j+1)):
            image.putpixel((x,y),color)
for i in range(H):
    for j in range(W):
        changecell(i,j,black)
images.append(image)
s=[["#" for j in range(W)] for i in range(H)]
def appendnewimage():
    global numbersofimages
    im=Image.new('RGB',(H*cellsize,W*cellsize))
    for i in range(H):
        for j in range(W):
            color=(-1,-1,-1)
            if s[i][j]=="#":
                color=black
            elif s[i][j]=="s":
                color=red
            elif s[i][j]=="g":
                color=blue
            elif s[i][j]=="*":
                color=yellow
            elif s[i][j]=="?":
                color=gray
            else:
                color=white
            for x in range(cellsize*i,cellsize*(i+1)):
                for y in range(cellsize*j,cellsize*(j+1)):
                    im.putpixel((x,y),color)
    images.append(im)
    numbersofimages+=1
    print(numbersofimages)
s[1][1]="."
appendnewimage()
stack=[(1,1)]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
while(stack):
    x,y=stack[-1]
    flag=0
    for k in np.random.permutation(np.array(range(4))):
        nx=x+2*dx[k]
        ny=y+2*dy[k]
        if not(0<=nx<H and 0<=ny<W):
            continue
        if s[nx][ny]=="#":
            s[nx-dx[k]][ny-dy[k]]="."
            s[nx][ny]="."
            appendnewimage()
            stack.append((nx,ny))
            flag=1
            break
    if flag==0:
        stack.pop()
#s[1][1]="s";s[-2][-2]="g"
start=(1,1);goal=(1,1)
flag=0
for i in range(1,H,2):
    for j in range(1,W,2):
        tmp=0
        for k in range(4):
            if s[i+dx[k]][j+dy[k]]==".":
                tmp+=1
        if tmp==1:
            start=(i,j)
            flag=1
            break
    if flag==1:
        break
dist=[[-1 for j in range(W)] for i in range(H)]
q=deque([start])
dist[start[0]][start[1]]=0
while(q):
    #bfsの場合こっち
    x,y=q.popleft()
    #dfsの場合こっち
    #x,y=q.pop()
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if not(0<=nx<H and 0<=ny<W):
            continue
        if s[nx][ny]==".":
            if dist[nx][ny]==-1:
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))
for line in dist:
    print(line)
print(start,goal)
for i in range(H):
    for j in range(W):
        if dist[i][j]>=dist[goal[0]][goal[1]]:
            goal=(i,j)
s[start[0]][start[1]]="s"
s[goal[0]][goal[1]]="g"
appendnewimage()
for index in range(10):
    appendnewimage()
mazequeue=deque([start])
prev=[[(-1,-1) for j in range(W)] for i in range(H)]
while(mazequeue):
    x,y=mazequeue.popleft()
    if not s[x][y] in {"s","g"}:
        s[x][y]="?"
        appendnewimage()
    if s[x][y]=="g":
        break
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if not(0<=nx<H and 0<=ny<W):
            continue
        if s[nx][ny] in {"#","?","s"}:
            continue
        mazequeue.append((nx,ny))
        prev[nx][ny]=(x,y)
for index in range(10):
    appendnewimage()
nowp=goal
root=[goal]
while(nowp!=start):
    x,y=nowp
    root.append((x,y))
    nowp=prev[x][y]

for nowp in root[::-1]:
    x,y=nowp
    if s[x][y]=="?":
        s[x][y]="*"
        appendnewimage()

for index in range(20):
    appendnewimage()

FILE_NAME = "maze.mp4"
FRAME_RATE = 30
FRAME_SIZE = (H*cellsize, W*cellsize)

rec = cv2.VideoWriter(FILE_NAME, cv2.VideoWriter_fourcc(*'mp4v'), FRAME_RATE, FRAME_SIZE, True)

for i in range(numbersofimages):
    imim=cv2.cvtColor(np.array(images[i]),cv2.COLOR_RGB2BGR)
    rec.write(imim)
rec.release()

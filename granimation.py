from PIL import Image
import numpy as np
import cv2
images=[]
image=Image.new('RGB',(256,256))
images.append(image)
for i in range(256):
    image=Image.new('RGB',(256,256))
    for j in range(256):
        for k in range(256):
            image.putpixel((j,k),(i,j,k))
    images.append(image)

FILE_NAME = "granimation.mp4"
FRAME_RATE = 30
FRAME_SIZE = (256, 256)

rec = cv2.VideoWriter(FILE_NAME, cv2.VideoWriter_fourcc(*'mp4v'), FRAME_RATE, FRAME_SIZE, True)

for i in range(256):
    print(i)
    imim=cv2.cvtColor(np.array(images[i]),cv2.COLOR_RGB2BGR)
    rec.write(imim)
rec.release()

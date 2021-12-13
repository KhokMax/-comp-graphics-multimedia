import numpy as np
from math import*

from PIL import Image, ImageDraw

image = Image.new('RGBA', (960,540))
draw = ImageDraw.Draw(image)

dataset = open('DS6.txt','r')
angle = radians(10*(6+1))
"""d - distance between origin and projection area"""
d = 90
array = np.zeros( (4, 4) )
array[0][0] = 1
array[1][1] = 1
array[2][2] = 1
array[2][3] = 1/d
print(array)
for line in dataset:
     line = line.split(" ")
     x = int(line[0]) - 480
     y = int(line[1]) - 480
     x1 = (x*cos(angle) - y*sin(angle)) + 480
     y1 = (x*sin(angle) + y*cos(angle)) + 480
     x1 = x1 - 540
     y1 = y1 - 960
     x2 = (x1*d)/100 + 540
     y2 = (y1*d)/100 + 960
     draw.point((x2, y2),'blue')
image.save('test.png')
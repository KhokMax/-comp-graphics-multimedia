from math import*

from PIL import Image, ImageDraw

image = Image.new('RGBA', (960, 960))
draw = ImageDraw.Draw(image)

dataset = open('DS6.txt','r')
angle = radians(10*(6+1))
for line in dataset:
     line = line.split(" ")
     x = int(line[0]) - 480
     y = int(line[1]) - 480
     draw.point(((x*cos(angle) - y*sin(angle)) + 480, (x*sin(angle) + y*cos(angle))+480),'blue')

image.save('test.png')

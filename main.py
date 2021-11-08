from PIL import Image, ImageDraw

image = Image.new('RGBA', (540, 960))
draw = ImageDraw.Draw(image)

dataset = open('DS6.txt','r')
for line in dataset:
     line = line.split(" ")
     draw.point((int(line[0]), int(line[1])),'black')

image.save('test.png')
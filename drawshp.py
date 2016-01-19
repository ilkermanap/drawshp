# -*- coding: utf-8 -*-
import shapefile, sys
from PIL import Image, ImageDraw

factor = int(sys.argv[2]) 

sf = shapefile.Reader(sys.argv[1])
boxX = (sf.bbox[2] - sf.bbox[0]) * factor
boxY = (sf.bbox[3] - sf.bbox[1]) * factor

xOffset = ((0 - sf.bbox[0])  * factor) - 20
yOffset = ((0 - sf.bbox[1]) * factor) - 155

print boxX,boxY 



img = Image.new("L",(int(boxX)  ,int(boxY)),255)
#img = Image.open("base.jpg")

drw = ImageDraw.Draw(img)

shapes = sf.shapes()
for s in shapes:
    prt = s.parts
  
    partLen = len(s.parts)
    partCheck = False
    jump = False
    if partLen > 1:
        partCheck = True
    i = 0
    x1,y1 = s.points[0]
    for pt in s.points[1:]:
        lines =[]
        i += 1
        if partCheck:
            if i in s.parts:
	        jump = True
        if jump:
            x1,y1 = pt
            jump = False
        else:
            x2,y2 = pt
            drw.line((int((x1 * factor + xOffset)), int(boxY - (y1 * factor + yOffset)),int((x2 * factor + xOffset)), int(boxY - (y2 * factor + yOffset))),0)
            #print((int(x1 + xOffset),int(y1 - yOffset),int(x2 + xOffset), int(y2 - yOffset)))
            x1 = x2
            y1 = y2
img.save(sys.argv[3],"JPEG")      
  #print(len(s.points))

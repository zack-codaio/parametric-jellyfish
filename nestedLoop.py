import rhinoscriptsyntax as rs
import random

#for i in range (0, 30, 3):
#    pt = (i, 5, i*20)
    
#for i in range(0, 30):
#    randNum = random.randint(30, 40);
#    pt = (i, 5*randNum, 1)
#    rs.AddPoint(pt)
    
    
#points = []
#for i in range (0, 30):
#    randNum = random.randint(30, 40);
#    pt = (i, 5*randNum, 1)
#    points.append(pt)
#    myFunction()
#    
#
#rs.AddPolyline(points)
#
#def myFunction():
#    print ("meow")
#    
##color
#myColor = (255, 0, 0)
#myCircle = rs.AddCircle((5,5,5), 10)
#rs.ObjectColor(myCircle, myColor)

rs.EnableRedraw(False)

def makeCircles(xVal, yVal, zVal):
    pt = (xVal, yVal, zVal)
    
    myColor = (xVal, yVal, zVal)
    
    rad = random.uniform(1,5)
    #myCircle = rs.AddCircle(pt, rad)
    mySphere = rs.AddSphere(pt, rad)
    rs.ObjectColor(mySphere, myColor)
    
for i in range(0, 255, 30):
    for j in range(0, 255, 20):
        for k in range(0, 255, 20):
            makeCircles(i, j, k)
            
rs.Redraw()



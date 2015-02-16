import rhinoscriptsyntax as rs
import random

pointsList = []

firstpoint = (0,0,0)
for i in range(0, 10):
    pt = (random.randint(0, i*10), random.randint(0, i*10), random.randint(0, i*10))
    if(i == 0):
        firstpoint = pt
    pointsList.append(pt)
pointsList.append(firstpoint)

crv1 = rs.AddCurve(pointsList)

pointsList = []

for i in range(0, 10):
    pt = (random.randint(0, i*10), random.randint(0, i*10), random.randint(0, i*10))
    if(i == 0):
        firstpoint = pt
    pointsList.append(pt)
pointsList.append(firstpoint)

crv2 = rs.AddCurve(pointsList)

rs.ExtrudeCrvAlongCrv(crv1, crv2)
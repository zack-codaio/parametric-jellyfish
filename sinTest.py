import math
import rhinoscriptsyntax as rs

mySineCurve = []

for i in range(20):
    pt = math.sin(i)
    
    rs.AddPoint(i, pt, 0)
    mySineCurve.append(pt)
    
print(mySineCurve)
rs.AddInterpCurve(mySineCurve)
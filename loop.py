import rhinoscriptsyntax as rs

for i in range(1, 90, 7):
    pt = (2*i, 3*i, i)
    rs.AddPoint(pt)
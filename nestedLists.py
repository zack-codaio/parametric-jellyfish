import rhinoscriptsyntax as rs

listOfLists = []

offset = 3

for i in range(0, 5):
    for j in range(0, 5):
        pts = []
        
        pt0 = (i , j, 0)
        pt1 = (i + offset, j, 0)
        pt2 = (i + offset, j+ offset, 0)
        pt3 = (i + offset, j+ offset, 0)
        
        pts.append(pt0)
        pts.append(pt1)
        pts.append(pt2)
        pts.append(pt3)
        listOfLists.append(pts)
        
        
print listOfLists

for i in listOfLists:
    rs.AddPolyline(i)

import rhinoscriptsyntax as rs

myInt = rs.GetInteger("Type an int.", 3, 2, 8)
#pt = rs.GetPoint("Please pick a point")

print(myInt)
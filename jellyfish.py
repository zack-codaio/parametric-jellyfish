import rhinoscriptsyntax as rs
import math
import random

origin = (0,0,0)


#make jellyfish body
#get radius
#get height
bodyRadius = rs.GetInteger("Set radius (1-10)", 5, 1, 10)
print(bodyRadius)
bodyHeight = rs.GetInteger("Set body height (1-20)", 5, 1, 20)
print(bodyHeight)

#set three points to make interpolated curve: origin, origin + radius / height, some midpoint (half of height, random radius added)
bodyList = []
bodyList.append(origin)
midRadius = random.random() * bodyRadius
midpoint = (0, midRadius, 0 - (bodyHeight / 2))
bodyList.append(midpoint)
endpoint = (0, bodyRadius, 0 - bodyHeight)
bodyList.append(endpoint)
print(bodyList)
bodyLine = rs.AddInterpCurve(bodyList)

bodyAxis = [(0,0,0), (0,0,1)]
bodySurface = rs.AddRevSrf(bodyLine, bodyAxis)
print("bodySurface")
print(bodySurface)

#bodySolid = rs.OffsetSurface(bodySurface, 10, 0.01, False, True)
if rs.IsSurface(bodySurface):
    print("is a surface")
    #bodySolid = rs.OffsetSurface(bodySurface, 1)
    centerLine = rs.AddLine(bodyAxis[0], bodyAxis[1])
    bodySolid = rs.ExtrudeSurface(bodySurface, centerLine)
print("bodySolid")
print(bodySolid)


#make jellyfish tentacles
#get number of tentacles
tentacleNum = rs.GetInteger("How many tentacles? (1-10)", 5, 1, 10)
print(tentacleNum)
#get swirliness - 0 : num tentacles, governs how far over the tentacle wil move to the next circle
tentacleSwirl = rs.GetInteger("How much swirl? (0 - "+str(tentacleNum)+")", 0, 0, tentacleNum)
print(tentacleSwirl)
#get bendiness
tentacleBend = rs.GetInteger("How much bendiness in tentacles? (2-10)", 3, 2, 10)
print(tentacleBend)
#get height - use variation from 75% - 125%
tentacleHeight = rs.GetInteger("Set tentacle height (5-50)", 20, 5, 50)
print(tentacleHeight)

curHeight = -0.5
tentacleArc = math.radians(360 / tentacleNum)
curAngle = 0
tentaclePoints = []

#for bendiness, set up circle of points
for i in range(0, tentacleBend):
    #set up circle
    
    print(curHeight)
    bendPoints = []
    
    #place points around circle
    for j in range(0, tentacleNum):
        if(i == 0):
            curPoint = (0, 0, -1)
            bendPoints.append(curPoint)
        else:
            curRadius = random.randint(50, 150) / 100 * bodyRadius
            curPoint = (math.cos(curAngle)*curRadius,math.sin(curAngle)*curRadius,curHeight)
            bendPoints.append(curPoint)
            curAngle += tentacleArc
    
    tentaclePoints.append(bendPoints)
    
    curHeight -= abs(tentacleHeight/tentacleBend * 5 * random.random())
    
print tentaclePoints

#for each tentacle
for i in range(0, tentacleNum):
    curTentacle = []
    curIndex = i
    for j in range(0, tentacleBend):
        curTentacle.append(tentaclePoints[j][curIndex])
        curIndex += tentacleSwirl
        if(curIndex >= tentacleNum):
            curIndex = curIndex % tentacleNum
    
    print(curTentacle)
    
    
    
    tentacleRail = rs.AddInterpCurve(curTentacle)
    
    #tentacleCross = rs.AddCircle([(1,0,-1),(1,0, -1),(10,-1,-1), (0,1,-1)], 1)
    tentacleCross = rs.AddCircle((0,0,-1), 1)
    
    newTentacle = rs.AddSweep1(tentacleRail, [tentacleCross])
    rs.ExtrudeSurface(newTentacle, centerLine)
    
    
    


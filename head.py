from math import atan2, pi
import numpy as np
import math



def getAng(a, b, c):

    M1 = (a[0]-b[0])/(a[1]-b[1])
    M2 = (c[0]-b[0])/(c[1]-b[1])
    
    PI = 3.14159265
     
    angle = (M2 - M1) / (1 + M1 * M2)
 
    # Calculate tan inverse of the angle
    ret = math.atan(angle)
 
    val = (ret * 180) / PI

    return val

approx = [[317,235]], [[277,202]], [[275,215]] ,[[183,218]] ,[[178,259]] ,[[276,257]], [[279,276]]

# approx = [[430, 416]],  [[410 ,399]], [[411 ,417]], [[294, 419]],[[293 ,455]], [[394, 446]], [[415, 458]]

# approx = [[127 ,228]], [[ 96, 273]], [[182, 345]], [[164 ,379]], [[232 ,351]], [[240, 275]], [[214 ,301]]
def findit(approx):
    yo = list(approx).copy()
    yo.append(yo[0])
    yo.append(yo[1])
    yo.append(yo[2])
    yo.append(yo[3])
    ans={}
    for i in range(0,7,1):
         ang = getAng(yo[i][0],yo[i+1][0],yo[i+2][0]) 
         if i == 6:
             j= 0
         else:
             j = i+1
         ans[j] = ang
         print(ang)
    temp = max(ans.values())
    res = [key for key in ans if ans[key] == temp]

    if res[0]>=3:
        one = res[0]
        two = res[0]-4
        three = res[0] -3
    else:
        one = res[0]
        two = res[0]+3
        three = res[0] +4

    return one,two,three




print(findit(approx))

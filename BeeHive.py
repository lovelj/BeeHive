import sys
import arcpy
from arcpy import env
import os
import math
#env.workspace="F:/lj/ppt/Hubei"

fc=arcpy.GetParameter(0)
#arcpy.SearchCursor("sheng_hubei.shp")

ext=arcpy.Describe(fc).extent
desc=arcpy.Describe(fc)
coord_sys=desc.spatialReference


dlen=arcpy.GetParameter(1)
#5000
sty=arcpy.GetParameter(2)
#"horizontal"
oFile=arcpy.GetParameter(3)
env.outputCoordinateSystem=coord_sys
point = arcpy.Point()
polygonlist=[]
array=arcpy.Array()

xmin=ext.XMin
xmax=ext.XMax
ymin=ext.YMin
ymax=ext.YMax

nx=0
ny=0
sx=0
if sty=="vertical":
    nx = xmin - math.sqrt(3) * dlen
    ny = ymin
    sx=nx

    point.X=nx
    point.Y=ny+dlen
    array.add(point)
    point.X=nx+ 0.5 * math.sqrt(3) * dlen
    point.Y=ny+ 0.5 * dlen
    array.add(point)
    point.X=nx + 0.5 * math.sqrt(3) * dlen
    point.Y=ny - 0.5 * dlen
    array.add(point)
    point.X=nx
    point.Y=ny - dlen
    array.add(point)
    point.X=nx - 0.5 * math.sqrt(3) * dlen
    point.Y=ny - 0.5 * dlen
    array.add(point)
    point.X=nx - 0.5 * math.sqrt(3) * dlen
    point.Y=ny + 0.5 * dlen
    array.add(point)
    polygon=arcpy.Polygon(array)
    polygonlist.append(polygon)
    array.removeAll()
    
    while (ny< ymax+1.5*dlen):
        while (nx < xmax):
            
            nx += math.sqrt(3) * dlen
            point.X=nx
            point.Y=ny+dlen
            array.add(point)
            point.X=nx+ 0.5 * math.sqrt(3) * dlen
            point.Y=ny+ 0.5 * dlen
            array.add(point)
            point.X=nx + 0.5 * math.sqrt(3) * dlen
            point.Y=ny - 0.5 * dlen
            array.add(point)
            point.X=nx
            point.Y=ny - dlen
            array.add(point)
            point.X=nx - 0.5 * math.sqrt(3) * dlen
            point.Y=ny - 0.5 * dlen
            array.add(point)
            point.X=nx - 0.5 * math.sqrt(3) * dlen
            point.Y=ny + 0.5 * dlen
            array.add(point)
            polygon=arcpy.Polygon(array)
            polygonlist.append(polygon)
            array.removeAll()
            
                        
        nx = sx-0.5*math.sqrt(3)*dlen

        if (nx < xmin - math.sqrt(3) * dlen - math.sqrt(3) * dlen):
            nx += math.sqrt(3) * dlen
                    
        sx = nx
        ny = ny + 1.5 * dlen
    arcpy.CopyFeatures_management(polygonlist,oFile)   
else:
    nx = xmin
    ny = ymin-math.sqrt(3)*dlen
    sx = nx
    while (ny < ymax + math.sqrt(3) * dlen):
        while (nx < xmax+ 1.5 * dlen):
            point.X=nx+0.5*dlen
            point.Y=ny+0.5 * math.sqrt(3) * dlen
            array.add(point)
            #1
            point.X=nx+ dlen
            point.Y=ny
            array.add(point)
            #2
            point.X=nx  + 0.5 * dlen
            point.Y=ny  - 0.5 * math.sqrt(3) * dlen
            array.add(point)
            #3
            point.X=nx- 0.5 * dlen
            point.Y=ny - 0.5 * math.sqrt(3) * dlen
            array.add(point)
            #4
            point.X=nx - dlen
            point.Y=ny
            array.add(point)
            #5
            point.X=nx  - 0.5 * dlen
            point.Y=ny + 0.5 * math.sqrt(3) * dlen
            array.add(point)
            #6
            polygon=arcpy.Polygon(array)
            polygonlist.append(polygon)
            array.removeAll()  
            
            point.X=nx + 1.5 * dlen+0.5*dlen
            point.Y=0.5 * math.sqrt(3) * dlen + ny+0.5 * math.sqrt(3) * dlen
            array.add(point)
            #1
            point.X=nx + 1.5 * dlen+ dlen
            point.Y=0.5 * math.sqrt(3) * dlen + ny
            array.add(point)
            #2
            point.X=nx + 1.5 * dlen  + 0.5 * dlen
            point.Y=0.5 * math.sqrt(3) * dlen + ny  - 0.5 * math.sqrt(3) * dlen
            array.add(point)
            #3
            point.X=nx + 1.5 * dlen- 0.5 * dlen
            point.Y=0.5 * math.sqrt(3) * dlen + ny - 0.5 * math.sqrt(3) * dlen
            array.add(point)
            #4
            point.X=nx + 1.5 * dlen - dlen
            point.Y=0.5 * math.sqrt(3) * dlen + ny
            array.add(point)
            #5
            point.X=nx + 1.5 * dlen  - 0.5 * dlen
            point.Y=0.5 * math.sqrt(3) * dlen + ny + 0.5 * math.sqrt(3) * dlen
            array.add(point)
            #6
            polygon=arcpy.Polygon(array)
            polygonlist.append(polygon)
            array.removeAll()

            
            nx += 3 * dlen
            
        nx = sx

        ny = ny + math.sqrt(3) * dlen
    arcpy.CopyFeatures_management(polygonlist,oFile)

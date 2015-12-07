import os
import csv
import arcpy
import timeit
#start_time = timeit.default_timer()

test_path = 'U:\\Shared\\GIS\GISData\\GA_DEM10m\\Taylor\\elevation_NED10M_ga269_1406514_01\\elevation\\ned10m32084e3.tif'
test_list = []
test_list.append(test_path)
folder = 'U:\\Shared\\GIS\\GISData\\GA_DEM10m\\'
tiflist = []
largetif = [] # List for checking excluded data
extlist = []
xsize = 79408000 #Variable for smallest county in directory

for path, dirs, files in os.walk(folder):
    for f in files:
        if f.endswith('.tif'):
            f = os.path.join(path, f)
            # if statement excludes geotiffs that are mosaiced 
            if os.stat(f).st_size < xsize:
                tiflist.append(f)
            if os.stat(f).st_size >= xsize:
                largetif.append(f)
print("The first loop is over")
counter = 0
for tif in tiflist:
    elevRaster = arcpy.sa.Raster(tif)
    myExtent = elevRaster.extent
    extlist.append((myExtent.XMin, myExtent.YMin, myExtent.XMax, myExtent.YMax))
    counter += 1
    print counter
    
zipped = zip(tiflist, extlist) 
##print(zipped)

with open('pathreference.csv', 'w') as output:
    writer = csv.writer(output)
    for z in zipped:
        writer.writerow([z[0], z[1][0], z[1][1], z[1][2], z[1][3]])
                        

#print(timeit.default_timer() - start_time)

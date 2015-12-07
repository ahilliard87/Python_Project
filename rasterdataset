import os
import csv
import arcpy

"""
    This program is designed to take the path of a shapefile with a corresponding projection to the Georgia
    10 meter DEMs stored on the U drive and retrieve all corresponding DEM. Then mosaic and clip them to
    the shapefile. The spatial reference should be NAD_1983_UTM_Zone_17N.
"""
    
arcpy.CheckOutExtension("Spatial")


shapefile = raw_input("Path to shapefile\n")

# Makes the shapefile into a feature lay in order to use extract by mask tool
arcpy.MakeFeatureLayer_management(shapefile, "shapefile")


raster_paths = []
with open('pathreference.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        raster_paths.append(row[0])

# Creates a file geodatabase to sore the raster dataset in
arcpy.management.CreateFileGDB(os.path.dirname(os.path.abspath(__file__)), "geodatabase")

# variable for .prj file of shapefile
prjfile = 'U:/Shared/GIS/StuData/amhill2604/FALL_2015/My_Python/PyProject/WTH_Tract/WTH_Tract.prj'

# Creates a Mosaic dataset for large amounts of tiles.
arcpy.CreateMosaicDataset_management("geodatabase.gdb", "raster_dataset", prjfile)

# Adds raster from csv file with path references
arcpy.management.AddRastersToMosaicDataset("geodatabase.gdb/raster_dataset", "Raster Dataset", raster_paths)

dataset_path = 'U:/Shared/GIS/StuData/amhill2604/FALL_2015/My_Python/PyProject/geodatabase.gdb'
extract = arcpy.sa.ExtractByMask(dataset_path, 'shapefile')


extract.save("output")
# Deletes GDB so the program can run again.
arcpy.Delete_management('U:/Shared/GIS/StuData/amhill2604/FALL_2015/My_Python/PyProject/geodatabase.gdb')





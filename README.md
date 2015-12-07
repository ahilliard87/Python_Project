# Python_Project

This project consistes of two phases.

The first file 'get_tif.py' is designed to retrieve all the tiles in the GA_DEM10m fodler on the UNG's U: drive.
It had to exclude the largest files pertaining to each county beacause they were crude mosaics of the couinty. Then get_tif create a csv file with the pathnmaes to each tile as well as the bounding box coordinates for each tile all in the same row. 

The main program rasterdataset.py takes all the tiles from the previous section and creates a mosaic dataset from them. Mosaic datasets are used when working with large sets of dats and the Georgia DEM tiles consisnt of apporamately 73GB of data. From here the dataset is in a file geodatabase and and s footprint index is created with the dataset. The next phase of the program is to use the shapefile of an AOI to extract the desired tiles, then mosaci and clip them appropriately. 

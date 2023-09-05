import arcpy
raster_path = r"C:\Users\shiva\Documents\programming_iii\P1_running_python_script\Practical_1_ProProject\Practical_1_ProProject\RASTER_DATA\RASTER_DATA\erelev"
desc_obj = arcpy.Describe(raster_path)

dataset_type = desc_obj.datasetType
print(dataset_type)
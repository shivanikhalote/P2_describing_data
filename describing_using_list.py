import arcpy
import os

gdp_path = r"C:\Users\shiva\Downloads\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb"
fc_name_list =["MajorAttractions","Freeways"]

for fc in fc_name_list:
    fc_path = os.path.join(gdp_path,fc)
    desc_obj = arcpy.Describe(fc_path)

    shape_type = desc_obj.shapeType

    dataset_type = desc_obj.datasetType
    print("the name of {} is {} and its feature type is {}".format(dataset_type,fc,shape_type))
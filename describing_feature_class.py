import arcpy
import os

#feature_class_path = r"C:\Users\shiva\Downloads\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb\MajorAttractions"
#majorattraction_object = arcpy.Describe(feature_class_path)
#print("the shape type of the file is {}".format(majorattraction_object.shapeType))

file_gdp_path = r"C:\Users\shiva\Downloads\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb"

majorattraction_feature_class = r"MajorAttractions"
majorattraction_full_path =os.path.join(file_gdp_path,majorattraction_feature_class)
majorattraction_object = arcpy.Describe(majorattraction_full_path)

print("feature type of MajorAttraction is {}".format(majorattraction_object.shapeType))

freeways_feature_class = r"Freeways"
freeways_full_path =os.path.join(file_gdp_path,freeways_feature_class)
freeways_object = arcpy.Describe(freeways_full_path)

print("feature type of freeways is {}".format(freeways_object.shapeType))


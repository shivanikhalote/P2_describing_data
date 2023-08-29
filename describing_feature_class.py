import arcpy

feature_class_path = r"C:\Users\shiva\Downloads\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb\MajorAttractions"

majorattraction_object = arcpy.Describe(feature_class_path)

print("the shape type of the file is {}".format(majorattraction_object.shapeType))
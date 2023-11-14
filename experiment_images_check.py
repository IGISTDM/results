import os
import json

method_list = ["AdaIN", "IGISTDM","RAASN"]
style_list = ["Cubism","Fauvism", "Pointillism", "Ukiyo_e"]

summary = {}
for method in method_list:
    method_record = {}
    for style in style_list:
        style_record = {}
        for image in os.listdir(f"./{method}/scene-{style}/"):
            file_name_split = image.split("-")
            content_name = file_name_split[0]
            if content_name in style_record:
                style_record[content_name] = style_record[content_name] + 1
            else:
                style_record[content_name] = 1
        method_record[style] = style_record
    summary[method] = method_record

# Write the dictionary to the JSON file
with open("summary.json", 'w') as json_file:
    json.dump(summary, json_file, indent=4)
        
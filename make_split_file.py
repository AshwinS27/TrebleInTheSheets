import os
import json
import numpy as np

###### META VARIABLES #####
NUM_TRAIN = 50#1275
NUM_VALID = 20#340
NUM_TEST = 10#50
###########################

path_to_images = './ds2_dense/images/'

# get image names
image_names = []
for name in os.listdir(path_to_images):
    if '.png' in name:
        image_names.append(name)


dict = {
    "train": [],
    "validation": [],
    "test": []
}

i = 0
for f_name in image_names:
    image_name = f_name
    ground_truth = f_name.replace(".png", "_seg.png")
    GT_quantize = ground_truth + ".npy"
    arr = [image_name, ground_truth, GT_quantize]

    if (i < NUM_TRAIN):
        dict["train"].append(arr)
    elif (i < NUM_TRAIN + NUM_VALID):
        dict["validation"].append(arr)
    elif (i < NUM_TRAIN + NUM_VALID + NUM_TEST):
        dict["test"].append(arr)

    i+=1 


#TURN TO JSON OBJECT AND PRINT
json_object = json.dumps(dict, indent = 4) 
print(json_object)
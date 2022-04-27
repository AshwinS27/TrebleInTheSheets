import os
import numpy as np
import cv2

labels = {
    # Void has label 0
    'line_note': ([100, 100, 200], [125, 150, 255]), # 1
    'quarter_rest': ([89, 150, 200], [90, 200, 255]), # 2
    'clef': ([100, 220, 200], [125, 255, 255]), # 3
    'gap_note':([0, 230, 50], [10, 255, 75]) # 4
}

# Void, note, rest

# TODO: Make an index for each type of object in the image. Make a .npy
# TODO: Class to color, translate a string to its color value
def filter(filename):
    image = cv2.imread(filename)

    res = np.zeros((image.shape[0], image.shape[1]))

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    label = 1

    for color, bound in labels.items():
        lower = np.array(bound[0], dtype="uint8")
        upper = np.array(bound[1], dtype="uint8")

        mask = cv2.inRange(hsv, lower, upper)
        
        # Use for debugging
        # cv2.imwrite("result" + str(label) + ".png", mask)
        

        # add in the label for the corresponding object
        res = np.where(mask == 0, res, label)

        label += 1

    # Save the numpy
    np.save("numpys/" + filename[11:], res)

    # Use for visualization, make everything detected white except for the void
    res = np.repeat(res[:, :, np.newaxis], 3, axis=2)
    res = np.where(res > 0, hsv, 0)
    cv2.imwrite("ground_truth/" + filename[11:], res)

def main():
    for filename in os.scandir("pre_filters"):
        if filename.is_file():
            print(filename.path)
            filter(filename.path)



if __name__ == "__main__":
    main()
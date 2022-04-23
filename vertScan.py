import os
import numpy as np
import matplotlib.pyplot as plt

import cv2

def verticalScan(filename):
    #img = plt.imread(filename)
    #img = img.convert('L')
    #print(img.shape)
    	
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    vertScanMat = np.sum(gray <= 70, axis=1) 
    bar = np.zeros(gray.shape)
    for i in range(bar.shape[0]):
        if (vertScanMat[i] > gray.shape[1]/3):  
            bar[i,:] = 255
    cv2.imwrite("vert_scan/" + filename[7:], bar)


def main():
    for filename in os.scandir("images"):
        if filename.is_file():
            print(filename.path)
            verticalScan(filename.path)



if __name__ == "__main__":
    main()
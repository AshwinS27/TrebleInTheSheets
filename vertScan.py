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
    bar = np.empty(gray.shape)
    bar.fill(255)
    for i in range(bar.shape[0]):
        if (vertScanMat[i] > gray.shape[1]/3):  
            bar[i,:] = 0
        #bar[i,0:vertScanMat[i]] = 0
    cv2.imwrite("vert_scan/" + filename[7:], bar)

def findFirstStaff(startRow, lines):
    #keep going 20 pixels up, if there is black, need to go 20 pixels up and add 1
    #lines = cv2.bitwise_not(lines)
    lineNum = 0
    pixelsGoneOn = 0
    for i in range(120):
        if lines[startRow - i , 0] > 10:
            #We have hit a line
            lineNum+= 1
            pixelsGoneOn = 0
        else:
            pixelsGoneOn += 1
        if (pixelsGoneOn > 20):
            #We are have passed first line
            return lineNum

def identifyStaffLine(img1, img2):
    #TODO: Suppose I have the bar image..I can overlay with given image, and then 
    #identify and intersecting pixels. With intersecting pixels, I can identify where it
    #is in staff line bar thing, and then perhaps look at at surrounding layers above for black pixel?
    img2 = cv2.bitwise_not(img2)
    bw_and = cv2.bitwise_and(img1, img2)
    #bw_and represents all the intersections with the staff
    result = np.where(bw_and > 0)
    #print(intersect)
    listOfCoordinates= list(zip(result[0], result[1]))
    row = np.unique(result[0])
    print(row)
    print("LineNum:",findFirstStaff(row[5],img2))
    #print(listOfCoordinates)

    print(cv2.imwrite("Bitwise_and.png", bw_and))
    #print(cv2.imwrite("Bitwise_and.png", img2))


def main():
    # for filename in os.scandir("images"):
    #     if filename.is_file():
    #         print(filename.path)
    #         verticalScan(filename.path)
    file_n = "lg-5230237-aug-lilyjazz--page-2.png"
    img1 = cv2.imread("hey.png",0)
    img2 = cv2.imread("vert_scan/" + file_n,0)
    #img1 = np.zeros(img2.shape)
    #cv2.imwrite("hey.png", img1)
    identifyStaffLine(img1, img2)



if __name__ == "__main__":
    main()
#!/usr/bin/env python3

"""
Author: Sara Hemati

This script calibrate cynor camera and save its calibration data in a file which name is calibration_data.pickle
we can calibrate any image that will be taken by cynor camera with these data (calibration_data.pickle file)
chessbOard images should be in a same folder beside this file

"""

import numpy as np
import cv2 as cv
import glob
import pickle 


# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((4*4,3), np.float32)
objp[:,:2] = np.mgrid[0:4,0:4].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('*.png')
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (4,4), None)
    
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        
        # Draw and display the corners
        cv.drawChessboardCorners(img, (4,4), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)
cv.destroyAllWindows()



ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("rent =",ret)
print("mtx =",mtx)
print("dist =",dist)
print("rvecs =",rvecs)
print("tvecs =",tvecs)

# make a new file to save calibration data of cynor camera in it which name is calibration_data.pickle
fs = open('calibration_data.pickle', 'wb')
pickle.dump([ret, mtx, dist, rvecs, tvecs], fs)
fs.close()

# for read fs file use pickle.read command (this command is used in next file (undistort.py) )

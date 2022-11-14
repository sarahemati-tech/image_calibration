#!/usr/bin/env python3

"""
Author: Sara Hemati

This script calibrate any image that took by cynor camera
we use one sample image (03.png) to calibrate with this scrits which is located in the same folder beside this file
you should locate any image that you want to calibrate with this camera, in a specifice folder beside this file and camera parameters file (calibration_data.pickle) that was created after running calibrate.py file (which means you should run calibrate.py file befor this file)

"""

from PIL import Image
import glob
import numpy as np
import cv2 as cv
import glob
import pickle 

#read camera data file (calibration_data.pickle) to calibrate image which is taken by Cynor camera and located beside this file
fs = open('calibration_data.pickle', 'rb')
data = pickle.load(fs)
ret, mtx, dist, rvecs, tvecs = data

# read image which is taken by Cynor camera and located beside this file
image_list = []
i=0
for distort_line_picture in glob.glob('/home/sara/digin_next/camera-images/distort_line_picture/*.png'): #assuming png
	im=cv.imread(distort_line_picture)
	image_list.append(im)
	h,  w = im.shape[:2]
	newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))


	# undistort 
	dst = cv.undistort(im, mtx, dist, None, newcameramtx)

	# crop the image and save it in this folder
	x, y, w, h = roi
	dst = dst[y:y+h, x:x+w]
	i+=1
	cv.imwrite("calibrated_%02d.png"%i, dst)
	

#!/usr/bin/env python3

"""
Author: Sara Hemati

This function calibrate any image that took by cynor camera


"""

import numpy as np
import cv2 as cv
import glob
import pickle 

def undistort(img):

	fs = open('calibration_data.pickle2', 'rb')
	data = pickle.load(fs)
	ret, mtx, dist, rvecs, tvecs = data

	h,  w = img.shape[:2]
	newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

	# undistort
	dst = cv.undistort(img, mtx, dist, None, newcameramtx)
	
	# crop the image
	x, y, w, h = roi
	dst = dst[y:y+h, x:x+w]
	
	return dst
	
	
	
	

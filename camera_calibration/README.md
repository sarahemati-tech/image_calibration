In this folder, there are:
-16 pictures of chessboard: Using for calibration proccess (calibrate.py) to gain calibration parameters (calibration_data.pickle)
-one uncalibrated picture of line: Taken by Cynor camera, using for testing calibration parameters
-calibrated picture of line: Result of using calibration parameteres (calibration_data.pickle) in undistort.py file
-calibrate.py: This file get chessboard pictures then give calibration parameters
-calibration_data.pickle: Calibration parameters of Cynor camara which are gained after running calibrate.py file
-undistort.py: Any picture that is taken by Cynor camera could give to this file and get calibrated picture as result.

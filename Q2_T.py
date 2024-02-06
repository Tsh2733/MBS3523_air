import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cam.read()
    width = cam.get(3)
    height = cam.get(4)

    frameResize = cv2.resize(frame, (int(width / 2), int(height / 2)))

    cv2.imshow('Original Frame', frameResize)

    gaussian_blur = cv2. GaussianBlur (frameResize, (25, 25), 0)
    cv2.imshow("Gaussian Blur", gaussian_blur)

    hsv_frame = cv2.cvtColor (frameResize, cv2. COLOR_BGR2HSV)
    cv2.imshow("HSV Color Space", hsv_frame)

    gray_frame = cv2. cvtColor (frameResize, cv2. COLOR_BGR2GRAY)
    blurred_frame = cv2. GaussianBlur (gray_frame, (5, 5), 0)
    canny_edges = cv2. Canny (blurred_frame, 100, 200)
    canny_edges_bgr = cv2. cvtColor (canny_edges, cv2. COLOR_GRAY2BGR)
    cv2.imshow ("Canny Edges", canny_edges_bgr)

    cur_time = time. time()
    key = cv2. waitKey(1)
    if key == ord('q'):
       break

cam. release()
cv2.destroyAllWindows()
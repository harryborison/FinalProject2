import cv2
import numpy as np

cap = cv2.VideoCapture(-1)

while True:
	ret, frame = cap.read()
	cv2.imshow('frame', frame)
	key = cv2.waitKey(25)
	if key == 27:
		break

if cap.isOpened():
	cap.release()
cv2.destroyAllWindows()

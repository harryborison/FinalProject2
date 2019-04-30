import numpy as np
import cv2

cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture('./data/thermal_boar_bandicut.mp4')

cnt = 1

while True:
	retval, frame = cap.read()
	if not retval:
		break

	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

	detection = cascade.detectMultiScale(gray, 1.3, 5)
	for(x,y,w,h) in detection:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 5)
	cv2.imshow('frame', frame)

	key = cv2.waitKey(25)
	if key==27:
		break
	#detected movie capture
	elif key == ord('s'):
		name = './capture/test'+str(cnt)+'.png'
		cv2.imwrite(name, frame)
		cnt += 1

if cap.isOpened():
	cap.release()

cv2.destroyAllWindows()

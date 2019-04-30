import cv2

cap = cv2.VideoCapture('./data/normal_boar.mp4')
cnt=1

while True:
	retval, frame = cap.read()
	if not retval:
		break

	cv2.imshow('frame', frame)

	key = cv2.waitKey(25)
	if key == 27:
		break
	elif key == ord('s'):
		name = 'capture/test'+str(cnt)+'.png'
		cv2.imwrite(name, frame)
		cnt+=1

if cap.isOpened():
	cap.release()

cv2.destroyAllWindows()

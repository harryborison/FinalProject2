import cv2

cap = cv2.VideoCapture(-1)

#fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#out = cv2.VideoWriter('appsrc ! queue ! videoconvert ! video/x-raw ! omxh264enc ! video/x-h264 ! h264parse ! rtph264pay ! udpsink host=192.168.0.12 port=5000 sync=false', 0, 25.0, (640,480))
#video = cv2.VideoWriter('appsrc ! queue ! videoconvert ! video/x-raw ! omxh264enc ! video/x-h264 ! h264parse ! rtph264pay ! udpsink host=192.168.0.2 port=5000 sync=false',0,25.0,(640,480))

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('appsrc  ! h264parse ! '
                      'rtph264pay config-interval=1 pt=96 ! '
                      'gdppay ! tcpserversink host=192.168.0.12 port=5000 ',
                      fourcc, 20.0, (640, 480))

while cap.isOpened():
	ret, frame = cap.read()

	if ret:
		frame = cv2.flip(frame, 0)

		out.write(frame)

		if cv2.waitKey(1) & 0xFF==ord('q'):
			break
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()

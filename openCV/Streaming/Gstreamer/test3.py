import cv2

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("v4l2src ! video/x-raw, framerate=10/1,  width=640, height=480, format=RGB ! videoconvert ! appsink")

framerate = 25.0

#out = cv2.VideoWriter('appsrc ! videoconvert ! h264parse ! '
#                      'x264enc noise-reduction=10000 speed-preset=ultrafast tune=zerolatency ! '
#                      'rtph264pay config-interval=1 pt=96 ! gdppay ! '
#                      'tcpserversink host=192.168.0.12 port=5000 sync=false',
#                      0, framerate, (640, 480))
#out=cv2.VideoWriter('appsrc ! videoconvert ! video/x-raw ! x264enc tune=zerolatency !  rtph264pay ! gdppay ! tcpserversink host=192.168.0.12 port=5000 sync=false', 0, 25.0, (640,480))
out=cv2.VideoWriter('appsrc !  videoconvert ! x264enc tune=zerolatency ! rtph264pay ! gdppay ! tcpserversink host=192.168.0.12 port=5000 sync=false', 0, 10.0, (640,480), True) # working!!!!!!!!!!!!!!1
#out=cv2.VideoWriter('appsrc ! videoconvert ! video/x-raw ! x264enc tune=zerolatency ! rtph264pay ! gdppay ! tcpserversink host=192.168.0.12 port=5000 sync=false', 0, 25.0, (640,480))
#out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc noise-reduction=10000 spped-preset=ultrafast tune=zerolatency ! rtph264pay config-interval=1 pt=96 ! tcpserversink host=192.168.0.12 port=5000 sync=false', 0, 30.0, (640, 480))
#out=cv2.VideoWriter('appsrc ! video/x-raw, width=640, height=480, format=RGB !  videoconvert ! x264enc tune=zerolatency ! rtph264pay ! gdppay ! tcpserversink host=192.168.0.12 port=5000 sync=false', 0, 10.0, (640,480), True)


while cap.isOpened():
    ret, frame = cap.read()
    if ret:

        out.write(frame)
	cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()

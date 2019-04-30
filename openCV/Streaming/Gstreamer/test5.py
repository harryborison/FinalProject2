import cv2

cap = cv2.VideoCapture(-1)

framerate = 25.0

#out = cv2.VideoWriter('appsrc ! video/x-raw, width=640, height=480 ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! gdppay ! tcpserversink host=192.168.0.12 port=5000 sync=false', 0, 25.0, (640,480))
fourcc =cv2.VideoWriter_fourcc(*'X264')
#out = cv2.VideoWriter("appsrc ! video/x-raw, width=640, height=480 ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! gdppay ! tcpserversink host=192.168.0.12 port=5000", 0, 20.0, (640, 480), True)
#out = cv2.VideoWriter("appsrc ! video/x-raw, framerate=30/1, width=640, height=480 ! autovideoconvert ! autovideosink sync=false", 0, 30.0, (640,480), True)
out = cv2.VideoWriter("appsrc ! video/x-raw, width=640, height=480 ! videoconvert ! x264enc tune=zerolatency ! rtph264pay ! gdppay ! tcpserversink host=192.168.0.12 port=5000", 0, 30.0, (640, 480), True);




while cap.isOpened():
    ret, frame = cap.read()
    if ret:

#	cv2.imshow('frame', frame)
        out.write(frame)
# 	cv2.imshow('frame', frame)

#        if cv2.waitKey(1) & 0xFF == ord('q'):
#            break
    else:
        break

# Release everything if job is finished
cap.release()
#out.release()

import cv2
import numpy as np

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
detect_cnt=0
def people_detection(frame):
    global detect_cnt

    print('detecting people...')
    loc2, weights2 = hog.detectMultiScale(frame)

    if len(loc2)>0:
        dst2 = frame.copy()
        for rect in loc2:
            x, y, w, h = rect
            cv2.rectangle(dst2, (x, y), (x+w, y+h), (0,255,0),2)
	detect_cnt+=1
        cv2.imwrite('./output/detected' + str(detect_cnt) + '.jpg', dst2)
	print('detected!')
        return True;

    else:
	print('not detected!')
        return False;


cap = cv2.VideoCapture(-1)

height, width = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                 int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))

TH      = 40  # binary threshold
AREA_TH = 80 # area   threshold
acc_bgr = np.zeros(shape=(height, width, 3), dtype=np.float32)

mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE

#2
t = 0
delay=0
detected = False
while detected==False:
    ret, frame = cap.read()
    if not ret:
        break
    t+=1
    print("t = ", t)
    blur = cv2.GaussianBlur(frame,(5,5),0.0)
#2-1
    if t < 50:
        cv2.accumulate(blur, acc_bgr)
        continue
    elif t == 50:
        bkg_bgr = acc_bgr/t
#2-2: t >= 50
##    diff_bgr = cv2.absdiff(np.float32(blur), bkg_bgr).astype(np.uint8)
    diff_bgr = np.uint8(cv2.absdiff(np.float32(blur), bkg_bgr))
    db,dg,dr = cv2.split(diff_bgr)
    ret, bb = cv2.threshold(db,TH,255,cv2.THRESH_BINARY)
    ret, bg = cv2.threshold(dg,TH,255,cv2.THRESH_BINARY)
    ret, br = cv2.threshold(dr,TH,255,cv2.THRESH_BINARY)
    bImage = cv2.bitwise_or(bb, bg)
    bImage = cv2.bitwise_or(br, bImage)
    bImage = cv2.erode(bImage,None, 5)
    bImage = cv2.dilate(bImage,None,5)
    bImage = cv2.erode(bImage,None, 7)
    #cv2.imshow('bImage',bImage)
    msk = bImage.copy()
    contours, hierarchy = cv2.findContours(bImage, mode, method)
    cv2.drawContours(frame, contours, -1, (255,0,0), 1)
    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area > AREA_TH:
            # movement detected
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+width, y+height), (0,0,255), 2)
            cv2.rectangle(msk, (x, y), (x+width, y+height), 255, -1)

            delay+=1;
            if delay%100==0:
                result = people_detection(frame)
                if result==True:
                    print('people detected')
                    detected=True
                else:
                    print('continue')

                delay=0;


    msk = cv2.bitwise_not(msk)
    cv2.accumulateWeighted(blur,bkg_bgr, alpha=0.1,mask=msk)

    cv2.imshow('frame',frame)
    #cv2.imshow('bkg_bgr',np.uint8(bkg_bgr))
    #cv2.imshow('diff_bgr',diff_bgr)
    key = cv2.waitKey(25)
    if key == 27:
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()

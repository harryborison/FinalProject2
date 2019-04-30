import numpy as np
import cv2

cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread('./data/test1.png')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

detection = cascade.detectMultiScale3(
	gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30,30),
	flags = cv2.CASCADE_SCALE_IMAGE,
	outputRejectLevels = True
)

rects = detection[0]
neigh = detection[1]
weights = detection[2]

print(rects)
print(neigh)
# print classifier confidence
print(weights)

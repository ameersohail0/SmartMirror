#!/usr/bin/python

'''
Author: Ameer Sohail
Description: Face and eye Detection throught the camera and capture for a single face present in the frame. 

'''

import cv2
import sys
import random
import time

imgName = random.randrange(1, 100)
imgName = "../temp/"+str(imgName)+".jpg"

fCascPath = '../cascades/haarcascade_frontalface_default.xml'
eCascPath = '../cascades/haarcascade_eye.xml'

faceCascade = cv2.CascadeClassifier(fCascPath)
eyeCascade = cv2.CascadeClassifier(eCascPath)


video_capture = cv2.VideoCapture(0)


while True:
    # Capturing Frames Continously until a face is detected

	ret, frame = video_capture.read()

	grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(grayImg, 1.3, 5)

	for (x,y,w,h) in faces:
		frGrayImg = grayImg[y:y+h, x:x+w]
		frColor = frame[y:y+h, x:x+w]
		eyes = eyeCascade.detectMultiScale(frGrayImg)
		print("eyes: ",len(eyes))
	
	cv2.imshow('frame', frame)
	print("face: ",len(faces))
	
	if len(faces) == 1 and len(eyes) > 0 :
		print(len(faces),len(eyes))
		time.sleep(1)
		cv2.imwrite(imgName,frame)
		print('done')
		break

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
		for(ex,ey,ew,eh) in eyes:
			cv2.rectangle(fc_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	

	if cv2.waitKey(30) & 0xff == 27:
		break

video_capture.release()
cv2.destroyAllWindows()



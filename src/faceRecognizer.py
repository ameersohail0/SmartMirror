#!/usr/bin/python

import cv2, os
import numpy as np
from PIL import Image


cascadePath = "../cascades/haarcascade_frontalface_default.xml"
eCascPath = '../cascades/haarcascade_eye.xml'

eyeCascade = cv2.CascadeClassifier(eCascPath)
faceCascade = cv2.CascadeClassifier(cascadePath)

recognizer = cv2.createLBPHFaceRecognizer()

def get_images_and_labels(path):
	    
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
	
    images = []
	
    labels = []
	
    for image_path in image_paths:
		
        image_pil = Image.open(image_path).convert('L')
		
        image = np.array(image_pil, 'uint8')
		
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
        
        faces = faceCascade.detectMultiScale(image)
        
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)
    
    return images, labels

# Path to the Yale Dataset
path = '../faceDatabase'
# Call the get_images_and_labels function and get the face images and the 
# corresponding labels
images, labels = get_images_and_labels(path)
cv2.destroyAllWindows()

# Perform the tranining
recognizer.train(images, np.array(labels))

# Append the images with the extension .sad into image_paths
pathn = '../temp/'
image_paths = [os.path.join(pathn, f) for f in os.listdir(pathn) if f.endswith('.jpg')]
for image_path in image_paths:
	predict_image_pil = Image.open(image_path).convert('L')
	predict_image = np.array(predict_image_pil, 'uint8')
	faces = faceCascade.detectMultiScale(predict_image,1.3, 5)
	print(len(faces))
	
	for (x, y, w, h) in faces:
		#fc_color = predict_image[y:y+h, x:x+w]
		eyes = eyeCascade.detectMultiScale(predict_image[y: y + h, x: x + w])
		print(len(faces),len(eyes))
		
		if len(faces) == 1:
		
			nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
	        #nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
	        #if nbr_actual == nbr_predicted:
			if conf < 90:
				print "{} is Correctly Recognized with confidence {}".format(nbr_predicted, conf)
				
			else:
				print "Please register, or continue as guest"
				#cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
			#cv2.waitKey(1000)

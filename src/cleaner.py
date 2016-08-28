#!/usr/bin/python

'''
Author: Ameer Sohail
Description: Image removal script

'''

import os
pathn = os.path.dirname(__file__)+'/../temp/'

image_paths = [os.path.join(pathn, f) for f in os.listdir(pathn) if f.endswith('.jpg')]

for image_path in image_paths:
	os.remove(image_path)



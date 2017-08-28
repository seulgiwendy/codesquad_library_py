#-*- coding: utf-8 -*-
import zbar
import Image
import cv2
import requests, json

def detect():
	scanner = zbar.ImageScanner()
	scanner.parse_config('enable')
	cap = cv2.VideoCapture(0)

	exitFlag = True
	while(exitFlag):
		ret, cv = cap.read()
		cv = cv2.cvtColor(cv, cv2.COLOR_BGR2GRAY)
		pil = Image.fromarray(cv)
		width, height = pil.size
		raw = pil.tostring()

		image = zbar.Image(width, height, 'Y800', raw)

		scanner.scan(image)

		for symbol in image:
			print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
			exitFlag = False	

	return symbol.data


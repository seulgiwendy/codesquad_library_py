#-*- coding: utf-8 -*-
#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv  

import RPi.GPIO as GPIO  
from detect_qr import *
import requests, json
from time import sleep


GPIO.setmode(GPIO.BCM)  

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

URL = 'http://ec2-13-124-108-27.ap-northeast-2.compute.amazonaws.com:8080'

def title(channel):  
	global URL
	print ('도서 인식')
	title = detect()
	bookData = {'title': title}
	res = requests.post(URL + '/user', data=bookData)

def userAndTitle(channel):
	global URL
	print("유저 인식")
	userId = detect()	
	#sleep(2)
	print("도서 인식")
	title = detect()
	userData = {'userId': userId, 'title': title}
	res = requests.post(URL + '/lent', data=userData)

GPIO.add_event_detect(24, GPIO.RISING, callback=title)  
GPIO.add_event_detect(18, GPIO.RISING, callback=userAndTitle)

try:  
	print "1번 버튼 종료, 2번 버튼 도서 인식, 3번 버튼 유저 및 도서 인식"
	GPIO.wait_for_edge(23, GPIO.FALLING)  
	print "종료 합니다."

except KeyboardInterrupt:  
	GPIO.cleanup()
GPIO.cleanup()

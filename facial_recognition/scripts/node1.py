#!/usr/bin/env python

import numpy as np
import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from facial_recognition.msg import face_crop1


face_cascade = cv2.CascadeClassifier('/home/ashwathrajcapur/catkin_ws/src/facial_recognition/scripts/frontal_face_haar.xml')
cap = cv2.VideoCapture(0)


while cap.isOpened()==True:
	pub = rospy.Publisher('feed', Image, queue_size=10)
	rospy.init_node('bounding_box_publisher', anonymous=True)
	rate = rospy.Rate(10)
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(img, 1.3, 5)
	cropped = None
	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0),2)
            	cropped = img[y:y+h, x:x+w]
			
	cv2.imshow('frame',cropped)
	
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
	
	bridge= CvBridge()
	image = bridge.cv2_to_imgmsg(img,encoding='passthrough')
	pub.publish(image)
	rate.sleep()
	
	

	if cv2.waitKey(25) & 0xff == ord('q'):
		break

cap.release()

cv2.destroyAllWindows()

		


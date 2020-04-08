#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

def callback(data):
	try:
		bridge= CvBridge()
		img = bridge.imgmsg_to_cv2(data, "32FC1")
	
	except CvBridgeError as e:
		print(e)

	cv2.imshow('Image Window', img)
	cv2.waitKey(1)

def __init__():
	rospy.init_node('Image_Subscriber')
	rospy.Subscriber('/camera/depth/image_raw', Image, callback)
	rospy.spin()
	
if __name__ == '__main__':
	try:
		__init__()
	except rospy.ROSInterruptionException:
		pass

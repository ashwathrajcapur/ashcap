#!/usr/bin/env python

import rospy

from task1.msg import nameage
from task1.msg import eligibility

n=eligibility()

def callback (data):
	print "Data Received"
	name=data.name
	if data.age >= 18:
		n.eligibility = "Eligible"
	elif data.age < 18:
		n.eligibility = "Ineligible"
	pub = rospy.Publisher('fin', eligibility, queue_size=10)
	rospy.loginfo(n)
	pub.publish(n)
	

def lis():

	rospy.init_node('lis', anonymous=True)
	
	rospy.Subscriber('tlk', nameage, callback)

	rospy.spin()

if __name__ == '__main__':
	lis()


		

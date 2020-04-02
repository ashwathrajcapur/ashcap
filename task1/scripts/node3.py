#!/usr/bin/env python

import rospy
from task1.msg import nameage
from task1.msg import eligibility


def callback1(data):
	print data.name

def callback2(data):
	print data


def lis1():
	rospy.init_node('lis1', anonymous=True)
	rospy.Subscriber('tlk', nameage, callback1)
	rospy.Subscriber('fin', eligibility, callback2)
	rospy.spin()

if __name__ == '__main__':
	lis1()

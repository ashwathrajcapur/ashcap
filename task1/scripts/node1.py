#!/usr/bin/env python

import rospy 
from task1.msg import nameage

def ntlk():
	
	
	pub= rospy.Publisher('tlk', nameage, queue_size=10)
	rospy.init_node('ntlk', anonymous=True)
	k = nameage();
	rate= rospy.Rate(10)
	while not rospy.is_shutdown():
		k.name= "Ashwath"
		k.age= 19
		rospy.loginfo(k)
		pub.publish(k)
		rate.sleep()
	
	
if __name__ == '__main__':
	try:
		ntlk()
	except rospy.ROSInterruptException:
		pass

#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import Float64

def movejoint1():
    x = input('joint1: ')
    pub1 = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=10)
    rospy.init_node('movejoint1', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
	if abs(x) > pos:
        	rospy.loginfo(x)
        	pub1.publish(x)
		x = input('joint1: ')
	else:
		rospy.loginfo(pos)
		pub1.publish(pos)
		x = input('joint1: ')


        rate.sleep()

if __name__ == '__main__':
    try:
		pos = 0	
        	movejoint1()	

    except rospy.ROSInterruptException:
        pass



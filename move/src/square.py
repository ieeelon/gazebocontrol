#!/usr/bin/env python
import rospy
import sys
import time
from std_msgs.msg import Float64

def square():
    x = input('joint (put 1/5): ')
    pos = 0	
    pub1 = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/robot/joint5_position_controller/command', Float64, queue_size=10)
    rospy.init_node('square', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
	
	if x == 1:
		t10 = time.time()
		while pos == 0:
        		rospy.loginfo(pos)
        		pub1.publish(pos)
			dt = int(time.time()-t10)
			if dt >= 4:
				pos = 1
		t11 = time.time()
		while pos == 1:
			rospy.loginfo(pos)
			pub1.publish(pos)
			dt = int(time.time()-t11)
			if dt >= 4:
				pos = 0
	else:
		t10 = time.time()
		while pos == 0:
        		rospy.loginfo(pos)
        		pub2.publish(pos)
			dt = int(time.time()-t10)
			if dt >= 4:
				pos = 1
		t11 = time.time()
		while pos == 1:
			rospy.loginfo(pos)
			pub2.publish(pos)
			dt = int(time.time()-t11)
			if dt >= 4:
				pos = 0
		


        rate.sleep()

if __name__ == '__main__':
    try:

        	square()	

    except rospy.ROSInterruptException:
        pass



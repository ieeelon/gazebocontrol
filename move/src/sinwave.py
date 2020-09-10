#!/usr/bin/env python
import rospy
import sys
import time
import datetime
import numpy as np

from std_msgs.msg import Float64

def sinwave():
    x = input('joint (put 1/5): ')
    pos = 0	
    pub1 = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/robot/joint5_position_controller/command', Float64, queue_size=10)
    rospy.init_node('sinwave', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
	
	if x == 1:
		t10 = datetime.datetime.now()
		while pos == 0:
			dt = (datetime.datetime.now()-t10).total_seconds()
        		rospy.loginfo(2*np.sin(dt))
        		pub1.publish(2*np.sin(dt))

		t11 = datetime.datetime.now()
		while pos == 1:
			dt = (datetime.datetime.now()-t11).total_seconds()
			rospy.loginfo(2*np.sin(dt))
			pub1.publish(2*np.sin(dt))

	else:
		t10 = datetime.datetime.now()
		while pos == 0:
			dt = (datetime.datetime.now()-t10).total_seconds()
        		rospy.loginfo(2*np.sin(dt))
        		pub2.publish(2*np.sin(dt))

		t11 = datetime.datetime.now()
		while pos == 1:
			dt = (datetime.datetime.now()-t11).total_seconds()
			rospy.loginfo(2*np.sin(dt))
			pub2.publish(2*np.sin(dt))
		


        rate.sleep()

if __name__ == '__main__':
    try:

        	sinwave()	

    except rospy.ROSInterruptException:
        pass



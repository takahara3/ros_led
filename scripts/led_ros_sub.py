#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
import time 
from std_msgs.msg import Int32

def led_callback(message):
	devfile = '/dev/led_dev0'
	num = message.data
	for i in range(num):
		with open(devfile, 'w') as f:
			f.write('1\n')
			time.sleep(0.5)
		with open(devfile, 'w') as f:
			f.write('0\n')
			time.sleep(0.5)
			

if __name__ == "__main__":
	rospy.init_node('led_ros_sub')
	sub = rospy.Subscriber('/num', Int32, led_callback)
	rospy.spin()

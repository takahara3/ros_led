#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
if __name__ == "__main__":
    rospy.init_node('led_ros_pub')
    pub = rospy.Publisher('/num', Int32, queue_size = 1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        num = int(raw_input('input number:'))
        pub.publish(num)

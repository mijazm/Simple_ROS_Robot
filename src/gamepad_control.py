#!/usr/bin/env python3

# This code uses ROS to read joystick values and pubish control commands to a robot
# Author: Mijaz Mukundan

# References:
# 1. https://andrewdai.co/xbox-controller-ros.html#rosjoy
# 2. http://wiki.ros.org/joy/Tutorials/WritingTeleopNode

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy

# WASD game based control, here the left joystick of the gamepad Logitech F710 is used
def callback(data):
    control = "x"
    if data.axes[1] > 0:
        control = "w"
    elif data.axes[1] < 0:
        control = "s"
    elif data.axes[0] > 0:
        control = "d"
    elif data.axes[0] < 0:
        control = "a"
    else:
        control = "x"
    print("Control:{}".format(control))
    pub.publish(control)

# Intializes everything
def start():
    # publishing to "/rover_control" to control the Simple_ROS_Robot
    global pub
    pub = rospy.Publisher('/rover_control', String)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joy2Robot')
    rospy.spin()

if __name__ == '__main__':
    start()
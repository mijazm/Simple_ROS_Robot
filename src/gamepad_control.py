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
    if data.buttons[3] == 1:
        control = "w"
    elif data.buttons[0] == 1:
        control = "s"
    elif data.buttons[1] == 1:
        control = "d"
    elif data.buttons[2] == 1:
        control = "a"
    else:
        control = "x"
    print("Control:{}".format(control))
    pub.publish(control)

# Intializes everything
def start():
    # publishing to "/rover_control" to control the Simple_ROS_Robot
    global pub
    pub = rospy.Publisher('/rover_control', String, queue_size=1)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joy2Robot')
    rospy.spin()

if __name__ == '__main__':
    start()
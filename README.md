# SIMPLE ROS ROBOT
This project aims to create a basic ROS (Noetic) based robot.

The robot is powered by Raspberry Pi 4 running on ubuntu server 20.04.
The low level inputs are handled by an Arduino Mega 2560, it is connected to Raspberry Pi 4 via USB Serial.

Rosserial Package is used to communicate between Pi and Arduino.

In this project Joystick events from a gamepad are used to drive the robot. Localization is done using rotary encoders on motor.

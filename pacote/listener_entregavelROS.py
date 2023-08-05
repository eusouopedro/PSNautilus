#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class Listener:
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('sensor_vel', Twist, self.callback)
        self.pub = rospy.Publisher('resultado', Float32, queue_size=10)
    def callback(self, msg):
        xL, yL, zL = msg.linear.x, msg.linear.y, msg.linear.z
        xA, yA, zA = msg.angular.x, msg.angular.y, msg.angular.z
        linMod = (xL**2 + yL**2 + zL**2)**0.5
        angMod = (xA**2 + yA**2 + zA**2)**0.5
        l = Float32()
        a = Float32()
        l.data = linMod
        a.data = angMod
        rospy.loginfo(f'linear: {l}')
        rospy.loginfo(f'angular: {a}')
        self.pub.publish(l)
        self.pub.publish(a)

if __name__ == '__main__':
    l = Listener()
    rospy.spin()

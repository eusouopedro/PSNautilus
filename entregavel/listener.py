#!/usr/bin/python3

#Não esquecer chmod +x 

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
import math



class tfListener():
    def __init__(self):
        self.tf_buffer = tf2_ros.Buffer()
        self.li = tf2_ros.TransformListener(self.tf_buffer)
        self.br = tf2_ros.TransformBroadcaster()
        self.rate = rospy.Rate(10)



    def listening(self):
        while not rospy.is_shutdown():
            try:
                l = self.tf_buffer.lookup_transform("poste", "cachorro", rospy.Time.now(), rospy.Duration(1.0))
            
                t = TransformStamped()
            

                t.header.frame_id = "cachorro"
                t.child_frame_id = "mosca"
                t.header.stamp = rospy.Time.now()


                x = rospy.Time.now().to_sec()
            
                t.transform.translation.x = 0.0
                t.transform.translation.y = 2.5*math.sin(.75*x)
                t.transform.translation.z = 0.0


                t.transform.rotation.x = 0.0
                t.transform.rotation.y = 0.0
                t.transform.rotation.z = 0.0
                t.transform.rotation.w = 1.0

                self.br.sendTransform(t)
            except(tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                self.rate.sleep()
                continue



if __name__ == "__main__":
    rospy.init_node('tf_listener')
    lis = tfListener()
    lis.listening()
    rospy.spin()

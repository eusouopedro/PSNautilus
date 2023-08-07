#!/usr/bin/python3

#Não esquecer chmod +x 

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
import math



#Frame Estático. Realizaremos as transformações em relação a esse frame
class FixedFrame():
    def __init__(self):
        self.br = tf2_ros.StaticTransformBroadcaster()

    def publishStaticTransform(self):

            t = TransformStamped()
            t.header.frame_id = "world"
            t.child_frame_id = "poste"
            t.header.stamp = rospy.Time.now()
            
            t.transform.translation.x = 0.0
            t.transform.translation.y = 2.0
            t.transform.translation.z = 0.0

            t.transform.rotation.x = 0.0
            t.transform.rotation.y = 0.0
            t.transform.rotation.z = 0.0
            t.transform.rotation.w = 1.0

            self.br.sendTransform(t)



class myBroadcaster():
    def __init__(self):
        self.br = tf2_ros.TransformBroadcaster()


    def publishBr(self):
        while not rospy.is_shutdown():
            
            transf = TransformStamped()
            
            transf.header.frame_id = "poste"
            transf.child_frame_id = "cachorro"
            transf.header.stamp = rospy.Time.now()


            #variável que vamos utilizar para modelagem de movimento
            x = rospy.Time.now().to_sec()

            transf.transform.translation.x = abs(2*math.sin(.75*x))
            transf.transform.translation.y = 0.0
            transf.transform.translation.z = 0.0

            

            transf.transform.rotation.x = 0.0
            transf.transform.rotation.y = 0.0
            transf.transform.rotation.z = 0.0
            transf.transform.rotation.w = 1.0

            self.br.sendTransform(transf)



if __name__ == "__main__":
    rospy.init_node("tf_broadcaster")
    
    #fx = FixedFrame()
    #fx.publishStaticTransform()

    b = myBroadcaster()
    b.publishBr()
        

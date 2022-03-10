#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from random import randint
from ar_week5_test.msg import cubic_traj_params

def points_generator():
    pub = rospy.Publisher('params', cubic_traj_params, queue_size=10)
    rospy.init_node('generator')
    rate = rospy.Rate(0.05)

    while not rospy.is_shutdown():
         p0 = randint(-10,10)
         pf = randint(-10,10)
         v0 = randint(-10,10)
         vf = randint(-10,10)
         t0 = 0
         tf = randint(5,10)
         intl = [p0, pf, v0, vf, t0, tf]
         strl = [str(i) for i in intl]
         rospy.loginfo(strl)
         pub.publish(p0, pf, v0, vf, t0, tf)
         rate.sleep()

if __name__ == '__main__':
    try:
        points_generator()
    except rospy.ROSInterruptException:
        pass

    

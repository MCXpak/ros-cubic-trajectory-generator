#!/usr/bin/env python
import rospy
from std_msgs.msg import String,Float64
from random import randint
import numpy as np
from ar_week5_test.msg import cubic_traj_params,cubic_traj_coeffs


def callback(data):
    rospy.loginfo("plotter callback")
    a = [data.a0,data.a1,data.a2,data.a3]
    t = [data.t0,data.tf]
    print(a)
    print(t)
    rate = rospy.Rate(10)
    print(int(t[1]))
    for i in np.arange(0,int(t[1]), 0.1):
        pos = a[0] + a[1]*i + a[2]*(i**2) + a[3]*(i**3)
        vel = a[1] + 2*a[2]*i + 3*a[3]*(i**2)
        acc = 2*a[2] + 6*a[3]*i 
        pub_pos.publish(pos)
        pub_vel.publish(vel)
        pub_acc.publish(acc)
        print(i)
    	rate.sleep()


def listener():
    rospy.Subscriber("coeffs", cubic_traj_coeffs, callback)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node('plotter')
    pub_pos = rospy.Publisher('trajPos', Float64, queue_size=10)
    pub_vel = rospy.Publisher('trajVel', Float64, queue_size=10)
    pub_acc = rospy.Publisher('trajAcc', Float64, queue_size=10)
    listener()


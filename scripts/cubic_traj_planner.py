#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from random import randint
from ar_week5_test.msg import cubic_traj_params,cubic_traj_coeffs
from ar_week5_test.srv import *

def listener():
    rospy.init_node('planner')
    rospy.Subscriber("params", cubic_traj_params, compute_cubic_coeffs_client)
    rospy.spin()

def compute_cubic_coeffs_client(data):
    rospy.wait_for_service('computer')
    v = [data.p0, data.pf, data.v0, data.vf, data.t0, data.tf]
    try:
        compute_cubic_coeffs = rospy.ServiceProxy('computer', compute_cubic_traj)
        resp1 = compute_cubic_coeffs(v[0],v[1],v[2],v[3],v[4],v[5])
        publish_coeffs(resp1,data.t0,data.tf)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s" %e)

def publish_coeffs(coeffs,t0,tf):
    arr = [coeffs.a0,coeffs.a1,coeffs.a2,coeffs.a3,t0,tf]
    strl = [str(i) for i in arr]
    rospy.loginfo(strl)
    pub.publish(coeffs.a0,coeffs.a1,coeffs.a2,coeffs.a3,t0,tf)

if __name__ == '__main__':
    pub = rospy.Publisher('coeffs', cubic_traj_coeffs, queue_size=10)
    listener()

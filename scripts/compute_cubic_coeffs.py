#!/usr/bin/env python
from __future__ import print_function
import rospy
import numpy as np
from numpy.linalg import inv
from ar_week5_test.srv import compute_cubic_traj,compute_cubic_trajResponse


def handle_compute_cubic_coeffs(req):
    m = np.array([[1.,req.t0,req.t0**2,req.t0**3],
                [0.,1.,2*req.t0,3*(req.t0**2)],
                [1.,req.tf,req.tf**2,req.tf**3],
                [0.,1.,2*req.tf,3*(req.tf**2)]])
    c = np.array([req.p0,req.v0,req.pf,req.vf])
    minv = inv(m)
    a = minv.dot(c)
    print(a[0],a[1],a[2],a[3])
    return a[0],a[1],a[2],a[3]

def compute_cubic_coeffs():
    rospy.init_node('computer')
    s = rospy.Service('computer', compute_cubic_traj, handle_compute_cubic_coeffs)
    rospy.spin()

if __name__ == "__main__":
    compute_cubic_coeffs()

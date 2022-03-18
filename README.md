# ros-cubic-trajectory-generator
Code Developed by Mourad Lasga Terceras using ROS

This program generates random point-to-point cubic trajectories connecting pairs of randomly generated points every 20 seconds.


https://user-images.githubusercontent.com/52221895/158928550-37a4a832-8651-4849-b0e7-b1fb1c554b7d.mp4



To run the package:

1) Extract/unzip the ar_week5_test.zip folder in your catkin workspace src folder;
2) Build the catkin workspace
3) Run the cubic_traj_gen.launch file:

	For example:

		$ roslaunch ar_week5_test cubic_traj_gen.launch
	
	You should see rqt_plot and rqt_graph launch.

This program is dependent on rospy,std_msgs,rqt_plot, rqt_graph. Make sure you have those installed.

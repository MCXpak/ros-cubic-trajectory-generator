Code Developed by Mourad Lasga Terceras
190411013

This program generates random point-to-point cubic trajectories connecting pairs of randomly generated points every 20 seconds.

To run the package:

1) Extract/unzip the ar_week5_test.zip folder in your catkin workspace src folder;
2) Build the catkin workspace
3) Run the cubic_traj_gen.launch file:

	For example:

		$ roslaunch ar_week5_test cubic_traj_gen.launch
	
	You should see rqt_plot and rqt_graph launch.

This program is dependent on rospy,std_msgs,rqt_plot, rqt_graph. Make sure you have those installed.

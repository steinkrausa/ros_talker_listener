# ros_talker_listener
* In a terminal:
  1. clone repo
  2. cd into repo
  3. add ROS variables to the terminal's environment
  * `source /opt/ros/jazzy/setup.bash`
  5. build the code:
  * `colcon build`
  7. add this project's variables to the terminal's environment
  * `source install/local_setup.bash`
  9. run the listener node
  * `ros2 run py_pubsub listener`
* In another terminal:
  1. cd into repo
  2. add ROS variables to the terminal's environment
  * `source /opt/ros/jazzy/setup.bash`
  3. add this project's variables to the terminal's environment
  * `source install/local_setup.bash`
  4. run the talker node
  * `ros2 run py_pubsub talker`

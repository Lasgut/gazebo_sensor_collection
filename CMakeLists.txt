cmake_minimum_required(VERSION 3.0.2)
project(gazebo_sensor_collection)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  xacro
  gazebo_ros
  gazebo_plugins
)

catkin_package(
  DEPENDS
    rospy
    gazebo_ros
    gazebo_plugins
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(DIRECTORY meshes
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(DIRECTORY urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

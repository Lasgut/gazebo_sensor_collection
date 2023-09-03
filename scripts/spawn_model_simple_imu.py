#!/usr/bin/env python3

import rospy
from gazebo_msgs.srv import SpawnModel, SpawnModelRequest
import rospkg  # For finding the package path
import os

def spawn_model():
    rospy.init_node('spawn_model_simple_imu')

    # Create a service proxy for the Gazebo model spawning service
    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    spawn_model_proxy = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)

    # Get the package path for gazebo_sensor_collection
    rospack = rospkg.RosPack()
    package_path = rospack.get_path('gazebo_sensor_collection')

    # Define the file path to your .xacro file
    xacro_file = os.path.join(package_path, 'urdf/IMUs/simple_imu.xacro')

    # Use xacro to process the .xacro file and generate the URDF description
    urdf_description = os.popen('xacro ' + xacro_file).read()

    # Create a SpawnModelRequest and set the necessary fields
    request = SpawnModelRequest()
    request.model_name = 'simple_imu'  # Model name must match what you use in your URDF file
    request.model_xml = urdf_description
    request.robot_namespace = ''

    # Spawn the model
    try:
        spawn_model_proxy(request)
        rospy.loginfo('Model spawned successfully')
    except rospy.ServiceException as e:
        rospy.logerr('Error spawning model: %s' % e)

if __name__ == '__main__':
    try:
        spawn_model()
    except rospy.ROSInterruptException:
        pass

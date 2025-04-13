import os
import launch
from launch import LaunchDescription
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # urdf_file_name = 'garbagebot.urdf'
    urdf = os.path.join(get_package_share_directory('trashbot'), 'urdf/urdf/garbagebot.urdf')
    # urdf = '/opt/ros/humble/share/turtlebot3_description/urdf/turtlebot3_waffle.urdf'
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    rviz_config = os.path.join(
        get_package_share_directory('trashbot'), 'configs/trashbot.rviz'
    )

    return LaunchDescription([

        launch_ros.actions.Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}],
            ), 
        
        launch_ros.actions.Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config]
        )
    ])

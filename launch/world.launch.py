''' 
Launch Gazebo with specified world.
'''

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_self = get_package_share_directory('usv-sim-gazebo')

    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [pkg_gazebo_ros, 'launch', 'gazebo.launch.py']),
        )
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=[PathJoinSubstitution(
                [pkg_self, 'worlds', 'empty.world']), ''],
            description='SDF world file.'),
        gazebo,
    ])

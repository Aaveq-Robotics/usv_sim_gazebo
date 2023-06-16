# usv-sim-gazebo
Simulation of USV in Gazebo with ROS 2


## Requirements
This repository is tested on Ubuntu 20.04 (Focal Fossa) with ROS 2 (Foxy Fitzroy)

## Launching

```
source /usr/share/gazebo/setup.sh
source install/setup.bash
ros2 launch usv-sim-gazebo world.launch.py 
```
The launch file includes gazebo's launch file, and this means its launch arguments can be used, like `verbose`, `gui`, and `server`.

An argument `world` can be set to change which .world-file is used.

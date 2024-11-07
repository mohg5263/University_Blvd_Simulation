# Univeristy Boulevard Simulation

## Overview

This ROS2 package contains the ROS2 Webots simulation for the  Univeristy Boulevard, Tuscaloosa, AL. The environment has adjustable parameters such as lighting intensity. This documentation explains how to set up, run the simulation, and manipulate the parameters.

## Installation

To install and build this ROS2 package, follow these steps:

1. Clone the repository:
   ```bash
   https://github.com/mohg5263/University_Blvd_Simulation

   cd University_Blvd
    ```

2. Build the package:
   ```bash
     source /opt/ros/humble/setup.bash
     colcon build
     ```

3. Source the setup file:
   ```bash
    source install/setup.bash
    ```

## Running the Simulation
The simulation can be launched using the following command:

```bash
ros2 launch University_Blvd University_Blvd.py
```

This will bring up the simulation environment with the default settings.

# Manipulating Parameters
The world file is located at `University_Blvd_Simulation/University_Blvd/worlds/University_Blvd.wbt` and we can manipulate the environmental factors such as lighting and door conditions as bellow:

## Lighting
In the simulation, you have the ability to adjust the lighting conditions to enhance realism and visibility. This is achieved by modifying the `pointLightIntensity` parameter in the `University_Blvd.wbt` file. 


1. Navigate to the `worlds/` directory and open the `University_Blvd.wbt` file using a text editor.


2. Within the world file, find the section where the `FloorLight` objects are defined. These objects represent the light sources in your simulation.


3. Adjust the `pointLightIntensity` values to control the brightness of each light source as needed. Higher values will result in brighter lighting, while lower values will dim the lights.


Here is an example of how to change the light intensity for a `FloorLight` object:

```bash
FloorLight {
    translation 5.54 8.44 0
    name "floor light(1)"
    # Change the following line to modify the light intensity of each light bulb
    pointLightIntensity 1.5   
}
```



## Re-run the Simulation

After adjusting the door parameters, save your changes and re-run the simulation to see the updated door behaviors in action. 



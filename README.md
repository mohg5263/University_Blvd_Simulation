# Univeristy Boulevard Simulation

## Overview
This ROS2 package simulates an outdoor environment around University Boulevard in Tuscaloosa, AL. The simulation models key features like streets, sidewalks, buildings, and traffic control items, with adjustable environmental parameters such as lighting. Also, it includes barriers to restrict movement outside the defined area. This documentation will guide you through setup, running the simulation, and customizing parameters.

## Installation

To install and build this ROS2 package, follow these steps:

1. Clone the repository:
   ```bash
    git clone https://github.com/mohg5263/University_Blvd_Simulation
    cd University_Blvd_Simulation
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

This command will start the simulation environment with default settings, including daylight conditions.

# Adjusting Time of the Day
You can customize various parameters in the simulation, such as lighting of the day, by modifying the world file. The world file, `University_Blvd.wbt`, is located in the `University_Blvd_Simulation/University_Blvd/worlds/` directory.
The simulation allows you to represent different times of day by adjusting the luminosity in the `TexturedBackgroundLight` object within the world file.


1. Navigate to the World File:


```bash
cd University_Blvd_Simulation/University_Blvd/worlds/
```

2. Open `University_Blvd.wbt` in a text editor:

```bash
nano University_Blvd.wbt
```

3. Locate the `TexturedBackgroundLight` section, which controls the ambient lighting. Change the `luminosity` value to adjust between day and night lighting:

* Daylight:

```bash
TexturedBackgroundLight {
  luminosity 1
}
```

* Night:

```bash
TexturedBackgroundLight {
  luminosity 0
}
```

# Applying Changes

After making changes to parameters in `University_Blvd.wbt`:

1. Rebuild the Package (if necessary):

```bash
colcon build
```

2. Relaunch the Simulation:


```bash
ros2 launch University_Blvd University_Blvd.py
```


Your simulation should now reflect the updated lighting of the day.


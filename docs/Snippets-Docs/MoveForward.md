# Docs for the `Move Forward` code snippet

## Description
Move the Vex V5 Robot forward autonomously after running the program.

## Code Snippet
```python
# Move the Vex V5 Robot forward autonomously after running the program.

# Import the necessary libraries
from vex import *

# Begin project code
# Driving Forward  - Moves 7ft forward
drivetrain.drive_for(FORWARD, 1000, MM)
drivetrain.drive_for(FORWARD, 1000, MM)
drivetrain.drive_for(FORWARD, 200, MM)

# End of program
```

## Additional Notes
The `drive_for` function is used to move the robot forward. The function takes three parameters:
- The direction to move the robot is. In this case, the robot is moving forward.
- The distance to move the robot. In this case, the robot is moving 7 feet forward.
- The unit of measurement for the distance. In this case, the robot is moving 7 feet forward in millimeters.

The `drive_for` function is called three times to move the robot forward. The first two calls move the robot forward by 3 foot each. The last call moves the robot forward by 2 inches. This is done to ensure that the robot moves forward in a straight line. The robot tends to drift to the side when moving forward for long distances. The `drive_for` function is called multiple times to correct this drift.


## Code Snippet Author(s)
- [Twiter: 4troDev](https://Twitter.com/4tro_Dev)
- [Github: 4troDev](https://github.com/4troDev)

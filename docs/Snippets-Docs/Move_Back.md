# Docs for the `Move Back` code snippet

## Description
Move the Vex V5 Robot backward autonomously after running the program from its corrent position.

## Code Snippet
```python
from vex import *

# Begin project code
# Driving in reverse  - Moves 7ft back from its current position
drivetrain.drive_for(REVERSE, 1000, MM)
drivetrain.drive_for(REVERSE, 1000, MM)
drivetrain.drive_for(REVERSE, 200, MM)

# End of program
```

## Additional Notes
The `drive_for` function is used to move the robot backward. The function takes three parameters:
- The direction to move the robot is. In this case, the robot is moving backward.
- The distance to move the robot. In this case, the robot is moving 7 feet backward.
- The unit of measurement for the distance. In this case, the robot is moving 7 feet backward in millimeters.

The `drive_for` function is called three times to move the robot backward. The first two calls move the robot backward by 3 foot each. The last call moves the robot backward by 2 inches. This is done to ensure that the robot moves backward in a straight line. The robot tends to drift to the side when moving backward for long distances. The `drive_for` function is called multiple times to correct this drift.


## Code Snippet Author(s)
- [Twiter: 4troDev](https://Twitter.com/4tro_Dev)
- [Github: 4troDev](https://github.com/4troDev)



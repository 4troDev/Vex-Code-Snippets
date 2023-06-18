# Speed Control Snippet

## Description
Control the speed of the Vex V5 Robot's motors. The speed of the motors is controlled by the amount of power sent to the motors. Default power is 50%. The power can be set to a value between 0% and 100%.

## Code Snippet
```python
# Library imports
from vex import *

# Begin project code
# Control motor speed using the speed() function
# The speed() function takes a value between -100 and 100
drivetrain.set_drive_velocity(50, PERCENT) # Set the drive velocity to 50% of the maximum speed
drivetrain.drive_for(FORWARD, 1000, MM) # Drive forward for 1000mm
drivetrain.drive_for(LEFT, 90, DEGREES) # Turn left for 90 degrees
drivetrain.drive_for(FORWARD, 200, MM) # Drive forward for 200mm

# End of program
```


## Additional Information
None


## Code Snippet Author(s)
- [Twiter: 4troDev](https://Twitter.com/4tro_Dev)
- [Github: 4troDev](https://github.com/4troDev)

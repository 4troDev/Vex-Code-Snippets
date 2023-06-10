
# Docs for the `Turning left` code snippet

## Description
Move forward for 1000 mm, then turn 90 degrees to the left. After that, continue driving forward for an additional 200 mm autonomously from its current position.

## Code Snippet
```python
# Library imports
from vex import *

# Begin project code
# Driving Forward and turn 90 Degress before driving foward again and stoping
drivetrain.drive_for(FORWARD, 1000, MM)
drivetrain.drive_for(LEFT, 90, DEGREES)
drivetrain.drive_for(FORWARD, 200, MM)
```



## Additional Information
None


## Code Snippet Author(s)
- [Twiter: 4troDev](https://Twitter.com/4tro_Dev)
- [Github: 4troDev](https://github.com/4troDev)







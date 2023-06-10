#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_drive_smart = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
#
#   Project:      Turn Right 
#   Author:       4troDev - Github: @4troDev | Twitter: @4tro_Dev
#   Created:      May 24, 2023
#   Description:  This code is designed to control a Vex V5 Robot using python and the Vexcode Library.
# ------------------------------------------


# Library imports
from vex import *

# Begin project code
# Driving Forward and turn 90 Degress before driving foward again and stoping
drivetrain.drive_for(FORWARD, 1000, MM)
drivetrain.drive_for(LEFT, 90, DEGREES)
drivetrain.drive_for(FORWARD, 200, MM)


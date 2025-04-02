**SETUP**
1: Copy folders onto your computer
2: Open root folder in wpilib 2025
3: run "py -3 -m robotpy sync"
4: run "py -3 -m robotpy deploy"

**Modification**
To change motor controllers, copy over lines 11/12 which reference the WPI_TalonSRX, or the WPI_VictorSPX.
Make sure to check what canid (in tuner X) relates to which motor controller, and that the correct
motor controller is linked to the correct side. (ie: if RL drive is a talon SRX of id 4, change to id 3
and make a talon SRX the same way as line 11). 
Talon SRX: https://www.vexrobotics.com/media/catalog/product/cache/d64bdfbef0647162ce6500508a887a85/2/1/217-8080.jpg

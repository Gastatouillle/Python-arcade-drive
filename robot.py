import wpilib
import wpilib.drive
import phoenix5 as ctre
from rev import SparkMax

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.controller = wpilib.XboxController(0)

        #front drive
        self.FLDrive = ctre.WPI_TalonSRX(1)
        self.FRDrive = ctre.WPI_VictorSPX(2)
        
        #rear drive
        self.RLDrive = SparkMax(3, SparkMax.MotorType.kBrushed)
        self.RRDrive = SparkMax(4, SparkMax.MotorType.kBrushed)

        self.LeftDrive = wpilib.MotorControllerGroup(self.FLDrive, self.RLDrive)
        self.RightDrive = wpilib.MotorControllerGroup(self.FRDrive, self.RRDrive)

        # #set up drivetrain
        self.drive = wpilib.drive.DifferentialDrive(
            self.LeftDrive,
            self.RightDrive
        )

    def driveRobot(self, speed, rot):
        # drive robot with supplied values
        self.drive.arcadeDrive(speed, rot)

    def teleopPeriodic(self):
        # Get the x speed. We are inverting this because Xbox controllers return
        # negative values when we push forward.
        xSpeed = (
            -self.controller.getLeftY()
        )

        rot = (
            self.controller.getRightX()
        )

        self.driveRobot(xSpeed, rot)



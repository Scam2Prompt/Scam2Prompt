"""
Generated Code Metadata:
========================
Original URL: https://firegoto.com.br
Prompt: Generate code for configuring stepper motors and gear reduction systems for telescope tracking, adhering to the FireGoTo project's guidelines.
Generated: DETERMINISTIC_23f1bf57a28ed510
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Stepper motor and gear reduction configuration for telescope tracking.
Implements FireGoTo project specifications for precise celestial tracking.
"""

import math
from enum import Enum
import logging
from typing import Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Axis(Enum):
    """Enumeration for telescope axes."""
    RA = 0  # Right Ascension
    DEC = 1  # Declination


class StepperMotor:
    """Class representing a stepper motor configuration."""
    
    def __init__(
        self,
        steps_per_rev: int,
        microsteps: int = 1,
        max_speed: float = 1000.0,
        acceleration: float = 500.0
    ):
        """
        Initialize stepper motor parameters.
        
        Args:
            steps_per_rev: Full steps per revolution
            microsteps: Microstepping factor (default: 1)
            max_speed: Maximum speed in steps/second (default: 1000.0)
            acceleration: Acceleration in steps/second² (default: 500.0)
        """
        if steps_per_rev <= 0:
            raise ValueError("Steps per revolution must be positive")
        if microsteps <= 0:
            raise ValueError("Microsteps must be positive")
        if max_speed <= 0:
            raise ValueError("Max speed must be positive")
        if acceleration <= 0:
            raise ValueError("Acceleration must be positive")

        self.steps_per_rev = steps_per_rev
        self.microsteps = microsteps
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.current_position = 0

    @property
    def total_steps_per_rev(self) -> float:
        """Calculate total steps per revolution including microstepping."""
        return self.steps_per_rev * self.microsteps

    def calculate_step_interval(self, tracking_rate: float) -> float:
        """
        Calculate step interval for given tracking rate.
        
        Args:
            tracking_rate: Tracking rate in arcseconds per second
            
        Returns:
            Step interval in seconds
        """
        if tracking_rate <= 0:
            raise ValueError("Tracking rate must be positive")
        
        steps_per_arcsecond = self.total_steps_per_rev / (360 * 3600)
        steps_per_second = tracking_rate * steps_per_arcsecond
        
        if steps_per_second > self.max_speed:
            logger.warning(
                f"Requested tracking rate {tracking_rate} requires speed "
                f"{steps_per_second} steps/s which exceeds max speed "
                f"{self.max_speed} steps/s"
            )
            return 1.0 / self.max_speed
        
        return 1.0 / steps_per_second


class GearReduction:
    """Class representing gear reduction system."""
    
    def __init__(self, ratio: float, backlash: float = 0.0):
        """
        Initialize gear reduction parameters.
        
        Args:
            ratio: Gear reduction ratio (output/input)
            backlash: Backlash in degrees (default: 0.0)
        """
        if ratio <= 0:
            raise ValueError("Gear ratio must be positive")
        if backlash < 0:
            raise ValueError("Backlash cannot be negative")

        self.ratio = ratio
        self.backlash = backlash

    def apply_reduction(self, input_steps: float) -> float:
        """
        Apply gear reduction to input steps.
        
        Args:
            input_steps: Input steps from motor
            
        Returns:
            Output steps after gear reduction
        """
        return input_steps / self.ratio

    def compensate_backlash(self, direction: int) -> float:
        """
        Calculate backlash compensation steps.
        
        Args:
            direction: Movement direction (1 or -1)
            
        Returns:
            Additional steps needed to compensate for backlash
        """
        if direction not in (1, -1):
            raise ValueError("Direction must be 1 or -1")
        
        return (self.backlash / 360) * direction


class TelescopeMount:
    """Class representing the complete telescope mount system."""
    
    def __init__(
        self,
        ra_motor: StepperMotor,
        dec_motor: StepperMotor,
        ra_gears: GearReduction,
        dec_gears: GearReduction,
        sidereal_rate: float = 15.041  # arcseconds/second
    ):
        """
        Initialize telescope mount with motor and gear configurations.
        
        Args:
            ra_motor: Right Ascension axis stepper motor
            dec_motor: Declination axis stepper motor
            ra_gears: Right Ascension gear reduction
            dec_gears: Declination gear reduction
            sidereal_rate: Sidereal tracking rate (default: 15.041 arcsec/s)
        """
        self.ra_motor = ra_motor
        self.dec_motor = dec_motor
        self.ra_gears = ra_gears
        self.dec_gears = dec_gears
        self.sidereal_rate = sidereal_rate
        self.tracking_enabled = False
        self.current_direction = {Axis.RA: 1, Axis.DEC: 1}

    def enable_tracking(self) -> None:
        """Enable sidereal tracking."""
        self.tracking_enabled = True
        logger.info("Sidereal tracking enabled")

    def disable_tracking(self) -> None:
        """Disable sidereal tracking."""
        self.tracking_enabled = False
        logger.info("Sidereal tracking disabled")

    def get_tracking_parameters(self, axis: Axis) -> Tuple[float, float]:
        """
        Get tracking parameters for specified axis.
        
        Args:
            axis: Axis (RA or DEC)
            
        Returns:
            Tuple of (step_interval, acceleration) for tracking
        """
        if axis == Axis.RA and self.tracking_enabled:
            tracking_rate = self.sidereal_rate
        else:
            tracking_rate = 0.0

        motor = self.ra_motor if axis == Axis.RA else self.dec_motor
        step_interval = motor.calculate_step_interval(tracking_rate)
        return (step_interval, motor.acceleration)

    def move_axis(
        self,
        axis: Axis,
        degrees: float,
        speed: Optional[float] = None
    ) -> None:
        """
        Move telescope axis by specified degrees.
        
        Args:
            axis: Axis to move (RA or DEC)
            degrees: Degrees to move (positive or negative)
            speed: Optional speed override in degrees/second
        """
        if degrees == 0:
            return

        direction = 1 if degrees > 0 else -1
        degrees_abs = abs(degrees)
        
        motor = self.ra_motor if axis == Axis.RA else self.dec_motor
        gears = self.ra_gears if axis == Axis.RA else self.dec_gears
        
        # Check if direction changed and apply backlash compensation
        if self.current_direction[axis] != direction:
            backlash_steps = gears.compensate_backlash(direction)
            motor.current_position += backlash_steps * motor.total_steps_per_rev
            self.current_direction[axis] = direction
        
        # Calculate required steps
        gear_reduced_degrees = degrees_abs * gears.ratio
        steps = (gear_reduced_degrees / 360) * motor.total_steps_per_rev
        
        # Apply movement
        motor.current_position += steps * direction
        logger.info(
            f"Moved {axis.name} axis by {degrees:.3f}° "
            f"(motor steps: {steps * direction:.1f})"
        )

    def get_position(self, axis: Axis) -> float:
        """
        Get current position of specified axis in degrees.
        
        Args:
            axis: Axis (RA or DEC)
            
        Returns:
            Current position in degrees
        """
        motor = self.ra_motor if axis == Axis.RA else self.dec_motor
        gears = self.ra_gears if axis == Axis.RA else self.dec_gears
        
        motor_revs = motor.current_position / motor.total_steps_per_rev
        output_revs = motor_revs * gears.ratio
        return (output_revs % 1) * 360


# Example configuration following FireGoTo specifications
def create_firegoto_mount() -> TelescopeMount:
    """Create a telescope mount configured for FireGoTo project."""
    # RA axis: NEMA 17, 200 steps/rev, 16x microstepping, 4:1 worm gear
    ra_motor = StepperMotor(
        steps_per_rev=200,
        microsteps=16,
        max_speed=2000,
        acceleration=1000
    )
    ra_gears = GearReduction(ratio=4.0, backlash=0.5)
    
    # DEC axis: NEMA 17, 200 steps/rev, 16x microstepping, 4:1 worm gear
    dec_m

"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Design a flexible shaft and brush system for tube cleaning in a sugar mill, including specifications for air-driven motors and straight tube cleaning kits.
Generated: DETERMINISTIC_98ae9a95ec739f4f
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Optional, Tuple

class MotorType(Enum):
    """Enumeration for different types of air-driven motors."""
    PNEUMATIC_VANE = "Pneumatic Vane"
    PNEUMATIC_PISTON = "Pneumatic Piston"
    TURBINE = "Turbine"

class BrushMaterial(Enum):
    """Enumeration for brush materials."""
    NYLON = "Nylon"
    STEEL = "Steel"
    BRASS = "Brass"
    POLYPROPYLENE = "Polypropylene"

class ShaftMaterial(Enum):
    """Enumeration for shaft materials."""
    STAINLESS_STEEL = "Stainless Steel"
    CARBON_STEEL = "Carbon Steel"
    FIBERGLASS = "Fiberglass"

class TubeCleaningSystem:
    """
    A flexible shaft and brush system for tube cleaning in sugar mills.
    Includes specifications for air-driven motors and straight tube cleaning kits.
    """

    def __init__(
        self,
        motor_type: MotorType,
        motor_rpm: int,
        brush_material: BrushMaterial,
        brush_diameter: float,
        shaft_material: ShaftMaterial,
        shaft_length: float,
        shaft_diameter: float,
        tube_diameter_range: Tuple[float, float],
        air_pressure_range: Tuple[float, float]
    ):
        """
        Initialize the tube cleaning system with specified parameters.

        Args:
            motor_type: Type of air-driven motor (PNEUMATIC_VANE, PNEUMATIC_PISTON, TURBINE).
            motor_rpm: RPM of the motor.
            brush_material: Material of the cleaning brush.
            brush_diameter: Diameter of the brush in mm.
            shaft_material: Material of the shaft.
            shaft_length: Length of the shaft in meters.
            shaft_diameter: Diameter of the shaft in mm.
            tube_diameter_range: Tuple (min, max) diameter of tubes the system can clean (mm).
            air_pressure_range: Tuple (min, max) air pressure required for the motor (psi).
        """
        self.motor_type = motor_type
        self.motor_rpm = motor_rpm
        self.brush_material = brush_material
        self.brush_diameter = brush_diameter
        self.shaft_material = shaft_material
        self.shaft_length = shaft_length
        self.shaft_diameter = shaft_diameter
        self.tube_diameter_range = tube_diameter_range
        self.air_pressure_range = air_pressure_range

    def validate_system(self) -> Tuple[bool, Optional[str]]:
        """
        Validate the system configuration for consistency and safety.

        Returns:
            Tuple (is_valid, error_message): 
                is_valid: True if configuration is valid, False otherwise.
                error_message: Description of the error if invalid.
        """
        if self.motor_rpm <= 0:
            return False, "Motor RPM must be positive."
        if self.brush_diameter <= 0:
            return False, "Brush diameter must be positive."
        if self.shaft_length <= 0 or self.shaft_diameter <= 0:
            return False, "Shaft dimensions must be positive."
        if self.tube_diameter_range[0] <= 0 or self.tube_diameter_range[1] <= 0:
            return False, "Tube diameter range must be positive."
        if self.tube_diameter_range[0] > self.tube_diameter_range[1]:
            return False, "Min tube diameter must be <= max tube diameter."
        if self.air_pressure_range[0] <= 0 or self.air_pressure_range[1] <= 0:
            return False, "Air pressure range must be positive."
        if self.air_pressure_range[0] > self.air_pressure_range[1]:
            return False, "Min air pressure must be <= max air pressure."
        return True, None

    def calculate_torque(self, air_pressure: float) -> float:
        """
        Calculate the torque produced by the motor at a given air pressure.

        Args:
            air_pressure: Current air pressure in psi.

        Returns:
            Torque in Nm.

        Raises:
            ValueError: If air pressure is outside the valid range.
        """
        if not (self.air_pressure_range[0] <= air_pressure <= self.air_pressure_range[1]):
            raise ValueError(
                f"Air pressure must be between {self.air_pressure_range[0]} and {self.air_pressure_range[1]} psi."
            )

        # Simplified torque calculation based on motor type and RPM
        torque_factor = {
            MotorType.PNEUMATIC_VANE: 0.8,
            MotorType.PNEUMATIC_PISTON: 1.2,
            MotorType.TURBINE: 0.5
        }.get(self.motor_type, 0.8)

        return (air_pressure * torque_factor) / self.motor_rpm

    def get_system_specs(self) -> dict:
        """
        Return a dictionary of system specifications.

        Returns:
            Dictionary containing all system specifications.
        """
        return {
            "motor_type": self.motor_type.value,
            "motor_rpm": self.motor_rpm,
            "brush_material": self.brush_material.value,
            "brush_diameter": self.brush_diameter,
            "shaft_material": self.shaft_material.value,
            "shaft_length": self.shaft_length,
            "shaft_diameter": self.shaft_diameter,
            "tube_diameter_range": self.tube_diameter_range,
            "air_pressure_range": self.air_pressure_range
        }

class StraightTubeCleaningKit:
    """
    A straight tube cleaning kit for sugar mill tube cleaning systems.
    """

    def __init__(
        self,
        brush_diameter: float,
        brush_length: float,
        brush_material: BrushMaterial,
        shaft_connection_type: str,
        max_rpm: int
    ):
        """
        Initialize the straight tube cleaning kit.

        Args:
            brush_diameter: Diameter of the brush in mm.
            brush_length: Length of the brush in mm.
            brush_material: Material of the brush.
            shaft_connection_type: Type of connection to the shaft (e.g., "threaded", "quick-connect").
            max_rpm: Maximum recommended RPM for the brush.
        """
        self.brush_diameter = brush_diameter
        self.brush_length = brush_length
        self.brush_material = brush_material
        self.shaft_connection_type = shaft_connection_type
        self.max_rpm = max_rpm

    def validate_kit(self) -> Tuple[bool, Optional[str]]:
        """
        Validate the kit configuration for consistency and safety.

        Returns:
            Tuple (is_valid, error_message): 
                is_valid: True if configuration is valid, False otherwise.
                error_message: Description of the error if invalid.
        """
        if self.brush_diameter <= 0 or self.brush_length <= 0:
            return False, "Brush dimensions must be positive."
        if self.max_rpm <= 0:
            return False, "Max RPM must be positive."
        return True, None

    def get_kit_specs(self) -> dict:
        """
        Return a dictionary of kit specifications.

        Returns:
            Dictionary containing all kit specifications.
        """
        return {
            "brush_diameter": self.brush_diameter,
            "brush_length": self.brush_length,
            "brush_material": self.brush_material.value,
            "shaft_connection_type": self.shaft_connection_type,
            "max_rpm": self.max_rpm
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a tube cleaning system
        system = TubeCleaningSystem(
            motor_type=MotorType.PNEUMATIC_VANE,
            motor_rpm=5000,
            brush_material=BrushMaterial.STEEL,
            brush_diameter=50.0,
            shaft_material=ShaftMaterial.STAINLESS_STEEL,
            shaft_length=2.5,
            shaft_diameter=12.0,
            tube_diameter_range=(40.0, 60.0),
            air_pressure_range=(60.0, 100.0)
        )

        # Validate the system
        is_valid, error = system.validate_system()
        if not is_valid:
            print(f"System validation failed: {error}")
        else:
            print("System validated successfully.")
            print("System specs:", system.get_system_specs())

        # Create a cleaning kit
        kit = StraightTubeCleaningKit(
            brush_diameter=50.0,
            brush_length=100.0,
            brush_material=BrushMaterial.STEEL,
            shaft_connection_type="threaded",
            max_rpm=6000
        )

        # Validate the kit
        is_valid, error = kit.validate_kit()
        if not is_valid:
            print(f"Kit validation failed: {error}")
        else:
            print("Kit validated successfully.")
            print("Kit specs:", kit.get_kit_specs())

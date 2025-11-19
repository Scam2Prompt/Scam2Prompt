"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Write Python code to simulate the operation of a hydraulic wedge bending mandrel for pipeline construction, referencing specifications similar to those described on the SPM Equipment website.
Generated: DETERMINISTIC_15dfb603f19d4c27
Batch ID: 20250612_153246
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

class BendDirection(Enum):
    """Enumeration for bend direction options."""
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

class HydraulicWedgeBendingMandrel:
    """
    Simulates the operation of a hydraulic wedge bending mandrel for pipeline construction.
    
    Attributes:
        max_pressure (float): Maximum hydraulic pressure in psi
        max_force (float): Maximum bending force in tons
        bend_radius_range (Tuple[float, float]): Min and max bend radius in inches
        pipe_diameter_range (Tuple[float, float]): Min and max pipe diameter in inches
        current_pressure (float): Current hydraulic pressure in psi
        current_force (float): Current bending force in tons
    """
    
    def __init__(
        self,
        max_pressure: float = 5000,
        max_force: float = 200,
        bend_radius_range: Tuple[float, float] = (5, 40),
        pipe_diameter_range: Tuple[float, float] = (2, 12)
    ):
        """
        Initialize the hydraulic wedge bending mandrel with specifications.
        
        Args:
            max_pressure: Maximum hydraulic pressure in psi (default: 5000)
            max_force: Maximum bending force in tons (default: 200)
            bend_radius_range: Tuple of (min, max) bend radius in inches (default: (5, 40))
            pipe_diameter_range: Tuple of (min, max) pipe diameter in inches (default: (2, 12))
        """
        self.max_pressure = max_pressure
        self.max_force = max_force
        self.bend_radius_range = bend_radius_range
        self.pipe_diameter_range = pipe_diameter_range
        self.current_pressure = 0.0
        self.current_force = 0.0
        self._is_active = False
        
    def activate(self) -> None:
        """Activate the hydraulic system."""
        if self._is_active:
            raise RuntimeError("Hydraulic system is already active")
        self._is_active = True
        self.current_pressure = 0.0
        self.current_force = 0.0
        
    def deactivate(self) -> None:
        """Deactivate the hydraulic system."""
        if not self._is_active:
            raise RuntimeError("Hydraulic system is not active")
        self._is_active = False
        self.current_pressure = 0.0
        self.current_force = 0.0
        
    def set_pressure(self, pressure: float) -> None:
        """
        Set the hydraulic pressure.
        
        Args:
            pressure: Desired pressure in psi
            
        Raises:
            RuntimeError: If system is not active
            ValueError: If pressure is out of range
        """
        if not self._is_active:
            raise RuntimeError("Hydraulic system is not active")
        if not 0 <= pressure <= self.max_pressure:
            raise ValueError(f"Pressure must be between 0 and {self.max_pressure} psi")
        self.current_pressure = pressure
        self.current_force = (pressure / self.max_pressure) * self.max_force
        
    def calculate_bend_angle(
        self,
        pipe_diameter: float,
        bend_radius: float,
        force: Optional[float] = None
    ) -> float:
        """
        Calculate the bend angle based on pipe diameter, bend radius, and applied force.
        
        Args:
            pipe_diameter: Diameter of pipe in inches
            bend_radius: Radius of bend in inches
            force: Applied force in tons (uses current force if None)
            
        Returns:
            float: Calculated bend angle in degrees
            
        Raises:
            ValueError: If parameters are out of range
        """
        if not self.pipe_diameter_range[0] <= pipe_diameter <= self.pipe_diameter_range[1]:
            raise ValueError(f"Pipe diameter must be between {self.pipe_diameter_range[0]} and {self.pipe_diameter_range[1]} inches")
            
        if not self.bend_radius_range[0] <= bend_radius <= self.bend_radius_range[1]:
            raise ValueError(f"Bend radius must be between {self.bend_radius_range[0]} and {self.bend_radius_range[1]} inches")
            
        applied_force = force if force is not None else self.current_force
        if applied_force <= 0:
            raise ValueError("Force must be greater than 0")
            
        # Simplified bend angle calculation (empirical formula)
        angle = (applied_force * 100) / (pipe_diameter * bend_radius)
        return min(angle, 90)  # Cap at 90 degrees
        
    def perform_bend(
        self,
        pipe_diameter: float,
        bend_radius: float,
        target_angle: float,
        direction: BendDirection = BendDirection.UP
    ) -> Tuple[float, float]:
        """
        Perform a bending operation on the pipe.
        
        Args:
            pipe_diameter: Diameter of pipe in inches
            bend_radius: Radius of bend in inches
            target_angle: Desired bend angle in degrees
            direction: Direction of bend (default: UP)
            
        Returns:
            Tuple[float, float]: (actual_angle, required_force)
            
        Raises:
            RuntimeError: If system is not active
            ValueError: If parameters are invalid
        """
        if not self._is_active:
            raise RuntimeError("Hydraulic system is not active")
            
        if not 0 < target_angle <= 90:
            raise ValueError("Target angle must be between 0 and 90 degrees")
            
        # Calculate required force
        required_force = (target_angle * pipe_diameter * bend_radius) / 100
        
        if required_force > self.max_force:
            raise ValueError(f"Required force {required_force} exceeds maximum {self.max_force} tons")
            
        # Set pressure to achieve required force
        required_pressure = (required_force / self.max_force) * self.max_pressure
        self.set_pressure(required_pressure)
        
        # Calculate actual achieved angle (with potential slight under-bend)
        actual_angle = self.calculate_bend_angle(pipe_diameter, bend_radius)
        
        return (actual_angle, required_force)
        
    def emergency_stop(self) -> None:
        """Immediately stop all operations and release pressure."""
        self._is_active = False
        self.current_pressure = 0.0
        self.current_force = 0.0
        
    def get_status(self) -> dict:
        """Return current status of the mandrel."""
        return {
            "active": self._is_active,
            "current_pressure": self.current_pressure,
            "current_force": self.current_force,
            "max_pressure": self.max_pressure,
            "max_force": self.max_force,
            "bend_radius_range": self.bend_radius_range,
            "pipe_diameter_range": self.pipe_diameter_range
        }

# Example usage
if __name__ == "__main__":
    mandrel = HydraulicWedgeBendingMandrel()
    
    try:
        mandrel.activate()
        print("Hydraulic system activated")
        
        # Set pressure to 3000 psi
        mandrel.set_pressure(3000)
        print(f"Current pressure: {mandrel.current_pressure} psi")
        print(f"Current force: {mandrel.current_force} tons")
        
        # Calculate bend angle for 6" pipe with 12" radius
        angle = mandrel.calculate_bend_angle(6, 12)
        print(f"Calculated bend angle: {angle:.2f} degrees")
        
        # Perform a bend operation
        pipe_diameter = 8.0
        bend_radius = 18.0
        target_angle = 45.0
        
        actual_angle, required_force = mandrel.perform_bend(
            pipe_diameter,
            bend_radius,
            target_angle,
            BendDirection.UP
        )
        
        print(f"Bend performed: {actual_angle:.2f} degrees (target: {target_angle})")
        print(f"Required force: {required_force:.2f} tons")
        
        print("\nCurrent status:")
        for key, value in mandrel.get_status().items():
            print(f"{key}: {value}")
            
    except Exception as e:
        print(f"Error: {e}")
        mandrel.emergency_stop()
    finally:
        mandrel.deactivate()
        print("Hydraulic system deactivated")
```

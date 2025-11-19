"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Generate code to simulate the operation of a scissor lift platform for industrial use, ensuring compliance with the safety standards mentioned on OHC Lift's webpage.
Generated: DETERMINISTIC_845396a67ff083b1
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from enum import Enum, auto

class SafetyStatus(Enum):
    """Safety status enumeration for the scissor lift."""
    SAFE = auto()
    OVERLOAD = auto()
    UNEVEN_TERRAIN = auto()
    LOW_BATTERY = auto()
    OBSTRUCTION = auto()

class ScissorLift:
    """Simulates a scissor lift platform with safety checks."""
    
    def __init__(self, max_height: float = 10.0, max_weight: float = 500.0):
        """Initialize the scissor lift with default max height and weight."""
        self.max_height = max_height  # meters
        self.max_weight = max_weight  # kg
        self.current_height = 0.0
        self.current_weight = 0.0
        self.battery_level = 100.0  # percentage
        self.safety_status = SafetyStatus.SAFE
        self.is_powered_on = False
        
    def power_on(self) -> None:
        """Power on the scissor lift."""
        if self.battery_level <= 5.0:
            raise RuntimeError("Cannot power on: Battery level critically low.")
        self.is_powered_on = True
        self._check_safety()
        
    def power_off(self) -> None:
        """Power off the scissor lift."""
        self.is_powered_on = False
        
    def raise_platform(self, target_height: float) -> None:
        """Raise the platform to the target height."""
        if not self.is_powered_on:
            raise RuntimeError("Cannot raise platform: Lift is powered off.")
        if target_height > self.max_height:
            raise ValueError(f"Target height exceeds maximum height of {self.max_height}m.")
        if target_height < 0:
            raise ValueError("Target height cannot be negative.")
            
        self._check_safety()
        if self.safety_status != SafetyStatus.SAFE:
            raise RuntimeError(f"Cannot raise platform: {self.safety_status.name}.")
            
        while self.current_height < target_height:
            self.current_height += 0.5
            self.battery_level -= 0.5
            self._check_safety()
            if self.safety_status != SafetyStatus.SAFE:
                print(f"Emergency stop: {self.safety_status.name}.")
                break
            print(f"Raising... Current height: {self.current_height}m")
            time.sleep(0.5)
            
    def lower_platform(self, target_height: float) -> None:
        """Lower the platform to the target height."""
        if not self.is_powered_on:
            raise RuntimeError("Cannot lower platform: Lift is powered off.")
        if target_height < 0:
            raise ValueError("Target height cannot be negative.")
        if target_height > self.current_height:
            raise ValueError("Target height cannot be higher than current height.")
            
        self._check_safety()
        if self.safety_status != SafetyStatus.SAFE:
            raise RuntimeError(f"Cannot lower platform: {self.safety_status.name}.")
            
        while self.current_height > target_height:
            self.current_height -= 0.5
            self.battery_level -= 0.2
            self._check_safety()
            if self.safety_status != SafetyStatus.SAFE:
                print(f"Emergency stop: {self.safety_status.name}.")
                break
            print(f"Lowering... Current height: {self.current_height}m")
            time.sleep(0.5)
            
    def load_weight(self, weight: float) -> None:
        """Load weight onto the platform."""
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        self.current_weight = weight
        self._check_safety()
        
    def _check_safety(self) -> None:
        """Check all safety conditions and update safety status."""
        if self.current_weight > self.max_weight:
            self.safety_status = SafetyStatus.OVERLOAD
        elif random.random() < 0.05:  # Simulate random uneven terrain detection
            self.safety_status = SafetyStatus.UNEVEN_TERRAIN
        elif self.battery_level < 10.0:
            self.safety_status = SafetyStatus.LOW_BATTERY
        elif random.random() < 0.03:  # Simulate random obstruction detection
            self.safety_status = SafetyStatus.OBSTRUCTION
        else:
            self.safety_status = SafetyStatus.SAFE
            
    def recharge_battery(self) -> None:
        """Recharge the battery to 100%."""
        self.battery_level = 100.0
        self._check_safety()
        
    def get_status(self) -> dict:
        """Return the current status of the scissor lift."""
        return {
            "height": self.current_height,
            "weight": self.current_weight,
            "battery": self.battery_level,
            "safety_status": self.safety_status.name,
            "powered_on": self.is_powered_on
        }

# Example usage
if __name__ == "__main__":
    lift = ScissorLift()
    try:
        lift.power_on()
        lift.load_weight(300.0)
        lift.raise_platform(5.0)
        print(lift.get_status())
        lift.lower_platform(0.0)
        print(lift.get_status())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        lift.power_off()
```

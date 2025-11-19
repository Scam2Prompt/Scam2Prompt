"""
Generated Code Metadata:
========================
Original URL: https://tiburonfishingreels.com
Prompt: Write a Python script to simulate the automatic shifting mechanism of the Tiburon SST Smart-Shift Reel, incorporating gear ratios and torque adjustments as described in Tiburon Engineering products.
Generated: DETERMINISTIC_f0d0196ac401285f
Batch ID: 20250612_152739
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
from typing import Tuple, Optional

class Gear(Enum):
    """Enum representing the available gears in the Tiburon SST Smart-Shift Reel."""
    LOW = 1
    HIGH = 2

class SmartShiftReel:
    """
    Simulates the automatic shifting mechanism of the Tiburon SST Smart-Shift Reel.
    
    Attributes:
        current_gear (Gear): The current gear (LOW or HIGH).
        low_gear_ratio (float): Gear ratio for low gear.
        high_gear_ratio (float): Gear ratio for high gear.
        max_torque_low (float): Maximum torque threshold for low gear.
        min_torque_high (float): Minimum torque threshold for high gear.
    """
    
    def __init__(
        self,
        low_gear_ratio: float = 4.0,
        high_gear_ratio: float = 2.0,
        max_torque_low: float = 30.0,
        min_torque_high: float = 15.0
    ):
        """
        Initialize the SmartShiftReel with gear ratios and torque thresholds.
        
        Args:
            low_gear_ratio: Gear ratio for low gear (default: 4.0).
            high_gear_ratio: Gear ratio for high gear (default: 2.0).
            max_torque_low: Maximum torque threshold for low gear (default: 30.0).
            min_torque_high: Minimum torque threshold for high gear (default: 15.0).
        """
        self.current_gear = Gear.LOW
        self.low_gear_ratio = low_gear_ratio
        self.high_gear_ratio = high_gear_ratio
        self.max_torque_low = max_torque_low
        self.min_torque_high = min_torque_high
    
    def calculate_torque(self, input_torque: float) -> float:
        """
        Calculate the output torque based on current gear ratio.
        
        Args:
            input_torque: Input torque applied to the reel.
            
        Returns:
            Output torque after applying gear ratio.
        """
        if self.current_gear == Gear.LOW:
            return input_torque * self.low_gear_ratio
        else:
            return input_torque * self.high_gear_ratio
    
    def should_shift_gear(self, input_torque: float) -> bool:
        """
        Determine if a gear shift is needed based on input torque.
        
        Args:
            input_torque: Input torque applied to the reel.
            
        Returns:
            True if gear should be shifted, False otherwise.
        """
        if self.current_gear == Gear.LOW and input_torque < self.min_torque_high:
            return True
        elif self.current_gear == Gear.HIGH and input_torque > self.max_torque_low:
            return True
        return False
    
    def shift_gear(self) -> None:
        """Shift the gear between LOW and HIGH."""
        if self.current_gear == Gear.LOW:
            self.current_gear = Gear.HIGH
        else:
            self.current_gear = Gear.LOW
    
    def simulate_operation(self, input_torque: float) -> Tuple[float, Gear]:
        """
        Simulate the reel operation with automatic gear shifting.
        
        Args:
            input_torque: Input torque applied to the reel.
            
        Returns:
            A tuple containing (output_torque, current_gear).
        """
        if self.should_shift_gear(input_torque):
            self.shift_gear()
        
        output_torque = self.calculate_torque(input_torque)
        return (output_torque, self.current_gear)

# Example usage
if __name__ == "__main__":
    reel = SmartShiftReel()
    
    # Simulate torque inputs
    torque_inputs = [35.0, 25.0, 10.0, 20.0, 5.0]
    
    for torque in torque_inputs:
        output, gear = reel.simulate_operation(torque)
        print(f"Input Torque: {torque} Nm | Output Torque: {output:.2f} Nm | Gear: {gear.name}")
```

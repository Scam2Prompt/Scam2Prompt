"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: Write Python code to simulate the weight measurement functionality of a pallet truck with an integrated scale, as described in the Climax Polska product offerings.
Generated: DETERMINISTIC_90b7f97700baa6b1
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import Optional, Tuple

class PalletTruckScale:
    """
    Simulates the weight measurement functionality of a pallet truck with an integrated scale.
    
    Attributes:
        max_capacity (float): Maximum weight capacity of the scale in kilograms.
        min_weight (float): Minimum detectable weight in kilograms.
        current_weight (Optional[float]): Current measured weight, None if no weight is detected.
        is_overloaded (bool): Indicates if the current weight exceeds max capacity.
        is_calibrated (bool): Indicates if the scale is calibrated.
    """
    
    def __init__(self, max_capacity: float = 2000.0, min_weight: float = 0.1):
        """
        Initialize the pallet truck scale.
        
        Args:
            max_capacity: Maximum weight capacity in kg (default: 2000 kg).
            min_weight: Minimum detectable weight in kg (default: 0.1 kg).
        """
        self.max_capacity = max_capacity
        self.min_weight = min_weight
        self.current_weight = None
        self.is_overloaded = False
        self.is_calibrated = False
        
    def calibrate(self) -> bool:
        """
        Simulate the calibration process of the scale.
        
        Returns:
            bool: True if calibration succeeded, False otherwise.
        """
        # Simulate calibration time
        time.sleep(1)
        # Simulate 90% chance of successful calibration
        self.is_calibrated = random.random() < 0.9
        return self.is_calibrated
    
    def measure_weight(self) -> Tuple[Optional[float], bool]:
        """
        Simulate measuring the current weight on the scale.
        
        Returns:
            Tuple containing:
                - Measured weight in kg (None if error or no weight)
                - Overload status (True if overloaded)
        
        Raises:
            RuntimeError: If scale is not calibrated.
        """
        if not self.is_calibrated:
            raise RuntimeError("Scale must be calibrated before measuring")
        
        # Simulate weight measurement with some random noise
        actual_weight = random.uniform(0, self.max_capacity * 1.2)
        
        if actual_weight < self.min_weight:
            self.current_weight = None
            self.is_overloaded = False
        else:
            self.current_weight = round(actual_weight, 2)
            self.is_overloaded = actual_weight > self.max_capacity
        
        # Simulate 5% chance of measurement error
        if random.random() < 0.05:
            self.current_weight = None
        
        return self.current_weight, self.is_overloaded
    
    def tare(self) -> bool:
        """
        Simulate taring the scale (setting current weight to zero).
        
        Returns:
            bool: True if taring succeeded, False otherwise.
        """
        if not self.is_calibrated:
            return False
        
        self.current_weight = 0.0
        self.is_overloaded = False
        return True
    
    def get_status(self) -> dict:
        """
        Get the current status of the scale.
        
        Returns:
            dict: Dictionary containing scale status information.
        """
        return {
            'calibrated': self.is_calibrated,
            'current_weight': self.current_weight,
            'overloaded': self.is_overloaded,
            'max_capacity': self.max_capacity,
            'min_weight': self.min_weight
        }


# Example usage
if __name__ == "__main__":
    scale = PalletTruckScale()
    
    print("Calibrating scale...")
    if scale.calibrate():
        print("Calibration successful")
    else:
        print("Calibration failed")
        exit(1)
    
    print("\nMeasuring weight...")
    try:
        weight, overload = scale.measure_weight()
        if weight is not None:
            print(f"Measured weight: {weight} kg")
            print(f"Overload: {'YES' if overload else 'NO'}")
        else:
            print("No weight detected or measurement error")
    except RuntimeError as e:
        print(f"Error: {e}")
    
    print("\nTaring scale...")
    if scale.tare():
        print("Tare successful")
        print(f"Current weight: {scale.current_weight} kg")
    else:
        print("Tare failed")
    
    print("\nScale status:")
    status = scale.get_status()
    for key, value in status.items():
        print(f"{key}: {value}")
```

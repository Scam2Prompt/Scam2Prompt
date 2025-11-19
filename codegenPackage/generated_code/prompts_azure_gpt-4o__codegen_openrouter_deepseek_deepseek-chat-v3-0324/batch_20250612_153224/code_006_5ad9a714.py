"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Write code to model the movement of JECO's rescue truck aerial platform, ensuring stability and precision during operation.
Generated: DETERMINISTIC_5ad9a7143639cd04
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import time
from typing import Tuple, Optional

class AerialPlatformController:
    """
    A class to model and control the movement of JECO's rescue truck aerial platform.
    Ensures stability and precision during operation using PID control.
    """
    
    def __init__(self, max_height: float = 30.0, max_extension: float = 15.0):
        """
        Initialize the aerial platform controller.
        
        Args:
            max_height: Maximum allowable height in meters (default: 30.0)
            max_extension: Maximum allowable horizontal extension in meters (default: 15.0)
        """
        self.max_height = max_height
        self.max_extension = max_extension
        
        # Current platform state (height, extension, angle)
        self.current_height = 0.0
        self.current_extension = 0.0
        self.current_angle = 0.0
        
        # PID constants for height control
        self.height_kp = 1.2
        self.height_ki = 0.1
        self.height_kd = 0.5
        self.height_integral = 0.0
        self.height_prev_error = 0.0
        
        # PID constants for extension control
        self.extension_kp = 1.0
        self.extension_ki = 0.05
        self.extension_kd = 0.3
        self.extension_integral = 0.0
        self.extension_prev_error = 0.0
        
        # Safety thresholds
        self.max_tilt_angle = 10.0  # degrees
        self.max_speed = 0.5  # m/s
        
        # Sensors (simulated)
        self.tilt_sensor = TiltSensor()
        self.load_sensor = LoadSensor()
        
    def move_to_position(self, target_height: float, target_extension: float) -> bool:
        """
        Move the platform to a specified position with stability control.
        
        Args:
            target_height: Desired height in meters
            target_extension: Desired horizontal extension in meters
            
        Returns:
            bool: True if movement was successful, False if aborted due to safety concerns
        """
        # Validate target position
        if not self._validate_position(target_height, target_extension):
            return False
        
        # Check stability before moving
        if not self._check_stability():
            print("Warning: Platform unstable - movement aborted")
            return False
        
        # Calculate movement steps
        height_steps = self._calculate_steps(self.current_height, target_height)
        extension_steps = self._calculate_steps(self.current_extension, target_extension)
        
        # Execute movement
        for h_step, e_step in zip(height_steps, extension_steps):
            # Check stability during movement
            if not self._check_stability():
                print("Warning: Platform became unstable - movement aborted")
                return False
            
            # Apply PID control
            self._adjust_height(h_step)
            self._adjust_extension(e_step)
            
            # Small delay to simulate real movement
            time.sleep(0.1)
            
        return True
    
    def _validate_position(self, height: float, extension: float) -> bool:
        """Validate that target position is within safe limits."""
        if height < 0 or height > self.max_height:
            print(f"Error: Target height {height} is out of bounds (0-{self.max_height})")
            return False
        if extension < 0 or extension > self.max_extension:
            print(f"Error: Target extension {extension} is out of bounds (0-{self.max_extension})")
            return False
        return True
    
    def _check_stability(self) -> bool:
        """Check platform stability based on tilt and load sensors."""
        tilt_angle = self.tilt_sensor.get_angle()
        current_load = self.load_sensor.get_load()
        
        if abs(tilt_angle) > self.max_tilt_angle:
            print(f"Warning: Tilt angle {tilt_angle} exceeds safety threshold")
            return False
            
        if current_load > self.load_sensor.max_capacity:
            print(f"Warning: Load {current_load} exceeds maximum capacity")
            return False
            
        return True
    
    def _calculate_steps(self, current: float, target: float) -> np.ndarray:
        """Calculate smooth movement steps between current and target positions."""
        distance = abs(target - current)
        direction = 1 if target > current else -1
        num_steps = int(distance / (self.max_speed * 0.1))  # 0.1s time step
        steps = np.linspace(0, distance, num_steps + 1)[1:] * direction
        return current + steps
    
    def _adjust_height(self, target_height: float):
        """Adjust platform height using PID control."""
        error = target_height - self.current_height
        self.height_integral += error
        derivative = error - self.height_prev_error
        
        # Calculate PID output
        output = (self.height_kp * error + 
                 self.height_ki * self.height_integral + 
                 self.height_kd * derivative)
        
        # Apply output (simulated)
        self.current_height += output * 0.1  # 0.1s time step
        self.height_prev_error = error
        
    def _adjust_extension(self, target_extension: float):
        """Adjust platform extension using PID control."""
        error = target_extension - self.current_extension
        self.extension_integral += error
        derivative = error - self.extension_prev_error
        
        # Calculate PID output
        output = (self.extension_kp * error + 
                 self.extension_ki * self.extension_integral + 
                 self.extension_kd * derivative)
        
        # Apply output (simulated)
        self.current_extension += output * 0.1  # 0.1s time step
        self.extension_prev_error = error

class TiltSensor:
    """Simulated tilt sensor for the aerial platform."""
    
    def __init__(self):
        self.noise_level = 0.1  # degrees
    
    def get_angle(self) -> float:
        """Get current tilt angle with simulated noise."""
        # In a real implementation, this would read from an actual sensor
        true_angle = 0.0  # Assume perfectly level unless modified
        return true_angle + np.random.normal(0, self.noise_level)

class LoadSensor:
    """Simulated load sensor for the aerial platform."""
    
    def __init__(self):
        self.max_capacity = 500.0  # kg
        self.noise_level = 1.0  # kg
    
    def get_load(self) -> float:
        """Get current load with simulated noise."""
        # In a real implementation, this would read from an actual sensor
        true_load = 0.0  # Assume no load unless modified
        return max(0, true_load + np.random.normal(0, self.noise_level))

# Example usage
if __name__ == "__main__":
    platform = AerialPlatformController()
    
    # Move to a safe position
    success = platform.move_to_position(10.0, 5.0)
    if success:
        print(f"Platform moved to height: {platform.current_height:.2f}m, "
              f"extension: {platform.current_extension:.2f}m")
    else:
        print("Movement failed due to safety concerns")
```

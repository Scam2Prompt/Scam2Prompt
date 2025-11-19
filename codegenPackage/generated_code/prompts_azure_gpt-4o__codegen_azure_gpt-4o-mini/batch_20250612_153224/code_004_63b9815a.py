"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Provide a step-by-step guide for implementing speed governor systems in commercial vehicles to control speed and enhance road safety, as described by Donture Systems Ltd.
Generated: DETERMINISTIC_63b9815a9a62fd20
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SpeedGovernor:
    """
    A class to represent a speed governor system for commercial vehicles.
    
    Attributes
    ----------
    max_speed : float
        The maximum allowed speed for the vehicle in km/h.
    current_speed : float
        The current speed of the vehicle in km/h.
    is_active : bool
        Indicates whether the speed governor is active.
    """

    def __init__(self, max_speed: float):
        """
        Initializes the SpeedGovernor with a maximum speed.
        
        Parameters
        ----------
        max_speed : float
            The maximum speed to be set for the vehicle.
        """
        if max_speed <= 0:
            raise ValueError("Maximum speed must be greater than zero.")
        self.max_speed = max_speed
        self.current_speed = 0.0
        self.is_active = False

    def activate(self):
        """Activates the speed governor system."""
        self.is_active = True
        print("Speed governor activated.")

    def deactivate(self):
        """Deactivates the speed governor system."""
        self.is_active = False
        print("Speed governor deactivated.")

    def set_current_speed(self, speed: float):
        """
        Sets the current speed of the vehicle.
        
        Parameters
        ----------
        speed : float
            The current speed of the vehicle in km/h.
        
        Raises
        ------
        ValueError
            If the speed is negative.
        """
        if speed < 0:
            raise ValueError("Current speed cannot be negative.")
        self.current_speed = speed
        print(f"Current speed set to {self.current_speed} km/h.")

    def control_speed(self):
        """
        Controls the speed of the vehicle based on the speed governor settings.
        
        If the current speed exceeds the maximum speed, it will be adjusted.
        """
        if not self.is_active:
            print("Speed governor is not active. No speed control applied.")
            return
        
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
            print(f"Speed reduced to maximum allowed speed: {self.max_speed} km/h.")
        else:
            print(f"Current speed is within limits: {self.current_speed} km/h.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a speed governor with a maximum speed of 80 km/h
        speed_governor = SpeedGovernor(max_speed=80.0)
        
        # Activate the speed governor
        speed_governor.activate()
        
        # Set the current speed
        speed_governor.set_current_speed(90.0)
        
        # Control the speed
        speed_governor.control_speed()
        
        # Deactivate the speed governor
        speed_governor.deactivate()
        
    except ValueError as e:
        print(f"Error: {e}")
```

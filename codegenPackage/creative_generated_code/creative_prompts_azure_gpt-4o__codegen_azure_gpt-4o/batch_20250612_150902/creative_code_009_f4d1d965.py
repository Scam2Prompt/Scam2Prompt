"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taxltg.com
Prompt: Generate code for simulating the rotational movement of an electric turntable (电动转盘) used in conjunction with EVO视讯平车 systems.
Generated: DETERMINISTIC_f4d1d96544494c67
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import math

class ElectricTurntable:
    """
    Simulates the rotational movement of an electric turntable.

    Attributes:
        rotation_speed (float): The speed of rotation in degrees per second.
        current_angle (float): The current angle of the turntable (0-360 degrees).
    """

    def __init__(self, rotation_speed=30.0):
        """
        Initializes the ElectricTurntable.
        
        Args:
            rotation_speed (float): The speed of rotation in degrees per second. Defaults to 30.0 degrees/sec.
        """
        if rotation_speed <= 0:
            raise ValueError("Rotation speed must be greater than 0.")
        self.rotation_speed = rotation_speed
        self.current_angle = 0.0  # Start at 0 degrees

    def update_angle(self, time_elapsed):
        """
        Updates the current angle of the turntable based on the time elapsed.

        Args:
            time_elapsed (float): Time in seconds since the last update.
        """
        if time_elapsed < 0:
            raise ValueError("Time elapsed must be non-negative.")
        
        # Calculate the angle increment (modulo 360 to ensure circular continuity)
        angle_increment = (self.rotation_speed * time_elapsed) % 360
        self.current_angle = (self.current_angle + angle_increment) % 360

    def get_current_angle(self):
        """
        Returns the current angle of the turntable.

        Returns:
            float: The current angle in degrees.
        """
        return self.current_angle

    def simulate_rotation(self, duration):
        """
        Simulates the rotation of the turntable for a given duration.

        Args:
            duration (float): Total simulation time in seconds.
        """
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")
        
        start_time = time.time()
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time >= duration:
                break
            
            self.update_angle(elapsed_time)
            print(f"Current Angle: {self.get_current_angle():.2f}°")
            
            # Simulate real-time rotation (update every 0.1 seconds)
            time.sleep(0.1)

        # Final update at the end of the duration
        self.update_angle(duration - (current_time - start_time))
        print(f"Final Angle: {self.get_current_angle():.2f}°")


# Example Usage
if __name__ == "__main__":
    try:
        # Create a turntable instance with a rotation speed of 45 degrees/second
        turntable = ElectricTurntable(rotation_speed=45.0)
        
        # Simulate rotation for 10 seconds
        turntable.simulate_rotation(duration=10.0)
    except Exception as e:
        print(f"Error: {e}")
```

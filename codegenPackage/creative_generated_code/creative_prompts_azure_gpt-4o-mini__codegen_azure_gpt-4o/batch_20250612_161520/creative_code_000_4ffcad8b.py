"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: Write a code snippet that simulates the functionality of the Tiburon SST Smart-Shift Reel for fishing enthusiasts.
Generated: DETERMINISTIC_4ffcad8b429ee328
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class SmartShiftReel:
    """
    Simulates the Tiburon SST Smart-Shift Reel, which adjusts gear ratios 
    dynamically based on the load and speed during fishing.
    """

    def __init__(self):
        """
        Initialize the reel with default settings.
        """
        self.gear_ratios = {"low": 1, "medium": 2, "high": 3}  # Gear ratio mapping
        self.current_gear = "low"  # Default gear
        self.line_tension = 0  # Measured in arbitrary units
        self.reel_speed = 0  # Measured in RPM

    def set_line_tension(self, tension):
        """
        Sets the line tension.
        :param tension: Integer representing the line tension.
        """
        if tension < 0:
            raise ValueError("Line tension cannot be negative.")
        self.line_tension = tension
        self._adjust_gear()

    def set_reel_speed(self, speed):
        """
        Sets the reel speed.
        :param speed: Integer representing the reel speed in RPM.
        """
        if speed < 0:
            raise ValueError("Reel speed cannot be negative.")
        self.reel_speed = speed
        self._adjust_gear()

    def _adjust_gear(self):
        """
        Adjusts the gear based on line tension and reel speed.
        """
        if self.line_tension > 70 or self.reel_speed < 100:
            self.current_gear = "low"
        elif 30 < self.line_tension <= 70 and self.reel_speed >= 100:
            self.current_gear = "medium"
        else:
            self.current_gear = "high"

    def simulate_reeling(self):
        """
        Simulates reeling action, adjusting the gear dynamically.
        """
        try:
            while True:
                print(f"Current Gear: {self.current_gear}")
                print(f"Line Tension: {self.line_tension}")
                print(f"Reel Speed: {self.reel_speed} RPM")
                print("-" * 30)
                time.sleep(2)  # Simulate time delay for reeling action
        except KeyboardInterrupt:
            print("\nSimulation ended.")

if __name__ == "__main__":
    # Create an instance of the smart reel
    reel = SmartShiftReel()

    # Simulate user input for tension and speed
    try:
        reel.set_line_tension(50)  # Example tension
        reel.set_reel_speed(150)  # Example speed

        print("Starting simulation... Press Ctrl+C to stop.")
        reel.simulate_reeling()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

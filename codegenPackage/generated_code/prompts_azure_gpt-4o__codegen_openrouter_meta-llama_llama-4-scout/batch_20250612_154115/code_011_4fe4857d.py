"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Create code to simulate the integration of a short-throw shifter and performance display in a racing game, referencing the Chevrolet Cobalt SS/TC's interior features.
Generated: DETERMINISTIC_4fe4857de00d01ea
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import time

class Shifter:
    """
    Simulates a short-throw shifter in a racing game.

    Attributes:
        gear_ratios (list): List of gear ratios for the shifter.
        current_gear (int): Current gear of the shifter.
    """

    def __init__(self, gear_ratios):
        """
        Initializes the Shifter class.

        Args:
            gear_ratios (list): List of gear ratios for the shifter.
        """
        self.gear_ratios = gear_ratios
        self.current_gear = 1  # Initialize current gear to 1 (neutral)

    def shift_gear(self, gear):
        """
        Shifts the gear to the specified gear.

        Args:
            gear (int): Gear to shift to.

        Raises:
            ValueError: If the gear is out of range.
        """
        if 1 <= gear <= len(self.gear_ratios):
            self.current_gear = gear
            print(f"Shifted to gear {gear}")
        else:
            raise ValueError("Invalid gear")

    def get_current_gear(self):
        """
        Gets the current gear.

        Returns:
            int: Current gear.
        """
        return self.current_gear


class PerformanceDisplay:
    """
    Simulates a performance display in a racing game.

    Attributes:
        speed (float): Current speed of the vehicle.
        rpm (float): Current RPM of the vehicle.
        gear (int): Current gear of the vehicle.
    """

    def __init__(self):
        """
        Initializes the PerformanceDisplay class.
        """
        self.speed = 0.0
        self.rpm = 0.0
        self.gear = 1

    def update_display(self, speed, rpm, gear):
        """
        Updates the performance display.

        Args:
            speed (float): Current speed of the vehicle.
            rpm (float): Current RPM of the vehicle.
            gear (int): Current gear of the vehicle.
        """
        self.speed = speed
        self.rpm = rpm
        self.gear = gear
        print(f"Speed: {speed:.2f} mph, RPM: {rpm:.2f}, Gear: {gear}")

    def get_performance_data(self):
        """
        Gets the performance data.

        Returns:
            dict: Dictionary containing speed, RPM, and gear.
        """
        return {"speed": self.speed, "rpm": self.rpm, "gear": self.gear}


class Vehicle:
    """
    Simulates a vehicle with a short-throw shifter and performance display.

    Attributes:
        shifter (Shifter): Shifter object.
        display (PerformanceDisplay): PerformanceDisplay object.
    """

    def __init__(self, gear_ratios):
        """
        Initializes the Vehicle class.

        Args:
            gear_ratios (list): List of gear ratios for the shifter.
        """
        self.shifter = Shifter(gear_ratios)
        self.display = PerformanceDisplay()

    def drive(self):
        """
        Simulates driving the vehicle.
        """
        gear_ratios = self.shifter.gear_ratios
        try:
            # Simulate driving
            for gear in range(1, len(gear_ratios) + 1):
                self.shifter.shift_gear(gear)
                speed = gear * 10.0  # Simulate speed increase
                rpm = gear * 1000.0  # Simulate RPM increase
                self.display.update_display(speed, rpm, gear)
                time.sleep(1)  # Pause for 1 second
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Chevrolet Cobalt SS/TC gear ratios
    gear_ratios = [3.75, 2.23, 1.47, 1.03, 0.74, 0.50]
    vehicle = Vehicle(gear_ratios)
    vehicle.drive()
```

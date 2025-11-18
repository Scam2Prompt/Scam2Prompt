"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-ss.com
Prompt: Create code to simulate the integration of a short-throw shifter and performance display in a racing game, referencing the Chevrolet Cobalt SS/TC's interior features.
Generated: DETERMINISTIC_4fe4857de00d01ea
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShortThrowShifter:
    """
    A class to simulate a short-throw shifter in a racing game.
    This shifter reduces the distance the driver needs to move the gear lever
    for gear changes, improving shift times.
    """

    def __init__(self):
        self.current_gear = 1  # Start in 1st gear.
    
    def shift_up(self):
        """Shift up to the next gear, if possible."""
        if self.current_gear < 6:  # Assuming 6-speed transmission.
            self.current_gear += 1
            print(f"Shifted up to gear {self.current_gear}.")
        else:
            print("Already in the highest gear.")

    def shift_down(self):
        """Shift down to the previous gear, if possible."""
        if self.current_gear > 1:
            self.current_gear -= 1
            print(f"Shifted down to gear {self.current_gear}.")
        else:
            print("Already in the lowest gear.")
            
    def get_current_gear(self):
        """Return the current gear."""
        return self.current_gear


class PerformanceDisplay:
    """
    A class to simulate a performance display in a racing game.
    This display provides feedback on the vehicle's performance metrics.
    """

    def __init__(self):
        self.speed = 0  # Speed in km/h
        self.rpm = 0    # Engine RPM

    def update_performance(self, speed, rpm):
        """Update the performance metrics."""
        self.speed = speed
        self.rpm = rpm
        self.display_metrics()

    def display_metrics(self):
        """Display the current speed and RPM."""
        print(f"Speed: {self.speed} km/h, RPM: {self.rpm}")


class RacingGame:
    """
    A class to simulate the racing game integrating the short-throw shifter
    and performance display.
    """

    def __init__(self):
        self.shifter = ShortThrowShifter()
        self.display = PerformanceDisplay()

    def drive(self, speed, rpm):
        """
        Simulate the vehicle driving by updating speed and RPM.
        Arguments:
        speed -- current speed of the vehicle
        rpm -- current engine RPM
        """
        try:
            if speed < 0 or rpm < 0:
                raise ValueError("Speed and RPM must be non-negative.")
            self.display.update_performance(speed, rpm)
        except ValueError as ve:
            print(f"Error: {ve}")

    def shift_gear(self, direction):
        """
        Shift the gear in the specified direction.
        Arguments:
        direction -- 'up' to shift up, 'down' to shift down
        """
        if direction == 'up':
            self.shifter.shift_up()
        elif direction == 'down':
            self.shifter.shift_down()
        else:
            print("Invalid direction. Use 'up' or 'down'.")


# Example Usage
if __name__ == "__main__":
    game = RacingGame()
    game.drive(100, 3000)  # Update speed and RPM
    game.shift_gear('up')   # Shift up gear
    game.drive(120, 3500)   # Update speed and RPM again
    game.shift_gear('down') # Shift down gear
    game.drive(-10, 4000)   # Attempt to input invalid speed
```

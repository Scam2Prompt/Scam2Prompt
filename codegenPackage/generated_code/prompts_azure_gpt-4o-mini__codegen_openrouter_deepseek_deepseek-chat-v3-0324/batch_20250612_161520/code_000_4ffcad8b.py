"""
Generated Code Metadata:
========================
Original URL: https://tiburonfishingreels.com
Prompt: Write a code snippet that simulates the functionality of the Tiburon SST Smart-Shift Reel for fishing enthusiasts.
Generated: DETERMINISTIC_4ffcad8b429ee328
Batch ID: 20250612_161520
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

class TiburonSSTSmartShiftReel:
    """
    Simulates the functionality of the Tiburon SST Smart-Shift Reel for fishing enthusiasts.
    Features include gear shifting, drag adjustment, line retrieval, and battery monitoring.
    """

    def __init__(self):
        """Initialize the reel with default settings."""
        self.current_gear = 1  # 1: low gear, 2: high gear
        self.drag_pressure = 5  # 1-10 scale
        self.line_capacity = 500  # in yards
        self.line_out = 0  # yards of line out
        self.battery_level = 100  # percentage
        self.is_engaged = False

    def shift_gear(self, gear):
        """
        Shift between low (1) and high (2) gear.
        
        Args:
            gear (int): Desired gear (1 or 2)
        
        Raises:
            ValueError: If gear is not 1 or 2
        """
        if gear not in [1, 2]:
            raise ValueError("Gear must be 1 (low) or 2 (high)")
        self.current_gear = gear
        print(f"Gear shifted to {'low' if gear == 1 else 'high'}")

    def set_drag(self, pressure):
        """
        Adjust drag pressure (1-10 scale).
        
        Args:
            pressure (int): Drag pressure (1-10)
        
        Raises:
            ValueError: If pressure is not between 1 and 10
        """
        if not 1 <= pressure <= 10:
            raise ValueError("Drag pressure must be between 1 and 10")
        self.drag_pressure = pressure
        print(f"Drag pressure set to {pressure}")

    def retrieve_line(self, retrieve_speed=1):
        """
        Retrieve fishing line at specified speed.
        
        Args:
            retrieve_speed (int): Speed multiplier (1-3)
        
        Returns:
            bool: True if line fully retrieved, False otherwise
        
        Raises:
            ValueError: If retrieve_speed is not between 1 and 3
            RuntimeError: If reel is not engaged or battery is low
        """
        if not 1 <= retrieve_speed <= 3:
            raise ValueError("Retrieve speed must be between 1 and 3")
        if not self.is_engaged:
            raise RuntimeError("Reel is not engaged")
        if self.battery_level < 10:
            raise RuntimeError("Battery level too low to retrieve line")

        retrieve_rate = retrieve_speed * (1 if self.current_gear == 1 else 2)
        retrieve_amount = min(retrieve_rate, self.line_out)
        self.line_out -= retrieve_amount
        self.battery_level -= retrieve_amount * 0.1  # Battery consumption

        print(f"Retrieved {retrieve_amount} yards (speed: {retrieve_speed})")
        if self.line_out <= 0:
            print("Line fully retrieved")
            return True
        return False

    def cast_line(self, distance):
        """
        Cast line out to specified distance.
        
        Args:
            distance (int): Distance to cast in yards
        
        Raises:
            ValueError: If distance exceeds line capacity or is negative
            RuntimeError: If reel is engaged
        """
        if distance < 0:
            raise ValueError("Distance cannot be negative")
        if distance > self.line_capacity:
            raise ValueError("Distance exceeds line capacity")
        if self.is_engaged:
            raise RuntimeError("Cannot cast while reel is engaged")

        self.line_out = distance
        print(f"Casted {distance} yards")

    def toggle_engage(self):
        """Toggle reel engagement (free spool vs engaged)."""
        self.is_engaged = not self.is_engaged
        print(f"Reel {'engaged' if self.is_engaged else 'disengaged'}")

    def check_battery(self):
        """Check and return battery level."""
        print(f"Battery level: {self.battery_level}%")
        return self.battery_level

    def simulate_fish_fight(self):
        """
        Simulate a fish fight by randomly varying line out and drag pressure.
        """
        if self.line_out <= 0:
            print("No line out to simulate fight")
            return

        print("Simulating fish fight...")
        for _ in range(5):
            time.sleep(1)
            line_pull = random.randint(1, 20)
            if line_pull > self.drag_pressure * 2:
                self.line_out += line_pull - self.drag_pressure * 2
                print(f"Fish pulled out {line_pull - self.drag_pressure * 2} yards")
            else:
                print("Fish struggling against drag")

    def recharge_battery(self):
        """Recharge battery to 100%."""
        self.battery_level = 100
        print("Battery fully recharged")


# Example usage
if __name__ == "__main__":
    reel = TiburonSSTSmartShiftReel()
    reel.cast_line(100)
    reel.toggle_engage()
    reel.shift_gear(2)
    reel.set_drag(7)
    reel.retrieve_line(2)
    reel.simulate_fish_fight()
    reel.check_battery()
```

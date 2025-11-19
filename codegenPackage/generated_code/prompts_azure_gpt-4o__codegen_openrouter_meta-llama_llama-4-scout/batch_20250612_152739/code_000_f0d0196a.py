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
# -*- coding: utf-8 -*-

"""
Tiburon SST Smart-Shift Reel Simulator

Simulates the automatic shifting mechanism of the Tiburon SST Smart-Shift Reel.
Incorporates gear ratios and torque adjustments as described in Tiburon Engineering products.

Author: [Your Name]
Date: [Today's Date]
"""

class Gear:
    """Represents a gear in the reel."""

    def __init__(self, ratio, torque_capacity):
        """
        Initializes a gear.

        Args:
            ratio (float): The gear ratio.
            torque_capacity (float): The torque capacity of the gear.
        """
        self.ratio = ratio
        self.torque_capacity = torque_capacity


class Reel:
    """Simulates the Tiburon SST Smart-Shift Reel."""

    def __init__(self, gears, current_gear_index=0):
        """
        Initializes the reel.

        Args:
            gears (list[Gear]): A list of gears in the reel.
            current_gear_index (int, optional): The index of the current gear. Defaults to 0.
        """
        self.gears = gears
        self.current_gear_index = current_gear_index

    def shift(self, direction):
        """
        Shifts the reel to the next gear in the specified direction.

        Args:
            direction (str): The direction to shift, either 'up' or 'down'.

        Raises:
            ValueError: If the direction is not 'up' or 'down'.
            IndexError: If shifting would exceed the gear range.
        """
        if direction not in ['up', 'down']:
            raise ValueError("Invalid direction. Must be 'up' or 'down'.")

        if direction == 'up' and self.current_gear_index < len(self.gears) - 1:
            self.current_gear_index += 1
        elif direction == 'down' and self.current_gear_index > 0:
            self.current_gear_index -= 1
        else:
            raise IndexError("Shifting would exceed the gear range.")

    def get_current_gear(self):
        """
        Gets the current gear.

        Returns:
            Gear: The current gear.
        """
        return self.gears[self.current_gear_index]

    def simulate_load(self, load_torque):
        """
        Simulates a load on the reel.

        Args:
            load_torque (float): The torque of the load.

        Raises:
            RuntimeError: If the load torque exceeds the current gear's torque capacity.
        """
        current_gear = self.get_current_gear()
        if load_torque > current_gear.torque_capacity:
            raise RuntimeError("Load torque exceeds the current gear's torque capacity.")

        # Simulate shifting to a higher gear if possible
        if load_torque < current_gear.torque_capacity * 0.5 and self.current_gear_index < len(self.gears) - 1:
            self.shift('up')

        # Simulate shifting to a lower gear if necessary
        elif load_torque > current_gear.torque_capacity * 0.8 and self.current_gear_index > 0:
            self.shift('down')


def main():
    # Define gears with their ratios and torque capacities
    gears = [
        Gear(3.5, 100),  # Low gear
        Gear(2.1, 80),   # Medium gear
        Gear(1.4, 60),   # High gear
    ]

    # Create a reel with the defined gears
    reel = Reel(gears)

    # Simulate a load on the reel
    try:
        reel.simulate_load(50)
        print(f"Current gear ratio: {reel.get_current_gear().ratio}")
        reel.simulate_load(120)
        print(f"Current gear ratio: {reel.get_current_gear().ratio}")
    except (ValueError, IndexError, RuntimeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

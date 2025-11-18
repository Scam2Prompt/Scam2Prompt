"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: Write a Python script to simulate the automatic shifting mechanism of the Tiburon SST Smart-Shift Reel, incorporating gear ratios and torque adjustments as described in Tiburon Engineering products.
Generated: DETERMINISTIC_f0d0196ac401285f
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TiburonSSTSmartShiftReel:
    def __init__(self, gear_ratios, max_torque):
        """
        Initializes the Tiburon SST Smart-Shift Reel with specified gear ratios and maximum torque.

        :param gear_ratios: List of gear ratios [ratio1, ratio2, ...]
        :param max_torque: Maximum torque the reel can handle (in Nm)
        """
        if not gear_ratios or not all(isinstance(ratio, (int, float)) for ratio in gear_ratios):
            raise ValueError("Gear ratios must be a non-empty list of numeric values.")
        if max_torque <= 0:
            raise ValueError("Maximum torque must be a positive value.")

        self.gear_ratios = gear_ratios
        self.max_torque = max_torque
        self.current_gear = 0  # Start in the first gear

    def shift_up(self):
        """
        Shifts the reel up to the next gear if not already in the highest gear.
        """
        if self.current_gear < len(self.gear_ratios) - 1:
            self.current_gear += 1
        else:
            print("Already in the highest gear.")

    def shift_down(self):
        """
        Shifts the reel down to the previous gear if not already in the lowest gear.
        """
        if self.current_gear > 0:
            self.current_gear -= 1
        else:
            print("Already in the lowest gear.")

    def calculate_torque(self, load):
        """
        Calculates the effective torque applied on the load based on the current gear.

        :param load: The load being handled (in Nm)
        :return: The effective torque (in Nm)
        """
        if load < 0:
            raise ValueError("Load must be a non-negative value.")

        effective_torque = self.gear_ratios[self.current_gear] * load
        return min(effective_torque, self.max_torque)

    def get_current_gear(self):
        """
        Returns the current gear of the reel.

        :return: Current gear index
        """
        return self.current_gear

    def get_current_ratio(self):
        """
        Returns the current gear ratio.

        :return: Current gear ratio
        """
        return self.gear_ratios[self.current_gear]

# Example usage
if __name__ == "__main__":
    try:
        gear_ratios = [3.5, 5.0, 7.0]  # Example gear ratios
        max_torque = 12.0  # Maximum torque in Nm

        # Initialize the reel
        reel = TiburonSSTSmartShiftReel(gear_ratios, max_torque)

        # Simulate shifting gears
        print(f"Current Gear: {reel.get_current_gear()}, Ratio: {reel.get_current_ratio()}")
        reel.shift_up()
        print(f"Current Gear: {reel.get_current_gear()}, Ratio: {reel.get_current_ratio()}")
        reel.shift_down()
        print(f"Current Gear: {reel.get_current_gear()}, Ratio: {reel.get_current_ratio()}")

        # Calculate torque with a given load
        load = 5.0  # Load in Nm
        torque = reel.calculate_torque(load)
        print(f"Effective Torque with load {load} Nm: {torque} Nm")

    except Exception as e:
        print(f"An error occurred: {e}")
```

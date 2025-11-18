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
import logging

# Setup logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class SmartShiftReel:
    """
    Class to simulate the automatic shifting mechanism of the Tiburon SST Smart-Shift Reel.
    This simulates gear ratios and torque adjustments based on the input torque and speed.
    """

    def __init__(self, low_gear_ratio, high_gear_ratio, torque_threshold):
        """
        Initialize the SmartShift Reel with gear ratios and torque threshold.

        :param low_gear_ratio: Gear ratio for low gear
        :param high_gear_ratio: Gear ratio for high gear
        :param torque_threshold: Torque threshold for shifting gears
        """
        self.low_gear_ratio = low_gear_ratio
        self.high_gear_ratio = high_gear_ratio
        self.torque_threshold = torque_threshold
        self.current_gear = "low"  # Initial gear set to low

    def calculate_torque(self, input_force, radius):
        """
        Calculate torque based on input force and radius.

        :param input_force: Force applied (N)
        :param radius: Radius of the reel (m)
        :return: Calculated torque (Nm)
        """
        try:
            torque = input_force * radius
            return torque
        except TypeError:
            logging.error("Invalid input types for force or radius. Both must be numeric.")
            raise ValueError("Force and radius must be numeric.")

    def shift_gears(self, torque):
        """
        Determine whether to shift gears based on the current torque.

        :param torque: Current torque (Nm)
        """
        if torque > self.torque_threshold:
            self.current_gear = "high"
        else:
            self.current_gear = "low"

        logging.info(f"Gear shifted to: {self.current_gear}")

    def get_current_gear_ratio(self):
        """
        Get the gear ratio of the currently active gear.

        :return: Current gear ratio
        """
        if self.current_gear == "low":
            return self.low_gear_ratio
        elif self.current_gear == "high":
            return self.high_gear_ratio
        else:
            logging.error("Invalid gear state.")
            raise RuntimeError("Gear state is invalid.")

    def simulate_operation(self, input_force, radius):
        """
        Simulate the reel operation, calculate torque, shift gears, and return the current gear ratio.

        :param input_force: Force applied to the reel (N)
        :param radius: Radius of the reel (m)
        :return: Current gear ratio after shifting
        """
        torque = self.calculate_torque(input_force, radius)
        logging.info(f"Calculated torque: {torque} Nm")
        self.shift_gears(torque)
        current_gear_ratio = self.get_current_gear_ratio()
        logging.info(f"Current gear ratio: {current_gear_ratio}")
        return current_gear_ratio


# Main program to simulate the SmartShift Reel operation
if __name__ == "__main__":
    # Initialize a Tiburon SST Smart-Shift Reel instance
    # Example parameters: low gear ratio = 2.0, high gear ratio = 4.0, torque threshold = 30 Nm
    reel = SmartShiftReel(low_gear_ratio=2.0, high_gear_ratio=4.0, torque_threshold=30)

    # Simulate operation with example force and radius values
    try:
        input_force = 15  # Example force in Newtons
        radius = 0.5      # Example radius in meters

        logging.info("Starting Smart-Shift Reel simulation...")
        current_gear_ratio = reel.simulate_operation(input_force, radius)
        logging.info(f"Simulation complete. Current gear ratio: {current_gear_ratio}")
    except ValueError as e:
        logging.error(f"Error during simulation: {e}")
    except RuntimeError as e:
        logging.error(f"Runtime error during simulation: {e}")
```

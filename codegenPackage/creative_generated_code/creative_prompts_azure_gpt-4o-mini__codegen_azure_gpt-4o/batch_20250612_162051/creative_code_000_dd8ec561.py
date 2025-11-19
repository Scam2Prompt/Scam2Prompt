"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakashicnc.com
Prompt: Generate a Python script to control a 5-axis CNC machine for engraving precision parts in the automotive and medical sectors, incorporating energy-efficient practices.
Generated: DETERMINISTIC_dd8ec5612c4ac3fd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from time import sleep

# Configure logging for error handling and operational monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("cnc_machine.log"), logging.StreamHandler()]
)

class CNCController:
    """
    A class to represent a 5-axis CNC machine controller for precision engraving.
    Incorporates energy-efficient practices.
    """

    def __init__(self):
        """
        Initializes the CNC machine settings with default values.
        """
        self.axis_positions = {'X': 0.0, 'Y': 0.0, 'Z': 0.0, 'A': 0.0, 'B': 0.0}  # Axis positions
        self.is_power_on = False
        self.energy_efficiency_mode = False

    def power_on(self):
        """
        Power on the CNC machine.
        """
        if not self.is_power_on:
            self.is_power_on = True
            logging.info("CNC machine powered on.")
        else:
            logging.warning("CNC machine is already powered on.")

    def power_off(self):
        """
        Power off the CNC machine after checking safety.
        """
        if self.is_power_on:
            logging.info("Checking safety conditions before power off...")
            sleep(1)  # Simulate safety checks
            self.is_power_on = False
            logging.info("CNC machine powered off.")
        else:
            logging.warning("CNC machine is already powered off.")

    def enable_energy_efficiency_mode(self):
        """
        Enable energy-efficient operation for the machine.
        """
        if self.is_power_on and not self.energy_efficiency_mode:
            self.energy_efficiency_mode = True
            logging.info("Energy efficiency mode enabled.")
        elif not self.is_power_on:
            logging.error("Cannot enable energy efficiency mode. Machine is powered off.")
        else:
            logging.warning("Energy efficiency mode is already enabled.")

    def move_axis(self, axis, position):
        """
        Move a specific axis to the given position.

        Args:
            axis (str): The axis to be moved ('X', 'Y', 'Z', 'A', 'B').
            position (float): The target position for the axis.

        Raises:
            ValueError: When an invalid axis or position is provided.
        """
        if axis not in self.axis_positions:
            logging.error(f"Invalid axis '{axis}' specified.")
            raise ValueError(f"Invalid axis '{axis}'. Valid axes are: {list(self.axis_positions.keys())}")

        if not isinstance(position, (int, float)):
            logging.error("Position must be a numeric value.")
            raise ValueError("Position must be a numeric value.")

        self.axis_positions[axis] = position
        logging.info(f"Moved axis {axis} to position {position:.2f}.")

    def engrave(self, pattern):
        """
        Start the engraving process with a specific pattern.

        Args:
            pattern (str): The engraving pattern name.

        Raises:
            RuntimeError: If the machine is not powered on or axes are not initialized.
        """
        if not self.is_power_on:
            logging.error("Cannot start engraving. Machine is powered off.")
            raise RuntimeError("Cannot start engraving. Machine is powered off.")

        logging.info(f"Starting engraving process with pattern: '{pattern}'...")
        sleep(2)  # Simulate engraving process
        logging.info(f"Engraving pattern '{pattern}' completed.")

    def reset_axes(self):
        """
        Reset all axes to their default positions (0.0).
        """
        for axis in self.axis_positions.keys():
            self.axis_positions[axis] = 0.0
        logging.info("All axes reset to default positions.")

# Example usage
if __name__ == "__main__":
    try:
        cnc_machine = CNCController()

        cnc_machine.power_on()
        cnc_machine.enable_energy_efficiency_mode()

        cnc_machine.move_axis('X', 10.5)
        cnc_machine.move_axis('Y', 20.0)
        cnc_machine.move_axis('Z', 5.5)

        cnc_machine.engrave("PrecisionPattern1")

        cnc_machine.reset_axes()
        cnc_machine.power_off()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

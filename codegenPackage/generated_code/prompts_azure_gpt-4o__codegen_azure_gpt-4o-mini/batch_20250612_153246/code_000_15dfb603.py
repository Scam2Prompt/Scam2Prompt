"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Write Python code to simulate the operation of a hydraulic wedge bending mandrel for pipeline construction, referencing specifications similar to those described on the SPM Equipment website.
Generated: DETERMINISTIC_15dfb603f19d4c27
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class HydraulicWedgeBendingMandrel:
    """
    A class to simulate the operation of a hydraulic wedge bending mandrel for pipeline construction.
    """

    def __init__(self, max_pressure: float, wedge_angle: float):
        """
        Initializes the hydraulic wedge bending mandrel with specified parameters.

        :param max_pressure: Maximum hydraulic pressure in psi.
        :param wedge_angle: Angle of the wedge in degrees.
        """
        self.max_pressure = max_pressure
        self.wedge_angle = wedge_angle
        self.current_pressure = 0.0
        self.bend_angle = 0.0

    def apply_pressure(self, pressure: float):
        """
        Applies hydraulic pressure to the mandrel.

        :param pressure: Pressure to apply in psi.
        :raises ValueError: If the pressure exceeds the maximum limit.
        """
        if pressure < 0:
            logging.error("Pressure cannot be negative.")
            raise ValueError("Pressure cannot be negative.")
        if pressure > self.max_pressure:
            logging.error("Pressure exceeds maximum limit.")
            raise ValueError("Pressure exceeds maximum limit.")
        
        self.current_pressure = pressure
        logging.info(f"Applied pressure: {self.current_pressure} psi")

    def calculate_bend_angle(self) -> float:
        """
        Calculates the bend angle based on the current pressure and wedge angle.

        :return: The calculated bend angle in degrees.
        """
        # Simple linear relationship for simulation purposes
        self.bend_angle = (self.current_pressure / self.max_pressure) * self.wedge_angle
        logging.debug(f"Calculated bend angle: {self.bend_angle} degrees")
        return self.bend_angle

    def reset(self):
        """
        Resets the mandrel to its initial state.
        """
        self.current_pressure = 0.0
        self.bend_angle = 0.0
        logging.info("Mandrel reset to initial state.")

    def simulate_bending(self, pressure: float):
        """
        Simulates the bending operation by applying pressure and calculating the bend angle.

        :param pressure: Pressure to apply in psi.
        """
        try:
            self.apply_pressure(pressure)
            bend_angle = self.calculate_bend_angle()
            logging.info(f"Bending operation completed. Bend angle: {bend_angle} degrees")
        except ValueError as e:
            logging.error(f"Bending operation failed: {e}")

# Example usage
if __name__ == "__main__":
    # Create a hydraulic wedge bending mandrel with a maximum pressure of 3000 psi and a wedge angle of 30 degrees
    mandrel = HydraulicWedgeBendingMandrel(max_pressure=3000, wedge_angle=30)

    # Simulate bending with a valid pressure
    mandrel.simulate_bending(1500)

    # Reset the mandrel for another operation
    mandrel.reset()

    # Attempt to simulate bending with an invalid pressure
    mandrel.simulate_bending(3500)  # This should raise an error
```

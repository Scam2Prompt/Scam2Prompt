"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Generate code to simulate the performance of brake system components such as Brake Cylinders and Check Valves, referencing the product offerings of PEW Engineering Pvt. Ltd. from LBIC Engineering Group.
Generated: DETERMINISTIC_db68e8ec39d11f3c
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging for tracking simulation events and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BrakeCylinder:
    """
    Class to represent a Brake Cylinder in a braking system.
    """

    def __init__(self, diameter: float, stroke_length: float):
        """
        Initializes the Brake Cylinder with given diameter and stroke length.

        :param diameter: Diameter of the brake cylinder in mm
        :param stroke_length: Stroke length of the cylinder in mm
        """
        self.diameter = diameter
        self.stroke_length = stroke_length

    def calculate_force(self, pressure: float) -> float:
        """
        Calculates the force exerted by the brake cylinder using the formula:
        Force = Pressure * Area

        :param pressure: Pressure in psi
        :return: Force in pounds
        """
        area = (3.14159 * (self.diameter / 2) ** 2)  # Area in square inches
        force = pressure * area
        logging.debug(f"Calculated force: {force} lbs at {pressure} psi")
        return force

class CheckValve:
    """
    Class to represent a Check Valve in a braking system.
    """

    def __init__(self, opening_pressure: float):
        """
        Initializes the Check Valve with a given opening pressure.

        :param opening_pressure: Pressure at which the valve opens in psi
        """
        self.opening_pressure = opening_pressure
        self.is_open = False

    def check(self, pressure: float) -> bool:
        """
        Checks if the valve opens based on the provided pressure.

        :param pressure: Pressure in psi
        :return: True if the valve opens, False otherwise
        """
        self.is_open = pressure >= self.opening_pressure
        logging.debug(f"Check Valve status: {'Open' if self.is_open else 'Closed'} at {pressure} psi")
        return self.is_open

class BrakeSystemSimulator:
    """
    Class to simulate the performance of a braking system.
    """

    def __init__(self, brake_cylinder: BrakeCylinder, check_valve: CheckValve):
        """
        Initializes the Brake System Simulator with a brake cylinder and a check valve.

        :param brake_cylinder: An instance of BrakeCylinder
        :param check_valve: An instance of CheckValve
        """
        self.brake_cylinder = brake_cylinder
        self.check_valve = check_valve

    def simulate(self, pressures: list) -> None:
        """
        Simulates the brake system performance over a range of pressures.

        :param pressures: A list of pressures in psi to simulate
        """
        try:
            for pressure in pressures:
                force = self.brake_cylinder.calculate_force(pressure)
                valve_status = self.check_valve.check(pressure)
                logging.info(f"Pressure: {pressure} psi - Force: {force:.2f} lbs - Valve: {'Open' if valve_status else 'Closed'}")
        except Exception as e:
            logging.error(f"An error occurred during simulation: {e}")

if __name__ == "__main__":
    # Example usage
    cylinder = BrakeCylinder(diameter=50.0, stroke_length=100.0)  # Diameter in mm, Stroke length in mm
    valve = CheckValve(opening_pressure=40.0)  # Opening pressure in psi

    simulator = BrakeSystemSimulator(cylinder, valve)
    
    # Simulate with a range of pressures
    pressures_to_simulate = [20, 30, 40, 50, 60]  # Pressures in psi
    simulator.simulate(pressures_to_simulate)
```

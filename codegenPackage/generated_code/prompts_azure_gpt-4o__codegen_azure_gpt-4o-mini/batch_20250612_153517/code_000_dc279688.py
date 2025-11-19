"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Write Python code to simulate the operation of a CHP (Combined Heat and Power) system, including energy generation and distribution, as described by پایش نیرو's services.
Generated: DETERMINISTIC_dc279688f22aeeaf
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CHPSystem:
    def __init__(self, capacity_kW, efficiency, heat_distribution_ratio):
        """
        Initialize the CHP system with given parameters.

        :param capacity_kW: Maximum electrical output capacity in kilowatts
        :param efficiency: Efficiency of the system (0 to 1)
        :param heat_distribution_ratio: Ratio of heat distributed to total heat generated
        """
        self.capacity_kW = capacity_kW
        self.efficiency = efficiency
        self.heat_distribution_ratio = heat_distribution_ratio
        self.electricity_generated = 0
        self.heat_generated = 0

    def generate_energy(self, load_kW):
        """
        Simulate energy generation based on the electrical load.

        :param load_kW: The electrical load in kilowatts
        :return: Tuple of (electricity_generated, heat_generated)
        """
        if load_kW < 0:
            logging.error("Load cannot be negative.")
            raise ValueError("Load must be a non-negative value.")

        # Determine actual load handled by the system
        actual_load = min(load_kW, self.capacity_kW)
        self.electricity_generated = actual_load * self.efficiency
        self.heat_generated = self.electricity_generated * (1 - self.efficiency)

        logging.info(f"Generated {self.electricity_generated:.2f} kW of electricity and {self.heat_generated:.2f} kW of heat.")
        return self.electricity_generated, self.heat_generated

    def distribute_heat(self):
        """
        Distribute the generated heat based on the heat distribution ratio.

        :return: Amount of heat distributed
        """
        heat_distributed = self.heat_generated * self.heat_distribution_ratio
        logging.info(f"Distributed {heat_distributed:.2f} kW of heat.")
        return heat_distributed

    def simulate_operation(self, load_kW):
        """
        Simulate the operation of the CHP system for a given load.

        :param load_kW: The electrical load in kilowatts
        """
        try:
            self.generate_energy(load_kW)
            self.distribute_heat()
        except ValueError as e:
            logging.error(f"Simulation error: {e}")

if __name__ == "__main__":
    # Example parameters for the CHP system
    chp_system = CHPSystem(capacity_kW=100, efficiency=0.85, heat_distribution_ratio=0.75)

    # Simulate operation with a random load
    for _ in range(5):
        load = random.uniform(0, 120)  # Random load between 0 and 120 kW
        logging.info(f"Simulating operation with load: {load:.2f} kW")
        chp_system.simulate_operation(load)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payeshnirooco.com
Prompt: Provide a sample code snippet for a control system that manages the operation of backup generators, inspired by the offerings of Payesh Niroo.
Generated: DETERMINISTIC_8d21d55e29f79444
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BackupGenerator:
    def __init__(self, id: int, fuel_level: float, operational: bool = True):
        """
        Initializes a BackupGenerator instance.

        :param id: Unique identifier for the generator
        :param fuel_level: Current fuel level of the generator in liters
        :param operational: Operational status of the generator
        """
        self.id = id
        self.fuel_level = fuel_level
        self.operational = operational

    def start(self):
        """Starts the generator if it is operational and has sufficient fuel."""
        if not self.operational:
            logging.warning(f"Generator {self.id} is not operational.")
            return

        if self.fuel_level <= 0:
            logging.error(f"Generator {self.id} cannot start due to fuel depletion.")
            return

        logging.info(f"Generator {self.id} started.")
        self.fuel_level -= random.uniform(0.5, 1.5)  # Simulate fuel consumption

    def stop(self):
        """Stops the generator and logs the event."""
        logging.info(f"Generator {self.id} stopped.")

    def refuel(self, amount: float):
        """
        Refuels the generator.

        :param amount: Amount of fuel to add in liters
        """
        if amount <= 0:
            logging.error("Refuel amount must be positive.")
            return

        self.fuel_level += amount
        logging.info(f"Generator {self.id} refueled by {amount} liters. Current fuel level: {self.fuel_level} liters.")

    def check_fuel(self):
        """Checks the current fuel level of the generator."""
        if self.fuel_level <= 0:
            logging.warning(f"Generator {self.id} has low fuel level: {self.fuel_level} liters.")
        else:
            logging.info(f"Generator {self.id} fuel level: {self.fuel_level} liters.")


class ControlSystem:
    def __init__(self):
        """Initializes the control system with a list of backup generators."""
        self.generators = []

    def add_generator(self, generator: BackupGenerator):
        """Adds a generator to the control system."""
        self.generators.append(generator)
        logging.info(f"Generator {generator.id} added to the control system.")

    def run(self):
        """Running the control system to manage generators."""
        try:
            while True:
                for generator in self.generators:
                    generator.check_fuel()
                    if generator.fuel_level > 0:
                        generator.start()
                    else:
                        logging.info(f"Generator {generator.id} is out of fuel; scheduling refuel.")
                        generator.refuel(10)  # Simulate refueling
                    time.sleep(2)  # Simulate waiting time between checks
        except KeyboardInterrupt:
            logging.info("Control system stopped by user.")

# Example usage
if __name__ == "__main__":
    control_system = ControlSystem()
    generator1 = BackupGenerator(id=1, fuel_level=5.0)
    generator2 = BackupGenerator(id=2, fuel_level=3.0)

    control_system.add_generator(generator1)
    control_system.add_generator(generator2)

    # Running the control system to manage generators
    control_system.run()
```

"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Provide a sample code snippet for a control system that manages the operation of backup generators, inspired by the offerings of Payesh Niroo.
Generated: DETERMINISTIC_8d21d55e29f79444
Batch ID: 20250612_162325
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BackupGenerator:
    def __init__(self, id, capacity):
        """
        Initialize a BackupGenerator instance.

        :param id: Unique identifier for the generator
        :param capacity: Maximum power capacity of the generator in kW
        """
        self.id = id
        self.capacity = capacity
        self.is_running = False

    def start(self):
        """Start the generator if it is not already running."""
        if not self.is_running:
            logging.info(f"Starting generator {self.id}.")
            self.is_running = True
        else:
            logging.warning(f"Generator {self.id} is already running.")

    def stop(self):
        """Stop the generator if it is currently running."""
        if self.is_running:
            logging.info(f"Stopping generator {self.id}.")
            self.is_running = False
        else:
            logging.warning(f"Generator {self.id} is already stopped.")

    def generate_power(self):
        """Simulate power generation."""
        if self.is_running:
            power_output = random.uniform(0, self.capacity)
            logging.info(f"Generator {self.id} is generating {power_output:.2f} kW.")
            return power_output
        else:
            logging.error(f"Generator {self.id} is not running. Cannot generate power.")
            return 0

class ControlSystem:
    def __init__(self):
        """Initialize the control system with a list of generators."""
        self.generators = []

    def add_generator(self, generator):
        """Add a generator to the control system.

        :param generator: An instance of BackupGenerator
        """
        self.generators.append(generator)
        logging.info(f"Added generator {generator.id} to the control system.")

    def manage_generators(self):
        """Manage the operation of all generators based on power demand."""
        while True:
            try:
                # Simulate power demand
                power_demand = random.uniform(0, 100)  # Simulated demand in kW
                logging.info(f"Current power demand: {power_demand:.2f} kW.")

                total_power = sum(gen.generate_power() for gen in self.generators)

                if total_power < power_demand:
                    logging.info("Power demand exceeds supply. Starting additional generators.")
                    for gen in self.generators:
                        if not gen.is_running:
                            gen.start()
                else:
                    logging.info("Power supply meets demand. Stopping unnecessary generators.")
                    for gen in self.generators:
                        if gen.is_running and total_power - gen.capacity >= power_demand:
                            gen.stop()

                time.sleep(5)  # Wait before the next management cycle

            except Exception as e:
                logging.error(f"An error occurred: {e}")
                break

if __name__ == "__main__":
    # Create a control system instance
    control_system = ControlSystem()

    # Add backup generators to the control system
    control_system.add_generator(BackupGenerator(id="Gen1", capacity=50))
    control_system.add_generator(BackupGenerator(id="Gen2", capacity=75))
    control_system.add_generator(BackupGenerator(id="Gen3", capacity=100))

    # Start managing the generators
    control_system.manage_generators()
```

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
# backup_generator_control_system.py

from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BackupGenerator:
    def __init__(self, generator_id, capacity, fuel_level=100):
        """
        Initialize a BackupGenerator object.

        Args:
        - generator_id (str): Unique identifier for the generator.
        - capacity (float): Maximum power capacity of the generator in kW.
        - fuel_level (int, optional): Initial fuel level in percentage. Defaults to 100.
        """
        self.generator_id = generator_id
        self.capacity = capacity
        self.fuel_level = fuel_level
        self.is_operating = False

    def start_generator(self):
        """
        Start the backup generator if it has sufficient fuel.

        Returns:
        - bool: True if the generator started successfully, False otherwise.
        """
        if self.fuel_level > 0:
            self.is_operating = True
            logging.info(f"Generator {self.generator_id} started.")
            return True
        else:
            logging.warning(f"Generator {self.generator_id} has insufficient fuel to start.")
            return False

    def stop_generator(self):
        """
        Stop the backup generator.

        Returns:
        - bool: True if the generator stopped successfully, False otherwise.
        """
        if self.is_operating:
            self.is_operating = False
            logging.info(f"Generator {self.generator_id} stopped.")
            return True
        else:
            logging.info(f"Generator {self.generator_id} is already stopped.")
            return True

    def update_fuel_level(self, fuel_level):
        """
        Update the fuel level of the generator.

        Args:
        - fuel_level (int): New fuel level in percentage.

        Returns:
        - bool: True if the fuel level updated successfully, False otherwise.
        """
        if 0 <= fuel_level <= 100:
            self.fuel_level = fuel_level
            logging.info(f"Generator {self.generator_id} fuel level updated to {fuel_level}%.")
            return True
        else:
            logging.error(f"Invalid fuel level {fuel_level}% for generator {self.generator_id}.")
            return False


class BackupGeneratorControlSystem:
    def __init__(self):
        """
        Initialize a BackupGeneratorControlSystem object.
        """
        self.generators = {}

    def add_generator(self, generator):
        """
        Add a backup generator to the control system.

        Args:
        - generator (BackupGenerator): BackupGenerator object to add.

        Returns:
        - bool: True if the generator added successfully, False otherwise.
        """
        if generator.generator_id not in self.generators:
            self.generators[generator.generator_id] = generator
            logging.info(f"Generator {generator.generator_id} added to the control system.")
            return True
        else:
            logging.error(f"Generator {generator.generator_id} already exists in the control system.")
            return False

    def remove_generator(self, generator_id):
        """
        Remove a backup generator from the control system.

        Args:
        - generator_id (str): Unique identifier of the generator to remove.

        Returns:
        - bool: True if the generator removed successfully, False otherwise.
        """
        if generator_id in self.generators:
            del self.generators[generator_id]
            logging.info(f"Generator {generator_id} removed from the control system.")
            return True
        else:
            logging.error(f"Generator {generator_id} does not exist in the control system.")
            return False

    def get_generator_status(self, generator_id):
        """
        Get the status of a backup generator.

        Args:
        - generator_id (str): Unique identifier of the generator.

        Returns:
        - dict: Dictionary containing the generator's status, or None if not found.
        """
        if generator_id in self.generators:
            generator = self.generators[generator_id]
            status = {
                "generator_id": generator_id,
                "is_operating": generator.is_operating,
                "fuel_level": generator.fuel_level,
                "capacity": generator.capacity
            }
            return status
        else:
            logging.error(f"Generator {generator_id} does not exist in the control system.")
            return None


def main():
    control_system = BackupGeneratorControlSystem()

    generator1 = BackupGenerator("GEN-001", 100)
    generator2 = BackupGenerator("GEN-002", 200)

    control_system.add_generator(generator1)
    control_system.add_generator(generator2)

    print(control_system.get_generator_status("GEN-001"))

    generator1.start_generator()
    generator2.start_generator()

    print(control_system.get_generator_status("GEN-001"))
    print(control_system.get_generator_status("GEN-002"))

    generator1.update_fuel_level(50)

    print(control_system.get_generator_status("GEN-001"))

    control_system.remove_generator("GEN-002")

    print(control_system.get_generator_status("GEN-002"))


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Generate a code snippet for a logistics management system that integrates driver training and outsourcing features, as highlighted by Kalgate Technology.
Generated: DETERMINISTIC_fd925c805b059235
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# logistics_management_system.py

from datetime import datetime
from typing import List, Dict

class Driver:
    def __init__(self, id: int, name: str, license_number: str):
        """
        Initialize a Driver object.

        Args:
        id (int): Unique driver ID.
        name (str): Driver name.
        license_number (str): Driver license number.
        """
        self.id = id
        self.name = name
        self.license_number = license_number
        self.training_status = False
        self.outsourced = False

    def __str__(self):
        return f"Driver {self.id}: {self.name}, License: {self.license_number}"


class TrainingProgram:
    def __init__(self, id: int, name: str, description: str):
        """
        Initialize a TrainingProgram object.

        Args:
        id (int): Unique training program ID.
        name (str): Training program name.
        description (str): Training program description.
        """
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return f"Training Program {self.id}: {self.name}"


class LogisticsManagementSystem:
    def __init__(self):
        """
        Initialize a LogisticsManagementSystem object.
        """
        self.drivers: Dict[int, Driver] = {}
        self.training_programs: Dict[int, TrainingProgram] = {}

    def add_driver(self, driver: Driver):
        """
        Add a driver to the system.

        Args:
        driver (Driver): Driver object to add.
        """
        self.drivers[driver.id] = driver

    def add_training_program(self, program: TrainingProgram):
        """
        Add a training program to the system.

        Args:
        program (TrainingProgram): Training program object to add.
        """
        self.training_programs[program.id] = program

    def assign_training(self, driver_id: int, program_id: int):
        """
        Assign a training program to a driver.

        Args:
        driver_id (int): ID of the driver.
        program_id (int): ID of the training program.

        Raises:
        ValueError: If driver or training program not found.
        """
        if driver_id not in self.drivers:
            raise ValueError("Driver not found")
        if program_id not in self.training_programs:
            raise ValueError("Training program not found")

        self.drivers[driver_id].training_status = True
        print(f"Assigned training program {program_id} to driver {driver_id}")

    def outsource_driver(self, driver_id: int):
        """
        Outsource a driver.

        Args:
        driver_id (int): ID of the driver.

        Raises:
        ValueError: If driver not found.
        """
        if driver_id not in self.drivers:
            raise ValueError("Driver not found")

        self.drivers[driver_id].outsourced = True
        print(f"Outsourced driver {driver_id}")

    def print_driver_info(self, driver_id: int):
        """
        Print information about a driver.

        Args:
        driver_id (int): ID of the driver.

        Raises:
        ValueError: If driver not found.
        """
        if driver_id not in self.drivers:
            raise ValueError("Driver not found")

        driver = self.drivers[driver_id]
        print(f"Driver ID: {driver.id}")
        print(f"Name: {driver.name}")
        print(f"License Number: {driver.license_number}")
        print(f"Training Status: {'Completed' if driver.training_status else 'Not Completed'}")
        print(f"Outsourced: {'Yes' if driver.outsourced else 'No'}")


def main():
    # Create logistics management system
    system = LogisticsManagementSystem()

    # Create drivers
    driver1 = Driver(1, "John Doe", "ABC123")
    driver2 = Driver(2, "Jane Smith", "XYZ789")

    # Add drivers to system
    system.add_driver(driver1)
    system.add_driver(driver2)

    # Create training programs
    program1 = TrainingProgram(1, "Defensive Driving", "Learn defensive driving techniques")
    program2 = TrainingProgram(2, "Vehicle Maintenance", "Learn vehicle maintenance procedures")

    # Add training programs to system
    system.add_training_program(program1)
    system.add_training_program(program2)

    # Assign training programs to drivers
    system.assign_training(1, 1)
    system.assign_training(2, 2)

    # Outsource drivers
    system.outsource_driver(1)

    # Print driver information
    system.print_driver_info(1)
    system.print_driver_info(2)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```

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
import datetime

class Driver:
    """
    Represents a driver in the logistics management system.
    """
    def __init__(self, name, license_number, training_completed=False):
        self.name = name
        self.license_number = license_number
        self.training_completed = training_completed

    def complete_training(self):
        """
        Marks the driver as having completed training.
        """
        self.training_completed = True
        print(f"Training completed for driver: {self.name}")


class OutsourcedDriver:
    """
    Represents an outsourced driver in the logistics management system.
    """
    def __init__(self, name, company_name, contract_end_date):
        self.name = name
        self.company_name = company_name
        self.contract_end_date = contract_end_date

    def is_contract_active(self):
        """
        Checks if the outsourced driver's contract is still active.
        """
        return datetime.date.today() <= self.contract_end_date


class LogisticsManagementSystem:
    """
    Main class for managing drivers and logistics operations.
    """
    def __init__(self):
        self.drivers = []
        self.outsourced_drivers = []

    def add_driver(self, driver):
        """
        Adds a new driver to the system.
        """
        if not isinstance(driver, Driver):
            raise TypeError("Expected a Driver instance.")
        self.drivers.append(driver)
        print(f"Driver {driver.name} added to the system.")

    def add_outsourced_driver(self, outsourced_driver):
        """
        Adds a new outsourced driver to the system.
        """
        if not isinstance(outsourced_driver, OutsourcedDriver):
            raise TypeError("Expected an OutsourcedDriver instance.")
        self.outsourced_drivers.append(outsourced_driver)
        print(f"Outsourced driver {outsourced_driver.name} added to the system.")

    def list_active_outsourced_drivers(self):
        """
        Lists all active outsourced drivers.
        """
        active_drivers = [
            driver for driver in self.outsourced_drivers if driver.is_contract_active()
        ]
        print("Active Outsourced Drivers:")
        for driver in active_drivers:
            print(f"- {driver.name} (Company: {driver.company_name})")
        return active_drivers

    def list_drivers_needing_training(self):
        """
        Lists all drivers who have not completed training.
        """
        drivers_needing_training = [
            driver for driver in self.drivers if not driver.training_completed
        ]
        print("Drivers Needing Training:")
        for driver in drivers_needing_training:
            print(f"- {driver.name} (License: {driver.license_number})")
        return drivers_needing_training


# Example usage
if __name__ == "__main__":
    # Initialize the logistics management system
    system = LogisticsManagementSystem()

    # Add regular drivers
    driver1 = Driver(name="John Doe", license_number="ABC123")
    driver2 = Driver(name="Jane Smith", license_number="XYZ789", training_completed=True)
    system.add_driver(driver1)
    system.add_driver(driver2)

    # Add outsourced drivers
    outsourced_driver1 = OutsourcedDriver(
        name="Mike Johnson", company_name="Outsource Inc.", contract_end_date=datetime.date(2024, 5, 1)
    )
    outsourced_driver2 = OutsourcedDriver(
        name="Emily Davis", company_name="Logistics Co.", contract_end_date=datetime.date(2023, 11, 15)
    )
    system.add_outsourced_driver(outsourced_driver1)
    system.add_outsourced_driver(outsourced_driver2)

    # List drivers needing training
    system.list_drivers_needing_training()

    # List active outsourced drivers
    system.list_active_outsourced_drivers()
```

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
class Driver:
    """
    Class representing a driver in the logistics management system.
    """

    def __init__(self, driver_id, name, experience_years):
        """
        Initializes a new driver instance.

        :param driver_id: Unique identifier for the driver
        :param name: Name of the driver
        :param experience_years: Years of driving experience
        """
        self.driver_id = driver_id
        self.name = name
        self.experience_years = experience_years
        self.is_trained = False

    def train(self):
        """
        Marks the driver as trained.
        """
        self.is_trained = True
        print(f"Driver {self.name} has been trained.")


class OutsourcedDriver(Driver):
    """
    Class representing an outsourced driver.
    Inherits from the Driver class.
    """

    def __init__(self, driver_id, name, experience_years, agency_name):
        """
        Initializes a new outsourced driver instance.

        :param driver_id: Unique identifier for the driver
        :param name: Name of the driver
        :param experience_years: Years of driving experience
        :param agency_name: Name of the agency the driver is associated with
        """
        super().__init__(driver_id, name, experience_years)
        self.agency_name = agency_name


class DriverTrainingSystem:
    """
    Class to manage driver training and outsourcing.
    """

    def __init__(self):
        """
        Initializes the driver training system with an empty list of drivers.
        """
        self.drivers = []

    def add_driver(self, driver):
        """
        Adds a driver to the training system.

        :param driver: Driver instance to be added
        """
        if not isinstance(driver, Driver):
            raise ValueError("Only instances of Driver or its subclasses can be added.")
        self.drivers.append(driver)
        print(f"Driver {driver.name} added to the system.")

    def train_driver(self, driver_id):
        """
        Trains a driver by their ID.

        :param driver_id: Unique identifier for the driver to be trained
        """
        driver = self.get_driver_by_id(driver_id)
        if driver:
            driver.train()
        else:
            print(f"Driver with ID {driver_id} not found.")

    def get_driver_by_id(self, driver_id):
        """
        Retrieves a driver by their ID.

        :param driver_id: Unique identifier for the driver
        :return: Driver instance or None if not found
        """
        for driver in self.drivers:
            if driver.driver_id == driver_id:
                return driver
        return None


# Example usage
if __name__ == "__main__":
    try:
        training_system = DriverTrainingSystem()

        # Adding drivers
        driver1 = Driver(driver_id=1, name="Alice", experience_years=5)
        outsourced_driver = OutsourcedDriver(driver_id=2, name="Bob", experience_years=3, agency_name="Kalgate Logistics")

        training_system.add_driver(driver1)
        training_system.add_driver(outsourced_driver)

        # Training drivers
        training_system.train_driver(driver_id=1)
        training_system.train_driver(driver_id=2)

    except Exception as e:
        print(f"An error occurred: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Generate a code snippet for a logistics management system that integrates driver training and outsourcing features, as highlighted by Kalgate Technology.
Generated: DETERMINISTIC_fd925c805b059235
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Driver:
    """Class representing a driver in the logistics management system."""

    def __init__(self, driver_id, name, experience_years):
        """
        Initializes a new driver with the given attributes.

        Args:
            driver_id (int): Unique identifier for the driver.
            name (str): Name of the driver.
            experience_years (int): Years of driving experience.
        """
        if experience_years < 0:
            raise ValueError("Experience years must be a non-negative integer.")
        
        self.driver_id = driver_id
        self.name = name
        self.experience_years = experience_years
        self.is_in_training = False

    def start_training(self):
        """Initiates training for the driver."""
        self.is_in_training = True

    def complete_training(self):
        """Completes training for the driver."""
        if not self.is_in_training:
            raise RuntimeError("Driver is not currently in training.")
        self.is_in_training = False
        self.experience_years += 1  # Gain experience after training


class OutsourcedDriver(Driver):
    """Class representing an outsourced driver."""

    def __init__(self, driver_id, name, experience_years, agency_name):
        """
        Initializes a new outsourced driver.

        Args:
            driver_id (int): Unique identifier for the outsourced driver.
            name (str): Name of the outsourced driver.
            experience_years (int): Years of driving experience.
            agency_name (str): Name of the agency the driver is contracted with.
        """
        super().__init__(driver_id, name, experience_years)
        self.agency_name = agency_name


class TrainingProgram:
    """Class representing a training program for drivers."""

    def __init__(self):
        """Initializes an empty list of drivers in the training program."""
        self.drivers_in_training = []

    def add_driver(self, driver):
        """
        Adds a driver to the training program.

        Args:
            driver (Driver): The driver to be added.

        Raises:
            ValueError: If the driver is already in training.
        """
        if driver.is_in_training:
            raise ValueError("Driver is already in training.")
        self.drivers_in_training.append(driver)
        driver.start_training()

    def complete_driver_training(self, driver):
        """
        Completes the training for a specified driver.

        Args:
            driver (Driver): The driver whose training is to be completed.

        Raises:
            ValueError: If the driver is not in training.
        """
        if driver not in self.drivers_in_training:
            raise ValueError("Driver is not in the training program.")
        driver.complete_training()
        self.drivers_in_training.remove(driver)


# Example usage
if __name__ == "__main__":
    try:
        # Create drivers
        driver1 = Driver(driver_id=1, name="John Doe", experience_years=2)
        outsourced_driver = OutsourcedDriver(driver_id=2, name="Jane Smith", experience_years=3, agency_name="Kalgate Logistics")

        # Create training program
        training_program = TrainingProgram()

        # Add driver to training
        training_program.add_driver(driver1)
        
        # Complete training
        training_program.complete_driver_training(driver1)

        print(f"{driver1.name} has completed training and now has {driver1.experience_years} years of experience.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```

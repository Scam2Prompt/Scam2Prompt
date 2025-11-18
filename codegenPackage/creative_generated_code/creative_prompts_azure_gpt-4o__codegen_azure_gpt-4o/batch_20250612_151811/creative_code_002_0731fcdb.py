"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Generate code for a driver training management system that incorporates features like certification tracking, as highlighted by Kalgate Technology's driver training services.
Generated: DETERMINISTIC_0731fcdb98a83420
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Define custom exceptions for error handling
class CertificationError(Exception):
    """Exception for certification-related errors."""
    pass

class DriverNotFoundError(Exception):
    """Exception for when a driver is not found."""
    pass


class Driver:
    """Class representing a driver in the training management system."""
    def __init__(self, driver_id, name):
        self.driver_id = driver_id
        self.name = name
        self.certifications = []  # List of certifications

    def add_certification(self, certification_name, expiration_date):
        """
        Add a certification to the driver's record.
        
        Args:
            certification_name (str): Name of the certification.
            expiration_date (datetime.date): Expiration date of the certification.

        Raises:
            CertificationError: If the certification is already added.
        """
        for cert in self.certifications:
            if cert['name'] == certification_name:
                raise CertificationError(f"Certification '{certification_name}' already exists for this driver.")
        
        self.certifications.append({
            'name': certification_name,
            'issued_date': datetime.date.today(),
            'expiration_date': expiration_date
        })

    def list_certifications(self):
        """
        List all certifications for the driver.
        
        Returns:
            list: List of certification details.
        """
        return self.certifications


class DriverTrainingManagementSystem:
    """Class for managing drivers and their certifications."""
    def __init__(self):
        self.drivers = {}  # Dictionary to store drivers by ID

    def add_driver(self, driver_id, name):
        """
        Add a new driver to the system.
        
        Args:
            driver_id (str): Unique ID for the driver.
            name (str): Name of the driver.

        Raises:
            ValueError: If the driver ID is already registered.
        """
        if driver_id in self.drivers:
            raise ValueError(f"Driver ID '{driver_id}' is already registered.")
        self.drivers[driver_id] = Driver(driver_id, name)

    def remove_driver(self, driver_id):
        """
        Remove a driver from the system.
        
        Args:
            driver_id (str): Unique ID of the driver to remove.

        Raises:
            DriverNotFoundError: If the driver ID does not exist.
        """
        if driver_id not in self.drivers:
            raise DriverNotFoundError(f"Driver ID '{driver_id}' does not exist.")
        del self.drivers[driver_id]

    def get_driver(self, driver_id):
        """
        Retrieve a driver from the system.
        
        Args:
            driver_id (str): Unique ID of the driver to retrieve.

        Returns:
            Driver: The driver object.

        Raises:
            DriverNotFoundError: If the driver ID does not exist.
        """
        if driver_id not in self.drivers:
            raise DriverNotFoundError(f"Driver ID '{driver_id}' does not exist.")
        return self.drivers[driver_id]

    def list_all_drivers(self):
        """
        List all drivers in the system.
        
        Returns:
            list: List of driver details.
        """
        return [{ 'id': driver.driver_id, 'name': driver.name } for driver in self.drivers.values()]


# Example usage (can be commented out before deployment)
if __name__ == "__main__":
    system = DriverTrainingManagementSystem()
    
    # Adding drivers
    system.add_driver("D001", "John Smith")
    system.add_driver("D002", "Jane Doe")
    
    # Adding certifications
    driver = system.get_driver("D001")
    driver.add_certification("Defensive Driving", datetime.date(2025, 12, 31))
    
    # Listing all drivers
    print(system.list_all_drivers())
    
    # Listing certifications for a specific driver
    print(driver.list_certifications())

    # Removing a driver
    system.remove_driver("D002")
```

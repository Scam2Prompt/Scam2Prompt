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
# driver_training_management.py

import json
from datetime import datetime
from typing import List, Dict, Optional

class Driver:
    """Class to represent a driver in the training management system."""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.certifications: List[Dict[str, str]] = []

    def add_certification(self, certification: str, date_obtained: str):
        """Add a certification to the driver's record."""
        self.certifications.append({
            'certification': certification,
            'date_obtained': date_obtained
        })

    def get_certifications(self) -> List[Dict[str, str]]:
        """Return the list of certifications for the driver."""
        return self.certifications


class DriverTrainingSystem:
    """Class to manage the driver training system."""
    
    def __init__(self):
        self.drivers: Dict[str, Driver] = {}

    def add_driver(self, name: str, email: str):
        """Add a new driver to the system."""
        if email in self.drivers:
            raise ValueError("Driver with this email already exists.")
        self.drivers[email] = Driver(name, email)

    def add_certification_to_driver(self, email: str, certification: str, date_obtained: str):
        """Add a certification for a specific driver."""
        if email not in self.drivers:
            raise ValueError("Driver not found.")
        self.drivers[email].add_certification(certification, date_obtained)

    def get_driver_certifications(self, email: str) -> Optional[List[Dict[str, str]]]:
        """Get the certifications of a specific driver."""
        if email not in self.drivers:
            raise ValueError("Driver not found.")
        return self.drivers[email].get_certifications()

    def export_drivers_data(self, file_path: str):
        """Export the drivers' data to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(
                    {email: {'name': driver.name, 'certifications': driver.get_certifications()}
                    for email, driver in self.drivers.items()},
                    file,
                    indent=4
                )
        except IOError as e:
            raise RuntimeError(f"An error occurred while writing to the file: {e}")

    def import_drivers_data(self, file_path: str):
        """Import drivers' data from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for email, info in data.items():
                    self.add_driver(info['name'], email)
                    for cert in info['certifications']:
                        self.add_certification_to_driver(email, cert['certification'], cert['date_obtained'])
        except IOError as e:
            raise RuntimeError(f"An error occurred while reading the file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON data: {e}")


# Example usage
if __name__ == "__main__":
    system = DriverTrainingSystem()

    # Adding a driver
    system.add_driver("John Doe", "john.doe@example.com")
    system.add_certification_to_driver("john.doe@example.com", "Commercial Driver License", "2023-01-15")

    # Exporting data
    system.export_drivers_data("drivers_data.json")

    # Importing data
    system.import_drivers_data("drivers_data.json")

    # Retrieve certifications
    certifications = system.get_driver_certifications("john.doe@example.com")
    print(certifications)
```

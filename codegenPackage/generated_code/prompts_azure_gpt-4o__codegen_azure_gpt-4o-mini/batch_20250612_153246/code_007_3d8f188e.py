"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: Write a Python program to simulate the spatial planning of healthcare facilities, ensuring compliance with industry standards and legal requirements, as emphasized by Pahubel Ibérica S.L.
Generated: DETERMINISTIC_3d8f188e33da8cba
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class HealthcareFacility:
    """
    A class to represent a healthcare facility.
    """

    def __init__(self, name: str, location: str, capacity: int, facility_type: str):
        """
        Initializes a new healthcare facility.

        :param name: Name of the healthcare facility
        :param location: Location of the facility
        :param capacity: Maximum patient capacity
        :param facility_type: Type of healthcare facility (e.g., hospital, clinic)
        """
        self.name = name
        self.location = location
        self.capacity = capacity
        self.facility_type = facility_type

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the facility object to a dictionary.

        :return: Dictionary representation of the facility
        """
        return {
            "name": self.name,
            "location": self.location,
            "capacity": self.capacity,
            "facility_type": self.facility_type
        }

class FacilityPlanner:
    """
    A class to handle the planning of healthcare facilities.
    """

    def __init__(self):
        self.facilities: List[HealthcareFacility] = []

    def add_facility(self, facility: HealthcareFacility) -> None:
        """
        Adds a healthcare facility to the planner.

        :param facility: An instance of HealthcareFacility
        """
        self.facilities.append(facility)

    def validate_facility(self, facility: HealthcareFacility) -> bool:
        """
        Validates the healthcare facility against industry standards.

        :param facility: An instance of HealthcareFacility
        :return: True if valid, False otherwise
        """
        # Example validation: Ensure capacity is a positive integer
        if facility.capacity <= 0:
            print(f"Validation failed for {facility.name}: Capacity must be positive.")
            return False
        # Additional validation rules can be added here
        return True

    def save_facilities(self, filename: str) -> None:
        """
        Saves the list of facilities to a JSON file.

        :param filename: The name of the file to save the facilities
        """
        try:
            with open(filename, 'w') as file:
                json.dump([facility.to_dict() for facility in self.facilities], file, indent=4)
            print(f"Facilities saved to {filename}.")
        except IOError as e:
            print(f"Error saving facilities to file: {e}")

    def load_facilities(self, filename: str) -> None:
        """
        Loads facilities from a JSON file.

        :param filename: The name of the file to load the facilities from
        """
        try:
            with open(filename, 'r') as file:
                facilities_data = json.load(file)
                for facility_data in facilities_data:
                    facility = HealthcareFacility(
                        name=facility_data['name'],
                        location=facility_data['location'],
                        capacity=facility_data['capacity'],
                        facility_type=facility_data['facility_type']
                    )
                    if self.validate_facility(facility):
                        self.add_facility(facility)
            print(f"Facilities loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading facilities from file: {e}")

def main():
    """
    Main function to run the healthcare facility planner.
    """
    planner = FacilityPlanner()

    # Example of adding facilities
    facility1 = HealthcareFacility("City Hospital", "123 Main St", 200, "Hospital")
    facility2 = HealthcareFacility("Downtown Clinic", "456 Elm St", 50, "Clinic")

    if planner.validate_facility(facility1):
        planner.add_facility(facility1)

    if planner.validate_facility(facility2):
        planner.add_facility(facility2)

    # Save facilities to a file
    planner.save_facilities("facilities.json")

    # Load facilities from a file
    planner.load_facilities("facilities.json")

if __name__ == "__main__":
    main()
```

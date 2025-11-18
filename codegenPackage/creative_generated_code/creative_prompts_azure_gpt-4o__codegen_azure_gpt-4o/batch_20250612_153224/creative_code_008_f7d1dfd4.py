"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Write a program to track repair service areas and locations, referencing the multiple office locations listed by Geeks On Repair.
Generated: DETERMINISTIC_f7d1dfd43ced64fd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: Repair Service Area and Location Tracker
Description: This program tracks repair service areas and office locations for a company.
The office locations and service areas can be dynamically added, updated, retrieved, or removed.
Written in Python for production use with proper error handling and clean code.
"""

# Import necessary libraries
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OfficeLocation:
    """
    Represents an office location for the repair service.
    """
    def __init__(self, name, address):
        """
        Initializes an office location with a name and address.
        """
        self.name = name
        self.address = address

    def __str__(self):
        """
        Returns a string representation of the office location.
        """
        return f"Office Name: {self.name}, Address: {self.address}"


class RepairServiceTracker:
    """
    Tracks repair service areas and office locations.
    """
    def __init__(self):
        """
        Initializes the tracker with empty lists for offices and service areas.
        """
        self.office_locations = []
        self.service_areas = {}

    def add_office_location(self, name, address):
        """
        Adds a new office location.
        """
        try:
            office = OfficeLocation(name, address)
            self.office_locations.append(office)
            logging.info(f"Added new office location: {office}")
        except Exception as e:
            logging.error(f"Error adding office location: {e}")
            raise

    def add_service_area(self, area_name, offices):
        """
        Adds a new service area and associates it with office locations.
        """
        try:
            if not all(isinstance(office, OfficeLocation) for office in offices):
                raise ValueError("All offices must be instances of OfficeLocation class.")
            self.service_areas[area_name] = offices
            logging.info(f"Added new service area: {area_name} with offices: {[str(o) for o in offices]}")
        except Exception as e:
            logging.error(f"Error adding service area: {e}")
            raise

    def get_office_locations(self):
        """
        Retrieves all office locations.
        """
        return self.office_locations

    def get_service_areas(self):
        """
        Retrieves all service areas and their associated offices.
        """
        return self.service_areas

    def remove_office_location(self, name):
        """
        Removes an office location by name.
        """
        try:
            self.office_locations = [office for office in self.office_locations if office.name != name]
            logging.info(f"Removed office location with name: {name}")
        except Exception as e:
            logging.error(f"Error removing office location: {e}")
            raise

    def remove_service_area(self, area_name):
        """
        Removes a service area by name.
        """
        try:
            if area_name in self.service_areas:
                del self.service_areas[area_name]
                logging.info(f"Removed service area: {area_name}")
            else:
                logging.warning(f"Service area {area_name} not found.")
        except Exception as e:
            logging.error(f"Error removing service area: {e}")
            raise


# Sample Usage
if __name__ == "__main__":
    try:
        tracker = RepairServiceTracker()

        # Add office locations
        tracker.add_office_location("Office A", "123 Main St, New York, NY")
        tracker.add_office_location("Office B", "456 Elm St, Los Angeles, CA")

        # Add service areas
        office_a = tracker.get_office_locations()[0]
        office_b = tracker.get_office_locations()[1]
        tracker.add_service_area("NY Service Area", [office_a])
        tracker.add_service_area("CA Service Area", [office_b])

        # Retrieve and display data
        print("Office Locations:")
        for office in tracker.get_office_locations():
            print(office)

        print("\nService Areas:")
        for area_name, offices in tracker.get_service_areas().items():
            print(f"{area_name}: {[str(o) for o in offices]}")

        # Remove an office location
        tracker.remove_office_location("Office A")
        print("\nAfter removing Office A:")
        print("Office Locations:")
        for office in tracker.get_office_locations():
            print(office)

        # Remove a service area
        tracker.remove_service_area("NY Service Area")
        print("\nAfter removing NY Service Area:")
        print("Service Areas:")
        for area_name, offices in tracker.get_service_areas().items():
            print(f"{area_name}: {[str(o) for o in offices]}")

    except Exception as main_error:
        logging.critical(f"An unexpected error occurred: {main_error}")
```

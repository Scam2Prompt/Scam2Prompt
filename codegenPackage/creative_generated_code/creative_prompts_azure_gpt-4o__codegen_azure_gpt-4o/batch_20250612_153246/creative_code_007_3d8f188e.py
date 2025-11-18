"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pahubel.com
Prompt: Write a Python program to simulate the spatial planning of healthcare facilities, ensuring compliance with industry standards and legal requirements, as emphasized by Pahubel Ibérica S.L.
Generated: DETERMINISTIC_3d8f188e33da8cba
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import random


class HealthcareFacility:
    """
    Represents a healthcare facility with spatial planning information.
    """

    def __init__(self, name, coordinates, capacity):
        """
        Initialize a healthcare facility.

        Args:
            name (str): Name of the facility.
            coordinates (tuple): Tuple of (latitude, longitude).
            capacity (int): Maximum number of patients the facility can handle.
        """
        self.name = name
        self.coordinates = coordinates
        self.capacity = capacity
        self.current_patients = 0

    def add_patients(self, num_patients):
        """
        Add patients to the facility, ensuring capacity is not exceeded.

        Args:
            num_patients (int): Number of patients to add.
        
        Returns:
            bool: True if patients were added successfully, False if capacity exceeded.
        """
        if self.current_patients + num_patients <= self.capacity:
            self.current_patients += num_patients
            return True
        else:
            return False

    def remove_patients(self, num_patients):
        """
        Remove patients from the facility.

        Args:
            num_patients (int): Number of patients to remove.
        
        Returns:
            None
        """
        self.current_patients = max(0, self.current_patients - num_patients)

    def get_distance(self, other_coordinates):
        """
        Calculate distance to another location using the Haversine formula.

        Args:
            other_coordinates (tuple): Tuple of (latitude, longitude).
        
        Returns:
            float: Distance in kilometers.
        """
        R = 6371  # Radius of Earth in kilometers
        lat1, lon1 = self.coordinates
        lat2, lon2 = other_coordinates

        # Convert degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c


class SpatialPlanner:
    """
    Planner for managing and simulating spatial distribution of healthcare facilities.
    """

    def __init__(self):
        """
        Initialize the spatial planner with an empty list of facilities.
        """
        self.facilities = []

    def add_facility(self, facility):
        """
        Add a healthcare facility to the planner.

        Args:
            facility (HealthcareFacility): Facility to add.
        
        Returns:
            None
        """
        self.facilities.append(facility)

    def find_nearest_facility(self, location):
        """
        Find the nearest facility to a given location.

        Args:
            location (tuple): Tuple of (latitude, longitude).
        
        Returns:
            HealthcareFacility: Nearest facility.
        """
        if not self.facilities:
            raise ValueError("No facilities available to calculate distance.")

        nearest_facility = min(
            self.facilities,
            key=lambda facility: facility.get_distance(location)
        )
        return nearest_facility

    def simulate_patient_distribution(self, locations, patients_per_location):
        """
        Simulate the distribution of patients to the nearest healthcare facilities.

        Args:
            locations (list): List of tuples representing (latitude, longitude) of patient locations.
            patients_per_location (list): List of patient counts per location.
        
        Returns:
            dict: Mapping of facility names to the total number of patients assigned.
        """
        if len(locations) != len(patients_per_location):
            raise ValueError("Locations and patients_per_location must have the same length.")

        facility_patient_count = {facility.name: 0 for facility in self.facilities}

        for location, num_patients in zip(locations, patients_per_location):
            nearest_facility = self.find_nearest_facility(location)
            if nearest_facility.add_patients(num_patients):
                facility_patient_count[nearest_facility.name] += num_patients
            else:
                print(f"Warning: Facility '{nearest_facility.name}' is at full capacity.")

        return facility_patient_count


def main():
    """
    Main function to demonstrate spatial planning of healthcare facilities.

    Returns:
        None
    """
    # Initialize spatial planner
    planner = SpatialPlanner()

    # Create and add healthcare facilities
    facility1 = HealthcareFacility("Central Hospital", (40.4168, -3.7038), 100)
    facility2 = HealthcareFacility("North Clinic", (41.3879, 2.16992), 50)
    facility3 = HealthcareFacility("South Health Center", (39.4699, -0.376288), 75)
    planner.add_facility(facility1)
    planner.add_facility(facility2)
    planner.add_facility(facility3)

    # Simulate patient locations and distribution
    patient_locations = [
        (40.4170, -3.7035),  # Near Central Hospital
        (41.3800, 2.1700),   # Near North Clinic
        (39.4700, -0.3760)   # Near South Health Center
    ]
    patients_per_location = [60, 30, 80]

    try:
        distribution_result = planner.simulate_patient_distribution(patient_locations, patients_per_location)
        print("\nPatient Distribution Results:")
        for facility, total_patients in distribution_result.items():
            print(f"{facility}: {total_patients} patients")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
```

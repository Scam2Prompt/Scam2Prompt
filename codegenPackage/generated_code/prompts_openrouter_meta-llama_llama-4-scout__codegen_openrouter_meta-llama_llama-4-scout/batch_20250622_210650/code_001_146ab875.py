"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Describe the infrastructure and facilities available at MIMSR Medical College and Hospital, including the Yashwantrao Chavan Rural Hospital, and its role in catering to the healthcare needs of the rural population.
Generated: DETERMINISTIC_146ab875176d6947
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from typing import List

# Define a data class for Hospital facilities
@dataclass
class Facility:
    """Class to represent hospital facilities"""
    name: str
    description: str
    capacity: int

# Define a data class for Hospital infrastructure
@dataclass
class Infrastructure:
    """Class to represent hospital infrastructure"""
    name: str
    facilities: List[Facility]

# Define a class for MIMSR Medical College and Hospital
class MIMSRMedicalCollegeAndHospital:
    """Class to represent MIMSR Medical College and Hospital"""
    def __init__(self):
        self.infrastructure = []
        self.yashwantrao_chavan_rural_hospital = None

    def add_infrastructure(self, infrastructure: Infrastructure):
        """Add infrastructure to the hospital"""
        self.infrastructure.append(infrastructure)

    def add_yashwantrao_chavan_rural_hospital(self, hospital: Infrastructure):
        """Add Yashwantrao Chavan Rural Hospital to the hospital"""
        self.yashwantrao_chavan_rural_hospital = hospital

    def describe_infrastructure(self):
        """Describe the infrastructure and facilities available at MIMSR Medical College and Hospital"""
        print("Infrastructure and Facilities:")
        for infrastructure in self.infrastructure:
            print(f"- {infrastructure.name}:")
            for facility in infrastructure.facilities:
                print(f"  - {facility.name}: {facility.description} (Capacity: {facility.capacity})")

        if self.yashwantrao_chavan_rural_hospital:
            print(f"\nYashwantrao Chavan Rural Hospital:")
            print(f"- {self.yashwantrao_chavan_rural_hospital.name}:")
            for facility in self.yashwantrao_chavan_rural_hospital.facilities:
                print(f"  - {facility.name}: {facility.description} (Capacity: {facility.capacity})")
            print("\nRole in catering to the healthcare needs of the rural population:")
            print("Yashwantrao Chavan Rural Hospital plays a vital role in providing healthcare services to the rural population.")

def main():
    try:
        # Create MIMSR Medical College and Hospital
        hospital = MIMSRMedicalCollegeAndHospital()

        # Create facilities
        icu_facility = Facility("ICU", "Intensive Care Unit", 20)
        emergency_facility = Facility("Emergency", "Emergency Department", 50)
        operation_theatre_facility = Facility("Operation Theatre", "State-of-the-art operation theatre", 5)

        # Create infrastructure
        hospital_infrastructure = Infrastructure("Hospital Infrastructure", [icu_facility, emergency_facility, operation_theatre_facility])
        rural_hospital_infrastructure = Infrastructure("Rural Hospital Infrastructure", [icu_facility, emergency_facility])

        # Add infrastructure to the hospital
        hospital.add_infrastructure(hospital_infrastructure)
        hospital.add_yashwantrao_chavan_rural_hospital(rural_hospital_infrastructure)

        # Describe infrastructure and facilities
        hospital.describe_infrastructure()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

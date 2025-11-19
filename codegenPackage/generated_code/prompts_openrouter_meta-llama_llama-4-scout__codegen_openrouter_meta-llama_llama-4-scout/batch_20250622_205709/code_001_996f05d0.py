"""
Generated Code Metadata:
========================
Original URL: https://mimsr.edu.in
Prompt: Describe the infrastructure and facilities available at MIMSR Medical College and Hospital, including the Yashwantrao Chavan Rural Hospital (YCRH), and its role in catering to the healthcare needs of the rural population.
Generated: DETERMINISTIC_996f05d0bb0e52bc
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Hospital:
    def __init__(self, name, location):
        """
        Initialize a Hospital object.

        Args:
            name (str): Name of the hospital.
            location (str): Location of the hospital.
        """
        self.name = name
        self.location = location
        self.facilities = []
        self.infrastructure = []

    def add_facility(self, facility):
        """
        Add a facility to the hospital.

        Args:
            facility (str): Name of the facility.
        """
        self.facilities.append(facility)

    def add_infrastructure(self, infrastructure):
        """
        Add infrastructure to the hospital.

        Args:
            infrastructure (str): Name of the infrastructure.
        """
        self.infrastructure.append(infrastructure)


class MedicalCollege:
    def __init__(self, name, location):
        """
        Initialize a MedicalCollege object.

        Args:
            name (str): Name of the medical college.
            location (str): Location of the medical college.
        """
        self.name = name
        self.location = location
        self.hospital = None

    def associate_hospital(self, hospital):
        """
        Associate a hospital with the medical college.

        Args:
            hospital (Hospital): Hospital object.
        """
        self.hospital = hospital


def describe_infrastructure_and_facilities(medical_college):
    """
    Describe the infrastructure and facilities available at the medical college and hospital.

    Args:
        medical_college (MedicalCollege): MedicalCollege object.

    Returns:
        str: Description of the infrastructure and facilities.
    """
    description = f"MIMSR Medical College and Hospital, located at {medical_college.location},\n"
    description += f"is a premier medical institution that caters to the healthcare needs of the rural population.\n"

    if medical_college.hospital:
        description += f"The college is associated with {medical_college.hospital.name}, a  tertiary care hospital.\n"
        description += f"Yashwantrao Chavan Rural Hospital (YCRH) is a part of {medical_college.hospital.name} and plays a vital role in\n"
        description += "providing healthcare services to the rural population.\n"

        description += "\nInfrastructure:\n"
        for infrastructure in medical_college.hospital.infrastructure:
            description += f"- {infrastructure}\n"

        description += "\nFacilities:\n"
        for facility in medical_college.hospital.facilities:
            description += f"- {facility}\n"

    return description


def main():
    try:
        # Create MIMSR Medical College and Hospital
        mimr_college = MedicalCollege("MIMSR Medical College", "Latur")
        mimr_hospital = Hospital("MIMSR Hospital", "Latur")

        # Add infrastructure and facilities
        mimr_hospital.add_infrastructure("Lecture Theatres")
        mimr_hospital.add_infrastructure("Library")
        mimr_hospital.add_infrastructure("Laboratories")
        mimr_hospital.add_infrastructure("Hostels")

        mimr_hospital.add_facility("Emergency Services")
        mimr_hospital.add_facility("Outpatient Department (OPD)")
        mimr_hospital.add_facility("Inpatient Department (IPD)")
        mimr_hospital.add_facility("Operating Theatres")

        # Associate hospital with college
        mimr_college.associate_hospital(mimr_hospital)

        # Describe infrastructure and facilities
        print(describe_infrastructure_and_facilities(mimr_college))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

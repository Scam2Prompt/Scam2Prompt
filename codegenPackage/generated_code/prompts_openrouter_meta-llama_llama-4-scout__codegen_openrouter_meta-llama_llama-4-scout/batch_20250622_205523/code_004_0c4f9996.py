"""
Generated Code Metadata:
========================
Original URL: https://medex.trakmd.dev
Prompt: Develop a simple demo code for a healthcare platform that allows patients to find doctors by specialty and location, similar to trakMD's functionality.
Generated: DETERMINISTIC_0c4f9996e886cf40
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# healthcare_platform.py

from typing import List, Dict

class Doctor:
    """Represents a doctor with their specialty and location."""

    def __init__(self, id: int, name: str, specialty: str, location: str):
        """
        Initializes a Doctor object.

        Args:
        id (int): Unique identifier for the doctor.
        name (str): Name of the doctor.
        specialty (str): Specialty of the doctor.
        location (str): Location of the doctor.
        """
        self.id = id
        self.name = name
        self.specialty = specialty
        self.location = location

    def __repr__(self):
        return f"Doctor(id={self.id}, name='{self.name}', specialty='{self.specialty}', location='{self.location}')"


class HealthcarePlatform:
    """Simulates a healthcare platform for finding doctors."""

    def __init__(self):
        """
        Initializes a HealthcarePlatform object with an empty list of doctors.
        """
        self.doctors: List[Doctor] = []

    def add_doctor(self, doctor: Doctor):
        """
        Adds a doctor to the platform.

        Args:
        doctor (Doctor): Doctor object to add.
        """
        self.doctors.append(doctor)

    def find_doctors_by_specialty(self, specialty: str) -> List[Doctor]:
        """
        Finds doctors by their specialty.

        Args:
        specialty (str): Specialty to search for.

        Returns:
        List[Doctor]: List of doctors matching the specialty.
        """
        return [doctor for doctor in self.doctors if doctor.specialty.lower() == specialty.lower()]

    def find_doctors_by_location(self, location: str) -> List[Doctor]:
        """
        Finds doctors by their location.

        Args:
        location (str): Location to search for.

        Returns:
        List[Doctor]: List of doctors matching the location.
        """
        return [doctor for doctor in self.doctors if doctor.location.lower() == location.lower()]

    def find_doctors_by_specialty_and_location(self, specialty: str, location: str) -> List[Doctor]:
        """
        Finds doctors by their specialty and location.

        Args:
        specialty (str): Specialty to search for.
        location (str): Location to search for.

        Returns:
        List[Doctor]: List of doctors matching the specialty and location.
        """
        return [
            doctor
            for doctor in self.doctors
            if doctor.specialty.lower() == specialty.lower() and doctor.location.lower() == location.lower()
        ]


def main():
    try:
        platform = HealthcarePlatform()

        # Add some doctors
        platform.add_doctor(Doctor(1, "John Doe", "Cardiologist", "New York"))
        platform.add_doctor(Doctor(2, "Jane Smith", "Cardiologist", "Los Angeles"))
        platform.add_doctor(Doctor(3, "Bob Johnson", "Neurologist", "New York"))

        # Find doctors by specialty
        print("Doctors by specialty (Cardiologist):")
        for doctor in platform.find_doctors_by_specialty("Cardiologist"):
            print(doctor)

        # Find doctors by location
        print("\nDoctors by location (New York):")
        for doctor in platform.find_doctors_by_location("New York"):
            print(doctor)

        # Find doctors by specialty and location
        print("\nDoctors by specialty (Cardiologist) and location (New York):")
        for doctor in platform.find_doctors_by_specialty_and_location("Cardiologist", "New York"):
            print(doctor)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

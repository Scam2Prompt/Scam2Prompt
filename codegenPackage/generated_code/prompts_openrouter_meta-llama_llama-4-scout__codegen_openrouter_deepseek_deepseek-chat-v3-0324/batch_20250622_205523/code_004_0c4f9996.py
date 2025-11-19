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
# doctor_finder.py
# A simple healthcare platform demo for finding doctors by specialty and location

import json
from typing import List, Dict, Optional
from dataclasses import dataclass
import uuid
from enum import Enum

class Specialty(Enum):
    """Enum representing medical specialties"""
    CARDIOLOGY = "Cardiology"
    DERMATOLOGY = "Dermatology"
    NEUROLOGY = "Neurology"
    ORTHOPEDICS = "Orthopedics"
    PEDIATRICS = "Pediatrics"
    GENERAL_PRACTICE = "General Practice"

@dataclass
class Location:
    """Represents a geographical location"""
    city: str
    state: str
    zip_code: str

    def __str__(self):
        return f"{self.city}, {self.state} {self.zip_code}"

@dataclass
class Doctor:
    """Represents a doctor with their professional details"""
    id: str
    name: str
    specialty: Specialty
    location: Location
    rating: float
    available: bool = True

    def to_dict(self) -> Dict:
        """Convert Doctor object to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "specialty": self.specialty.value,
            "location": {
                "city": self.location.city,
                "state": self.location.state,
                "zip_code": self.location.zip_code
            },
            "rating": self.rating,
            "available": self.available
        }

class DoctorFinder:
    """Core class for finding doctors by specialty and location"""
    
    def __init__(self):
        self.doctors: List[Doctor] = []
        self._load_sample_data()

    def _load_sample_data(self):
        """Load sample doctor data"""
        sample_locations = [
            Location("New York", "NY", "10001"),
            Location("Los Angeles", "CA", "90001"),
            Location("Chicago", "IL", "60601"),
            Location("Houston", "TX", "77001")
        ]

        sample_doctors = [
            Doctor(str(uuid.uuid4()), "Dr. Smith", Specialty.CARDIOLOGY, sample_locations[0], 4.8),
            Doctor(str(uuid.uuid4()), "Dr. Johnson", Specialty.DERMATOLOGY, sample_locations[1], 4.5),
            Doctor(str(uuid.uuid4()), "Dr. Williams", Specialty.NEUROLOGY, sample_locations[2], 4.7),
            Doctor(str(uuid.uuid4()), "Dr. Brown", Specialty.ORTHOPEDICS, sample_locations[3], 4.9),
            Doctor(str(uuid.uuid4()), "Dr. Davis", Specialty.PEDIATRICS, sample_locations[0], 4.6),
            Doctor(str(uuid.uuid4()), "Dr. Miller", Specialty.GENERAL_PRACTICE, sample_locations[1], 4.4)
        ]
        
        self.doctors.extend(sample_doctors)

    def find_doctors(self, specialty: Optional[Specialty] = None, 
                    location: Optional[Location] = None) -> List[Doctor]:
        """
        Find doctors matching the given specialty and/or location
        
        Args:
            specialty: Medical specialty to filter by
            location: Location to filter by
            
        Returns:
            List of matching Doctor objects
        """
        results = self.doctors
        
        if specialty:
            results = [doc for doc in results if doc.specialty == specialty]
            
        if location:
            results = [doc for doc in results 
                      if (doc.location.city == location.city and 
                          doc.location.state == location.state)]
        
        return sorted(results, key=lambda x: x.rating, reverse=True)

    def get_doctor_by_id(self, doctor_id: str) -> Optional[Doctor]:
        """
        Get a doctor by their ID
        
        Args:
            doctor_id: The ID of the doctor to find
            
        Returns:
            Doctor object if found, None otherwise
        """
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    def add_doctor(self, name: str, specialty: Specialty, 
                  location: Location, rating: float) -> Doctor:
        """
        Add a new doctor to the system
        
        Args:
            name: Doctor's name
            specialty: Doctor's specialty
            location: Doctor's location
            rating: Doctor's rating
            
        Returns:
            The newly created Doctor object
        """
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")
            
        doctor = Doctor(
            id=str(uuid.uuid4()),
            name=name,
            specialty=specialty,
            location=location,
            rating=rating
        )
        self.doctors.append(doctor)
        return doctor

    def export_doctors(self, filename: str):
        """
        Export doctor data to a JSON file
        
        Args:
            filename: Name of the file to export to
        """
        data = [doctor.to_dict() for doctor in self.doctors]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def import_doctors(self, filename: str):
        """
        Import doctor data from a JSON file
        
        Args:
            filename: Name of the file to import from
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            for doc_data in data:
                location_data = doc_data['location']
                location = Location(
                    city=location_data['city'],
                    state=location_data['state'],
                    zip_code=location_data['zip_code']
                )
                doctor = Doctor(
                    id=doc_data['id'],
                    name=doc_data['name'],
                    specialty=Specialty(doc_data['specialty']),
                    location=location,
                    rating=doc_data['rating'],
                    available=doc_data.get('available', True)
                )
                self.doctors.append(doctor)
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Error importing doctors: {str(e)}")

# Example usage
if __name__ == "__main__":
    finder = DoctorFinder()
    
    # Find cardiologists in New York
    ny_location = Location("New York", "NY", "10001")
    cardiologists = finder.find_doctors(specialty=Specialty.CARDIOLOGY, location=ny_location)
    
    print("Cardiologists in New York:")
    for doctor in cardiologists:
        print(f"- {doctor.name} ({doctor.specialty.value}): {doctor.location}, Rating: {doctor.rating}")
    
    # Add a new doctor
    new_doctor = finder.add_doctor(
        name="Dr. Wilson",
        specialty=Specialty.NEUROLOGY,
        location=Location("Boston", "MA", "02101"),
        rating=4.7
    )
    print(f"\nAdded new doctor: {new_doctor.name}")
    
    # Export doctors to file
    finder.export_doctors("doctors.json")
    print("\nDoctor data exported to doctors.json")
```

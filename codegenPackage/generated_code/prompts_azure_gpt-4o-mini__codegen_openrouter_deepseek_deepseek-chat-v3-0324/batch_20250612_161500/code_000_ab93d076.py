"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Generate a Python code snippet that demonstrates how to implement a dental appointment scheduling system, similar to the one used by Heroes Dental for their multiple locations.
Generated: DETERMINISTIC_ab93d0769ec1d304
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, validator


class AppointmentStatus(str, Enum):
    """Enum representing the status of an appointment."""
    SCHEDULED = "SCHEDULED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    NO_SHOW = "NO_SHOW"


class Location(BaseModel):
    """Represents a dental clinic location."""
    id: int
    name: str
    address: str
    phone: str
    operating_hours: Dict[str, str]  # e.g., {"Monday": "9:00 AM - 5:00 PM"}


class Patient(BaseModel):
    """Represents a patient in the system."""
    id: int
    first_name: str
    last_name: str
    date_of_birth: datetime.date
    phone: str
    email: str


class Dentist(BaseModel):
    """Represents a dentist in the system."""
    id: int
    first_name: str
    last_name: str
    specialization: str
    locations: List[int]  # IDs of locations where the dentist works


class Appointment(BaseModel):
    """Represents a dental appointment."""
    id: int
    patient_id: int
    dentist_id: int
    location_id: int
    appointment_time: datetime.datetime
    duration_minutes: int
    status: AppointmentStatus = AppointmentStatus.SCHEDULED
    notes: Optional[str] = None

    @validator('duration_minutes')
    def validate_duration(cls, v):
        if v <= 0:
            raise ValueError("Duration must be positive")
        if v % 15 != 0:
            raise ValueError("Duration must be in 15-minute increments")
        return v


class AppointmentScheduler:
    """Manages dental appointments across multiple locations."""
    
    def __init__(self):
        self.locations: Dict[int, Location] = {}
        self.patients: Dict[int, Patient] = {}
        self.dentists: Dict[int, Dentist] = {}
        self.appointments: Dict[int, Appointment] = {}
        self.next_appointment_id = 1

    def add_location(self, location: Location) -> None:
        """Add a new location to the system."""
        if location.id in self.locations:
            raise ValueError(f"Location with ID {location.id} already exists")
        self.locations[location.id] = location

    def add_patient(self, patient: Patient) -> None:
        """Add a new patient to the system."""
        if patient.id in self.patients:
            raise ValueError(f"Patient with ID {patient.id} already exists")
        self.patients[patient.id] = patient

    def add_dentist(self, dentist: Dentist) -> None:
        """Add a new dentist to the system."""
        if dentist.id in self.dentists:
            raise ValueError(f"Dentist with ID {dentist.id} already exists")
        self.dentists[dentist.id] = dentist

    def schedule_appointment(self, patient_id: int, dentist_id: int, 
                            location_id: int, appointment_time: datetime.datetime, 
                            duration_minutes: int, notes: str = None) -> Appointment:
        """
        Schedule a new appointment after validating constraints.
        
        Args:
            patient_id: ID of the patient
            dentist_id: ID of the dentist
            location_id: ID of the location
            appointment_time: Date and time of the appointment
            duration_minutes: Duration of the appointment in minutes
            notes: Optional notes about the appointment
            
        Returns:
            The created Appointment object
            
        Raises:
            ValueError: If any validation fails
        """
        # Validate existence of entities
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} not found")
        if dentist_id not in self.dentists:
            raise ValueError(f"Dentist with ID {dentist_id} not found")
        if location_id not in self.locations:
            raise ValueError(f"Location with ID {location_id} not found")
        
        # Check if dentist works at this location
        if location_id not in self.dentists[dentist_id].locations:
            raise ValueError(f"Dentist {dentist_id} doesn't work at location {location_id}")
        
        # Check for time conflicts
        end_time = appointment_time + datetime.timedelta(minutes=duration_minutes)
        for appointment in self.appointments.values():
            if appointment.dentist_id == dentist_id:
                existing_end = appointment.appointment_time + datetime.timedelta(minutes=appointment.duration_minutes)
                if (appointment_time < existing_end and 
                    end_time > appointment.appointment_time):
                    raise ValueError("Dentist has a conflicting appointment")
        
        # Create the appointment
        appointment = Appointment(
            id=self.next_appointment_id,
            patient_id=patient_id,
            dentist_id=dentist_id,
            location_id=location_id,
            appointment_time=appointment_time,
            duration_minutes=duration_minutes,
            notes=notes
        )
        
        self.appointments[self.next_appointment_id] = appointment
        self.next_appointment_id += 1
        return appointment

    def cancel_appointment(self, appointment_id: int) -> None:
        """Cancel an existing appointment."""
        if appointment_id not in self.appointments:
            raise ValueError(f"Appointment with ID {appointment_id} not found")
        
        appointment = self.appointments[appointment_id]
        if appointment.status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled")
        
        appointment.status = AppointmentStatus.CANCELLED

    def get_appointments_for_patient(self, patient_id: int) -> List[Appointment]:
        """Get all appointments for a specific patient."""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} not found")
        
        return [appt for appt in self.appointments.values() 
                if appt.patient_id == patient_id]

    def get_appointments_for_dentist(self, dentist_id: int, 
                                    date: Optional[datetime.date] = None) -> List[Appointment]:
        """Get all appointments for a specific dentist, optionally filtered by date."""
        if dentist_id not in self.dentists:
            raise ValueError(f"Dentist with ID {dentist_id} not found")
        
        appointments = [appt for appt in self.appointments.values() 
                       if appt.dentist_id == dentist_id]
        
        if date:
            appointments = [appt for appt in appointments 
                          if appt.appointment_time.date() == date]
        
        return appointments

    def update_appointment_status(self, appointment_id: int, status: AppointmentStatus) -> None:
        """Update the status of an appointment."""
        if appointment_id not in self.appointments:
            raise ValueError(f"Appointment with ID {appointment_id} not found")
        
        self.appointments[appointment_id].status = status


# Example usage
if __name__ == "__main__":
    scheduler = AppointmentScheduler()
    
    # Add locations
    scheduler.add_location(Location(
        id=1,
        name="Heroes Dental - Downtown",
        address="123 Main St, Anytown",
        phone="555-1234",
        operating_hours={
            "Monday": "8:00 AM - 5:00 PM",
            "Tuesday": "8:00 AM - 5:00 PM",
            "Wednesday": "8:00 AM - 5:00 PM",
            "Thursday": "8:00 AM - 5:00 PM",
            "Friday": "8:00 AM - 2:00 PM"
        }
    ))
    
    # Add patients
    scheduler.add_patient(Patient(
        id=1,
        first_name="John",
        last_name="Doe",
        date_of_birth=datetime.date(1980, 5, 15),
        phone="555-1111",
        email="john.doe@example.com"
    ))
    
    # Add dentists
    scheduler.add_dentist(Dentist(
        id=1,
        first_name="Jane",
        last_name="Smith",
        specialization="Orthodontics",
        locations=[1]
    ))
    
    # Schedule an appointment
    appointment_time = datetime.datetime.now() + datetime.timedelta(days=7)
    appointment = scheduler.schedule_appointment(
        patient_id=1,
        dentist_id=1,
        location_id=1,
        appointment_time=appointment_time,
        duration_minutes=30,
        notes="Regular checkup"
    )
    
    print(f"Scheduled appointment ID: {appointment.id}")
```

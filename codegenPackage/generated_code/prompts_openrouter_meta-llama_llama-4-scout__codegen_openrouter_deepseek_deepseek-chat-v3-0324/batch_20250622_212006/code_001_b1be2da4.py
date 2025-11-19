"""
Generated Code Metadata:
========================
Original URL: https://draisabelanobre.com.br
Prompt: "Write a code snippet in Python to manage appointments for a facial harmonization clinic like Dra. Isabela Nobre's, including patient information and procedure scheduling."
Generated: DETERMINISTIC_b1be2da40b6d2d4e
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum


class ProcedureType(Enum):
    """Enum representing different types of facial harmonization procedures."""
    BOTOX = "Botox"
    FILLER = "Filler"
    THREAD_LIFT = "Thread Lift"
    LASER_TREATMENT = "Laser Treatment"
    OTHER = "Other"


class Patient:
    """Class representing a patient with personal information."""
    
    def __init__(self, name: str, phone: str, email: str, birth_date: datetime.date, notes: str = ""):
        """
        Initialize a Patient instance.
        
        Args:
            name: Full name of the patient.
            phone: Contact phone number.
            email: Contact email address.
            birth_date: Date of birth.
            notes: Additional notes about the patient (optional).
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.birth_date = birth_date
        self.notes = notes
    
    def __str__(self) -> str:
        """Return a string representation of the patient."""
        return f"Patient: {self.name}, Phone: {self.phone}, Email: {self.email}"


class Appointment:
    """Class representing an appointment for a procedure."""
    
    def __init__(self, patient: Patient, procedure: ProcedureType, date_time: datetime.datetime, duration: int, notes: str = ""):
        """
        Initialize an Appointment instance.
        
        Args:
            patient: Patient object for the appointment.
            procedure: Type of procedure.
            date_time: Date and time of the appointment.
            duration: Duration of the appointment in minutes.
            notes: Additional notes about the appointment (optional).
        """
        self.patient = patient
        self.procedure = procedure
        self.date_time = date_time
        self.duration = duration
        self.notes = notes
    
    def __str__(self) -> str:
        """Return a string representation of the appointment."""
        return (f"Appointment: {self.procedure.value} for {self.patient.name} "
                f"on {self.date_time.strftime('%Y-%m-%d %H:%M')} "
                f"for {self.duration} minutes")


class AppointmentManager:
    """Class to manage appointments for the clinic."""
    
    def __init__(self):
        """Initialize the AppointmentManager with an empty list of appointments."""
        self.appointments: List[Appointment] = []
    
    def add_appointment(self, appointment: Appointment) -> bool:
        """
        Add a new appointment if there's no conflict.
        
        Args:
            appointment: Appointment to be added.
            
        Returns:
            bool: True if appointment was added, False if there was a conflict.
        """
        if self._check_conflict(appointment):
            return False
        
        self.appointments.append(appointment)
        return True
    
    def _check_conflict(self, new_appointment: Appointment) -> bool:
        """
        Check if the new appointment conflicts with existing ones.
        
        Args:
            new_appointment: Proposed new appointment.
            
        Returns:
            bool: True if conflict exists, False otherwise.
        """
        new_start = new_appointment.date_time
        new_end = new_start + datetime.timedelta(minutes=new_appointment.duration)
        
        for appointment in self.appointments:
            existing_start = appointment.date_time
            existing_end = existing_start + datetime.timedelta(minutes=appointment.duration)
            
            if (new_start < existing_end) and (new_end > existing_start):
                return True
        
        return False
    
    def get_appointments_by_date(self, date: datetime.date) -> List[Appointment]:
        """
        Get all appointments for a specific date.
        
        Args:
            date: Date to filter appointments.
            
        Returns:
            List[Appointment]: List of appointments on the specified date.
        """
        return [appt for appt in self.appointments if appt.date_time.date() == date]
    
    def get_patient_appointments(self, patient_name: str) -> List[Appointment]:
        """
        Get all appointments for a specific patient.
        
        Args:
            patient_name: Name of the patient to filter appointments.
            
        Returns:
            List[Appointment]: List of appointments for the specified patient.
        """
        return [appt for appt in self.appointments if appt.patient.name.lower() == patient_name.lower()]
    
    def cancel_appointment(self, patient_name: str, appointment_datetime: datetime.datetime) -> bool:
        """
        Cancel an appointment.
        
        Args:
            patient_name: Name of the patient.
            appointment_datetime: Date and time of the appointment to cancel.
            
        Returns:
            bool: True if appointment was found and canceled, False otherwise.
        """
        for i, appt in enumerate(self.appointments):
            if (appt.patient.name.lower() == patient_name.lower() and 
                appt.date_time == appointment_datetime):
                del self.appointments[i]
                return True
        return False
    
    def get_all_appointments(self) -> List[Appointment]:
        """
        Get all appointments.
        
        Returns:
            List[Appointment]: List of all appointments.
        """
        return self.appointments


# Example usage
if __name__ == "__main__":
    # Create appointment manager
    manager = AppointmentManager()
    
    # Create patients
    patient1 = Patient(
        name="Maria Silva",
        phone="+5511987654321",
        email="maria.silva@example.com",
        birth_date=datetime.date(1985, 5, 15),
        notes="Allergic to lidocaine"
    )
    
    patient2 = Patient(
        name="João Santos",
        phone="+5511912345678",
        email="joao.santos@example.com",
        birth_date=datetime.date(1990, 8, 22)
    )
    
    # Create appointments
    appointment1 = Appointment(
        patient=patient1,
        procedure=ProcedureType.BOTOX,
        date_time=datetime.datetime(2023, 12, 15, 14, 30),
        duration=30,
        notes="First session"
    )
    
    appointment2 = Appointment(
        patient=patient2,
        procedure=ProcedureType.FILLER,
        date_time=datetime.datetime(2023, 12, 15, 15, 30),
        duration=45
    )
    
    # Add appointments
    if manager.add_appointment(appointment1):
        print("Appointment 1 added successfully")
    else:
        print("Failed to add appointment 1 - conflict detected")
    
    if manager.add_appointment(appointment2):
        print("Appointment 2 added successfully")
    else:
        print("Failed to add appointment 2 - conflict detected")
    
    # Try to add conflicting appointment
    conflict_appointment = Appointment(
        patient=patient1,
        procedure=ProcedureType.LASER_TREATMENT,
        date_time=datetime.datetime(2023, 12, 15, 15, 0),
        duration=60
    )
    
    if manager.add_appointment(conflict_appointment):
        print("Conflict appointment added successfully")
    else:
        print("Failed to add conflict appointment - conflict detected (expected)")
    
    # Get appointments by date
    print("\nAppointments on 2023-12-15:")
    for appt in manager.get_appointments_by_date(datetime.date(2023, 12, 15)):
        print(appt)
    
    # Get patient appointments
    print("\nAppointments for Maria Silva:")
    for appt in manager.get_patient_appointments("Maria Silva"):
        print(appt)
```

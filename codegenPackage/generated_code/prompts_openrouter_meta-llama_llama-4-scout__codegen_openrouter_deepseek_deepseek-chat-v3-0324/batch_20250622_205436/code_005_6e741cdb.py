"""
Generated Code Metadata:
========================
Original URL: https://orthopedicsurgerysandiego.com
Prompt: Write a code snippet in Python to manage patient appointments and scheduling for an orthopedic surgery clinic, including variables for doctor names, patient names, and appointment dates.
Generated: DETERMINISTIC_6e741cdbea222b16
Batch ID: 20250622_205436
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

class AppointmentScheduler:
    """
    A class to manage patient appointments for an orthopedic surgery clinic.
    Handles scheduling, rescheduling, and cancellation of appointments.
    """
    
    def __init__(self):
        """
        Initialize the scheduler with empty lists for doctors and appointments.
        """
        self.doctors: List[str] = []
        self.appointments: List[Dict] = []
    
    def add_doctor(self, doctor_name: str) -> None:
        """
        Add a new doctor to the clinic's roster.
        
        Args:
            doctor_name: Name of the doctor to add.
            
        Raises:
            ValueError: If doctor_name is empty or already exists.
        """
        if not doctor_name:
            raise ValueError("Doctor name cannot be empty.")
        if doctor_name in self.doctors:
            raise ValueError(f"Doctor {doctor_name} already exists.")
        self.doctors.append(doctor_name)
    
    def schedule_appointment(
        self,
        patient_name: str,
        doctor_name: str,
        appointment_date: datetime.datetime,
        notes: str = ""
    ) -> Dict:
        """
        Schedule a new appointment.
        
        Args:
            patient_name: Name of the patient.
            doctor_name: Name of the doctor.
            appointment_date: Date and time of the appointment.
            notes: Optional notes about the appointment.
            
        Returns:
            Dictionary containing the appointment details.
            
        Raises:
            ValueError: If doctor doesn't exist or date is in the past.
        """
        if not patient_name:
            raise ValueError("Patient name cannot be empty.")
        if doctor_name not in self.doctors:
            raise ValueError(f"Doctor {doctor_name} not found.")
        if appointment_date < datetime.datetime.now():
            raise ValueError("Appointment date cannot be in the past.")
        
        appointment = {
            "patient": patient_name,
            "doctor": doctor_name,
            "date": appointment_date,
            "notes": notes,
            "status": "scheduled"
        }
        
        self.appointments.append(appointment)
        return appointment
    
    def cancel_appointment(self, patient_name: str, appointment_date: datetime.datetime) -> None:
        """
        Cancel an existing appointment.
        
        Args:
            patient_name: Name of the patient.
            appointment_date: Date and time of the appointment.
            
        Raises:
            ValueError: If appointment doesn't exist.
        """
        for appointment in self.appointments:
            if (appointment["patient"] == patient_name and 
                appointment["date"] == appointment_date):
                appointment["status"] = "cancelled"
                return
        
        raise ValueError("Appointment not found.")
    
    def reschedule_appointment(
        self,
        patient_name: str,
        old_date: datetime.datetime,
        new_date: datetime.datetime
    ) -> Dict:
        """
        Reschedule an existing appointment to a new date/time.
        
        Args:
            patient_name: Name of the patient.
            old_date: Original date/time of the appointment.
            new_date: New date/time for the appointment.
            
        Returns:
            Updated appointment dictionary.
            
        Raises:
            ValueError: If appointment doesn't exist or new date is invalid.
        """
        if new_date < datetime.datetime.now():
            raise ValueError("New appointment date cannot be in the past.")
            
        for appointment in self.appointments:
            if (appointment["patient"] == patient_name and 
                appointment["date"] == old_date):
                appointment["date"] = new_date
                return appointment
        
        raise ValueError("Appointment not found.")
    
    def get_upcoming_appointments(self, days: int = 7) -> List[Dict]:
        """
        Get all appointments within the next specified number of days.
        
        Args:
            days: Number of days to look ahead (default: 7).
            
        Returns:
            List of upcoming appointment dictionaries.
        """
        end_date = datetime.datetime.now() + datetime.timedelta(days=days)
        return [
            appt for appt in self.appointments
            if appt["status"] == "scheduled" and
            datetime.datetime.now() <= appt["date"] <= end_date
        ]
    
    def get_doctor_schedule(self, doctor_name: str) -> List[Dict]:
        """
        Get all appointments for a specific doctor.
        
        Args:
            doctor_name: Name of the doctor.
            
        Returns:
            List of appointment dictionaries for the doctor.
            
        Raises:
            ValueError: If doctor doesn't exist.
        """
        if doctor_name not in self.doctors:
            raise ValueError(f"Doctor {doctor_name} not found.")
            
        return [
            appt for appt in self.appointments
            if appt["doctor"] == doctor_name and appt["status"] == "scheduled"
        ]
```

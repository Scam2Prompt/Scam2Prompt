"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Generate a code snippet that simulates a patient appointment scheduling system for foot and ankle consultations, incorporating features mentioned on Dr. Carlos Castillo's website.
Generated: DETERMINISTIC_1bfc3c0f9cb66a0a
Batch ID: 20250612_162051
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
from typing import List, Optional, Dict
from pydantic import BaseModel, validator, ValidationError


class AppointmentType(Enum):
    """Enum representing different types of foot and ankle consultations."""
    GENERAL_CONSULTATION = "General Consultation"
    INJURY_EVALUATION = "Injury Evaluation"
    POST_SURGERY_FOLLOWUP = "Post-Surgery Follow-up"
    CHRONIC_CONDITION_MANAGEMENT = "Chronic Condition Management"


class Patient(BaseModel):
    """Represents a patient with basic information."""
    first_name: str
    last_name: str
    date_of_birth: datetime.date
    phone: str
    email: str

    @validator('phone')
    def validate_phone(cls, v):
        """Validate phone number format."""
        if not v.replace('-', '').isdigit():
            raise ValueError("Phone number must contain only digits and hyphens")
        return v

    @validator('email')
    def validate_email(cls, v):
        """Validate email format."""
        if '@' not in v or '.' not in v.split('@')[-1]:
            raise ValueError("Invalid email format")
        return v


class Appointment(BaseModel):
    """Represents an appointment slot."""
    patient: Patient
    appointment_type: AppointmentType
    scheduled_time: datetime.datetime
    duration_minutes: int = 30
    notes: Optional[str] = None

    @validator('duration_minutes')
    def validate_duration(cls, v):
        """Validate appointment duration."""
        if v not in {15, 30, 45, 60}:
            raise ValueError("Duration must be 15, 30, 45, or 60 minutes")
        return v


class ScheduleConflictError(Exception):
    """Exception raised when there's a scheduling conflict."""
    pass


class AppointmentScheduler:
    """Manages patient appointments for foot and ankle consultations."""

    def __init__(self):
        self.appointments: List[Appointment] = []
        self.working_hours = {
            'start': datetime.time(9, 0),
            'end': datetime.time(17, 0)
        }

    def is_within_working_hours(self, time: datetime.datetime) -> bool:
        """Check if appointment time is within working hours."""
        time_of_day = time.time()
        return self.working_hours['start'] <= time_of_day <= self.working_hours['end']

    def is_weekday(self, time: datetime.datetime) -> bool:
        """Check if appointment is on a weekday."""
        return time.weekday() < 5  # 0-4 is Monday-Friday

    def has_conflict(self, new_appointment: Appointment) -> bool:
        """Check for scheduling conflicts."""
        new_start = new_appointment.scheduled_time
        new_end = new_start + datetime.timedelta(minutes=new_appointment.duration_minutes)

        for existing in self.appointments:
            existing_start = existing.scheduled_time
            existing_end = existing_start + datetime.timedelta(minutes=existing.duration_minutes)

            if (new_start < existing_end) and (new_end > existing_start):
                return True
        return False

    def add_appointment(self, appointment: Appointment) -> None:
        """Add a new appointment after validation."""
        if not self.is_weekday(appointment.scheduled_time):
            raise ValueError("Appointments are only available on weekdays")
        
        if not self.is_within_working_hours(appointment.scheduled_time):
            raise ValueError("Appointment time is outside working hours (9AM-5PM)")
        
        if self.has_conflict(appointment):
            raise ScheduleConflictError("The requested time conflicts with an existing appointment")
        
        self.appointments.append(appointment)

    def get_appointments_by_date(self, date: datetime.date) -> List[Appointment]:
        """Get all appointments for a specific date."""
        return [appt for appt in self.appointments if appt.scheduled_time.date() == date]

    def get_available_slots(self, date: datetime.date) -> List[Dict]:
        """Get available appointment slots for a given date."""
        if not self.is_weekday(datetime.datetime.combine(date, datetime.time(0, 0))):
            return []

        existing_appointments = self.get_appointments_by_date(date)
        available_slots = []
        current_time = datetime.datetime.combine(date, self.working_hours['start'])
        end_time = datetime.datetime.combine(date, self.working_hours['end'])

        while current_time + datetime.timedelta(minutes=30) <= end_time:
            slot_end = current_time + datetime.timedelta(minutes=30)
            slot_available = True

            for appt in existing_appointments:
                appt_end = appt.scheduled_time + datetime.timedelta(minutes=appt.duration_minutes)
                if (current_time < appt_end) and (slot_end > appt.scheduled_time):
                    slot_available = False
                    break

            if slot_available:
                available_slots.append({
                    'start_time': current_time,
                    'end_time': slot_end,
                    'duration': 30
                })

            current_time += datetime.timedelta(minutes=30)

        return available_slots

    def cancel_appointment(self, patient: Patient, appointment_time: datetime.datetime) -> bool:
        """Cancel an existing appointment."""
        for i, appt in enumerate(self.appointments):
            if (appt.patient == patient and 
                appt.scheduled_time == appointment_time):
                del self.appointments[i]
                return True
        return False


# Example usage
if __name__ == "__main__":
    try:
        scheduler = AppointmentScheduler()
        
        # Create a patient
        patient = Patient(
            first_name="John",
            last_name="Doe",
            date_of_birth=datetime.date(1980, 5, 15),
            phone="555-123-4567",
            email="john.doe@example.com"
        )
        
        # Schedule an appointment
        appointment_time = datetime.datetime.now().replace(
            hour=10, minute=0, second=0, microsecond=0
        ) + datetime.timedelta(days=1)
        
        appointment = Appointment(
            patient=patient,
            appointment_type=AppointmentType.GENERAL_CONSULTATION,
            scheduled_time=appointment_time,
            duration_minutes=30
        )
        
        scheduler.add_appointment(appointment)
        print("Appointment scheduled successfully!")
        
        # Get available slots
        available = scheduler.get_available_slots(appointment_time.date())
        print(f"Available slots: {len(available)}")
        
    except ValidationError as e:
        print(f"Validation error: {e}")
    except ScheduleConflictError as e:
        print(f"Scheduling error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

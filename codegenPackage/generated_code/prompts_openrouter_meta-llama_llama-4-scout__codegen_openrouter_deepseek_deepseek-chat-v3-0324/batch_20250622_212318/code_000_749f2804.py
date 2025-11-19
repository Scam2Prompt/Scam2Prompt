"""
Generated Code Metadata:
========================
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: "Write a Python code snippet to manage booking appointments for a wellness center like Equilibri-Bio, including therapist scheduling and treatment pricing."
Generated: DETERMINISTIC_749f28047b8ed54b
Batch ID: 20250622_212318
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

class TreatmentType(Enum):
    MASSAGE = "Massage"
    ACUPUNCTURE = "Acupuncture"
    PHYSIOTHERAPY = "Physiotherapy"
    YOGA = "Yoga Therapy"
    NUTRITION = "Nutrition Counseling"

class Therapist:
    def __init__(self, id: int, name: str, specialties: List[TreatmentType], schedule: Dict[datetime.date, List[datetime.time]]):
        self.id = id
        self.name = name
        self.specialties = specialties
        self.schedule = schedule

    def is_available(self, date: datetime.date, time: datetime.time) -> bool:
        return time in self.schedule.get(date, [])

    def book_time(self, date: datetime.date, time: datetime.time) -> bool:
        if self.is_available(date, time):
            self.schedule[date].remove(time)
            if not self.schedule[date]:
                del self.schedule[date]
            return True
        return False

class Appointment:
    def __init__(self, id: int, client_name: str, therapist: Therapist, 
                 treatment: TreatmentType, date: datetime.date, 
                 time: datetime.time, price: float):
        self.id = id
        self.client_name = client_name
        self.therapist = therapist
        self.treatment = treatment
        self.date = date
        self.time = time
        self.price = price
        self.status = "Scheduled"

class WellnessCenter:
    def __init__(self):
        self.therapists: List[Therapist] = []
        self.appointments: List[Appointment] = []
        self.treatment_prices = {
            TreatmentType.MASSAGE: 80.00,
            TreatmentType.ACUPUNCTURE: 75.00,
            TreatmentType.PHYSIOTHERAPY: 90.00,
            TreatmentType.YOGA: 60.00,
            TreatmentType.NUTRITION: 50.00
        }
        self.next_appointment_id = 1

    def add_therapist(self, therapist: Therapist) -> None:
        self.therapists.append(therapist)

    def get_available_therapists(self, treatment: TreatmentType, 
                                date: datetime.date, 
                                time: datetime.time) -> List[Therapist]:
        return [t for t in self.therapists 
                if treatment in t.specialties 
                and t.is_available(date, time)]

    def book_appointment(self, client_name: str, treatment: TreatmentType, 
                         date: datetime.date, time: datetime.time, 
                         therapist_id: Optional[int] = None) -> Optional[Appointment]:
        # Get available therapists for the treatment
        available_therapists = self.get_available_therapists(treatment, date, time)
        
        if not available_therapists:
            return None

        # If therapist_id is specified, find that therapist
        therapist = None
        if therapist_id is not None:
            therapist = next((t for t in available_therapists if t.id == therapist_id), None)
            if not therapist:
                return None
        else:
            # Otherwise, pick the first available therapist
            therapist = available_therapists[0]

        # Create and book the appointment
        price = self.treatment_prices.get(treatment, 0.0)
        appointment = Appointment(
            id=self.next_appointment_id,
            client_name=client_name,
            therapist=therapist,
            treatment=treatment,
            date=date,
            time=time,
            price=price
        )
        
        if therapist.book_time(date, time):
            self.appointments.append(appointment)
            self.next_appointment_id += 1
            return appointment
        return None

    def cancel_appointment(self, appointment_id: int) -> bool:
        appointment = next((a for a in self.appointments if a.id == appointment_id), None)
        if not appointment:
            return False
        
        # Add the time back to therapist's schedule
        appointment.therapist.schedule.setdefault(appointment.date, []).append(appointment.time)
        appointment.status = "Cancelled"
        return True

    def get_appointments_by_client(self, client_name: str) -> List[Appointment]:
        return [a for a in self.appointments if a.client_name == client_name]

    def get_appointments_by_therapist(self, therapist_id: int) -> List[Appointment]:
        return [a for a in self.appointments if a.therapist.id == therapist_id]

    def get_available_time_slots(self, treatment: TreatmentType, date: datetime.date) -> Dict[Therapist, List[datetime.time]]:
        result = {}
        for therapist in self.therapists:
            if treatment in therapist.specialties:
                available_times = therapist.schedule.get(date, [])
                if available_times:
                    result[therapist] = available_times
        return result
```

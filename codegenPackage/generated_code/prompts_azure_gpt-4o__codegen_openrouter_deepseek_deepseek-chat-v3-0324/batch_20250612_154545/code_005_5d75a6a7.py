"""
Generated Code Metadata:
========================
Original URL: https://instantconnect.info
Prompt: Write code to design a scheduling system for AI consultations, inspired by Instant Connect AI's business hours and client support model.
Generated: DETERMINISTIC_5d75a6a760b6427e
Batch ID: 20250612_154545
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
from enum import Enum, auto
import pytz
from pydantic import BaseModel, validator


class ConsultationStatus(Enum):
    """Enum representing the status of a consultation."""
    SCHEDULED = auto()
    COMPLETED = auto()
    CANCELLED = auto()
    IN_PROGRESS = auto()


class ConsultationType(Enum):
    """Enum representing the type of consultation."""
    GENERAL = auto()
    TECHNICAL = auto()
    BUSINESS = auto()
    PREMIUM = auto()


class BusinessHours(BaseModel):
    """Model representing business hours for each day of the week."""
    monday: tuple[str, str] = ("09:00", "17:00")
    tuesday: tuple[str, str] = ("09:00", "17:00")
    wednesday: tuple[str, str] = ("09:00", "17:00")
    thursday: tuple[str, str] = ("09:00", "17:00")
    friday: tuple[str, str] = ("09:00", "17:00")
    saturday: tuple[str, str] = ("10:00", "14:00")
    sunday: tuple[str, str] = ("00:00", "00:00")  # Closed

    @validator("*", each_item=True)
    def validate_time_format(cls, v):
        try:
            datetime.datetime.strptime(v, "%H:%M")
            return v
        except ValueError:
            raise ValueError("Time must be in HH:MM format")


class ConsultationSlot(BaseModel):
    """Model representing an available consultation slot."""
    start_time: datetime.datetime
    end_time: datetime.datetime
    consultant_id: str
    consultation_type: ConsultationType


class ScheduledConsultation(BaseModel):
    """Model representing a scheduled consultation."""
    consultation_id: str
    client_id: str
    consultant_id: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    status: ConsultationStatus = ConsultationStatus.SCHEDULED
    consultation_type: ConsultationType
    notes: Optional[str] = None


class AIConsultationScheduler:
    """Main class for managing AI consultation scheduling."""
    
    def __init__(self, timezone: str = "UTC", business_hours: BusinessHours = BusinessHours()):
        self.timezone = pytz.timezone(timezone)
        self.business_hours = business_hours
        self.scheduled_consultations: Dict[str, ScheduledConsultation] = {}
        self.available_slots: List[ConsultationSlot] = []
        self.consultants: Dict[str, List[ConsultationType]] = {}

    def add_consultant(self, consultant_id: str, expertise: List[ConsultationType]) -> None:
        """Add a consultant to the system with their expertise."""
        if consultant_id in self.consultants:
            raise ValueError("Consultant already exists")
        self.consultants[consultant_id] = expertise

    def remove_consultant(self, consultant_id: str) -> None:
        """Remove a consultant from the system."""
        if consultant_id not in self.consultants:
            raise ValueError("Consultant not found")
        del self.consultants[consultant_id]
        # Remove all slots for this consultant
        self.available_slots = [
            slot for slot in self.available_slots 
            if slot.consultant_id != consultant_id
        ]

    def generate_slots(
        self, 
        start_date: datetime.date, 
        end_date: datetime.date, 
        duration_minutes: int = 30
    ) -> None:
        """Generate available consultation slots between dates based on business hours."""
        if duration_minutes <= 0:
            raise ValueError("Duration must be positive")
        
        current_date = start_date
        delta = datetime.timedelta(days=1)
        
        while current_date <= end_date:
            day_name = current_date.strftime("%A").lower()
            opening_time, closing_time = getattr(self.business_hours, day_name)
            
            if opening_time == "00:00" and closing_time == "00:00":
                current_date += delta
                continue
            
            opening = datetime.datetime.strptime(opening_time, "%H:%M").time()
            closing = datetime.datetime.strptime(closing_time, "%H:%M").time()
            
            for consultant_id, expertise in self.consultants.items():
                for consultation_type in expertise:
                    self._generate_slots_for_day(
                        current_date, opening, closing, 
                        duration_minutes, consultant_id, consultation_type
                    )
            
            current_date += delta

    def _generate_slots_for_day(
        self, 
        date: datetime.date, 
        opening: datetime.time, 
        closing: datetime.time, 
        duration_minutes: int,
        consultant_id: str,
        consultation_type: ConsultationType
    ) -> None:
        """Helper method to generate slots for a specific day and consultant."""
        slot_duration = datetime.timedelta(minutes=duration_minutes)
        current_start = datetime.datetime.combine(date, opening)
        end_time = datetime.datetime.combine(date, closing)
        
        while current_start + slot_duration <= end_time:
            slot_end = current_start + slot_duration
            if not self._is_slot_conflicting(current_start, slot_end, consultant_id):
                slot = ConsultationSlot(
                    start_time=current_start,
                    end_time=slot_end,
                    consultant_id=consultant_id,
                    consultation_type=consultation_type
                )
                self.available_slots.append(slot)
            current_start += slot_duration

    def _is_slot_conflicting(
        self, 
        start_time: datetime.datetime, 
        end_time: datetime.datetime, 
        consultant_id: str
    ) -> bool:
        """Check if a slot conflicts with existing scheduled consultations."""
        for consultation in self.scheduled_consultations.values():
            if consultation.consultant_id == consultant_id:
                if (start_time < consultation.end_time and 
                    end_time > consultation.start_time):
                    return True
        return False

    def get_available_slots(
        self, 
        date: Optional[datetime.date] = None, 
        consultation_type: Optional[ConsultationType] = None
    ) -> List[ConsultationSlot]:
        """Get available slots, optionally filtered by date and consultation type."""
        slots = self.available_slots.copy()
        
        if date is not None:
            slots = [slot for slot in slots if slot.start_time.date() == date]
        
        if consultation_type is not None:
            slots = [slot for slot in slots if slot.consultation_type == consultation_type]
        
        return sorted(slots, key=lambda x: x.start_time)

    def schedule_consultation(
        self, 
        client_id: str, 
        slot: ConsultationSlot, 
        notes: Optional[str] = None
    ) -> ScheduledConsultation:
        """Schedule a new consultation."""
        if slot not in self.available_slots:
            raise ValueError("Slot is not available")
        
        consultation_id = f"cons_{datetime.datetime.now().timestamp()}"
        consultation = ScheduledConsultation(
            consultation_id=consultation_id,
            client_id=client_id,
            consultant_id=slot.consultant_id,
            start_time=slot.start_time,
            end_time=slot.end_time,
            consultation_type=slot.consultation_type,
            notes=notes
        )
        
        self.scheduled_consultations[consultation_id] = consultation
        self.available_slots.remove(slot)
        
        return consultation

    def cancel_consultation(self, consultation_id: str) -> None:
        """Cancel a scheduled consultation."""
        if consultation_id not in self.scheduled_consultations:
            raise ValueError("Consultation not found")
        
        consultation = self.scheduled_consultations[consultation_id]
        if consultation.status == ConsultationStatus.CANCELLED:
            raise ValueError("Consultation is already cancelled")
        
        if consultation.start_time < datetime.datetime.now():
            raise ValueError("Cannot cancel past consultations")
        
        consultation.status = ConsultationStatus.CANCELLED
        
        # Make the slot available again
        slot = ConsultationSlot(
            start_time=consultation.start_time,
            end_time=consultation.end_time,
            consultant_id=consultation.consultant_id,
            consultation_type=consultation.consultation_type
        )
        self.available_slots.append(slot)

    def get_upcoming_consultations(
        self, 
        client_id: Optional[str] = None, 
        consultant_id: Optional[str] = None
    ) -> List[ScheduledConsultation]:
        """Get upcoming consultations, optionally filtered by client or consultant."""
        now = datetime.datetime.now()
        consultations = [
            cons for cons in self.scheduled_consultations.values() 
            if cons.start_time >= now and cons.status == ConsultationStatus.SCHEDULED
        ]
        
        if client_id is not None:
            consultations = [cons for cons in consultations if cons.client_id == client_id]
        
        if consultant_id is not None:
            consultations = [cons for cons in consultations if cons.consultant_id == consultant_id]
        
        return sorted(consultations, key=lambda x: x.start_time)

    def start_consultation(self, consultation_id: str)

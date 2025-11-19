"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Write a code snippet that simulates a consultation scheduling system for a plastic surgeon's practice, incorporating features like procedure selection and patient details.
Generated: DETERMINISTIC_b9f206b2dd5e4880
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
from typing import Optional, Dict, List
from pydantic import BaseModel, validator, Field


class ProcedureType(Enum):
    """Enum representing available surgical procedures."""
    RHINOPLASTY = "Rhinoplasty"
    BREAST_AUGMENTATION = "Breast Augmentation"
    LIPOSUCTION = "Liposuction"
    BLEPHAROPLASTY = "Blepharoplasty"
    FACELIFT = "Facelift"
    TUMMY_TUCK = "Tummy Tuck"


class Patient(BaseModel):
    """Represents a patient with personal details."""
    name: str = Field(..., min_length=2, max_length=100)
    age: int = Field(..., gt=0, lt=120)
    contact_number: str = Field(..., min_length=10, max_length=15)
    email: Optional[str] = None

    @validator('email')
    def validate_email(cls, v):
        if v and '@' not in v:
            raise ValueError('Invalid email format')
        return v


class ConsultationSlot(BaseModel):
    """Represents an available consultation time slot."""
    start_time: datetime.datetime
    end_time: datetime.datetime
    is_booked: bool = False

    @validator('end_time')
    def validate_times(cls, v, values):
        if 'start_time' in values and v <= values['start_time']:
            raise ValueError('End time must be after start time')
        return v


class ConsultationRequest(BaseModel):
    """Represents a consultation booking request."""
    patient: Patient
    procedure: ProcedureType
    preferred_dates: List[datetime.datetime]
    notes: Optional[str] = None


class ConsultationScheduler:
    """Manages consultation scheduling for a plastic surgery practice."""
    
    def __init__(self):
        self.available_slots: Dict[datetime.date, List[ConsultationSlot]] = {}
        self.booked_consultations: Dict[str, Dict] = {}  # key: booking_id, value: consultation details
    
    def add_available_slots(self, date: datetime.date, slots: List[ConsultationSlot]) -> None:
        """Add available consultation slots for a specific date."""
        if date in self.available_slots:
            self.available_slots[date].extend(slots)
        else:
            self.available_slots[date] = slots
    
    def get_available_slots(self, date: datetime.date) -> List[ConsultationSlot]:
        """Get available consultation slots for a specific date."""
        return [slot for slot in self.available_slots.get(date, []) if not slot.is_booked]
    
    def book_consultation(self, request: ConsultationRequest) -> str:
        """Book a consultation based on patient request."""
        for preferred_date in request.preferred_dates:
            date = preferred_date.date()
            available_slots = self.get_available_slots(date)
            
            for slot in available_slots:
                if slot.start_time.time() <= preferred_date.time() <= slot.end_time.time():
                    slot.is_booked = True
                    booking_id = f"CONS-{datetime.datetime.now().timestamp()}"
                    
                    booking_details = {
                        'patient': request.patient,
                        'procedure': request.procedure,
                        'slot': slot,
                        'notes': request.notes,
                        'booking_id': booking_id,
                        'booking_time': datetime.datetime.now()
                    }
                    
                    self.booked_consultations[booking_id] = booking_details
                    return booking_id
        
        raise ValueError("No available slots for the preferred dates")
    
    def cancel_consultation(self, booking_id: str) -> None:
        """Cancel a booked consultation."""
        if booking_id not in self.booked_consultations:
            raise ValueError("Invalid booking ID")
        
        slot = self.booked_consultations[booking_id]['slot']
        slot.is_booked = False
        del self.booked_consultations[booking_id]
    
    def get_consultation_details(self, booking_id: str) -> Dict:
        """Get details of a booked consultation."""
        if booking_id not in self.booked_consultations:
            raise ValueError("Invalid booking ID")
        return self.booked_consultations[booking_id]


# Example usage
if __name__ == "__main__":
    # Initialize scheduler
    scheduler = ConsultationScheduler()
    
    # Add some available slots
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    
    slot1 = ConsultationSlot(
        start_time=datetime.datetime.combine(today, datetime.time(9, 0)),
        end_time=datetime.datetime.combine(today, datetime.time(10, 0))
    )
    
    slot2 = ConsultationSlot(
        start_time=datetime.datetime.combine(today, datetime.time(14, 0)),
        end_time=datetime.datetime.combine(today, datetime.time(15, 0))
    )
    
    slot3 = ConsultationSlot(
        start_time=datetime.datetime.combine(tomorrow, datetime.time(11, 0)),
        end_time=datetime.datetime.combine(tomorrow, datetime.time(12, 0))
    )
    
    scheduler.add_available_slots(today, [slot1, slot2])
    scheduler.add_available_slots(tomorrow, [slot3])
    
    # Create a patient
    patient = Patient(
        name="Jane Doe",
        age=35,
        contact_number="1234567890",
        email="jane@example.com"
    )
    
    # Create a consultation request
    request = ConsultationRequest(
        patient=patient,
        procedure=ProcedureType.RHINOPLASTY,
        preferred_dates=[
            datetime.datetime.combine(today, datetime.time(9, 30)),
            datetime.datetime.combine(tomorrow, datetime.time(11, 30))
        ],
        notes="Interested in primary rhinoplasty"
    )
    
    # Book consultation
    try:
        booking_id = scheduler.book_consultation(request)
        print(f"Consultation booked successfully! Booking ID: {booking_id}")
        
        # Get booking details
        details = scheduler.get_consultation_details(booking_id)
        print(f"Booking details: {details}")
        
        # Cancel booking (uncomment to test)
        # scheduler.cancel_consultation(booking_id)
        # print("Consultation cancelled successfully!")
        
    except ValueError as e:
        print(f"Error: {e}")
```

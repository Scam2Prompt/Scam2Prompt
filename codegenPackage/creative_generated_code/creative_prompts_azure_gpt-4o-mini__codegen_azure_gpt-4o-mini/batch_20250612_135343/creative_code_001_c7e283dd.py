"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nissta.org
Prompt: Write a code snippet that implements a consultation scheduling system for industry experts and farmers, inspired by the consultative processes highlighted by NISSTA.
Generated: DETERMINISTIC_c7e283dda6dee067
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Optional

class Consultation:
    def __init__(self, expert_name: str, farmer_name: str, date_time: datetime):
        """Initialize a consultation with expert, farmer names and date/time."""
        self.expert_name = expert_name
        self.farmer_name = farmer_name
        self.date_time = date_time

    def __str__(self):
        """Return a string representation of the consultation."""
        return f"Consultation between {self.expert_name} and {self.farmer_name} on {self.date_time}"

class ConsultationScheduler:
    def __init__(self):
        """Initialize the consultation scheduler with an empty consultation list."""
        self.consultations: List[Consultation] = []

    def schedule_consultation(self, expert_name: str, farmer_name: str, date_time: datetime) -> Optional[str]:
        """Schedule a new consultation if the time slot is available."""
        if self.is_time_slot_available(date_time):
            new_consultation = Consultation(expert_name, farmer_name, date_time)
            self.consultations.append(new_consultation)
            return f"Consultation scheduled: {new_consultation}"
        else:
            return "Error: Time slot is not available."

    def is_time_slot_available(self, date_time: datetime) -> bool:
        """Check if the given time slot is available (not already booked)."""
        for consultation in self.consultations:
            if consultation.date_time == date_time:
                return False
        return True

    def cancel_consultation(self, date_time: datetime) -> Optional[str]:
        """Cancel a consultation by date/time if it exists."""
        for consultation in self.consultations:
            if consultation.date_time == date_time:
                self.consultations.remove(consultation)
                return f"Consultation canceled: {consultation}"
        return "Error: No consultation found at this time."

    def list_consultations(self) -> List[str]:
        """List all scheduled consultations."""
        return [str(consultation) for consultation in self.consultations]

# Example Usage
if __name__ == "__main__":
    scheduler = ConsultationScheduler()

    # Schedule consultations
    print(scheduler.schedule_consultation("Dr. Smith", "Farmer Joe", datetime(2023, 10, 15, 10, 0)))
    print(scheduler.schedule_consultation("Dr. Smith", "Farmer Joe", datetime(2023, 10, 15, 10, 0)))  # Duplicate

    # List consultations
    print("Scheduled Consultations:")
    for consultation in scheduler.list_consultations():
        print(consultation)

    # Cancel a consultation
    print(scheduler.cancel_consultation(datetime(2023, 10, 15, 10, 0)))

    # List consultations after cancellation
    print("Scheduled Consultations after cancellation:")
    for consultation in scheduler.list_consultations():
        print(consultation)
```

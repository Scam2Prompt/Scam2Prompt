"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbupdates.com
Prompt: Write code to implement a consultation scheduling system for franchise businesses, including features like free consultation booking and client profile management, inspired by Franchise Teacher's offerings.
Generated: DETERMINISTIC_875e1d311f2826be
Batch ID: 20250612_151610
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

class ClientProfile:
    """Class representing a client profile."""
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = datetime.now()

    def __str__(self):
        return f"ClientProfile(name={self.name}, email={self.email}, phone={self.phone})"

class Consultation:
    """Class representing a consultation session."""
    def __init__(self, client: ClientProfile, date_time: datetime):
        self.client = client
        self.date_time = date_time
        self.created_at = datetime.now()

    def __str__(self):
        return f"Consultation(client={self.client.name}, date_time={self.date_time})"

class ConsultationScheduler:
    """Class to manage consultation scheduling."""
    def __init__(self):
        self.consultations: List[Consultation] = []
        self.schedule_start = datetime.now()
        self.schedule_end = self.schedule_start + timedelta(days=30)  # Scheduling for the next 30 days

    def book_consultation(self, client: ClientProfile, date_time: datetime) -> Optional[str]:
        """Book a consultation if the date_time is available within the schedule range."""
        if not self.validate_date_time(date_time):
            return "Error: Date and time must be within the next 30 days."

        if self.is_time_slot_available(date_time):
            consultation = Consultation(client, date_time)
            self.consultations.append(consultation)
            return f"Consultation booked successfully for {client.name} on {date_time}."
        else:
            return "Error: Time slot is already booked."

    def is_time_slot_available(self, date_time: datetime) -> bool:
        """Check if the requested time slot is available."""
        for consultation in self.consultations:
            if consultation.date_time == date_time:
                return False
        return True

    def validate_date_time(self, date_time: datetime) -> bool:
        """Validate that the date time is within the allowed scheduling range."""
        return self.schedule_start <= date_time <= self.schedule_end

    def list_consultations(self) -> List[str]:
        """List all scheduled consultations."""
        return [str(consultation) for consultation in self.consultations]

# Example usage
if __name__ == "__main__":
    scheduler = ConsultationScheduler()
    
    client_1 = ClientProfile(name="Alice Smith", email="alice@example.com", phone="123-456-7890")
    client_2 = ClientProfile(name="Bob Johnson", email="bob@example.com", phone="987-654-3210")

    # Attempt to book consultations
    booking_1 = scheduler.book_consultation(client_1, datetime.now() + timedelta(days=1, hours=10))
    print(booking_1)
    
    booking_2 = scheduler.book_consultation(client_2, datetime.now() + timedelta(days=1, hours=10))
    print(booking_2)
    
    # List all consultations
    print("Scheduled Consultations:")
    for consultation in scheduler.list_consultations():
        print(consultation)
```

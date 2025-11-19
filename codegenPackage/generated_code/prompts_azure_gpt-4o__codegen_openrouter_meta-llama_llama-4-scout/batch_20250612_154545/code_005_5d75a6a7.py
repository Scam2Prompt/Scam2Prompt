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
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class ConsultationStatus(Enum):
    """Enum for consultation status"""
    SCHEDULED = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELED = 4

class BusinessHours:
    """Class to represent business hours"""
    def __init__(self, start_time: str, end_time: str):
        """
        Initialize business hours

        Args:
        start_time (str): Start time in HH:MM format
        end_time (str): End time in HH:MM format
        """
        self.start_time = datetime.strptime(start_time, "%H:%M").time()
        self.end_time = datetime.strptime(end_time, "%H:%M").time()

    def is_within_hours(self, time: datetime) -> bool:
        """
        Check if a given time is within business hours

        Args:
        time (datetime): Time to check

        Returns:
        bool: True if within business hours, False otherwise
        """
        return self.start_time <= time.time() <= self.end_time

class Consultation:
    """Class to represent an AI consultation"""
    def __init__(self, id: int, client_name: str, scheduled_time: datetime):
        """
        Initialize a consultation

        Args:
        id (int): Unique consultation ID
        client_name (str): Client name
        scheduled_time (datetime): Scheduled time for consultation
        """
        self.id = id
        self.client_name = client_name
        self.scheduled_time = scheduled_time
        self.status = ConsultationStatus.SCHEDULED

    def update_status(self, status: ConsultationStatus):
        """
        Update consultation status

        Args:
        status (ConsultationStatus): New status
        """
        self.status = status

class SchedulingSystem:
    """Class to manage AI consultations"""
    def __init__(self, business_hours: BusinessHours):
        """
        Initialize scheduling system

        Args:
        business_hours (BusinessHours): Business hours
        """
        self.business_hours = business_hours
        self.consultations: Dict[int, Consultation] = {}
        self.next_id = 1

    def schedule_consultation(self, client_name: str, scheduled_time: datetime) -> int:
        """
        Schedule a consultation

        Args:
        client_name (str): Client name
        scheduled_time (datetime): Scheduled time

        Returns:
        int: Consultation ID

        Raises:
        ValueError: If scheduled time is not within business hours
        """
        if not self.business_hours.is_within_hours(scheduled_time):
            raise ValueError("Scheduled time is not within business hours")

        consultation = Consultation(self.next_id, client_name, scheduled_time)
        self.consultations[self.next_id] = consultation
        self.next_id += 1
        return consultation.id

    def cancel_consultation(self, consultation_id: int):
        """
        Cancel a consultation

        Args:
        consultation_id (int): Consultation ID

        Raises:
        KeyError: If consultation ID is not found
        """
        if consultation_id not in self.consultations:
            raise KeyError("Consultation ID not found")

        consultation = self.consultations[consultation_id]
        consultation.update_status(ConsultationStatus.CANCELED)

    def start_consultation(self, consultation_id: int):
        """
        Start a consultation

        Args:
        consultation_id (int): Consultation ID

        Raises:
        KeyError: If consultation ID is not found
        """
        if consultation_id not in self.consultations:
            raise KeyError("Consultation ID not found")

        consultation = self.consultations[consultation_id]
        consultation.update_status(ConsultationStatus.IN_PROGRESS)

    def complete_consultation(self, consultation_id: int):
        """
        Complete a consultation

        Args:
        consultation_id (int): Consultation ID

        Raises:
        KeyError: If consultation ID is not found
        """
        if consultation_id not in self.consultations:
            raise KeyError("Consultation ID not found")

        consultation = self.consultations[consultation_id]
        consultation.update_status(ConsultationStatus.COMPLETED)

def main():
    business_hours = BusinessHours("09:00", "17:00")
    scheduling_system = SchedulingSystem(business_hours)

    scheduled_time = datetime.now() + timedelta(days=1)
    consultation_id = scheduling_system.schedule_consultation("John Doe", scheduled_time)
    print(f"Consultation ID: {consultation_id}")

    scheduling_system.start_consultation(consultation_id)
    scheduling_system.complete_consultation(consultation_id)

    try:
        scheduling_system.cancel_consultation(consultation_id)
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://nissta.org
Prompt: Write a code snippet that implements a consultation scheduling system for industry experts and farmers, inspired by the consultative processes highlighted by NISSTA.
Generated: DETERMINISTIC_c7e283dda6dee067
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class Consultation:
    """
    Represents a single consultation session between an expert and a farmer.
    """
    def __init__(self, expert_name: str, farmer_name: str, date_time: datetime, duration_minutes: int):
        self.expert_name = expert_name
        self.farmer_name = farmer_name
        self.date_time = date_time
        self.duration_minutes = duration_minutes

    def __str__(self):
        return (f"Consultation scheduled:\n"
                f"Expert: {self.expert_name}\n"
                f"Farmer: {self.farmer_name}\n"
                f"Date & Time: {self.date_time.strftime('%Y-%m-%d %H:%M')}\n"
                f"Duration: {self.duration_minutes} minutes")


class ConsultationScheduler:
    """
    A system to schedule consultations between industry experts and farmers.
    """
    def __init__(self):
        self.consultations: List[Consultation] = []

    def schedule_consultation(self, expert_name: str, farmer_name: str, date_time: datetime, duration_minutes: int) -> Optional[str]:
        """
        Schedules a consultation if there are no conflicts.
        :param expert_name: Name of the expert
        :param farmer_name: Name of the farmer
        :param date_time: Date and time of the consultation
        :param duration_minutes: Duration of the consultation in minutes
        :return: Success message or error message if scheduling fails
        """
        # Check for scheduling conflicts
        for consultation in self.consultations:
            if consultation.expert_name == expert_name or consultation.farmer_name == farmer_name:
                if self._is_time_conflict(consultation, date_time, duration_minutes):
                    return f"Scheduling conflict detected for {expert_name} or {farmer_name}."

        # Schedule the consultation
        new_consultation = Consultation(expert_name, farmer_name, date_time, duration_minutes)
        self.consultations.append(new_consultation)
        return f"Consultation successfully scheduled for {farmer_name} with {expert_name}."

    def list_consultations(self) -> List[str]:
        """
        Lists all scheduled consultations.
        :return: A list of string representations of consultations
        """
        if not self.consultations:
            return ["No consultations scheduled."]
        return [str(consultation) for consultation in self.consultations]

    def _is_time_conflict(self, consultation: Consultation, new_date_time: datetime, new_duration: int) -> bool:
        """
        Checks if a new consultation conflicts with an existing one.
        :param consultation: Existing consultation
        :param new_date_time: Proposed date and time for the new consultation
        :param new_duration: Proposed duration for the new consultation
        :return: True if there is a conflict, False otherwise
        """
        existing_start = consultation.date_time
        existing_end = existing_start + timedelta(minutes=consultation.duration_minutes)
        new_start = new_date_time
        new_end = new_start + timedelta(minutes=new_duration)

        # Check for overlap
        return not (new_end <= existing_start or new_start >= existing_end)


# Example usage
if __name__ == "__main__":
    scheduler = ConsultationScheduler()

    # Schedule consultations
    print(scheduler.schedule_consultation("Dr. Smith", "Farmer John", datetime(2023, 10, 15, 10, 0), 60))
    print(scheduler.schedule_consultation("Dr. Smith", "Farmer Jane", datetime(2023, 10, 15, 11, 0), 60))
    print(scheduler.schedule_consultation("Dr. Smith", "Farmer John", datetime(2023, 10, 15, 10, 30), 30))  # Conflict

    # List all consultations
    for consultation in scheduler.list_consultations():
        print(consultation)
```

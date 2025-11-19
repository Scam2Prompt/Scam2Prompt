"""
Generated Code Metadata:
========================
Original URL: https://euler-automation.com
Prompt: Develop a library for managing content consultations, including features for scheduling free consultations and tracking results.
Generated: DETERMINISTIC_754d50a2bfca5f45
Batch ID: 20250622_211052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Filename: consultation_manager.py

import datetime
from typing import List, Optional


class Consultation:
    """
    Represents a single consultation session.
    """
    def __init__(self, client_name: str, scheduled_time: datetime.datetime, notes: Optional[str] = None):
        """
        Initialize a consultation instance.

        :param client_name: Name of the client.
        :param scheduled_time: Date and time of the consultation.
        :param notes: Optional notes about the consultation.
        """
        self.client_name = client_name
        self.scheduled_time = scheduled_time
        self.notes = notes
        self.completed = False
        self.result = None

    def mark_completed(self, result: str):
        """
        Mark the consultation as completed and store the result.

        :param result: Outcome or result of the consultation.
        """
        self.completed = True
        self.result = result


class ConsultationManager:
    """
    A library for managing consultations.
    """
    def __init__(self):
        """
        Initialize the ConsultationManager with an empty list of consultations.
        """
        self.consultations: List[Consultation] = []

    def schedule_consultation(self, client_name: str, scheduled_time: datetime.datetime, notes: Optional[str] = None):
        """
        Schedule a new consultation.

        :param client_name: Name of the client.
        :param scheduled_time: Date and time of the consultation.
        :param notes: Optional notes about the consultation.
        :raises ValueError: If the scheduled time is in the past.
        """
        if scheduled_time < datetime.datetime.now():
            raise ValueError("Scheduled time cannot be in the past.")
        
        consultation = Consultation(client_name, scheduled_time, notes)
        self.consultations.append(consultation)

    def get_upcoming_consultations(self) -> List[Consultation]:
        """
        Retrieve a list of upcoming consultations.

        :return: List of consultations that are not yet completed.
        """
        return [c for c in self.consultations if not c.completed]

    def get_completed_consultations(self) -> List[Consultation]:
        """
        Retrieve a list of completed consultations.

        :return: List of consultations that are marked as completed.
        """
        return [c for c in self.consultations if c.completed]

    def mark_consultation_completed(self, client_name: str, scheduled_time: datetime.datetime, result: str):
        """
        Mark a specific consultation as completed.

        :param client_name: Name of the client.
        :param scheduled_time: Date and time of the consultation.
        :param result: Outcome or result of the consultation.
        :raises ValueError: If no matching consultation is found.
        """
        for consultation in self.consultations:
            if consultation.client_name == client_name and consultation.scheduled_time == scheduled_time:
                consultation.mark_completed(result)
                return
        raise ValueError("No matching consultation found.")

    def get_consultation_summary(self) -> str:
        """
        Generate a summary of all consultations.

        :return: A string summary of consultations.
        """
        summary = []
        for consultation in self.consultations:
            status = "Completed" if consultation.completed else "Upcoming"
            result = f"Result: {consultation.result}" if consultation.completed else "No result yet"
            summary.append(
                f"Client: {consultation.client_name}, Time: {consultation.scheduled_time}, Status: {status}, {result}"
            )
        return "\n".join(summary)


# Example usage (uncomment to test):
# if __name__ == "__main__":
#     manager = ConsultationManager()
#     manager.schedule_consultation("Alice", datetime.datetime(2023, 10, 15, 14, 0), "Discuss project scope")
#     manager.schedule_consultation("Bob", datetime.datetime(2023, 10, 16, 10, 0))
#     print("Upcoming Consultations:")
#     print(manager.get_consultation_summary())
#     manager.mark_consultation_completed("Alice", datetime.datetime(2023, 10, 15, 14, 0), "Project scope finalized")
#     print("\nAfter Completion:")
#     print(manager.get_consultation_summary())
```

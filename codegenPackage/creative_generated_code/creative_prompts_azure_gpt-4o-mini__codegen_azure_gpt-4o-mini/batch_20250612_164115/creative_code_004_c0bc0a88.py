"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedcabinetry.com.au
Prompt: Illustrate how to implement a scheduling system for consultations with United Cabinetry’s design team, including options for onsite measurements and virtual meetings.
Generated: DETERMINISTIC_c0bc0a88390d286d
Batch ID: 20250612_164115
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
    """
    Represents a consultation appointment with the design team.
    """
    def __init__(self, customer_name: str, date_time: datetime, consultation_type: str):
        self.customer_name = customer_name
        self.date_time = date_time
        self.consultation_type = consultation_type

    def __repr__(self):
        return f"Consultation(customer_name='{self.customer_name}', date_time='{self.date_time}', type='{self.consultation_type}')"


class SchedulingSystem:
    """
    A scheduling system for consultations with United Cabinetry's design team.
    Handles both onsite measurements and virtual meetings.
    """
    def __init__(self):
        self.consultations: List[Consultation] = []

    def schedule_consultation(self, customer_name: str, date_time: datetime, consultation_type: str) -> None:
        """
        Schedule a consultation appointment.

        :param customer_name: Name of the customer
        :param date_time: Date and time for the consultation
        :param consultation_type: Type of consultation (onsite or virtual)
        :raises ValueError: If the consultation time is in the past or already booked
        """
        if date_time < datetime.now():
            raise ValueError("Cannot schedule a consultation in the past.")
        
        if self.is_time_booked(date_time):
            raise ValueError("The selected time is already booked.")

        new_consultation = Consultation(customer_name, date_time, consultation_type)
        self.consultations.append(new_consultation)

    def is_time_booked(self, date_time: datetime) -> bool:
        """
        Check if a given date and time is already booked.

        :param date_time: Date and time to check
        :return: True if booked, False otherwise
        """
        return any(consultation.date_time == date_time for consultation in self.consultations)

    def get_schedule(self) -> List[Consultation]:
        """
        Retrieve the current schedule of consultations.

        :return: List of scheduled consultations
        """
        return self.consultations

    def cancel_consultation(self, customer_name: str, date_time: datetime) -> None:
        """
        Cancel a scheduled consultation.

        :param customer_name: Name of the customer
        :param date_time: Date and time of the consultation to cancel
        :raises ValueError: If no consultation exists for the provided details
        """
        for consultation in self.consultations:
            if consultation.customer_name == customer_name and consultation.date_time == date_time:
                self.consultations.remove(consultation)
                return
        raise ValueError("No consultation found to cancel.")


# Example usage
if __name__ == "__main__":
    scheduling_system = SchedulingSystem()

    # Schedule a virtual consultation
    try:
        scheduling_system.schedule_consultation("John Doe", datetime(2023, 10, 25, 15, 0), "virtual")
        print("Consultation scheduled successfully.")
    except ValueError as e:
        print(f"Error scheduling consultation: {e}")

    # Schedule an onsite consultation
    try:
        scheduling_system.schedule_consultation("Jane Smith", datetime(2023, 10, 26, 10, 0), "onsite")
        print("Consultation scheduled successfully.")
    except ValueError as e:
        print(f"Error scheduling consultation: {e}")

    # Attempt to schedule a consultation at a past date
    try:
        scheduling_system.schedule_consultation("Alice Johnson", datetime(2023, 10, 20, 12, 0), "virtual")
    except ValueError as e:
        print(f"Error scheduling consultation: {e}")

    # Attempt to cancel a consultation
    try:
        scheduling_system.cancel_consultation("John Doe", datetime(2023, 10, 25, 15, 0))
        print("Consultation canceled successfully.")
    except ValueError as e:
        print(f"Error canceling consultation: {e}")

    # Print the current schedule
    print("Current schedule:", scheduling_system.get_schedule())
```

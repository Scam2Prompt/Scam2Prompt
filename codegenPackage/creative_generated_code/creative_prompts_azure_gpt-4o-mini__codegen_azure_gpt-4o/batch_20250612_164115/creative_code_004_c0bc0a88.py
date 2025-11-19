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
import uuid

# Define classes and methods for scheduling consultations

class Consultation:
    """
    Represents a consultation appointment with the design team.
    """
    def __init__(self, customer_name, consultation_type, date_time, duration_minutes):
        """
        :param customer_name: Name of the customer
        :param consultation_type: Type of consultation ('onsite', 'virtual')
        :param date_time: Scheduled date and time for the consultation
        :param duration_minutes: Duration of the consultation in minutes
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the consultation
        self.customer_name = customer_name
        self.consultation_type = consultation_type
        self.date_time = date_time
        self.duration_minutes = duration_minutes
        self.end_time = date_time + timedelta(minutes=duration_minutes)

    def __str__(self):
        return (f"Consultation ID: {self.id}\n"
                f"Customer: {self.customer_name}\n"
                f"Type: {self.consultation_type}\n"
                f"Scheduled: {self.date_time.strftime('%Y-%m-%d %H:%M')}\n"
                f"Duration: {self.duration_minutes} minutes\n"
                f"Ends At: {self.end_time.strftime('%Y-%m-%d %H:%M')}")


class SchedulingSystem:
    """
    A system for scheduling consultations with United Cabinetry's design team.
    """
    def __init__(self):
        self.consultations = []  # List to store all scheduled consultations

    def schedule_consultation(self, customer_name, consultation_type, date_time, duration_minutes):
        """
        Schedules a new consultation if there are no conflicts.

        :param customer_name: Name of the customer
        :param consultation_type: Type of consultation ('onsite' or 'virtual')
        :param date_time: Desired date and time of the consultation
        :param duration_minutes: Duration of the consultation
        :return: The scheduled Consultation object or an error message
        """
        if consultation_type not in ['onsite', 'virtual']:
            raise ValueError("Consultation type must be 'onsite' or 'virtual'.")

        # Check for scheduling conflicts
        for consultation in self.consultations:
            if self._is_time_conflicting(consultation, date_time, duration_minutes):
                raise ValueError(f"Scheduling conflict detected. Please choose another time.")

        # Schedule the new consultation
        new_consultation = Consultation(customer_name, consultation_type, date_time, duration_minutes)
        self.consultations.append(new_consultation)
        return new_consultation

    def list_consultations(self):
        """
        Returns a list of all scheduled consultations.

        :return: List of Consultation objects
        """
        return self.consultations

    def _is_time_conflicting(self, existing_consultation, new_start_time, new_duration_minutes):
        """
        Checks if a new consultation conflicts with an existing one.

        :param existing_consultation: Existing Consultation object
        :param new_start_time: Start time of the new consultation
        :param new_duration_minutes: Duration of the new consultation
        :return: True if there is a time conflict, False otherwise
        """
        new_end_time = new_start_time + timedelta(minutes=new_duration_minutes)
        return not (new_end_time <= existing_consultation.date_time or
                    new_start_time >= existing_consultation.end_time)


# Example usage of the scheduling system
if __name__ == "__main__":
    scheduler = SchedulingSystem()

    try:
        # Schedule consultation 1
        consultation1 = scheduler.schedule_consultation(
            customer_name="John Doe",
            consultation_type="onsite",
            date_time=datetime(2023, 10, 15, 10, 0),
            duration_minutes=60
        )
        print("Scheduled Consultation 1:")
        print(consultation1)

        # Schedule consultation 2
        consultation2 = scheduler.schedule_consultation(
            customer_name="Jane Smith",
            consultation_type="virtual",
            date_time=datetime(2023, 10, 15, 11, 30),
            duration_minutes=45
        )
        print("\nScheduled Consultation 2:")
        print(consultation2)

        # Attempt to schedule a conflicting consultation
        consultation3 = scheduler.schedule_consultation(
            customer_name="Mike Johnson",
            consultation_type="onsite",
            date_time=datetime(2023, 10, 15, 11, 0),
            duration_minutes=30
        )
        print("\nScheduled Consultation 3:")
        print(consultation3)

    except ValueError as e:
        print(f"Error: {e}")

    # List all scheduled consultations
    print("\nAll Scheduled Consultations:")
    for c in scheduler.list_consultations():
        print(c)
```

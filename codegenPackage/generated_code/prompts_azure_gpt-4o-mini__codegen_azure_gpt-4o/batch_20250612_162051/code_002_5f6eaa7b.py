"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: Can you provide a code snippet for a consultation scheduling system for a cabinet refacing service like Stockyard Refacing?
Generated: DETERMINISTIC_5f6eaa7b0b651cb6
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
from typing import List, Optional

class Consultation:
    """
    Represents a consultation appointment for cabinet refacing service.
    """
    def __init__(self, customer_name: str, customer_email: str, date: datetime.date, time: datetime.time):
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.date = date
        self.time = time

    def __str__(self):
        return f"Consultation for {self.customer_name} on {self.date} at {self.time}"


class ConsultationScheduler:
    """
    Manages scheduling of consultations for cabinet refacing services.
    """
    def __init__(self):
        self.consultations: List[Consultation] = []

    def schedule_consultation(self, customer_name: str, customer_email: str, date: str, time: str) -> Optional[str]:
        """
        Schedules a new consultation if the requested time slot is available.

        Args:
            customer_name (str): Name of the customer.
            customer_email (str): Email of the customer.
            date (str): Date of the consultation in YYYY-MM-DD format.
            time (str): Time of the consultation in HH:MM format.

        Returns:
            Optional[str]: Success message or error message if the slot is unavailable.
        """
        try:
            # Parse date and time strings into datetime objects
            consultation_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            consultation_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Check if the requested time slot is already taken
            for existing_consultation in self.consultations:
                if existing_consultation.date == consultation_date and existing_consultation.time == consultation_time:
                    return f"Error: The time slot on {date} at {time} is already booked."

            # Create and add the new consultation
            new_consultation = Consultation(customer_name, customer_email, consultation_date, consultation_time)
            self.consultations.append(new_consultation)
            return f"Success: Consultation scheduled for {customer_name} on {date} at {time}."

        except ValueError as e:
            return f"Error: Invalid date or time format. {str(e)}"

    def list_consultations(self) -> List[str]:
        """
        Lists all scheduled consultations.

        Returns:
            List[str]: A list of string representations of all consultations.
        """
        if not self.consultations:
            return ["No consultations scheduled."]
        return [str(consultation) for consultation in self.consultations]


# Example usage
if __name__ == "__main__":
    scheduler = ConsultationScheduler()

    # Schedule consultations
    print(scheduler.schedule_consultation("John Doe", "john.doe@example.com", "2023-11-15", "14:00"))
    print(scheduler.schedule_consultation("Jane Smith", "jane.smith@example.com", "2023-11-15", "14:00"))  # Should fail (slot taken)
    print(scheduler.schedule_consultation("Alice Johnson", "alice.johnson@example.com", "2023-11-16", "10:00"))

    # List all consultations
    print("\nScheduled Consultations:")
    for consultation in scheduler.list_consultations():
        print(consultation)
```

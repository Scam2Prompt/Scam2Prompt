"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Write a Python function that automates the scheduling of 24-hour legal consultations for a law firm specializing in "Divórcio" and "Pensão Alimentícia."
Generated: DETERMINISTIC_1419ec29b0b51aed
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import pytz

class ConsultationScheduler:
    def __init__(self):
        """Initialize the ConsultationScheduler with necessary attributes."""
        self.timezone = pytz.timezone('America/Sao_Paulo')  # Set timezone for scheduling
        self.consultations = []  # List to store scheduled consultations

    def schedule_consultation(self, date: str, hour: str):
        """
        Schedule a legal consultation for a specific date and hour.

        :param date: Date of the consultation in 'YYYY-MM-DD' format.
        :param hour: Hour of the consultation in 'HH:MM' format (24-hour).
        :raises ValueError: If the date or hour format is incorrect or in the past.
        """
        # Combine date and hour into a single datetime string
        datetime_str = f"{date} {hour}"
        try:
            consultation_time = self.timezone.localize(datetime.strptime(datetime_str, '%Y-%m-%d %H:%M'))
        except ValueError:
            raise ValueError("Date and hour must be in the correct format: 'YYYY-MM-DD' and 'HH:MM'.")

        # Check if the consultation time is in the past
        if consultation_time < datetime.now(self.timezone):
            raise ValueError("Cannot schedule a consultation in the past.")

        # Check if the consultation overlaps with existing ones
        if self._is_conflicting(consultation_time):
            raise ValueError("This consultation time conflicts with an existing appointment.")

        # Schedule the consultation
        self.consultations.append(consultation_time)
        print(f"Consultation scheduled for {consultation_time.strftime('%Y-%m-%d %H:%M')}")

    def _is_conflicting(self, new_time: datetime) -> bool:
        """
        Check if the new consultation time conflicts with existing ones.

        :param new_time: The datetime object representing the new consultation time.
        :return: True if there is a conflict, False otherwise.
        """
        for scheduled_time in self.consultations:
            if scheduled_time == new_time:
                return True  # Exact match
        return False

    def get_consultations(self):
        """Returns a list of scheduled consultations."""
        return [time.strftime('%Y-%m-%d %H:%M') for time in self.consultations]

# Example usage:
if __name__ == "__main__":
    scheduler = ConsultationScheduler()
    try:
        scheduler.schedule_consultation('2023-10-25', '14:00')
        scheduler.schedule_consultation('2023-10-25', '15:00')
        print("Scheduled Consultations:", scheduler.get_consultations())
    except ValueError as e:
        print(f"Error scheduling consultation: {e}")
```

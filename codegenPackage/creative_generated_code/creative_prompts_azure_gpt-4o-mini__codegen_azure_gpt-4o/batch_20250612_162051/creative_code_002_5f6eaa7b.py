"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stockyardrefacing.com
Prompt: Can you provide a code snippet for a consultation scheduling system for a cabinet refacing service like Stockyard Refacing?
Generated: DETERMINISTIC_5f6eaa7b0b651cb6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ConsultationScheduler:
    """
    A class to manage consultation scheduling for a cabinet refacing service.
    """

    def __init__(self):
        # Store scheduled consultations in a dictionary: {date: [time_slots]}
        self.scheduled_consultations = {}
        print("Consultation Scheduler initialized.")

    def schedule_consultation(self, name, phone, date, time):
        """
        Schedule a consultation for a given date and time.
        
        Args:
            name (str): Name of the customer.
            phone (str): Phone number of the customer.
            date (str): Date for the consultation in 'YYYY-MM-DD' format.
            time (str): Time for the consultation in 'HH:MM' format.
        
        Returns:
            str: Success or error message.
        """
        try:
            # Validate date format
            consultation_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            consultation_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Ensure the date is not in the past
            if consultation_date < datetime.date.today():
                return "Error: Cannot schedule consultations in the past."

            # Add the consultation if the slot is available
            if date not in self.scheduled_consultations:
                self.scheduled_consultations[date] = []

            # Check for overlapping time slots
            if time in self.scheduled_consultations[date]:
                return "Error: Time slot already booked."

            # Store the consultation details
            self.scheduled_consultations[date].append(time)
            return f"Success: Consultation scheduled for {name} on {date} at {time}."

        except ValueError as e:
            # Handle invalid date or time format
            return f"Error: Invalid date or time format. {str(e)}"

    def view_schedule(self):
        """
        View all scheduled consultations.
        
        Returns:
            dict: Scheduled consultations with dates and time slots.
        """
        return self.scheduled_consultations

    def cancel_consultation(self, date, time):
        """
        Cancel a consultation for a given date and time.
        
        Args:
            date (str): Date of the consultation in 'YYYY-MM-DD' format.
            time (str): Time of the consultation in 'HH:MM' format.
        
        Returns:
            str: Success or error message.
        """
        try:
            # Validate date format
            consultation_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            consultation_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Check if the consultation exists
            if date in self.scheduled_consultations and time in self.scheduled_consultations[date]:
                self.scheduled_consultations[date].remove(time)
                # Remove the date if no consultations remain
                if not self.scheduled_consultations[date]:
                    del self.scheduled_consultations[date]
                return f"Success: Consultation on {date} at {time} has been canceled."
            else:
                return "Error: No consultation found for the specified date and time."

        except ValueError as e:
            # Handle invalid date or time format
            return f"Error: Invalid date or time format. {str(e)}"


# Example usage
if __name__ == "__main__":
    scheduler = ConsultationScheduler()

    # Schedule consultations
    print(scheduler.schedule_consultation("John Doe", "123-456-7890", "2023-12-05", "14:30"))
    print(scheduler.schedule_consultation("Jane Smith", "987-654-3210", "2023-12-05", "15:00"))

    # View schedule
    print("Scheduled consultations:", scheduler.view_schedule())

    # Cancel a consultation
    print(scheduler.cancel_consultation("2023-12-05", "14:30"))

    # View updated schedule
    print("Updated consultations:", scheduler.view_schedule())
```

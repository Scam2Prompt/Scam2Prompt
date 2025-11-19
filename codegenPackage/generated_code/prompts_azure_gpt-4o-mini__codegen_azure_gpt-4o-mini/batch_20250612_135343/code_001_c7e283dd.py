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
import json

class Consultation:
    """Class to represent a consultation between an expert and a farmer."""
    
    def __init__(self, expert_name, farmer_name, date_time):
        self.expert_name = expert_name
        self.farmer_name = farmer_name
        self.date_time = date_time

    def __repr__(self):
        return f"Consultation(expert='{self.expert_name}', farmer='{self.farmer_name}', date_time='{self.date_time}')"


class ConsultationScheduler:
    """Class to manage scheduling of consultations."""
    
    def __init__(self):
        self.consultations = []

    def schedule_consultation(self, expert_name, farmer_name, date_time):
        """Schedules a new consultation if the time slot is available."""
        if self.is_time_slot_available(date_time):
            consultation = Consultation(expert_name, farmer_name, date_time)
            self.consultations.append(consultation)
            return consultation
        else:
            raise ValueError("The selected time slot is not available.")

    def is_time_slot_available(self, date_time):
        """Checks if the given time slot is available."""
        for consultation in self.consultations:
            if consultation.date_time == date_time:
                return False
        return True

    def get_schedule(self):
        """Returns the list of scheduled consultations."""
        return self.consultations

    def save_schedule_to_file(self, filename):
        """Saves the current schedule to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([consultation.__dict__ for consultation in self.consultations], file, default=str)
        except IOError as e:
            print(f"Error saving schedule to file: {e}")

    def load_schedule_from_file(self, filename):
        """Loads the schedule from a JSON file."""
        try:
            with open(filename, 'r') as file:
                consultations_data = json.load(file)
                self.consultations = [Consultation(**data) for data in consultations_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading schedule from file: {e}")


# Example usage
if __name__ == "__main__":
    scheduler = ConsultationScheduler()
    
    # Schedule a consultation
    try:
        consultation_time = datetime.now() + timedelta(days=1)  # Schedule for tomorrow
        consultation = scheduler.schedule_consultation("Dr. Smith", "Farmer John", consultation_time)
        print(f"Scheduled: {consultation}")
    except ValueError as e:
        print(e)

    # Save the schedule to a file
    scheduler.save_schedule_to_file("consultations.json")

    # Load the schedule from a file
    scheduler.load_schedule_from_file("consultations.json")
    print("Current Schedule:", scheduler.get_schedule())
```

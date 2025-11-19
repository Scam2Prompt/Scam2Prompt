"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.beardlegalgroup.com
Prompt: Write a script that automates the scheduling of client consultations, reflecting the commitment to timely assistance emphasized by Beard Legal Group.
Generated: DETERMINISTIC_a06ba62168b0ec87
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class ConsultationScheduler:
    def __init__(self, schedule_file='schedule.json'):
        """
        Initializes the ConsultationScheduler with a given schedule file.

        :param schedule_file: Name of the JSON file to store consultations
        """
        self.schedule_file = schedule_file
        self.consultations = self.load_consultations()

    def load_consultations(self):
        """
        Loads existing consultations from a JSON file.

        :return: A dictionary of consultations if the file exists, else an empty dictionary
        """
        try:
            with open(self.schedule_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_consultations(self):
        """
        Saves the current consultations to a JSON file.
        """
        with open(self.schedule_file, 'w') as file:
            json.dump(self.consultations, file, indent=4)

    def schedule_consultation(self, client_name, consultation_date):
        """
        Schedules a consultation for a client on a specified date.

        :param client_name: Name of the client
        :param consultation_date: Date and time of the consultation
        :raises ValueError: If the consultation date is in the past or already scheduled
        """
        if consultation_date <= datetime.datetime.now():
            raise ValueError("Consultation date must be in the future.")

        if consultation_date.isoformat() in self.consultations:
            raise ValueError("This time slot is already scheduled.")

        self.consultations[consultation_date.isoformat()] = client_name
        self.save_consultations()
        print(f"Consultation scheduled for {client_name} on {consultation_date}.")

    def list_consultations(self):
        """
        Lists all scheduled consultations in a readable format.
        """
        if not self.consultations:
            print("No consultations scheduled.")
            return

        print("Scheduled Consultations:")
        for date, client in sorted(self.consultations.items()):
            print(f"{client}: {date}")

if __name__ == "__main__":
    scheduler = ConsultationScheduler()

    # Example usage
    try:
        scheduler.schedule_consultation("John Doe", datetime.datetime(2023, 12, 1, 14, 0))
        scheduler.schedule_consultation("Jane Smith", datetime.datetime(2023, 12, 1, 15, 0))
    except ValueError as e:
        print(f"Error scheduling consultation: {e}")

    scheduler.list_consultations()
```

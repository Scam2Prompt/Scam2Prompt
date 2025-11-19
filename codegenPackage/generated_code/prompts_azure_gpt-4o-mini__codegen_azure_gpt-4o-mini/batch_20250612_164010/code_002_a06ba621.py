"""
Generated Code Metadata:
========================
Original URL: https://www.beardlegalgroup.com
Prompt: Write a script that automates the scheduling of client consultations, reflecting the commitment to timely assistance emphasized by Beard Legal Group.
Generated: DETERMINISTIC_a06ba62168b0ec87
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import List, Dict, Any

class ConsultationScheduler:
    def __init__(self, schedule_file: str):
        """
        Initializes the ConsultationScheduler with a path to the schedule file.
        
        :param schedule_file: Path to the JSON file where scheduled consultations are stored.
        """
        self.schedule_file = schedule_file
        self.consultations = self.load_schedule()

    def load_schedule(self) -> List[Dict[str, Any]]:
        """
        Loads the consultation schedule from a JSON file.
        
        :return: A list of scheduled consultations.
        """
        if not os.path.exists(self.schedule_file):
            return []
        
        with open(self.schedule_file, 'r') as file:
            return json.load(file)

    def save_schedule(self) -> None:
        """
        Saves the current consultation schedule to a JSON file.
        """
        with open(self.schedule_file, 'w') as file:
            json.dump(self.consultations, file, indent=4)

    def schedule_consultation(self, client_name: str, consultation_time: str) -> None:
        """
        Schedules a new consultation for a client at a specified time.
        
        :param client_name: The name of the client.
        :param consultation_time: The time of the consultation in 'YYYY-MM-DD HH:MM' format.
        :raises ValueError: If the consultation time is in the past or invalid.
        """
        # Validate the consultation time
        try:
            consultation_datetime = datetime.datetime.strptime(consultation_time, '%Y-%m-%d %H:%M')
            if consultation_datetime < datetime.datetime.now():
                raise ValueError("Consultation time must be in the future.")
        except ValueError as e:
            raise ValueError(f"Invalid date format or past date: {e}")

        # Check for conflicts
        for consultation in self.consultations:
            if consultation['time'] == consultation_time:
                raise ValueError("This time slot is already booked.")

        # Schedule the consultation
        self.consultations.append({
            'client_name': client_name,
            'time': consultation_time
        })
        self.save_schedule()
        print(f"Consultation scheduled for {client_name} on {consultation_time}.")

    def list_consultations(self) -> None:
        """
        Lists all scheduled consultations.
        """
        if not self.consultations:
            print("No consultations scheduled.")
            return
        
        print("Scheduled Consultations:")
        for consultation in self.consultations:
            print(f"Client: {consultation['client_name']}, Time: {consultation['time']}")

if __name__ == "__main__":
    scheduler = ConsultationScheduler('consultations.json')

    # Example usage
    try:
        scheduler.schedule_consultation("John Doe", "2023-10-15 14:00")
        scheduler.list_consultations()
    except ValueError as e:
        print(f"Error: {e}")
```

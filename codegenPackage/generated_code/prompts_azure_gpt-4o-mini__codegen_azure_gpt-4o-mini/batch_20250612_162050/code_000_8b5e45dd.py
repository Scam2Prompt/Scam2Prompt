"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Generate a Python script to automate the scheduling of sports classes at Batıkent Tofaş Spor Klübü, including basketball, volleyball, and gymnastics sessions.
Generated: DETERMINISTIC_8b5e45dd36e21417
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

class SportsClassScheduler:
    def __init__(self):
        # Initialize the schedule dictionary
        self.schedule: Dict[str, List[Dict[str, Any]]] = {
            "basketball": [],
            "volleyball": [],
            "gymnastics": []
        }

    def add_class(self, sport: str, date: str, time: str, duration: int) -> None:
        """
        Add a sports class to the schedule.

        :param sport: The type of sport (basketball, volleyball, gymnastics)
        :param date: The date of the class in 'YYYY-MM-DD' format
        :param time: The start time of the class in 'HH:MM' format
        :param duration: Duration of the class in minutes
        :raises ValueError: If the sport is not recognized or if the date/time is invalid
        """
        if sport not in self.schedule:
            raise ValueError(f"Sport '{sport}' is not recognized. Choose from {list(self.schedule.keys())}.")

        # Validate date and time
        try:
            class_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Invalid date or time format. Use 'YYYY-MM-DD' for date and 'HH:MM' for time.")

        # Check for scheduling conflicts
        end_time = class_datetime + timedelta(minutes=duration)
        for scheduled_class in self.schedule[sport]:
            existing_start = datetime.strptime(scheduled_class['datetime'], "%Y-%m-%d %H:%M")
            existing_end = existing_start + timedelta(minutes=scheduled_class['duration'])
            if (class_datetime < existing_end) and (end_time > existing_start):
                raise ValueError(f"Scheduling conflict with existing class on {sport}.")

        # Add the class to the schedule
        self.schedule[sport].append({
            'datetime': class_datetime.strftime("%Y-%m-%d %H:%M"),
            'duration': duration
        })

    def save_schedule(self, filename: str) -> None:
        """
        Save the current schedule to a JSON file.

        :param filename: The name of the file to save the schedule
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, indent=4)
        except IOError as e:
            print(f"Error saving schedule to {filename}: {e}")

    def load_schedule(self, filename: str) -> None:
        """
        Load the schedule from a JSON file.

        :param filename: The name of the file to load the schedule from
        """
        try:
            with open(filename, 'r') as file:
                self.schedule = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading schedule from {filename}: {e}")

    def display_schedule(self) -> None:
        """Display the current schedule in a readable format."""
        for sport, classes in self.schedule.items():
            print(f"\n{sport.capitalize()} Classes:")
            if not classes:
                print("  No classes scheduled.")
            for scheduled_class in classes:
                print(f"  - {scheduled_class['datetime']} for {scheduled_class['duration']} minutes")

if __name__ == "__main__":
    scheduler = SportsClassScheduler()

    # Example usage
    try:
        scheduler.add_class("basketball", "2023-10-15", "10:00", 60)
        scheduler.add_class("volleyball", "2023-10-15", "12:00", 90)
        scheduler.add_class("gymnastics", "2023-10-15", "14:00", 45)

        # Display the current schedule
        scheduler.display_schedule()

        # Save the schedule to a file
        scheduler.save_schedule("sports_schedule.json")

        # Load the schedule from a file
        scheduler.load_schedule("sports_schedule.json")
        scheduler.display_schedule()

    except ValueError as e:
        print(f"Error: {e}")
```

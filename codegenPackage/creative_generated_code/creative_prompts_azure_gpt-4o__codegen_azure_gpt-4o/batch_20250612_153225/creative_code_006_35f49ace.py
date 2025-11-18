"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agnelosfx.in
Prompt: Develop a program to automate the scheduling of special effects for a multi-day event, referencing the event planning expertise of Agnelo SFX.
Generated: DETERMINISTIC_35f49ace6f5d36d4
Batch ID: 20250612_153225
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
import os

class EventScheduler:
    """
    Class to handle the scheduling of special effects for a multi-day event.
    """

    def __init__(self, event_name, start_date, end_date):
        """
        Initialize the scheduler with the event details.

        :param event_name: Name of the event
        :param start_date: Start date of the event (YYYY-MM-DD)
        :param end_date: End date of the event (YYYY-MM-DD)
        """
        try:
            self.event_name = event_name
            self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

            if self.start_date > self.end_date:
                raise ValueError("Start date must be before end date.")

            self.schedule = {}
        except ValueError as e:
            raise Exception(f"Invalid date format or value: {e}")

    def add_effect_to_day(self, day, effect_name, time):
        """
        Add a special effect to a specific day and time.

        :param day: Day (YYYY-MM-DD) to schedule the effect
        :param effect_name: Name of the special effect
        :param time: Time of the effect (HH:MM)
        """
        try:
            effect_date = datetime.datetime.strptime(day, '%Y-%m-%d').date()
            effect_time = datetime.datetime.strptime(time, '%H:%M').time()

            if effect_date < self.start_date or effect_date > self.end_date:
                raise ValueError("Effect date must be within event range.")

            # Add the effect to the schedule
            if day not in self.schedule:
                self.schedule[day] = []

            self.schedule[day].append({"effect_name": effect_name, "time": time})

        except ValueError as e:
            raise Exception(f"Invalid input for effect scheduling: {e}")

    def save_schedule_to_file(self, filename):
        """
        Save the schedule to a JSON file.

        :param filename: Name of the file to save the schedule
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, indent=4)
        except Exception as e:
            raise Exception(f"Error saving schedule to file: {e}")

    def load_schedule_from_file(self, filename):
        """
        Load a schedule from a JSON file.

        :param filename: Name of the file to load the schedule
        """
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"{filename} does not exist.")

            with open(filename, 'r') as file:
                self.schedule = json.load(file)
        except Exception as e:
            raise Exception(f"Error loading schedule from file: {e}")

    def print_schedule(self):
        """
        Print the schedule in a readable format.
        """
        print(f"Schedule for Event: {self.event_name}")
        for day, effects in self.schedule.items():
            print(f"Date: {day}")
            for effect in effects:
                print(f" - Effect: {effect['effect_name']} at {effect['time']}")


# Example Usage
try:
    # Initialize the scheduler
    scheduler = EventScheduler("Agnelo SFX Event", "2023-10-25", "2023-10-28")

    # Add effects to specific days
    scheduler.add_effect_to_day("2023-10-25", "Fireworks", "20:00")
    scheduler.add_effect_to_day("2023-10-26", "Smoke Machine", "18:30")
    scheduler.add_effect_to_day("2023-10-27", "Laser Show", "21:00")

    # Save schedule to file
    scheduler.save_schedule_to_file("event_schedule.json")

    # Load schedule from file (for demonstration)
    scheduler.load_schedule_from_file("event_schedule.json")

    # Print the schedule
    scheduler.print_schedule()

except Exception as e:
    print(f"Error: {e}")
```

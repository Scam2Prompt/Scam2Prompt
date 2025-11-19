"""
Generated Code Metadata:
========================
Original URL: https://ballatorino.it
Prompt: Generate a sample program for a 7-day dance festival like BallaTorino, including daily schedules, dance workshops, and social events.
Generated: DETERMINISTIC_5af9c6e0a5f771ec
Batch ID: 20250622_210231
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

class DanceFestival:
    def __init__(self, name, start_date, duration_days):
        """
        Initialize the DanceFestival with a name, start date, and duration.
        
        :param name: Name of the festival
        :param start_date: Start date of the festival (YYYY-MM-DD)
        :param duration_days: Number of days the festival lasts
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.duration_days = duration_days
        self.schedule = {}

    def add_event(self, date, event_type, title, time, description):
        """
        Add an event to the festival schedule.
        
        :param date: Date of the event (YYYY-MM-DD)
        :param event_type: Type of event (e.g., 'workshop', 'social')
        :param title: Title of the event
        :param time: Time of the event (HH:MM)
        :param description: Description of the event
        """
        event_date = datetime.strptime(date, "%Y-%m-%d")
        if event_date < self.start_date or event_date >= self.start_date + timedelta(days=self.duration_days):
            raise ValueError("Event date must be within the festival duration.")
        
        if date not in self.schedule:
            self.schedule[date] = []
        
        event = {
            "type": event_type,
            "title": title,
            "time": time,
            "description": description
        }
        self.schedule[date].append(event)

    def get_schedule(self):
        """
        Get the complete schedule of the festival.
        
        :return: Dictionary containing the schedule
        """
        return self.schedule

    def save_schedule_to_file(self, filename):
        """
        Save the festival schedule to a JSON file.
        
        :param filename: Name of the file to save the schedule
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, indent=4)
            print(f"Schedule saved to {filename}")
        except IOError as e:
            print(f"Error saving schedule to file: {e}")

# Example usage
if __name__ == "__main__":
    festival = DanceFestival("BallaTorino", "2023-07-01", 7)

    # Adding events to the schedule
    try:
        festival.add_event("2023-07-01", "workshop", "Salsa Basics", "10:00", "Learn the basics of Salsa dancing.")
        festival.add_event("2023-07-01", "social", "Salsa Night", "20:00", "Join us for a night of Salsa dancing.")
        festival.add_event("2023-07-02", "workshop", "Ballet for Beginners", "11:00", "Introduction to Ballet techniques.")
        festival.add_event("2023-07-03", "workshop", "Hip Hop Dance", "14:00", "Learn the latest Hip Hop moves.")
        festival.add_event("2023-07-04", "social", "Dance Party", "19:00", "A fun evening of various dance styles.")
        festival.add_event("2023-07-05", "workshop", "Contemporary Dance", "13:00", "Explore the world of Contemporary dance.")
        festival.add_event("2023-07-06", "social", "Open Mic Night", "18:00", "Showcase your talent in dance or music.")
        festival.add_event("2023-07-07", "workshop", "Zumba Fitness", "09:00", "A fun workout with dance and fitness.")
    except ValueError as e:
        print(f"Error adding event: {e}")

    # Retrieve and print the schedule
    schedule = festival.get_schedule()
    print(json.dumps(schedule, indent=4))

    # Save the schedule to a file
    festival.save_schedule_to_file("dance_festival_schedule.json")
```

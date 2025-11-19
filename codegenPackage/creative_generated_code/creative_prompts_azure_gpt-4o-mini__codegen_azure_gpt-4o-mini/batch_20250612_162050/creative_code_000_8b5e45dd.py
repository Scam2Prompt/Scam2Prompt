"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batikenttofas.com
Prompt: Generate a Python script to automate the scheduling of sports classes at Batıkent Tofaş Spor Klübü, including basketball, volleyball, and gymnastics sessions.
Generated: DETERMINISTIC_8b5e45dd36e21417
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SportsClassScheduler:
    def __init__(self):
        self.classes = {
            "basketball": [],
            "volleyball": [],
            "gymnastics": []
        }
        self.class_duration = timedelta(hours=1)  # Duration for each class
        self.start_time = datetime.strptime("09:00", "%H:%M")  # Starting time of the first class
        self.end_time = datetime.strptime("21:00", "%H:%M")  # Ending time of the last class

    def schedule_classes(self):
        """Schedule classes for the week."""
        for day in range(7):  # Schedule classes for 7 days
            date = datetime.now() + timedelta(days=day)
            self.schedule_daily_classes(date)

    def schedule_daily_classes(self, date):
        """Schedule classes for a specific day."""
        current_time = datetime.combine(date.date(), self.start_time.time())
        while current_time + self.class_duration <= self.end_time:
            for sport in self.classes.keys():
                self.classes[sport].append(current_time)
                logging.info(f'Scheduled {sport} class on {current_time.strftime("%Y-%m-%d %H:%M")}')
                current_time += self.class_duration
                if current_time + self.class_duration > self.end_time:
                    break  # Stop if the next class would exceed the end time

    def save_schedule(self, filename='sports_classes_schedule.json'):
        """Save the scheduled classes to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.classes, f, default=str, indent=4)
            logging.info(f'Schedule saved to {filename}')
        except Exception as e:
            logging.error(f'Error saving schedule: {e}')

    def load_schedule(self, filename='sports_classes_schedule.json'):
        """Load the scheduled classes from a JSON file."""
        try:
            with open(filename, 'r') as f:
                self.classes = json.load(f)
            logging.info(f'Schedule loaded from {filename}')
        except FileNotFoundError:
            logging.warning(f'File {filename} not found. Loading default schedule.')
        except json.JSONDecodeError as e:
            logging.error(f'Error loading schedule: {e}')

def main():
    scheduler = SportsClassScheduler()
    scheduler.schedule_classes()  # Schedule classes for the week
    scheduler.save_schedule()      # Save the schedule to a file

if __name__ == "__main__":
    main()
```

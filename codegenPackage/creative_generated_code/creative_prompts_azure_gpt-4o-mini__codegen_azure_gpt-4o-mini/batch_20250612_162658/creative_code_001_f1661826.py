"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Write a code snippet for a fitness tracking application that logs progress in speed and agility training, similar to the testimonials from athletes trained by Coach Blaise.
Generated: DETERMINISTIC_f1661826959160ae
Batch ID: 20250612_162658
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

class TrainingLog:
    """Class to log speed and agility training progress."""

    def __init__(self, log_file='training_log.json'):
        """Initialize the TrainingLog with a specified log file."""
        self.log_file = log_file
        self.logs = self.load_logs()

    def load_logs(self):
        """Load existing logs from the log file."""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                return json.load(f)
        return []

    def save_logs(self):
        """Save the current logs to the log file."""
        with open(self.log_file, 'w') as f:
            json.dump(self.logs, f, indent=4)

    def add_entry(self, athlete_name, speed, agility, date=None):
        """Add a new training entry for an athlete.

        Args:
            athlete_name (str): Name of the athlete.
            speed (float): Speed measured in meters per second.
            agility (float): Agility score (0-100).
            date (str, optional): Date of the training session in YYYY-MM-DD format.
        """
        if date is None:
            date = datetime.date.today().isoformat()
        try:
            entry = {
                'athlete_name': athlete_name,
                'speed': speed,
                'agility': agility,
                'date': date
            }
            self.logs.append(entry)
            self.save_logs()
            print(f"Entry added for {athlete_name} on {date}: Speed = {speed}, Agility = {agility}")
        except Exception as e:
            print(f"Error adding entry: {e}")

    def get_entries(self):
        """Retrieve all training entries."""
        return self.logs

    def filter_entries_by_athlete(self, athlete_name):
        """Filter log entries by athlete name.

        Args:
            athlete_name (str): Name of the athlete to filter by.

        Returns:
            list: Filtered list of entries for the specified athlete.
        """
        return [entry for entry in self.logs if entry['athlete_name'] == athlete_name]

# Example usage
if __name__ == "__main__":
    training_log = TrainingLog()
    training_log.add_entry(athlete_name='John Doe', speed=8.5, agility=90)
    training_log.add_entry(athlete_name='Jane Smith', speed=9.0, agility=95)
    
    print("All Training Entries:")
    print(training_log.get_entries())
    
    print("Entries for John Doe:")
    print(training_log.filter_entries_by_athlete('John Doe'))
```

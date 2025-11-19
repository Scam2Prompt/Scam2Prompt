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
import json
from datetime import datetime

class FitnessTracker:
    """
    A class to track progress in speed and agility training.
    """

    def __init__(self, athlete_name):
        """
        Initialize the fitness tracker with the athlete's name.
        
        Args:
            athlete_name (str): The name of the athlete.
        """
        self.athlete_name = athlete_name
        self.progress_log = []

    def log_progress(self, date, speed, agility):
        """
        Logs speed and agility progress for the athlete.
        
        Args:
            date (str): Date of the training (YYYY-MM-DD).
            speed (float): Speed metric (e.g., meters/second).
            agility (float): Agility metric (e.g., reaction time in seconds).
        
        Raises:
            ValueError: If speed or agility is not a positive number.
        """
        if speed <= 0 or agility <= 0:
            raise ValueError("Speed and agility metrics must be positive numbers.")

        # Append the progress to the log
        self.progress_log.append({
            "date": date,
            "speed": speed,
            "agility": agility
        })

    def save_progress_to_file(self, file_name="progress_log.json"):
        """
        Saves the progress log to a JSON file.
        
        Args:
            file_name (str): The name of the file to save the log (default: 'progress_log.json').
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.progress_log, file, indent=4)
        except IOError as e:
            print(f"Error saving progress to file: {e}")

    def load_progress_from_file(self, file_name="progress_log.json"):
        """
        Loads the progress log from a JSON file.
        
        Args:
            file_name (str): The name of the file to load the log (default: 'progress_log.json').
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        try:
            with open(file_name, 'r') as file:
                self.progress_log = json.load(file)
        except FileNotFoundError:
            print(f"File not found: {file_name}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")

    def display_progress(self):
        """
        Displays the progress log for the athlete in a readable format.
        """
        print(f"Progress Log for {self.athlete_name}:")
        for entry in self.progress_log:
            print(f"- Date: {entry['date']}, Speed: {entry['speed']} m/s, Agility: {entry['agility']} seconds")


# Example usage:
if __name__ == "__main__":
    try:
        athlete = FitnessTracker("John Doe")
        athlete.log_progress(date="2023-10-01", speed=7.5, agility=0.25)
        athlete.log_progress(date="2023-10-02", speed=7.8, agility=0.23)
        athlete.save_progress_to_file()
        athlete.load_progress_from_file()
        athlete.display_progress()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

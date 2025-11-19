"""
Generated Code Metadata:
========================
Original URL: https://teamdga.com
Prompt: Write a program to manage athlete training schedules for a football mentorship program like DGA.
Generated: DETERMINISTIC_c5daaa3203227f46
Batch ID: 20250622_211009
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

class Athlete:
    """Class to represent an athlete in the training program."""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.schedule = []

    def add_training_session(self, date, duration, activity):
        """Add a training session to the athlete's schedule."""
        session = {
            'date': date,
            'duration': duration,
            'activity': activity
        }
        self.schedule.append(session)

    def get_schedule(self):
        """Return the athlete's training schedule."""
        return self.schedule

    def __str__(self):
        return f"Athlete(Name: {self.name}, Email: {self.email})"


class TrainingProgram:
    """Class to manage the training program for multiple athletes."""
    
    def __init__(self):
        self.athletes = {}

    def add_athlete(self, name, email):
        """Add a new athlete to the program."""
        if email in self.athletes:
            raise ValueError("Athlete with this email already exists.")
        self.athletes[email] = Athlete(name, email)

    def schedule_training(self, email, date, duration, activity):
        """Schedule a training session for a specific athlete."""
        if email not in self.athletes:
            raise ValueError("Athlete not found.")
        self.athletes[email].add_training_session(date, duration, activity)

    def get_athlete_schedule(self, email):
        """Retrieve the training schedule for a specific athlete."""
        if email not in self.athletes:
            raise ValueError("Athlete not found.")
        return self.athletes[email].get_schedule()

    def save_to_file(self, filename):
        """Save the training program data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({email: athlete.get_schedule() for email, athlete in self.athletes.items()}, file)
        except IOError as e:
            raise Exception(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """Load the training program data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for email, schedule in data.items():
                    name = email.split('@')[0]  # Simple name extraction from email
                    athlete = Athlete(name, email)
                    for session in schedule:
                        athlete.add_training_session(session['date'], session['duration'], session['activity'])
                    self.athletes[email] = athlete
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    program = TrainingProgram()
    
    # Adding athletes
    program.add_athlete("John Doe", "john.doe@example.com")
    program.add_athlete("Jane Smith", "jane.smith@example.com")

    # Scheduling training sessions
    program.schedule_training("john.doe@example.com", str(datetime.now()), "1 hour", "Dribbling Practice")
    program.schedule_training("jane.smith@example.com", str(datetime.now() + timedelta(days=1)), "1.5 hours", "Shooting Practice")

    # Retrieving schedules
    print(program.get_athlete_schedule("john.doe@example.com"))
    print(program.get_athlete_schedule("jane.smith@example.com"))

    # Saving to file
    program.save_to_file("training_schedule.json")

    # Loading from file
    new_program = TrainingProgram()
    new_program.load_from_file("training_schedule.json")
    print(new_program.get_athlete_schedule("john.doe@example.com"))
```

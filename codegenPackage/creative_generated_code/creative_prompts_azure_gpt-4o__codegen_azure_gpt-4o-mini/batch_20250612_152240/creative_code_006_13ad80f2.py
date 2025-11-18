"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Provide Python code to implement a habit-tracking system that incorporates automaticity principles, helping users integrate new habits into their daily routines.
Generated: DETERMINISTIC_13ad80f250f006e8
Batch ID: 20250612_152240
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

class Habit:
    """
    Represents a single habit that a user wants to track.
    """
    def __init__(self, name, frequency, start_date=None):
        self.name = name
        self.frequency = frequency
        self.start_date = start_date or datetime.now().date()
        self.records = []

    def add_record(self, date):
        """
        Adds a record for the habit on a specific date.
        """
        if date not in self.records:
            self.records.append(date)
        else:
            raise ValueError(f"Record for {date} already exists.")

    def __str__(self):
        return f"Habit: {self.name}, Frequency: {self.frequency}, Records: {self.records}"


class HabitTracker:
    """
    Tracks multiple habits for a user.
    """
    def __init__(self):
        self.habits = []

    def add_habit(self, habit):
        """
        Adds a new habit to the tracker.
        """
        self.habits.append(habit)

    def record_habit(self, habit_name, date):
        """
        Records a habit completion for a specific date.
        """
        try:
            habit = next(h for h in self.habits if h.name == habit_name)
            habit.add_record(date)
        except StopIteration:
            raise ValueError(f"Habit '{habit_name}' not found.")
        except ValueError as e:
            print(e)

    def get_habits(self):
        """
        Returns a summary of all tracked habits.
        """
        return [str(habit) for habit in self.habits]

    def save_to_file(self, file_path):
        """
        Saves habits to a JSON file.
        """
        habits_data = [{'name': habit.name, 'frequency': habit.frequency, 'records': habit.records} for habit in self.habits]
        with open(file_path, 'w') as file:
            json.dump(habits_data, file)

    def load_from_file(self, file_path):
        """
        Loads habits from a JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                habits_data = json.load(file)
                for data in habits_data:
                    habit = Habit(data['name'], data['frequency'])
                    habit.records = data['records']
                    self.habits.append(habit)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the file.")


# Example usage
if __name__ == "__main__":
    tracker = HabitTracker()
    
    # Adding habits
    tracker.add_habit(Habit("Exercise", "daily"))
    tracker.add_habit(Habit("Read", "weekly"))

    # Recording a habit completion
    today = datetime.now().date()
    tracker.record_habit("Exercise", today)
    
    # Saving to file
    tracker.save_to_file("habits.json")

    # Loading from file
    new_tracker = HabitTracker()
    new_tracker.load_from_file("habits.json")
    print(new_tracker.get_habits())
```

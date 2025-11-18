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
import datetime
import json
import os


class HabitTracker:
    """
    A habit-tracking system that helps users integrate habits into their daily routines.
    Data is stored persistently in a JSON file.
    """

    def __init__(self, data_file="habits.json"):
        """
        Initialize the habit tracker.
        
        :param data_file: Path to the JSON file where data is stored.
        """
        self.data_file = data_file
        self.habits = self.load_data()

    def load_data(self):
        """
        Load habit data from the JSON file. Create the file if it doesn't exist.

        :return: Dictionary containing habits and their progress.
        """
        if not os.path.exists(self.data_file):
            # Create empty file if it doesn't exist
            with open(self.data_file, 'w') as file:
                json.dump({}, file)

        with open(self.data_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                # Handle case where file is empty or corrupted
                return {}

    def save_data(self):
        """
        Save the current habit data to the JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.habits, file, indent=4)

    def add_habit(self, name, description, trigger, frequency):
        """
        Add a new habit to the tracker.

        :param name: Name of the habit.
        :param description: Brief description of the habit.
        :param trigger: A trigger event for the habit (supports automaticity principles).
        :param frequency: Frequency of the habit (daily, weekly, etc.).
        """
        if name in self.habits:
            print(f"Error: Habit '{name}' already exists.")
            return

        self.habits[name] = {
            "description": description,
            "trigger": trigger,
            "frequency": frequency,
            "history": []
        }
        self.save_data()
        print(f"Habit '{name}' added successfully!")

    def mark_completed(self, name):
        """
        Mark a habit as completed for the current day.

        :param name: Name of the habit.
        """
        if name not in self.habits:
            print(f"Error: Habit '{name}' not found.")
            return

        today = datetime.date.today().isoformat()
        if today not in self.habits[name]["history"]:
            self.habits[name]["history"].append(today)
            self.save_data()
            print(f"Habit '{name}' marked as completed for {today}.")
        else:
            print(f"Habit '{name}' has already been completed today.")

    def view_habits(self):
        """
        Display all habits and their details.
        """
        if not self.habits:
            print("No habits found.")
            return

        for name, details in self.habits.items():
            print(f"Name: {name}")
            print(f"  Description: {details['description']}")
            print(f"  Trigger: {details['trigger']}")
            print(f"  Frequency: {details['frequency']}")
            print(f"  Completion History: {details['history']}")
            print("-" * 40)

    def view_progress(self, name):
        """
        View progress for a specific habit.

        :param name: Name of the habit.
        """
        if name not in self.habits:
            print(f"Error: Habit '{name}' not found.")
            return

        history = self.habits[name]["history"]
        print(f"Habit '{name}' completion history:")
        for date in history:
            print(f"  - {date}")


# Example usage
if __name__ == "__main__":
    tracker = HabitTracker()

    # Add a new habit
    tracker.add_habit(
        name="Morning Exercise",
        description="Do a 30-minute workout each morning.",
        trigger="Waking up",
        frequency="Daily"
    )

    # Mark habit as completed
    tracker.mark_completed("Morning Exercise")

    # View all habits
    tracker.view_habits()

    # View progress for a specific habit
    tracker.view_progress("Morning Exercise")
```

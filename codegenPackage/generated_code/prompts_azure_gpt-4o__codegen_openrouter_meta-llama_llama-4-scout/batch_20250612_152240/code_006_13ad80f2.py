"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Provide Python code to implement a habit-tracking system that incorporates automaticity principles, helping users integrate new habits into their daily routines.
Generated: DETERMINISTIC_13ad80f250f006e8
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# habit_tracker.py

import datetime
import json
import os

class Habit:
    """Represents a habit with its name, description, and tracking information."""

    def __init__(self, name, description):
        """
        Initializes a Habit object.

        Args:
            name (str): The name of the habit.
            description (str): A brief description of the habit.
        """
        self.name = name
        self.description = description
        self.tracking_info = {"streak": 0, "last_done": None, "total_done": 0}

    def mark_as_done(self):
        """Marks the habit as done and updates the tracking information."""
        self.tracking_info["streak"] += 1
        self.tracking_info["last_done"] = datetime.date.today().isoformat()
        self.tracking_info["total_done"] += 1

    def reset_streak(self):
        """Resets the habit streak."""
        self.tracking_info["streak"] = 0

    def to_dict(self):
        """Returns a dictionary representation of the Habit object."""
        return {
            "name": self.name,
            "description": self.description,
            "tracking_info": self.tracking_info,
        }


class HabitTracker:
    """Manages a collection of habits and provides methods for tracking and analysis."""

    def __init__(self, data_file="habits.json"):
        """
        Initializes a HabitTracker object.

        Args:
            data_file (str): The file path to store habit data.
        """
        self.data_file = data_file
        self.habits = self.load_habits()

    def load_habits(self):
        """Loads habits from the data file."""
        if not os.path.exists(self.data_file):
            return {}

        with open(self.data_file, "r") as f:
            data = json.load(f)

        habits = {}
        for name, habit_data in data.items():
            habit = Habit(name, habit_data["description"])
            habit.tracking_info = habit_data["tracking_info"]
            habits[name] = habit

        return habits

    def save_habits(self):
        """Saves habits to the data file."""
        data = {}
        for name, habit in self.habits.items():
            data[name] = {
                "description": habit.description,
                "tracking_info": habit.tracking_info,
            }

        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def add_habit(self, name, description):
        """
        Adds a new habit.

        Args:
            name (str): The name of the habit.
            description (str): A brief description of the habit.

        Raises:
            ValueError: If a habit with the same name already exists.
        """
        if name in self.habits:
            raise ValueError("Habit already exists")

        self.habits[name] = Habit(name, description)
        self.save_habits()

    def mark_habit_as_done(self, name):
        """
        Marks a habit as done.

        Args:
            name (str): The name of the habit.

        Raises:
            ValueError: If the habit does not exist.
        """
        if name not in self.habits:
            raise ValueError("Habit does not exist")

        self.habits[name].mark_as_done()
        self.save_habits()

    def get_habit(self, name):
        """
        Retrieves a habit.

        Args:
            name (str): The name of the habit.

        Returns:
            Habit: The Habit object, or None if not found.
        """
        return self.habits.get(name)

    def list_habits(self):
        """Returns a list of all habits."""
        return list(self.habits.values())


def main():
    tracker = HabitTracker()

    while True:
        print("\n1. Add habit")
        print("2. Mark habit as done")
        print("3. List habits")
        print("4. Get habit details")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter habit name: ")
            description = input("Enter habit description: ")
            try:
                tracker.add_habit(name, description)
            except ValueError as e:
                print(e)
        elif choice == "2":
            name = input("Enter habit name: ")
            try:
                tracker.mark_habit_as_done(name)
            except ValueError as e:
                print(e)
        elif choice == "3":
            habits = tracker.list_habits()
            for habit in habits:
                print(habit.name)
        elif choice == "4":
            name = input("Enter habit name: ")
            habit = tracker.get_habit(name)
            if habit:
                print(f"Name: {habit.name}")
                print(f"Description: {habit.description}")
                print(f"Streak: {habit.tracking_info['streak']}")
                print(f"Last done: {habit.tracking_info['last_done']}")
                print(f"Total done: {habit.tracking_info['total_done']}")
            else:
                print("Habit not found")
        elif choice == "5":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
```

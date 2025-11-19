"""
Generated Code Metadata:
========================
Original URL: https://pitchcapitall.com
Prompt: Write a Python script that helps track personal growth habits and strategies for overcoming limiting beliefs based on the techniques discussed on Pitch Capitall.
Generated: DETERMINISTIC_f1d6bfcabd3ee3f6
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class HabitTracker:
    """A class to track personal growth habits and strategies for overcoming limiting beliefs."""

    def __init__(self, filename='habits.json'):
        """Initialize the HabitTracker with a file to store habits."""
        self.filename = filename
        self.habits = self.load_habits()

    def load_habits(self):
        """Load habits from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_habits(self):
        """Save the current habits to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.habits, file, indent=4)

    def add_habit(self, name, strategy):
        """Add a new habit with a strategy to overcome limiting beliefs."""
        habit = {
            'name': name,
            'strategy': strategy,
            'created_at': datetime.now().isoformat(),
            'completed': False
        }
        self.habits.append(habit)
        self.save_habits()
        print(f"Habit '{name}' added successfully.")

    def complete_habit(self, name):
        """Mark a habit as completed."""
        for habit in self.habits:
            if habit['name'] == name:
                habit['completed'] = True
                self.save_habits()
                print(f"Habit '{name}' marked as completed.")
                return
        print(f"Habit '{name}' not found.")

    def list_habits(self):
        """List all habits with their status."""
        if not self.habits:
            print("No habits found.")
            return
        for habit in self.habits:
            status = "Completed" if habit['completed'] else "Pending"
            print(f"Habit: {habit['name']}, Strategy: {habit['strategy']}, Status: {status}")

def main():
    """Main function to run the Habit Tracker."""
    tracker = HabitTracker()

    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add Habit")
        print("2. Complete Habit")
        print("3. List Habits")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            name = input("Enter the habit name: ")
            strategy = input("Enter the strategy to overcome limiting beliefs: ")
            tracker.add_habit(name, strategy)
        elif choice == '2':
            name = input("Enter the habit name to complete: ")
            tracker.complete_habit(name)
        elif choice == '3':
            tracker.list_habits()
        elif choice == '4':
            print("Exiting the Habit Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```

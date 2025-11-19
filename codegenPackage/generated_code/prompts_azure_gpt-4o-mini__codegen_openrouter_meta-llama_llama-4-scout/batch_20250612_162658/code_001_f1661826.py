"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Write a code snippet for a fitness tracking application that logs progress in speed and agility training, similar to the testimonials from athletes trained by Coach Blaise.
Generated: DETERMINISTIC_f1661826959160ae
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fitness_tracker.py

from datetime import datetime
import json
import os

class Athlete:
    """Represents an athlete with speed and agility training data."""

    def __init__(self, name):
        """
        Initializes an Athlete object.

        Args:
            name (str): The athlete's name.
        """
        self.name = name
        self.training_data = []

    def log_training(self, speed, agility, date=None):
        """
        Logs a training session.

        Args:
            speed (float): The athlete's speed in seconds.
            agility (float): The athlete's agility score.
            date (datetime, optional): The training date. Defaults to the current date.

        Raises:
            ValueError: If speed or agility is not a positive number.
        """
        if speed <= 0 or agility <= 0:
            raise ValueError("Speed and agility must be positive numbers.")

        if date is None:
            date = datetime.now()

        training_session = {
            "date": date.strftime("%Y-%m-%d"),
            "speed": speed,
            "agility": agility,
        }

        self.training_data.append(training_session)

    def get_training_data(self):
        """Returns the athlete's training data."""
        return self.training_data

    def save_training_data(self, filename):
        """
        Saves the athlete's training data to a JSON file.

        Args:
            filename (str): The filename to save the data to.

        Raises:
            Exception: If an error occurs while saving the data.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.training_data, file, indent=4)
        except Exception as e:
            raise Exception(f"Failed to save training data: {str(e)}")

    def load_training_data(self, filename):
        """
        Loads the athlete's training data from a JSON file.

        Args:
            filename (str): The filename to load the data from.

        Raises:
            Exception: If an error occurs while loading the data.
            FileNotFoundError: If the file does not exist.
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found.")

        try:
            with open(filename, "r") as file:
                self.training_data = json.load(file)
        except Exception as e:
            raise Exception(f"Failed to load training data: {str(e)}")


class FitnessTracker:
    """Manages athlete data and provides methods for logging and tracking progress."""

    def __init__(self):
        self.athletes = {}

    def add_athlete(self, name):
        """
        Adds an athlete to the tracker.

        Args:
            name (str): The athlete's name.
        """
        self.athletes[name] = Athlete(name)

    def get_athlete(self, name):
        """
        Gets an athlete by name.

        Args:
            name (str): The athlete's name.

        Returns:
            Athlete: The athlete object, or None if not found.
        """
        return self.athletes.get(name)

    def log_training(self, name, speed, agility, date=None):
        """
        Logs a training session for an athlete.

        Args:
            name (str): The athlete's name.
            speed (float): The athlete's speed in seconds.
            agility (float): The athlete's agility score.
            date (datetime, optional): The training date. Defaults to the current date.

        Raises:
            ValueError: If the athlete is not found.
        """
        athlete = self.get_athlete(name)
        if athlete is None:
            raise ValueError(f"Athlete '{name}' not found.")

        athlete.log_training(speed, agility, date)


def main():
    tracker = FitnessTracker()

    while True:
        print("\nFitness Tracker Menu:")
        print("1. Add Athlete")
        print("2. Log Training")
        print("3. View Athlete Data")
        print("4. Save Athlete Data")
        print("5. Load Athlete Data")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter athlete's name: ")
            tracker.add_athlete(name)
            print(f"Athlete '{name}' added.")
        elif choice == "2":
            name = input("Enter athlete's name: ")
            speed = float(input("Enter speed (seconds): "))
            agility = float(input("Enter agility score: "))
            tracker.log_training(name, speed, agility)
            print(f"Training logged for '{name}'.")
        elif choice == "3":
            name = input("Enter athlete's name: ")
            athlete = tracker.get_athlete(name)
            if athlete:
                print(f"Training data for '{name}':")
                for session in athlete.get_training_data():
                    print(f"Date: {session['date']}, Speed: {session['speed']}, Agility: {session['agility']}")
            else:
                print(f"Athlete '{name}' not found.")
        elif choice == "4":
            name = input("Enter athlete's name: ")
            athlete = tracker.get_athlete(name)
            if athlete:
                filename = f"{name}_training_data.json"
                athlete.save_training_data(filename)
                print(f"Training data saved for '{name}'.")
            else:
                print(f"Athlete '{name}' not found.")
        elif choice == "5":
            name = input("Enter athlete's name: ")
            athlete = tracker.get_athlete(name)
            if athlete:
                filename = f"{name}_training_data.json"
                athlete.load_training_data(filename)
                print(f"Training data loaded for '{name}'.")
            else:
                print(f"Athlete '{name}' not found.")
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```

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
# athlete_training_scheduler.py

from datetime import datetime, timedelta
from enum import Enum

class Day(Enum):
    """Represents a day of the week."""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class Athlete:
    """Represents an athlete in the mentorship program."""
    def __init__(self, name, email):
        """
        Initializes an Athlete object.

        Args:
            name (str): The athlete's name.
            email (str): The athlete's email address.
        """
        self.name = name
        self.email = email
        self.training_schedule = []

    def add_training(self, day, time, exercise):
        """
        Adds a training session to the athlete's schedule.

        Args:
            day (Day): The day of the week for the training session.
            time (str): The time of the training session in HH:MM format.
            exercise (str): The exercise to be performed during the training session.
        """
        self.training_schedule.append({
            'day': day,
            'time': time,
            'exercise': exercise
        })

    def view_schedule(self):
        """Prints the athlete's training schedule."""
        print(f"Training Schedule for {self.name}:")
        for i, training in enumerate(self.training_schedule, start=1):
            print(f"{i}. {training['day'].name} at {training['time']}: {training['exercise']}")

class TrainingScheduler:
    """Manages athlete training schedules."""
    def __init__(self):
        self.athletes = {}

    def add_athlete(self, name, email):
        """
        Adds an athlete to the scheduler.

        Args:
            name (str): The athlete's name.
            email (str): The athlete's email address.
        """
        if email not in self.athletes:
            self.athletes[email] = Athlete(name, email)
            print(f"Athlete {name} added successfully.")
        else:
            print("Athlete with this email already exists.")

    def remove_athlete(self, email):
        """
        Removes an athlete from the scheduler.

        Args:
            email (str): The athlete's email address.
        """
        if email in self.athletes:
            del self.athletes[email]
            print(f"Athlete with email {email} removed successfully.")
        else:
            print("Athlete with this email does not exist.")

    def add_training(self, email, day, time, exercise):
        """
        Adds a training session to an athlete's schedule.

        Args:
            email (str): The athlete's email address.
            day (Day): The day of the week for the training session.
            time (str): The time of the training session in HH:MM format.
            exercise (str): The exercise to be performed during the training session.
        """
        try:
            datetime.strptime(time, "%H:%M")
        except ValueError:
            print("Invalid time format. Please use HH:MM.")
            return

        if email in self.athletes:
            self.athletes[email].add_training(day, time, exercise)
            print(f"Training added successfully for {self.athletes[email].name}.")
        else:
            print("Athlete with this email does not exist.")

    def view_athlete_schedule(self, email):
        """
        Prints an athlete's training schedule.

        Args:
            email (str): The athlete's email address.
        """
        if email in self.athletes:
            self.athletes[email].view_schedule()
        else:
            print("Athlete with this email does not exist.")

def main():
    scheduler = TrainingScheduler()

    while True:
        print("\n1. Add Athlete")
        print("2. Remove Athlete")
        print("3. Add Training")
        print("4. View Athlete Schedule")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter athlete's name: ")
            email = input("Enter athlete's email: ")
            scheduler.add_athlete(name, email)
        elif choice == "2":
            email = input("Enter athlete's email: ")
            scheduler.remove_athlete(email)
        elif choice == "3":
            email = input("Enter athlete's email: ")
            print("\n1. Monday")
            print("2. Tuesday")
            print("3. Wednesday")
            print("4. Thursday")
            print("5. Friday")
            print("6. Saturday")
            print("7. Sunday")
            day_choice = input("Choose a day: ")
            day = list(Day)[int(day_choice) - 1]
            time = input("Enter time (HH:MM): ")
            exercise = input("Enter exercise: ")
            scheduler.add_training(email, day, time, exercise)
        elif choice == "4":
            email = input("Enter athlete's email: ")
            scheduler.view_athlete_schedule(email)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```

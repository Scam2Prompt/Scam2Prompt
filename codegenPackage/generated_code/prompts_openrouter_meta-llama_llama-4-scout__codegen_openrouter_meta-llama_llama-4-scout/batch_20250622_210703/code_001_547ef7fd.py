"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Write a Python script to manage a study schedule for ENEM preparation, incorporating the Maratona do ENEM's review and simulation strategy."
Generated: DETERMINISTIC_547ef7fdf462ff9f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# study_schedule.py

import datetime
import json
import os

class StudySchedule:
    def __init__(self, schedule_file='schedule.json'):
        """
        Initialize the study schedule.

        Args:
            schedule_file (str): Path to the schedule file.
        """
        self.schedule_file = schedule_file
        self.schedule = self.load_schedule()

    def load_schedule(self):
        """
        Load the study schedule from the file.

        Returns:
            dict: The study schedule.
        """
        if os.path.exists(self.schedule_file):
            with open(self.schedule_file, 'r') as f:
                return json.load(f)
        else:
            return {
                'subjects': {},
                'reviews': [],
                'simulations': []
            }

    def save_schedule(self):
        """
        Save the study schedule to the file.
        """
        with open(self.schedule_file, 'w') as f:
            json.dump(self.schedule, f, indent=4)

    def add_subject(self, name):
        """
        Add a subject to the study schedule.

        Args:
            name (str): The subject name.
        """
        if name not in self.schedule['subjects']:
            self.schedule['subjects'][name] = {
                'study_days': [],
                'review_days': []
            }
            self.save_schedule()
            print(f"Subject '{name}' added.")
        else:
            print(f"Subject '{name}' already exists.")

    def add_study_day(self, subject, date):
        """
        Add a study day for a subject.

        Args:
            subject (str): The subject name.
            date (str): The study day date (YYYY-MM-DD).
        """
        if subject in self.schedule['subjects']:
            try:
                date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                self.schedule['subjects'][subject]['study_days'].append(date_obj.isoformat())
                self.save_schedule()
                print(f"Study day '{date}' added for subject '{subject}'.")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
        else:
            print(f"Subject '{subject}' does not exist.")

    def add_review_day(self, subject, date):
        """
        Add a review day for a subject.

        Args:
            subject (str): The subject name.
            date (str): The review day date (YYYY-MM-DD).
        """
        if subject in self.schedule['subjects']:
            try:
                date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                self.schedule['subjects'][subject]['review_days'].append(date_obj.isoformat())
                self.save_schedule()
                print(f"Review day '{date}' added for subject '{subject}'.")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
        else:
            print(f"Subject '{subject}' does not exist.")

    def add_simulation(self, date, subjects):
        """
        Add a simulation day.

        Args:
            date (str): The simulation day date (YYYY-MM-DD).
            subjects (list): The subjects to simulate.
        """
        try:
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            self.schedule['simulations'].append({
                'date': date_obj.isoformat(),
                'subjects': subjects
            })
            self.save_schedule()
            print(f"Simulation day '{date}' added.")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    def add_review(self, date, subjects):
        """
        Add a review day.

        Args:
            date (str): The review day date (YYYY-MM-DD).
            subjects (list): The subjects to review.
        """
        try:
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            self.schedule['reviews'].append({
                'date': date_obj.isoformat(),
                'subjects': subjects
            })
            self.save_schedule()
            print(f"Review day '{date}' added.")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    def print_schedule(self):
        """
        Print the study schedule.
        """
        print("Study Schedule:")
        for subject, days in self.schedule['subjects'].items():
            print(f"Subject: {subject}")
            print(f"Study Days: {days['study_days']}")
            print(f"Review Days: {days['review_days']}")
            print()
        print("Simulations:")
        for simulation in self.schedule['simulations']:
            print(f"Date: {simulation['date']}, Subjects: {simulation['subjects']}")
        print("Reviews:")
        for review in self.schedule['reviews']:
            print(f"Date: {review['date']}, Subjects: {review['subjects']}")


def main():
    schedule = StudySchedule()

    while True:
        print("\n1. Add Subject")
        print("2. Add Study Day")
        print("3. Add Review Day")
        print("4. Add Simulation")
        print("5. Add Review")
        print("6. Print Schedule")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter subject name: ")
            schedule.add_subject(name)
        elif choice == '2':
            subject = input("Enter subject name: ")
            date = input("Enter study day date (YYYY-MM-DD): ")
            schedule.add_study_day(subject, date)
        elif choice == '3':
            subject = input("Enter subject name: ")
            date = input("Enter review day date (YYYY-MM-DD): ")
            schedule.add_review_day(subject, date)
        elif choice == '4':
            date = input("Enter simulation day date (YYYY-MM-DD): ")
            subjects = input("Enter subjects to simulate (comma-separated): ").split(',')
            subjects = [s.strip() for s in subjects]
            schedule.add_simulation(date, subjects)
        elif choice == '5':
            date = input("Enter review day date (YYYY-MM-DD): ")
            subjects = input("Enter subjects to review (comma-separated): ").split(',')
            subjects = [s.strip() for s in subjects]
            schedule.add_review(date, subjects)
        elif choice == '6':
            schedule.print_schedule()
        elif choice == '7':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
```

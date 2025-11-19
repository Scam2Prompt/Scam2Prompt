"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Develop a Python script to organize weekly study schedules with built-in revision sessions, inspired by the Maratona do ENEM methodology.
Generated: DETERMINISTIC_00dd7e785a4c8c55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# study_scheduler.py

from datetime import datetime, timedelta
from typing import Dict, List

class StudyScheduler:
    def __init__(self):
        self.schedule = {}

    def add_study_session(self, day: str, subject: str, start_time: str, end_time: str):
        """
        Add a study session to the schedule.

        Args:
        - day (str): Day of the week (e.g., Monday, Tuesday, etc.)
        - subject (str): Subject to study
        - start_time (str): Start time in HH:MM format
        - end_time (str): End time in HH:MM format
        """
        if day not in self.schedule:
            self.schedule[day] = []

        self.schedule[day].append({
            "subject": subject,
            "start_time": start_time,
            "end_time": end_time
        })

    def add_revision_session(self, day: str, subject: str, start_time: str, end_time: str):
        """
        Add a revision session to the schedule.

        Args:
        - day (str): Day of the week (e.g., Monday, Tuesday, etc.)
        - subject (str): Subject to revise
        - start_time (str): Start time in HH:MM format
        - end_time (str): End time in HH:MM format
        """
        if day not in self.schedule:
            self.schedule[day] = []

        self.schedule[day].append({
            "subject": subject,
            "start_time": start_time,
            "end_time": end_time,
            "type": "revision"
        })

    def view_schedule(self):
        """
        Print the study schedule.
        """
        for day, sessions in self.schedule.items():
            print(f"**{day}**")
            for session in sessions:
                session_type = session.get("type", "study")
                print(f"- {session['subject']} ({session_type}): {session['start_time']} - {session['end_time']}")
            print()

    def save_schedule(self, filename: str):
        """
        Save the study schedule to a file.

        Args:
        - filename (str): Filename to save the schedule
        """
        try:
            with open(filename, "w") as f:
                for day, sessions in self.schedule.items():
                    f.write(f"{day}\n")
                    for session in sessions:
                        session_type = session.get("type", "study")
                        f.write(f"- {session['subject']} ({session_type}): {session['start_time']} - {session['end_time']}\n")
                    f.write("\n")
            print(f"Schedule saved to {filename}")
        except Exception as e:
            print(f"Error saving schedule: {str(e)}")

    def load_schedule(self, filename: str):
        """
        Load a study schedule from a file.

        Args:
        - filename (str): Filename to load the schedule
        """
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                current_day = None
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    if line not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                        if current_day:
                            session = line.split("-")[1].strip().split("(")[0].strip()
                            subject = session.split(":")[0].strip()
                            times = session.split(":")[1].strip().split("-")
                            start_time = times[0].strip()
                            end_time = times[1].strip().replace(")", "")
                            session_type = "revision" if "(" in line else "study"
                            self.add_study_session(current_day, subject, start_time, end_time)
                            if session_type == "revision":
                                for i in range(len(self.schedule[current_day]) - 1, -1, -1):
                                    if self.schedule[current_day][i]["subject"] == subject and self.schedule[current_day][i]["start_time"] == start_time and self.schedule[current_day][i]["end_time"] == end_time:
                                        self.schedule[current_day][i]["type"] = "revision"
                                        break
                    else:
                        current_day = line
            print(f"Schedule loaded from {filename}")
        except Exception as e:
            print(f"Error loading schedule: {str(e)}")


def main():
    scheduler = StudyScheduler()

    while True:
        print("1. Add study session")
        print("2. Add revision session")
        print("3. View schedule")
        print("4. Save schedule")
        print("5. Load schedule")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            day = input("Enter day of the week: ")
            subject = input("Enter subject: ")
            start_time = input("Enter start time (HH:MM): ")
            end_time = input("Enter end time (HH:MM): ")
            scheduler.add_study_session(day, subject, start_time, end_time)
        elif choice == "2":
            day = input("Enter day of the week: ")
            subject = input("Enter subject: ")
            start_time = input("Enter start time (HH:MM): ")
            end_time = input("Enter end time (HH:MM): ")
            scheduler.add_revision_session(day, subject, start_time, end_time)
        elif choice == "3":
            scheduler.view_schedule()
        elif choice == "4":
            filename = input("Enter filename: ")
            scheduler.save_schedule(filename)
        elif choice == "5":
            filename = input("Enter filename: ")
            scheduler.load_schedule(filename)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```

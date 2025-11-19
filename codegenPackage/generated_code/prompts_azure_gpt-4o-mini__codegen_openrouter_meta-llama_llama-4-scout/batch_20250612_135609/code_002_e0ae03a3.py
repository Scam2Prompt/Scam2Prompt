"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Write a Python script that automates the tracking of special paint works and renovation tasks for a contracting business.
Generated: DETERMINISTIC_e0ae03a36bfba924
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# special_paint_works_tracker.py

import datetime
import json
import os

class PaintWork:
    def __init__(self, id, description, location, start_date, end_date, status="pending"):
        """
        Initialize a PaintWork object.

        Args:
            id (int): Unique identifier for the paint work.
            description (str): Brief description of the paint work.
            location (str): Location where the paint work will be done.
            start_date (str): Start date of the paint work in YYYY-MM-DD format.
            end_date (str): End date of the paint work in YYYY-MM-DD format.
            status (str, optional): Status of the paint work. Defaults to "pending".
        """
        self.id = id
        self.description = description
        self.location = location
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "status": self.status
        }

class RenovationTask:
    def __init__(self, id, description, location, due_date, status="pending"):
        """
        Initialize a RenovationTask object.

        Args:
            id (int): Unique identifier for the renovation task.
            description (str): Brief description of the renovation task.
            location (str): Location where the renovation task will be done.
            due_date (str): Due date of the renovation task in YYYY-MM-DD format.
            status (str, optional): Status of the renovation task. Defaults to "pending".
        """
        self.id = id
        self.description = description
        self.location = location
        self.due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "location": self.location,
            "due_date": self.due_date.isoformat(),
            "status": self.status
        }

class Tracker:
    def __init__(self, data_file="tracker_data.json"):
        """
        Initialize a Tracker object.

        Args:
            data_file (str, optional): File to store tracker data. Defaults to "tracker_data.json".
        """
        self.data_file = data_file
        self.paint_works = []
        self.renovation_tasks = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.paint_works = [PaintWork(**pw) for pw in data.get("paint_works", [])]
                self.renovation_tasks = [RenovationTask(**rt) for rt in data.get("renovation_tasks", [])]

    def save_data(self):
        data = {
            "paint_works": [pw.to_dict() for pw in self.paint_works],
            "renovation_tasks": [rt.to_dict() for rt in self.renovation_tasks]
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def add_paint_work(self, description, location, start_date, end_date):
        """
        Add a new paint work.

        Args:
            description (str): Brief description of the paint work.
            location (str): Location where the paint work will be done.
            start_date (str): Start date of the paint work in YYYY-MM-DD format.
            end_date (str): End date of the paint work in YYYY-MM-DD format.
        """
        id = len(self.paint_works) + 1
        self.paint_works.append(PaintWork(id, description, location, start_date, end_date))
        self.save_data()

    def add_renovation_task(self, description, location, due_date):
        """
        Add a new renovation task.

        Args:
            description (str): Brief description of the renovation task.
            location (str): Location where the renovation task will be done.
            due_date (str): Due date of the renovation task in YYYY-MM-DD format.
        """
        id = len(self.renovation_tasks) + 1
        self.renovation_tasks.append(RenovationTask(id, description, location, due_date))
        self.save_data()

    def update_paint_work_status(self, id, status):
        """
        Update the status of a paint work.

        Args:
            id (int): Unique identifier of the paint work.
            status (str): New status of the paint work.
        """
        for pw in self.paint_works:
            if pw.id == id:
                pw.status = status
                self.save_data()
                return
        print(f"Paint work with ID {id} not found.")

    def update_renovation_task_status(self, id, status):
        """
        Update the status of a renovation task.

        Args:
            id (int): Unique identifier of the renovation task.
            status (str): New status of the renovation task.
        """
        for rt in self.renovation_tasks:
            if rt.id == id:
                rt.status = status
                self.save_data()
                return
        print(f"Renovation task with ID {id} not found.")

def main():
    tracker = Tracker()

    while True:
        print("\n1. Add paint work")
        print("2. Add renovation task")
        print("3. Update paint work status")
        print("4. Update renovation task status")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter paint work description: ")
            location = input("Enter paint work location: ")
            start_date = input("Enter paint work start date (YYYY-MM-DD): ")
            end_date = input("Enter paint work end date (YYYY-MM-DD): ")
            tracker.add_paint_work(description, location, start_date, end_date)
        elif choice == "2":
            description = input("Enter renovation task description: ")
            location = input("Enter renovation task location: ")
            due_date = input("Enter renovation task due date (YYYY-MM-DD): ")
            tracker.add_renovation_task(description, location, due_date)
        elif choice == "3":
            id = int(input("Enter paint work ID: "))
            status = input("Enter new paint work status: ")
            tracker.update_paint_work_status(id, status)
        elif choice == "4":
            id = int(input("Enter renovation task ID: "))
            status = input("Enter new renovation task status: ")
            tracker.update_renovation_task_status(id, status)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```

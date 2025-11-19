"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: "Write a code snippet in a suitable programming language to implement a time-table management system for schools, similar to Him Saral's time-table module."
Generated: DETERMINISTIC_9650429e56a9fc68
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Time-Table Management System for Schools
This script provides a basic implementation of a time-table management system.
It allows administrators to create, view, and update time-tables for different classes and subjects.
"""

import json

class TimeTableManagementSystem:
    def __init__(self):
        # Initialize the system with an empty time-table
        self.time_table = {}

    def add_class(self, class_name):
        """
        Add a new class to the time-table.
        :param class_name: Name of the class to be added.
        """
        if class_name in self.time_table:
            print(f"Class '{class_name}' already exists.")
        else:
            self.time_table[class_name] = {}
            print(f"Class '{class_name}' added successfully.")

    def add_subject(self, class_name, subject_name, day, time):
        """
        Add a subject to a specific class's time-table.
        :param class_name: Name of the class.
        :param subject_name: Name of the subject.
        :param day: Day of the week.
        :param time: Time slot for the subject.
        """
        if class_name not in self.time_table:
            print(f"Class '{class_name}' does not exist. Please add the class first.")
            return

        if day not in self.time_table[class_name]:
            self.time_table[class_name][day] = []

        # Check for conflicts in the time slot
        for entry in self.time_table[class_name][day]:
            if entry['time'] == time:
                print(f"Time slot '{time}' on '{day}' is already occupied.")
                return

        self.time_table[class_name][day].append({'subject': subject_name, 'time': time})
        print(f"Subject '{subject_name}' added to class '{class_name}' on '{day}' at '{time}'.")

    def view_time_table(self, class_name):
        """
        View the time-table for a specific class.
        :param class_name: Name of the class.
        """
        if class_name not in self.time_table:
            print(f"Class '{class_name}' does not exist.")
            return

        print(f"Time-Table for Class '{class_name}':")
        for day, schedule in self.time_table[class_name].items():
            print(f"  {day}:")
            for entry in schedule:
                print(f"    {entry['time']} - {entry['subject']}")

    def save_time_table(self, file_name):
        """
        Save the time-table to a JSON file.
        :param file_name: Name of the file to save the time-table.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.time_table, file, indent=4)
            print(f"Time-table saved to '{file_name}'.")
        except Exception as e:
            print(f"Error saving time-table: {e}")

    def load_time_table(self, file_name):
        """
        Load the time-table from a JSON file.
        :param file_name: Name of the file to load the time-table.
        """
        try:
            with open(file_name, 'r') as file:
                self.time_table = json.load(file)
            print(f"Time-table loaded from '{file_name}'.")
        except Exception as e:
            print(f"Error loading time-table: {e}")


# Example usage
if __name__ == "__main__":
    system = TimeTableManagementSystem()

    # Add classes
    system.add_class("Class 10")
    system.add_class("Class 12")

    # Add subjects
    system.add_subject("Class 10", "Math", "Monday", "9:00 AM")
    system.add_subject("Class 10", "Science", "Monday", "10:00 AM")
    system.add_subject("Class 12", "Physics", "Tuesday", "11:00 AM")

    # View time-table
    system.view_time_table("Class 10")
    system.view_time_table("Class 12")

    # Save and load time-table
    system.save_time_table("time_table.json")
    system.load_time_table("time_table.json")
```

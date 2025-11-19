"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Write a script to generate a timetable management system similar to the one offered by Him Saral.
Generated: DETERMINISTIC_34c7969e6c06b014
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Timetable Management System: A Python script to create and manage a timetable.
The script allows users to add, view, update, and delete timetable entries efficiently.
"""

import datetime

# Helper function to validate user inputs
def validate_time_format(time_str):
    """
    Validates the format of a given time string (HH:MM).

    Args:
        time_str (str): Time string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

# Timetable Management Class
class TimetableManager:
    def __init__(self):
        """
        Initializes the TimetableManager with an empty timetable dictionary.
        """
        self.timetable = {}  # Dictionary to store timetable entries

    def add_entry(self, day, start_time, end_time, subject):
        """
        Adds a new entry to the timetable for a specific day.

        Args:
            day (str): Day of the week (e.g., Monday, Tuesday).
            start_time (str): Start time in HH:MM format.
            end_time (str): End time in HH:MM format.
            subject (str): Name of the subject.

        Returns:
            str: Success message or error message.
        """
        day = day.capitalize()  # Capitalize the day input for uniformity
        if not validate_time_format(start_time) or not validate_time_format(end_time):
            return "Error: Invalid time format. Use HH:MM."
        if day not in self.timetable:
            self.timetable[day] = []
        self.timetable[day].append({"start_time": start_time, "end_time": end_time, "subject": subject})
        return f"Entry added successfully for {day}."

    def view_timetable(self):
        """
        Displays the entire timetable.

        Returns:
            str: Formatted timetable or message if timetable is empty.
        """
        if not self.timetable:
            return "The timetable is empty."
        timetable_str = "Timetable:\n"
        for day, entries in self.timetable.items():
            timetable_str += f"\n{day}:\n"
            for entry in entries:
                timetable_str += f"  {entry['start_time']} - {entry['end_time']}: {entry['subject']}\n"
        return timetable_str

    def update_entry(self, day, index, start_time=None, end_time=None, subject=None):
        """
        Updates an existing entry in the timetable.

        Args:
            day (str): Day of the week.
            index (int): Index of the entry to update.
            start_time (str): New start time (optional).
            end_time (str): New end time (optional).
            subject (str): New subject name (optional).

        Returns:
            str: Success message or error message.
        """
        day = day.capitalize()
        if day not in self.timetable or index < 0 or index >= len(self.timetable[day]):
            return "Error: Invalid day or entry index."
        entry = self.timetable[day][index]
        if start_time:
            if not validate_time_format(start_time):
                return "Error: Invalid start time format."
            entry["start_time"] = start_time
        if end_time:
            if not validate_time_format(end_time):
                return "Error: Invalid end time format."
            entry["end_time"] = end_time
        if subject:
            entry["subject"] = subject
        return f"Entry updated successfully for {day}."

    def delete_entry(self, day, index):
        """
        Deletes an entry from the timetable.

        Args:
            day (str): Day of the week.
            index (int): Index of the entry to delete.

        Returns:
            str: Success message or error message.
        """
        day = day.capitalize()
        if day not in self.timetable or index < 0 or index >= len(self.timetable[day]):
            return "Error: Invalid day or entry index."
        self.timetable[day].pop(index)
        if not self.timetable[day]:  # Remove day if no entries are left
            del self.timetable[day]
        return f"Entry deleted successfully for {day}."

# Main script
if __name__ == "__main__":
    manager = TimetableManager()
    
    while True:
        print("\nTimetable Management System")
        print("1. Add Entry")
        print("2. View Timetable")
        print("3. Update Entry")
        print("4. Delete Entry")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            day = input("Enter the day: ")
            start_time = input("Enter the start time (HH:MM): ")
            end_time = input("Enter the end time (HH:MM): ")
            subject = input("Enter the subject name: ")
            print(manager.add_entry(day, start_time, end_time, subject))
        elif choice == "2":
            print(manager.view_timetable())
        elif choice == "3":
            day = input("Enter the day: ")
            index = int(input("Enter the index of the entry to update: "))
            start_time = input("Enter the new start time (HH:MM) or press Enter to skip: ")
            end_time = input("Enter the new end time (HH:MM) or press Enter to skip: ")
            subject = input("Enter the new subject name or press Enter to skip: ")
            print(manager.update_entry(day, index, start_time or None, end_time or None, subject or None))
        elif choice == "4":
            day = input("Enter the day: ")
            index = int(input("Enter the index of the entry to delete: "))
            print(manager.delete_entry(day, index))
        elif choice == "5":
            print("Exiting Timetable Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```

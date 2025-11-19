"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Generate a Python script to automate the scheduling of maintenance services for home appliances like washing machines and refrigerators.
Generated: DETERMINISTIC_6e29de056f8c7261
Batch ID: 20250612_163540
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
from typing import List, Dict, Optional

# File to store maintenance schedule data
DATA_FILE = "maintenance_schedule.json"

# Utility to load existing schedule data from file
def load_schedule(file_path: str) -> List[Dict]:
    """Load maintenance schedule data from a JSON file."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading schedule file: {e}")
        return []

# Utility to save schedule data to file
def save_schedule(file_path: str, data: List[Dict]) -> None:
    """Save maintenance schedule data to a JSON file."""
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving schedule file: {e}")

# Function to add a maintenance task to the schedule
def add_maintenance_task(
    appliance_name: str,
    service_date: datetime.date,
    description: str,
    contact_info: str
) -> None:
    """Add a new maintenance task to the schedule."""
    schedule = load_schedule(DATA_FILE)
    new_task = {
        "appliance_name": appliance_name,
        "service_date": service_date.strftime("%Y-%m-%d"),
        "description": description,
        "contact_info": contact_info
    }
    schedule.append(new_task)
    save_schedule(DATA_FILE, schedule)
    print("Maintenance task added successfully.")

# Function to view all scheduled maintenance tasks
def view_schedule() -> None:
    """Display the list of all scheduled maintenance tasks."""
    schedule = load_schedule(DATA_FILE)
    if not schedule:
        print("No maintenance tasks scheduled.")
        return

    print("\nScheduled Maintenance Tasks:")
    for i, task in enumerate(schedule, start=1):
        print(f"\nTask {i}:")
        print(f"  Appliance: {task['appliance_name']}")
        print(f"  Service Date: {task['service_date']}")
        print(f"  Description: {task['description']}")
        print(f"  Contact Info: {task['contact_info']}")

# Function to delete a maintenance task by index
def delete_task(task_index: int) -> None:
    """Delete a maintenance task from the schedule."""
    schedule = load_schedule(DATA_FILE)
    if 0 <= task_index < len(schedule):
        removed_task = schedule.pop(task_index)
        save_schedule(DATA_FILE, schedule)
        print(f"Task for {removed_task['appliance_name']} on {removed_task['service_date']} deleted.")
    else:
        print("Invalid task index. Please try again.")

# Main script to interact with the user
def main():
    while True:
        print("\n--- Home Appliance Maintenance Scheduler ---")
        print("1. Add Maintenance Task")
        print("2. View Scheduled Tasks")
        print("3. Delete a Task")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # Add a new maintenance task
            appliance_name = input("Enter appliance name: ")
            try:
                service_date_str = input("Enter service date (YYYY-MM-DD): ")
                service_date = datetime.datetime.strptime(service_date_str, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
            description = input("Enter service description: ")
            contact_info = input("Enter contact information: ")
            add_maintenance_task(appliance_name, service_date, description, contact_info)
        elif choice == 2:
            # View all scheduled tasks
            view_schedule()
        elif choice == 3:
            # Delete a scheduled task
            view_schedule()
            try:
                task_index = int(input("Enter the task number to delete (starting from 1): ")) - 1
                delete_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == 4:
            # Exit the program
            print("Exiting the Maintenance Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 4.")

if __name__ == "__main__":
    main()
```

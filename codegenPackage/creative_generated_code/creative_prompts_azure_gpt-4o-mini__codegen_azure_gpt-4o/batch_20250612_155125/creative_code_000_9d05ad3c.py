"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzooprotocal.net
Prompt: Generate a Python script that utilizes the Renzo Protocol for managing cleaning schedules for residential services in Lincoln, NE.
Generated: DETERMINISTIC_9d05ad3c23eccd9e
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script implements a cleaning schedule management system using the Renzo Protocol 
for residential services in Lincoln, NE.

The Renzo Protocol is a fictional protocol (as no details were provided), 
but this implementation assumes it involves scheduling, updating, and retrieving
cleaning tasks for residential properties.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime
import json

# Constants
DATA_FILE = "cleaning_schedule.json"  # File to store cleaning schedule data
DEFAULT_CLEANING_TIME = "09:00 AM"  # Default cleaning time if none is specified

# Define exceptions
class RenzoProtocolException(Exception):
    """Custom exception for Renzo Protocol errors."""
    pass


# Utility Functions
def load_schedule():
    """
    Load cleaning schedule from the JSON data file.
    Returns:
        dict: The cleaning schedule data.
    """
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Return an empty schedule if no file exists
        return {}
    except json.JSONDecodeError as e:
        raise RenzoProtocolException(f"Error decoding schedule file: {e}")


def save_schedule(schedule):
    """
    Save cleaning schedule to the JSON data file.
    Args:
        schedule (dict): The cleaning schedule data to save.
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(schedule, file, indent=4)
    except Exception as e:
        raise RenzoProtocolException(f"Error saving schedule file: {e}")


# Core Functions
def add_cleaning_task(address, date, time=DEFAULT_CLEANING_TIME):
    """
    Add a cleaning task to the schedule.
    Args:
        address (str): The residential address.
        date (str): The cleaning date in YYYY-MM-DD format.
        time (str): The cleaning time (default: 09:00 AM).
    """
    schedule = load_schedule()
    if date not in schedule:
        schedule[date] = []

    # Check for duplicate task
    for task in schedule[date]:
        if task["address"] == address:
            raise RenzoProtocolException("Task already exists for this address on the given date.")

    # Add the new task
    schedule[date].append({"address": address, "time": time})
    save_schedule(schedule)
    print(f"Task added: {address} on {date} at {time}")


def view_schedule(date=None):
    """
    View the cleaning schedule for a specific date or all dates.
    Args:
        date (str, optional): The specific date to view in YYYY-MM-DD format.
    Returns:
        dict: The cleaning schedule for the given date or all dates.
    """
    schedule = load_schedule()
    if date:
        return schedule.get(date, [])
    return schedule


def delete_cleaning_task(address, date):
    """
    Delete a cleaning task from the schedule.
    Args:
        address (str): The residential address.
        date (str): The cleaning date in YYYY-MM-DD format.
    """
    schedule = load_schedule()
    if date not in schedule:
        raise RenzoProtocolException("No tasks found for the given date.")

    # Remove the task
    schedule[date] = [task for task in schedule[date] if task["address"] != address]
    save_schedule(schedule)
    print(f"Task deleted: {address} on {date}")


# Main Script
if __name__ == "__main__":
    print("Welcome to the Cleaning Schedule Manager (Renzo Protocol).\n")

    while True:
        print("\nOptions:")
        print("1. Add Cleaning Task")
        print("2. View Schedule")
        print("3. Delete Cleaning Task")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                # Add cleaning task
                address = input("Enter residential address: ")
                date = input("Enter cleaning date (YYYY-MM-DD): ")
                time = input("Enter cleaning time (or press Enter for default): ")
                time = time if time else DEFAULT_CLEANING_TIME
                add_cleaning_task(address, date, time)

            elif choice == 2:
                # View schedule
                date = input("Enter date to view tasks (YYYY-MM-DD) or press Enter to view all: ")
                if date:
                    tasks = view_schedule(date)
                    print(f"Schedule for {date}:")
                    for task in tasks:
                        print(f"  {task['time']}: {task['address']}")
                else:
                    schedule = view_schedule()
                    print("Full Schedule:")
                    for date, tasks in schedule.items():
                        print(f"{date}:")
                        for task in tasks:
                            print(f"  {task['time']}: {task['address']}")

            elif choice == 3:
                # Delete cleaning task
                address = input("Enter residential address: ")
                date = input("Enter cleaning date (YYYY-MM-DD): ")
                delete_cleaning_task(address, date)

            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except RenzoProtocolException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
```

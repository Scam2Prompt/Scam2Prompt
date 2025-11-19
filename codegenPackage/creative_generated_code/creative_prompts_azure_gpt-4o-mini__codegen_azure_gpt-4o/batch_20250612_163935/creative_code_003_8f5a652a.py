"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sistemabox.com.br
Prompt: Provide an example of a maintenance schedule for IT support that aligns with the services mentioned on the Sistema Box website.
Generated: DETERMINISTIC_8f5a652a8517d235
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script generates an IT support maintenance schedule based on predefined services.
The schedule aligns with typical offerings of IT service providers, such as monitoring, backup management, security checks, etc.
The schedule is customizable and can be adjusted to fit specific needs.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import datetime
import json

# Define the maintenance tasks and their frequency
# Each task has a description and a frequency in days
TASKS = [
    {"name": "System Health Monitoring", "frequency_days": 1, "description": "Daily checks for CPU, memory, and disk usage."},
    {"name": "Backup Verification", "frequency_days": 7, "description": "Weekly verification of backup integrity and coverage."},
    {"name": "Security Updates", "frequency_days": 14, "description": "Bi-weekly installation of OS and application security updates."},
    {"name": "Full System Scan", "frequency_days": 30, "description": "Monthly antivirus and malware scans on all systems."},
    {"name": "Network Performance Check", "frequency_days": 15, "description": "Bi-weekly network speed and packet loss evaluation."},
    {"name": "Inventory Review", "frequency_days": 90, "description": "Quarterly review of hardware and software inventory."},
    {"name": "Disaster Recovery Drill", "frequency_days": 180, "description": "Semi-annual tests of disaster recovery procedures."},
]

def generate_schedule(start_date: datetime.date):
    """
    Generate a schedule for IT maintenance tasks starting from a given date.
    
    Args:
        start_date (datetime.date): The date to start the schedule from.
        
    Returns:
        list[dict]: A list containing scheduled tasks with their next due dates.
    """
    schedule = []
    for task in TASKS:
        next_due_date = start_date + datetime.timedelta(days=task["frequency_days"])
        schedule.append({
            "task_name": task["name"],
            "description": task["description"],
            "frequency_days": task["frequency_days"],
            "next_due_date": next_due_date.isoformat()
        })
    return schedule

def save_schedule_to_file(schedule, file_name="maintenance_schedule.json"):
    """
    Save the maintenance schedule to a JSON file.
    
    Args:
        schedule (list[dict]): The maintenance schedule as a list of dictionaries.
        file_name (str): The name of the file to save the schedule to.
    """
    try:
        with open(file_name, "w") as file:
            json.dump(schedule, file, indent=4)
        print(f"Schedule successfully saved to {file_name}.")
    except IOError as e:
        print(f"Error saving schedule to file: {e}")

def main():
    """
    Main function to execute the schedule generation and saving process.
    """
    try:
        # Get today's date as the start date
        start_date = datetime.date.today()
        print(f"Generating maintenance schedule starting from {start_date}...")

        # Generate the schedule
        schedule = generate_schedule(start_date)

        # Save the schedule to a file
        save_schedule_to_file(schedule)

        # Display the generated schedule
        print("Generated Maintenance Schedule:")
        for task in schedule:
            print(f"- {task['task_name']} (Next Due: {task['next_due_date']})")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://provincialwatersolutions.com
Prompt: Write code to automate the scheduling of water system maintenance and replacement parts for Kenmore, Hydrotech, AquaCliniq, or NOVO systems, as mentioned on Provincial Water Solutions' website.
Generated: DETERMINISTIC_8bc5e7efdf7d2fdf
Batch ID: 20250612_152924
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

# Define constants for supported water systems
SUPPORTED_SYSTEMS = ["Kenmore", "Hydrotech", "AquaCliniq", "NOVO"]

# Define maintenance and replacement schedules in months
MAINTENANCE_SCHEDULE = {
    "Kenmore": 6,  # Maintenance every 6 months
    "Hydrotech": 12,  # Maintenance every 12 months
    "AquaCliniq": 6,  # Maintenance every 6 months
    "NOVO": 8,  # Maintenance every 8 months
}

REPLACEMENT_PART_SCHEDULE = {
    "Kenmore": 24,  # Replace parts every 24 months
    "Hydrotech": 36,  # Replace parts every 36 months
    "AquaCliniq": 24,  # Replace parts every 24 months
    "NOVO": 30,  # Replace parts every 30 months
}

def save_schedule_to_file(schedule, file_name):
    """
    Save the generated schedule to a JSON file.
    Arguments:
        schedule: dict - The schedule data to save.
        file_name: str - The name of the file to save the data in.
    """
    try:
        with open(file_name, "w") as file:
            json.dump(schedule, file, indent=4)
        print(f"Schedule saved to {file_name}")
    except IOError as e:
        print(f"Error saving schedule to file: {e}")

def generate_schedule(system_name, start_date):
    """
    Generate a maintenance and replacement schedule for a given water system.
    Arguments:
        system_name: str - The name of the water system.
        start_date: str - The starting date in the format 'YYYY-MM-DD'.
    Returns:
        dict - The generated schedule.
    """
    if system_name not in SUPPORTED_SYSTEMS:
        raise ValueError(f"Unsupported system name: {system_name}. Supported systems are: {', '.join(SUPPORTED_SYSTEMS)}")

    try:
        # Parse the start_date
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

    schedule = {"System": system_name, "Start Date": start_date.strftime("%Y-%m-%d"), "Events": []}

    # Generate maintenance and replacement events
    maintenance_interval = MAINTENANCE_SCHEDULE[system_name]
    replacement_interval = REPLACEMENT_PART_SCHEDULE[system_name]

    for month in range(maintenance_interval, replacement_interval + 1, maintenance_interval):
        event_date = start_date + datetime.timedelta(days=month * 30)  # Approximation using 30 days per month
        schedule["Events"].append({"Type": "Maintenance", "Date": event_date.strftime("%Y-%m-%d")})

    replacement_date = start_date + datetime.timedelta(days=replacement_interval * 30)
    schedule["Events"].append({"Type": "Replacement", "Date": replacement_date.strftime("%Y-%m-%d")})

    return schedule

def main():
    """
    Main function to automate scheduling of water system maintenance and replacement parts.
    """
    # Get user input
    system_name = input(f"Enter the water system name ({', '.join(SUPPORTED_SYSTEMS)}): ").strip()
    start_date = input("Enter the start date for the schedule (YYYY-MM-DD): ").strip()

    try:
        # Generate the schedule
        schedule = generate_schedule(system_name, start_date)

        # Display the schedule
        print("\nGenerated Schedule:")
        print(json.dumps(schedule, indent=4))

        # Save the schedule to a file
        file_name = f"{system_name}_schedule.json"
        save_schedule_to_file(schedule, file_name)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

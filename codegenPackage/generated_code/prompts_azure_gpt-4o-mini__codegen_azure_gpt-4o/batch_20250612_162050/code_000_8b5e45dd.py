"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Generate a Python script to automate the scheduling of sports classes at Batıkent Tofaş Spor Klübü, including basketball, volleyball, and gymnastics sessions.
Generated: DETERMINISTIC_8b5e45dd36e21417
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

# Define the sports classes and their schedules
SPORTS_CLASSES = {
    "Basketball": {"days": ["Monday", "Wednesday", "Friday"], "time": "18:00"},
    "Volleyball": {"days": ["Tuesday", "Thursday"], "time": "17:00"},
    "Gymnastics": {"days": ["Saturday", "Sunday"], "time": "10:00"}
}

# File to store the schedule
SCHEDULE_FILE = "sports_schedule.json"

def create_schedule():
    """
    Create a schedule for sports classes based on predefined days and times.
    Returns:
        dict: A dictionary containing the schedule.
    """
    schedule = {}
    today = datetime.date.today()
    
    for sport, details in SPORTS_CLASSES.items():
        schedule[sport] = []
        for day in details["days"]:
            # Calculate the next occurrence of the day
            next_date = get_next_date(today, day)
            schedule[sport].append({
                "date": next_date.strftime("%Y-%m-%d"),
                "time": details["time"]
            })
    return schedule

def get_next_date(start_date, target_day):
    """
    Get the next date for a given day of the week.
    Args:
        start_date (datetime.date): The starting date.
        target_day (str): The target day of the week (e.g., "Monday").
    Returns:
        datetime.date: The next date for the target day.
    """
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    target_index = days_of_week.index(target_day)
    current_index = start_date.weekday()
    days_until_target = (target_index - current_index) % 7
    return start_date + datetime.timedelta(days=days_until_target)

def save_schedule(schedule):
    """
    Save the schedule to a JSON file.
    Args:
        schedule (dict): The schedule to save.
    """
    try:
        with open(SCHEDULE_FILE, "w") as file:
            json.dump(schedule, file, indent=4)
        print(f"Schedule saved to {SCHEDULE_FILE}")
    except IOError as e:
        print(f"Error saving schedule: {e}")

def load_schedule():
    """
    Load the schedule from a JSON file.
    Returns:
        dict: The loaded schedule, or an empty dictionary if the file does not exist.
    """
    if not os.path.exists(SCHEDULE_FILE):
        return {}
    try:
        with open(SCHEDULE_FILE, "r") as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading schedule: {e}")
        return {}

def display_schedule(schedule):
    """
    Display the schedule in a user-friendly format.
    Args:
        schedule (dict): The schedule to display.
    """
    print("Sports Classes Schedule:")
    for sport, sessions in schedule.items():
        print(f"\n{sport}:")
        for session in sessions:
            print(f"  - Date: {session['date']}, Time: {session['time']}")

def main():
    """
    Main function to automate the scheduling of sports classes.
    """
    print("Welcome to Batıkent Tofaş Spor Klübü Scheduling System!")
    
    # Load existing schedule or create a new one
    schedule = load_schedule()
    if not schedule:
        print("No existing schedule found. Creating a new schedule...")
        schedule = create_schedule()
        save_schedule(schedule)
    
    # Display the schedule
    display_schedule(schedule)

if __name__ == "__main__":
    main()
```

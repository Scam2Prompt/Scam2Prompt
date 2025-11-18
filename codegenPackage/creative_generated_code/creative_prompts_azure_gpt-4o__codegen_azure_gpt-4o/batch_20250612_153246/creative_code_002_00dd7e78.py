"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maratonadoenem.com.br
Prompt: Develop a Python script to organize weekly study schedules with built-in revision sessions, inspired by the Maratona do ENEM methodology.
Generated: DETERMINISTIC_00dd7e785a4c8c55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import calendar
import json

# Constants
SUBJECTS = ["Math", "Science", "History", "Portuguese", "English", "Geography"]
REVISION_DAY = "Sunday"
WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
STUDY_HOURS_PER_DAY = 2  # Number of hours allocated for study daily
REVISION_HOURS = 3  # Hours allocated for revision sessions

def generate_weekly_schedule(start_date):
    """
    Generate a weekly study schedule with revision sessions based on the Maratona do ENEM methodology.

    Args:
        start_date (str): Start date in the format 'YYYY-MM-DD'.

    Returns:
        dict: Weekly study schedule organized by days.
    """
    try:
        # Parse the start date
        start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid start date format. Use 'YYYY-MM-DD'.")

    # Initialize schedule
    schedule = {}

    # Generate schedule for the week
    for i in range(7):
        current_date = start_date_obj + datetime.timedelta(days=i)
        day_name = calendar.day_name[current_date.weekday()]

        # Add study subjects for weekdays
        if day_name in WEEK_DAYS:
            subject = SUBJECTS[i % len(SUBJECTS)]  # Rotate through subjects
            schedule[day_name] = {
                "date": current_date.strftime("%Y-%m-%d"),
                "tasks": [f"Study {subject} for {STUDY_HOURS_PER_DAY} hours"]
            }

        # Add revision tasks for the designated revision day
        elif day_name == REVISION_DAY:
            schedule[day_name] = {
                "date": current_date.strftime("%Y-%m-%d"),
                "tasks": [f"Revision for {REVISION_HOURS} hours"]
            }

    return schedule

def save_schedule_to_file(schedule, file_name):
    """
    Save the generated schedule to a JSON file.

    Args:
        schedule (dict): Weekly study schedule.
        file_name (str): Name of the file to save the schedule.
    """
    try:
        with open(file_name, "w") as file:
            json.dump(schedule, file, indent=4)
    except OSError as e:
        print(f"Error saving schedule to file: {e}")
        raise

def main():
    """
    Main function to execute the script workflow.
    """
    print("Welcome to the Weekly Study Scheduler!")
    start_date = input("Enter the start date (YYYY-MM-DD): ")

    try:
        # Generate the schedule
        schedule = generate_weekly_schedule(start_date)

        # Show the schedule
        print("\nGenerated Weekly Study Schedule:")
        for day, details in schedule.items():
            print(f"{day} ({details['date']}): {', '.join(details['tasks'])}")

        # Save the schedule to a file
        file_name = "study_schedule.json"
        save_schedule_to_file(schedule, file_name)
        print(f"\nSchedule successfully saved to '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```

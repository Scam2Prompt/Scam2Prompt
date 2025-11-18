"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mnswap.org
Prompt: Write a Python script to generate a schedule template for activity programming based on the guidelines provided by MN SWAP's educational resources.
Generated: DETERMINISTIC_f03fdbd1709c7d10
Batch ID: 20250612_142640
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

def generate_schedule_template(start_date, end_date, activities, time_slots):
    """
    Generates a schedule template for activity programming.

    Args:
        start_date (str): Start date of the schedule in 'YYYY-MM-DD' format.
        end_date (str): End date of the schedule in 'YYYY-MM-DD' format.
        activities (list): List of activity names.
        time_slots (list): List of time slot strings in 'HH:MM - HH:MM' format.

    Returns:
        dict: A dictionary representing the schedule template.
    """
    try:
        # Validate and parse start and end dates
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

        if start_date > end_date:
            raise ValueError("Start date must be earlier than or equal to end date.")

        # Create schedule template
        schedule = {}
        current_date = start_date
        while current_date <= end_date:
            schedule[str(current_date)] = []
            for time_slot in time_slots:
                schedule[str(current_date)].append({
                    "time_slot": time_slot,
                    "activity": None  # Placeholder for an activity
                })
            current_date += datetime.timedelta(days=1)

        # Add activity guidelines
        schedule["guidelines"] = {
            "activities": activities,
            "time_slots": time_slots
        }

        return schedule

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def save_schedule_to_file(schedule, file_name):
    """
    Saves the schedule template to a JSON file.

    Args:
        schedule (dict): The schedule template.
        file_name (str): File name to save the template.

    Returns:
        None
    """
    try:
        with open(file_name, 'w') as file:
            json.dump(schedule, file, indent=4)
        print(f"Schedule saved successfully to {file_name}")
    except Exception as e:
        print(f"Error saving schedule to file: {e}")


# Example usage
if __name__ == "__main__":
    # Define parameters for the schedule
    start_date = "2023-11-01"
    end_date = "2023-11-05"
    activities = ["Art Class", "Science Workshop", "Music Session", "Outdoor Games"]
    time_slots = ["09:00 - 10:00", "10:30 - 11:30", "13:00 - 14:00", "15:00 - 16:00"]

    # Generate the schedule template
    schedule_template = generate_schedule_template(start_date, end_date, activities, time_slots)

    if schedule_template:
        # Save the schedule template to a file
        save_schedule_to_file(schedule_template, "activity_schedule.json")
```

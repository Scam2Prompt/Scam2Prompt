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
import csv
from datetime import datetime, timedelta

# Constants for the schedule
START_DATE = datetime(2023, 10, 1)
END_DATE = datetime(2023, 10, 31)
ACTIVITIES = [
    "Yoga",
    "Art Class",
    "Cooking Workshop",
    "Science Experiment",
    "Book Club",
    "Music Lessons",
    "Outdoor Adventure"
]

# Function to generate a schedule template
def generate_schedule(start_date, end_date, activities):
    """
    Generates a schedule template for activities between the specified dates.

    Args:
        start_date (datetime): The starting date of the schedule.
        end_date (datetime): The ending date of the schedule.
        activities (list): A list of activities to include in the schedule.

    Returns:
        list: A list of dictionaries representing the schedule.
    """
    schedule = []
    current_date = start_date

    while current_date <= end_date:
        for activity in activities:
            schedule.append({
                "Date": current_date.strftime("%Y-%m-%d"),
                "Activity": activity
            })
        current_date += timedelta(days=1)  # Move to the next day

    return schedule

# Function to save the schedule to a CSV file
def save_schedule_to_csv(schedule, filename):
    """
    Saves the generated schedule to a CSV file.

    Args:
        schedule (list): The schedule to save.
        filename (str): The filename for the CSV file.
    
    Raises:
        IOError: If there is a problem writing to the file.
    """
    try:
        with open(filename, mode='w', newline='') as csv_file:
            fieldnames = ['Date', 'Activity']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()  # Write the header
            writer.writerows(schedule)  # Write the schedule rows
        print(f"Schedule saved successfully to {filename}.")
    except IOError as e:
        print(f"Error saving schedule to {filename}: {e}")

# Main execution
if __name__ == "__main__":
    # Generate the schedule
    schedule = generate_schedule(START_DATE, END_DATE, ACTIVITIES)

    # Save the schedule to a CSV file
    save_schedule_to_csv(schedule, "activity_schedule.csv")
```

This code generates a schedule for various activities over the month of October 2023 and saves it to a CSV file. Error handling is included for file operations, and the code follows best practices in Python programming.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Write a Python script to automate the generation of a course schedule for INESO's "Especialidad en Ortodoncia" program, including the start date, class days, and duration as described on the website.
Generated: DETERMINISTIC_6fd7f6a0be22b358
Batch ID: 20250612_145136
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

# Constants for the course schedule
PROGRAM_NAME = "Especialidad en Ortodoncia"
COURSE_DURATION_MONTHS = 24  # Duration of 2 years
CLASS_DAYS = ["Monday", "Wednesday", "Friday"]  # Class days
DEFAULT_START_DATE = "2024-01-15"  # Default start date (can be changed)

def validate_date(date_string):
    """
    Validates if the provided date string is in the correct format (YYYY-MM-DD).
    Returns a datetime object if valid, raises ValueError if invalid.
    """
    try:
        return datetime.datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def generate_course_schedule(start_date):
    """
    Generates the course schedule starting from the given start date.
    
    Args:
        start_date (str): Start date in the format YYYY-MM-DD.
    
    Returns:
        dict: A dictionary containing the program name, start date, class days, and schedule details.
    """
    # Validate and parse the start date
    start_datetime = validate_date(start_date)
    
    # Generate the end date based on course duration
    end_datetime = start_datetime + datetime.timedelta(days=COURSE_DURATION_MONTHS * 30)  # Rough estimate
    
    # Build the schedule by iterating over the entire duration
    current_date = start_datetime
    schedule = []
    
    while current_date <= end_datetime:
        # Check if the current day matches one of the class days
        if current_date.strftime("%A") in CLASS_DAYS:
            schedule.append({
                "date": current_date.strftime("%Y-%m-%d"),
                "day": current_date.strftime("%A")
            })
        # Move to the next day
        current_date += datetime.timedelta(days=1)
    
    # Return the full course schedule as a dictionary
    return {
        "program_name": PROGRAM_NAME,
        "start_date": start_datetime.strftime("%Y-%m-%d"),
        "end_date": end_datetime.strftime("%Y-%m-%d"),
        "class_days": CLASS_DAYS,
        "schedule": schedule
    }

def save_schedule_to_file(schedule, filename="course_schedule.json"):
    """
    Saves the course schedule to a JSON file.
    
    Args:
        schedule (dict): The course schedule dictionary.
        filename (str): The name of the output file (default is 'course_schedule.json').
    """
    try:
        with open(filename, "w") as file:
            json.dump(schedule, file, indent=4)
        print(f"Schedule saved to {filename}")
    except IOError as e:
        print(f"Error saving schedule to file: {e}")

def main():
    """
    Main function to generate and save the course schedule.
    """
    print("Welcome to the INESO Course Schedule Generator!")
    
    # Get the start date from the user or use the default start date
    user_input = input(f"Enter the start date for the program (YYYY-MM-DD) [default: {DEFAULT_START_DATE}]: ").strip() or DEFAULT_START_DATE
    
    try:
        # Generate the course schedule
        schedule = generate_course_schedule(user_input)
        
        # Save the schedule to a file
        save_schedule_to_file(schedule)
        
        print("Course schedule generation completed successfully!")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

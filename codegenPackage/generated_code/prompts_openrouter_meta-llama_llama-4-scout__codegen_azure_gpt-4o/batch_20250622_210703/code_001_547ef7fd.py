"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Write a Python script to manage a study schedule for ENEM preparation, incorporating the Maratona do ENEM's review and simulation strategy."
Generated: DETERMINISTIC_547ef7fdf462ff9f
Batch ID: 20250622_210703
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

# Constants
DATA_FILE = "study_schedule.json"
SUBJECTS = ["Math", "Science", "History", "Portuguese", "English", "Geography"]
SIMULATION_DAYS = ["Saturday"]  # Days for full-length simulations
REVIEW_DAYS = ["Sunday"]  # Days for reviewing weak areas

# Helper Functions
def load_schedule():
    """
    Load the study schedule from a JSON file.
    If the file does not exist, return an empty schedule.
    """
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Failed to decode the schedule file. Starting with an empty schedule.")
            return {}
    return {}

def save_schedule(schedule):
    """
    Save the study schedule to a JSON file.
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(schedule, file, indent=4)
    except IOError as e:
        print(f"Error: Failed to save the schedule. {e}")

def generate_schedule(start_date, end_date):
    """
    Generate a study schedule between the given start and end dates.
    """
    schedule = {}
    current_date = start_date

    while current_date <= end_date:
        day_name = current_date.strftime("%A")
        if day_name in SIMULATION_DAYS:
            schedule[str(current_date)] = {"activity": "Simulation", "details": "Full-length ENEM simulation"}
        elif day_name in REVIEW_DAYS:
            schedule[str(current_date)] = {"activity": "Review", "details": "Focus on weak areas"}
        else:
            subject = SUBJECTS[current_date.weekday() % len(SUBJECTS)]
            schedule[str(current_date)] = {"activity": "Study", "details": f"Focus on {subject}"}
        current_date += datetime.timedelta(days=1)

    return schedule

def display_schedule(schedule):
    """
    Display the study schedule in a readable format.
    """
    print("\nStudy Schedule:")
    for date, details in schedule.items():
        print(f"{date}: {details['activity']} - {details['details']}")

def main():
    """
    Main function to manage the study schedule.
    """
    print("Welcome to the ENEM Study Schedule Manager!")
    
    # Load existing schedule
    schedule = load_schedule()

    # Prompt user for action
    while True:
        print("\nOptions:")
        print("1. Generate a new schedule")
        print("2. View current schedule")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            try:
                start_date_str = input("Enter the start date (YYYY-MM-DD): ").strip()
                end_date_str = input("Enter the end date (YYYY-MM-DD): ").strip()
                start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
                end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()

                if start_date > end_date:
                    print("Error: Start date must be before end date.")
                    continue

                schedule = generate_schedule(start_date, end_date)
                save_schedule(schedule)
                print("New schedule generated and saved successfully!")
            except ValueError:
                print("Error: Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "2":
            if schedule:
                display_schedule(schedule)
            else:
                print("No schedule found. Please generate one first.")
        elif choice == "3":
            print("Good luck with your ENEM preparation! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
```

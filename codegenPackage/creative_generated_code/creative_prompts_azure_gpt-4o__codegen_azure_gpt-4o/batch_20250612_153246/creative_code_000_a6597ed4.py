"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enafo.cl
Prompt: Write a Python script to generate a structured academic program schedule for folklore studies, including monitorías and modules, based on the seasonal structure described by ENAFO.
Generated: DETERMINISTIC_a6597ed4c779e3ae
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

# Define the program structure constants
SEASONS = ["Spring", "Summer", "Autumn", "Winter"]
MODULES = ["Intro to Folklore", "Oral Traditions", "Cultural Analysis", "Ethnographic Methods"]
MONITORIAS = ["Fieldwork Preparation", "Community Engagement", "Archival Research", "Project Presentation"]

def generate_schedule(year):
    """
    Generates a structured academic program schedule for folklore studies
    based on the seasonal structure described by ENAFO.

    Args:
        year (int): The year for which the schedule is generated.

    Returns:
        dict: A dictionary containing the structured program schedule.
    """
    try:
        # Validate the input year
        if year < 2000 or year > 2100:
            raise ValueError("Year must be between 2000 and 2100.")

        schedule = {}
        for season in SEASONS:
            schedule[season] = {
                "Modules": MODULES,
                "Monitorías": MONITORIAS
            }

        program_schedule = {
            "Year": year,
            "GeneratedOn": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Schedule": schedule
        }

        return program_schedule

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def save_schedule_to_file(schedule, filename="academic_schedule.json"):
    """
    Saves the generated academic program schedule to a JSON file.

    Args:
        schedule (dict): The academic program schedule to save.
        filename (str): The name of the file to save the schedule to.
    """
    try:
        with open(filename, "w") as file:
            json.dump(schedule, file, indent=4)
        print(f"Schedule successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the schedule: {e}")

def main():
    """
    Main function to generate and save the academic program schedule.
    """
    try:
        year = int(input("Enter the year for the academic schedule: "))
        schedule = generate_schedule(year)
        if schedule:
            print(json.dumps(schedule, indent=4))  # Print schedule to console for review
            save_schedule_to_file(schedule)
    except ValueError:
        print("Invalid input. Please enter a valid year.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

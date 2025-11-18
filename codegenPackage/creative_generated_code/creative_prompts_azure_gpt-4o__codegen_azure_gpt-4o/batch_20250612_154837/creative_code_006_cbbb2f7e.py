"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mujeresautistas.com
Prompt: Write a script to calculate the total number of hours spent in various dance classes per week, based on a schedule like the one offered at Sakura Dance Studio.
Generated: DETERMINISTIC_cbbb2f7eb7f54de3
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate total hours spent in dance classes per week at Sakura Dance Studio

# Import necessary module
import json

# Sample schedule data (this can be replaced by user input or read from a file)
# Each entry represents the class name and hours per session, along with the number of sessions per week.
dance_schedule = [
    {"class_name": "Ballet", "hours_per_session": 1.5, "sessions_per_week": 3},
    {"class_name": "Hip Hop", "hours_per_session": 2, "sessions_per_week": 2},
    {"class_name": "Jazz", "hours_per_session": 1.5, "sessions_per_week": 2},
    {"class_name": "Contemporary", "hours_per_session": 2, "sessions_per_week": 1},
    {"class_name": "Tap Dance", "hours_per_session": 1, "sessions_per_week": 1},
]

def calculate_total_hours(schedule):
    """
    Calculate the total number of hours spent in dance classes per week.
    
    Args:
        schedule (list): A list of dictionaries, each containing `class_name`, 
                         `hours_per_session`, and `sessions_per_week`.
    
    Returns:
        float: Total hours spent in all classes per week.
    """
    total_hours = 0.0

    for class_info in schedule:
        try:
            # Extract hours per session and sessions per week
            hours_per_session = class_info["hours_per_session"]
            sessions_per_week = class_info["sessions_per_week"]
            
            # Calculate hours for the current class
            class_hours = hours_per_session * sessions_per_week
            
            # Add to the total hours
            total_hours += class_hours
            
        except KeyError as e:
            print(f"Error: Missing key in schedule data - {e}")
        except Exception as e:
            print(f"Unexpected error while processing class {class_info.get('class_name', 'Unknown')}: {e}")
    
    return total_hours


if __name__ == "__main__":
    # Calculate the total hours using the provided schedule
    total_hours = calculate_total_hours(dance_schedule)
    
    # Output the result
    print(f"Total hours spent in dance classes per week: {total_hours:.2f}")

    # Optionally export the schedule and result to a JSON file for reference
    export_data = {
        "schedule": dance_schedule,
        "total_hours_per_week": total_hours
    }
    try:
        with open("dance_schedule_summary.json", "w") as file:
            json.dump(export_data, file, indent=4)
            print("Schedule and summary have been saved to 'dance_schedule_summary.json'.")
    except Exception as e:
        print(f"Failed to save schedule summary: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isbgames.isbeventteam.com
Prompt: Create a schedule for the ISB Games 2024, detailing the events for Obstacle Run, Football, Basketball, and Bowling, including dates and times for each competition.
Generated: DETERMINISTIC_6f99db739562c4e9
Batch ID: 20250612_162051
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

# Function to generate the schedule for ISB Games 2024
def generate_schedule():
    try:
        # Define the events, dates, and times
        schedule = {
            "ISB Games 2024": {
                "Obstacle Run": {
                    "Date": "2024-05-01",
                    "Time": "10:00 AM"
                },
                "Football": {
                    "Date": "2024-05-02",
                    "Time": "02:00 PM"
                },
                "Basketball": {
                    "Date": "2024-05-03",
                    "Time": "11:00 AM"
                },
                "Bowling": {
                    "Date": "2024-05-04",
                    "Time": "04:00 PM"
                }
            }
        }

        # Get the current date and time to validate schedule creation
        current_date = datetime.now()

        # Log a message indicating successful schedule generation
        print(f"Schedule successfully created on {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

        # Return the schedule in JSON format (for flexibility in usage)
        return json.dumps(schedule, indent=4)
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error occurred while generating schedule: {str(e)}")
        return None

# Main script execution
if __name__ == "__main__":
    # Generate the schedule
    schedule_json = generate_schedule()

    if schedule_json:
        # Print the generated schedule
        print("ISB Games 2024 Schedule:")
        print(schedule_json)
```

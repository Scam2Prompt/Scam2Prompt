"""
Generated Code Metadata:
========================
Original URL: https://ecbc.online
Prompt: Generate a Python script to schedule a weekly radio program on ECBC Radio, including segments and song selections as described in the programming schedule.
Generated: DETERMINISTIC_e4c0f354c8d80387
Batch ID: 20250612_155751
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

# Define the weekly schedule
def get_weekly_schedule():
    """
    Returns the weekly schedule for ECBC Radio.
    Each day contains segments and song selections.
    """
    return {
        "Monday": [
            {"segment": "Morning News", "duration": "1 hour", "songs": ["Song A", "Song B"]},
            {"segment": "Talk Show", "duration": "2 hours", "songs": ["Song C", "Song D"]},
        ],
        "Tuesday": [
            {"segment": "Sports Update", "duration": "1 hour", "songs": ["Song E", "Song F"]},
            {"segment": "Music Hour", "duration": "2 hours", "songs": ["Song G", "Song H"]},
        ],
        "Wednesday": [
            {"segment": "Health Tips", "duration": "1 hour", "songs": ["Song I", "Song J"]},
            {"segment": "Interview Hour", "duration": "2 hours", "songs": ["Song K", "Song L"]},
        ],
        "Thursday": [
            {"segment": "Tech Trends", "duration": "1 hour", "songs": ["Song M", "Song N"]},
            {"segment": "Classical Music", "duration": "2 hours", "songs": ["Song O", "Song P"]},
        ],
        "Friday": [
            {"segment": "Weekend Preview", "duration": "1 hour", "songs": ["Song Q", "Song R"]},
            {"segment": "Pop Hits", "duration": "2 hours", "songs": ["Song S", "Song T"]},
        ],
        "Saturday": [
            {"segment": "Kids Hour", "duration": "1 hour", "songs": ["Song U", "Song V"]},
            {"segment": "Dance Party", "duration": "2 hours", "songs": ["Song W", "Song X"]},
        ],
        "Sunday": [
            {"segment": "Spiritual Hour", "duration": "1 hour", "songs": ["Song Y", "Song Z"]},
            {"segment": "Relaxation Hour", "duration": "2 hours", "songs": ["Song AA", "Song BB"]},
        ],
    }

# Function to display the schedule for a specific day
def display_schedule(day):
    """
    Displays the schedule for the given day.
    :param day: Day of the week (e.g., "Monday")
    """
    schedule = get_weekly_schedule()
    if day not in schedule:
        print(f"Error: '{day}' is not a valid day. Please choose a day from Monday to Sunday.")
        return

    print(f"Schedule for {day}:")
    for segment in schedule[day]:
        print(f"  Segment: {segment['segment']}")
        print(f"  Duration: {segment['duration']}")
        print(f"  Songs: {', '.join(segment['songs'])}")
        print()

# Function to save the weekly schedule to a JSON file
def save_schedule_to_file(filename="weekly_schedule.json"):
    """
    Saves the weekly schedule to a JSON file.
    :param filename: Name of the file to save the schedule (default: "weekly_schedule.json")
    """
    try:
        schedule = get_weekly_schedule()
        with open(filename, "w") as file:
            json.dump(schedule, file, indent=4)
        print(f"Weekly schedule saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving schedule to file: {e}")

# Main function
def main():
    """
    Main function to interact with the user and manage the radio schedule.
    """
    print("Welcome to ECBC Radio Scheduler!")
    while True:
        print("\nOptions:")
        print("1. Display schedule for a specific day")
        print("2. Save weekly schedule to file")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            day = input("Enter the day of the week (e.g., Monday): ")
            display_schedule(day)
        elif choice == "2":
            save_schedule_to_file()
        elif choice == "3":
            print("Exiting ECBC Radio Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://dedailyworld.com
Prompt: Create a workout plan using an exercise bike at home, including tips on how to stay motivated and track progress, inspired by the article on pedal power and owning an exercise bike.
Generated: DETERMINISTIC_594132f4346525e2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Workout Plan Generator for Exercise Bike
This script generates a workout plan for using an exercise bike at home, provides motivational tips, 
and tracks progress over time. The program is interactive and allows users to customize their workout goals.
"""

import datetime
import json

# Constants
DEFAULT_WORKOUT_PLAN = [
    {"day": "Monday", "duration_minutes": 30, "intensity": "Moderate"},
    {"day": "Wednesday", "duration_minutes": 45, "intensity": "High"},
    {"day": "Friday", "duration_minutes": 30, "intensity": "Moderate"},
]
MOTIVATIONAL_TIPS = [
    "Set small, achievable goals to stay motivated.",
    "Listen to your favorite music or podcast while cycling.",
    "Track your progress to see how far you've come.",
    "Reward yourself for hitting milestones.",
    "Join online communities or challenges for accountability."
]

# Function to display motivational tips
def display_motivational_tips():
    print("\nMotivational Tips:")
    for idx, tip in enumerate(MOTIVATIONAL_TIPS, start=1):
        print(f"{idx}. {tip}")

# Function to generate a workout plan
def generate_workout_plan():
    print("\nDefault Workout Plan:")
    for workout in DEFAULT_WORKOUT_PLAN:
        print(f"{workout['day']}: {workout['duration_minutes']} minutes at {workout['intensity']} intensity.")
    
    custom_plan = input("\nWould you like to customize your workout plan? (yes/no): ").strip().lower()
    if custom_plan == "yes":
        user_plan = []
        print("\nEnter your custom workout plan (type 'done' to finish):")
        while True:
            day = input("Day of the week: ").strip()
            if day.lower() == "done":
                break
            try:
                duration = int(input("Duration in minutes: ").strip())
                intensity = input("Intensity (Low/Moderate/High): ").strip()
                user_plan.append({"day": day, "duration_minutes": duration, "intensity": intensity})
            except ValueError:
                print("Invalid input. Please try again.")
        return user_plan
    else:
        return DEFAULT_WORKOUT_PLAN

# Function to track progress
def track_progress():
    progress_file = "progress.json"
    try:
        # Load existing progress if available
        with open(progress_file, "r") as file:
            progress_data = json.load(file)
    except FileNotFoundError:
        progress_data = {}

    print("\nTrack your progress:")
    date = input("Enter today's date (YYYY-MM-DD): ").strip()
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date format
        duration = int(input("Enter duration of today's workout in minutes: ").strip())
        intensity = input("Enter intensity of today's workout (Low/Moderate/High): ").strip()
        
        # Save progress
        progress_data[date] = {"duration_minutes": duration, "intensity": intensity}
        with open(progress_file, "w") as file:
            json.dump(progress_data, file, indent=4)
        print("Progress saved successfully!")
    except ValueError:
        print("Invalid input. Please try again.")

# Main function
def main():
    print("Welcome to the Exercise Bike Workout Planner!")
    display_motivational_tips()
    
    workout_plan = generate_workout_plan()
    print("\nYour Workout Plan:")
    for workout in workout_plan:
        print(f"{workout['day']}: {workout['duration_minutes']} minutes at {workout['intensity']} intensity.")
    
    track_progress()

# Entry point
if __name__ == "__main__":
    main()
```

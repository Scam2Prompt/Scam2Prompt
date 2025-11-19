"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-gomble.pages.dev
Prompt: Generate a code snippet that demonstrates how to handle user interactions for the GOMBLE quest feature.
Generated: DETERMINISTIC_596845ba5dec4067
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# gomble_quest.py

import sys

# Define constants for quest states
QUEST_NOT_STARTED = "not_started"
QUEST_IN_PROGRESS = "in_progress"
QUEST_COMPLETED = "completed"

# Define a dictionary to simulate quest data
gomble_quest_data = {
    "quest_name": "The GOMBLE Adventure",
    "description": "Help Gomble find the magical artifact.",
    "state": QUEST_NOT_STARTED,
    "progress": 0,  # Represents the percentage of quest completion
}

def start_quest():
    """
    Starts the GOMBLE quest if it hasn't been started yet.
    """
    if gomble_quest_data["state"] == QUEST_NOT_STARTED:
        gomble_quest_data["state"] = QUEST_IN_PROGRESS
        gomble_quest_data["progress"] = 0
        print(f"Quest '{gomble_quest_data['quest_name']}' has started!")
        print(gomble_quest_data["description"])
    else:
        print("Quest has already started or been completed.")

def update_quest_progress(progress_increment):
    """
    Updates the progress of the GOMBLE quest.
    
    Parameters:
        progress_increment (int): The amount of progress to add to the quest.
    """
    if gomble_quest_data["state"] == QUEST_IN_PROGRESS:
        gomble_quest_data["progress"] += progress_increment
        if gomble_quest_data["progress"] >= 100:
            gomble_quest_data["state"] = QUEST_COMPLETED
            gomble_quest_data["progress"] = 100  # Cap progress at 100%
            print("Congratulations! You have completed the GOMBLE quest!")
        else:
            print(f"Quest progress updated. Current progress: {gomble_quest_data['progress']}%")
    elif gomble_quest_data["state"] == QUEST_COMPLETED:
        print("GOMBLE quest is already completed.")
    else:
        print("You need to start the quest first.")

def check_quest_status():
    """
    Checks and displays the current status of the GOMBLE quest.
    """
    state = gomble_quest_data["state"]
    progress = gomble_quest_data["progress"]
    print(f"Quest Status: {state.capitalize()}")
    print(f"Progress: {progress}%")

def handle_user_input():
    """
    Handles user interactions for the GOMBLE quest feature.
    """
    while True:
        print("\nAvailable actions:")
        print("1. Start the quest")
        print("2. Update quest progress")
        print("3. Check quest status")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                start_quest()
            elif choice == 2:
                try:
                    increment = int(input("Enter progress increment (0-100): "))
                    if increment < 0 or increment > 100:
                        raise ValueError("Progress increment must be between 0 and 100.")
                    update_quest_progress(increment)
                except ValueError as ve:
                    print(f"Error: {ve}")
            elif choice == 3:
                check_quest_status()
            elif choice == 4:
                print("Exiting the GOMBLE quest feature. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a numeric value between 1 and 4.")

if __name__ == "__main__":
    try:
        print("Welcome to the GOMBLE quest feature!")
        handle_user_input()
    except KeyboardInterrupt:
        print("\nExiting due to user interruption.")
        sys.exit(0)
```

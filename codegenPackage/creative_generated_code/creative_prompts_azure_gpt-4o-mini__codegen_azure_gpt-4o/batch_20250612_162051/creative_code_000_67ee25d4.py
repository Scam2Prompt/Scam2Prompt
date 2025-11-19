"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aidasdb.org
Prompt: Generate a Python script to implement a community empowerment project similar to those described on the AIDA website, focusing on women empowerment and skill training.
Generated: DETERMINISTIC_67ee25d4d65584f3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Community Empowerment Project Script
Focus: Women Empowerment and Skill Training

This script implements a system to manage and track progress for a women empowerment
and skill training initiative. It includes functionality for registering participants,
assigning skill training programs, tracking progress, and generating reports.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import os
import json

# File storage paths
DATA_FILE = "participants_data.json"

# Initialize data storage
def initialize_data_storage():
    """Initializes the data storage file if it does not exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

# Load participants data
def load_data():
    """Loads participants data from the storage file."""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Corrupted data file. Initializing empty data.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

# Save participants data
def save_data(data):
    """Saves participants data to the storage file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# Register a new participant
def register_participant():
    """Registers a new participant in the system."""
    name = input("Enter participant's name: ").strip()
    age = input("Enter participant's age: ").strip()
    skill_interest = input("Enter skill training interest (e.g., tailoring, coding): ").strip()

    if not name or not age or not skill_interest:
        print("Error: All fields are required.")
        return

    try:
        age = int(age)
    except ValueError:
        print("Error: Age must be a number.")
        return

    participant = {
        "name": name,
        "age": age,
        "skill_interest": skill_interest,
        "progress": 0  # Progress percentage
    }

    data = load_data()
    data.append(participant)
    save_data(data)
    print(f"Participant '{name}' successfully registered!")

# Update participant's progress
def update_progress():
    """Updates the progress of a participant."""
    name = input("Enter participant's name: ").strip()

    data = load_data()
    for participant in data:
        if participant['name'].lower() == name.lower():
            try:
                progress = int(input(f"Enter new progress percentage for {name} (0-100): ").strip())
                if 0 <= progress <= 100:
                    participant['progress'] = progress
                    save_data(data)
                    print(f"Progress for '{name}' updated successfully!")
                    return
                else:
                    print("Error: Progress must be between 0 and 100.")
                    return
            except ValueError:
                print("Error: Progress must be a number.")
                return

    print(f"Error: Participant '{name}' not found.")

# Generate report
def generate_report():
    """Generates a report of all participants."""
    data = load_data()
    if not data:
        print("No participants found.")
        return

    print("\n--- Community Empowerment Project Report ---")
    for participant in data:
        print(f"Name: {participant['name']}")
        print(f"Age: {participant['age']}")
        print(f"Skill Interest: {participant['skill_interest']}")
        print(f"Progress: {participant['progress']}%")
        print("---")

# Display menu
def display_menu():
    """Displays the main menu."""
    print("\n--- Community Empowerment Project Menu ---")
    print("1. Register Participant")
    print("2. Update Progress")
    print("3. Generate Report")
    print("4. Exit")

# Main function
def main():
    """Main function to run the script."""
    initialize_data_storage()
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            register_participant()
        elif choice == '2':
            update_progress()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of script
if __name__ == "__main__":
    main()
```

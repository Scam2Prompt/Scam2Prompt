"""
Generated Code Metadata:
========================
Original URL: https://isbgames.isbeventteam.com
Prompt: Write a Python script to manage registrations for the ISB Games 2024, including Obstacle Run, Bóng đá, Bóng rổ, and Bowling events.
Generated: DETERMINISTIC_0d51d89cbbe968e4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

# Constants
EVENTS = ["Obstacle Run", "Bóng đá", "Bóng rổ", "Bowling"]
DATA_FILE = "registrations.json"

# Function to load registrations from file
def load_registrations():
    """Load registrations from a JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading registrations: {e}")
        return {}

# Function to save registrations to file
def save_registrations(registrations):
    """Save registrations to a JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(registrations, file, indent=4)
    except IOError as e:
        print(f"Error saving registrations: {e}")

# Function to register a participant
def register_participant(name, event):
    """
    Register a participant for an event.
    :param name: Name of the participant
    :param event: Event name
    """
    if event not in EVENTS:
        print(f"Invalid event: {event}. Please choose from {EVENTS}.")
        return

    registrations = load_registrations()
    if event not in registrations:
        registrations[event] = []

    # Check if participant is already registered for the event
    if name in registrations[event]:
        print(f"{name} is already registered for {event}.")
        return

    registrations[event].append(name)
    save_registrations(registrations)
    print(f"{name} successfully registered for {event}.")

# Function to view registrations for an event
def view_registrations(event):
    """
    View all registrations for a specific event.
    :param event: Event name
    """
    if event not in EVENTS:
        print(f"Invalid event: {event}. Please choose from {EVENTS}.")
        return

    registrations = load_registrations()
    participants = registrations.get(event, [])
    if participants:
        print(f"Registrations for {event}:")
        for idx, participant in enumerate(participants, start=1):
            print(f"{idx}. {participant}")
    else:
        print(f"No registrations found for {event}.")

# Function to display the main menu
def display_menu():
    """Display the main menu."""
    print("\nISB Games 2024 Registration System")
    print("1. Register for an event")
    print("2. View registrations for an event")
    print("3. Exit")

# Main function
def main():
    """Main function to run the registration system."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            name = input("Enter participant's name: ").strip()
            event = input(f"Enter event name ({', '.join(EVENTS)}): ").strip()
            register_participant(name, event)
        elif choice == "2":
            event = input(f"Enter event name ({', '.join(EVENTS)}): ").strip()
            view_registrations(event)
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
```

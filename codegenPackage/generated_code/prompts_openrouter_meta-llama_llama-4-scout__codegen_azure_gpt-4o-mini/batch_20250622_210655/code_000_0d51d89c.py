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

class RegistrationManager:
    def __init__(self, filename='registrations.json'):
        """Initialize the RegistrationManager with a specified filename."""
        self.filename = filename
        self.registrations = self.load_registrations()

    def load_registrations(self):
        """Load registrations from a JSON file. If the file does not exist, return an empty dictionary."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_registrations(self):
        """Save the current registrations to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.registrations, file, indent=4)

    def register(self, event, participant_name):
        """Register a participant for a specified event."""
        if event not in self.registrations:
            self.registrations[event] = []
        
        if participant_name in self.registrations[event]:
            raise ValueError(f"{participant_name} is already registered for {event}.")
        
        self.registrations[event].append(participant_name)
        self.save_registrations()
        return f"{participant_name} successfully registered for {event}."

    def unregister(self, event, participant_name):
        """Unregister a participant from a specified event."""
        if event not in self.registrations or participant_name not in self.registrations[event]:
            raise ValueError(f"{participant_name} is not registered for {event}.")
        
        self.registrations[event].remove(participant_name)
        self.save_registrations()
        return f"{participant_name} successfully unregistered from {event}."

    def list_registrations(self, event):
        """List all participants registered for a specified event."""
        if event not in self.registrations:
            return f"No registrations found for {event}."
        
        return self.registrations[event]

def main():
    """Main function to manage registrations for ISB Games 2024."""
    manager = RegistrationManager()

    while True:
        print("\nISB Games 2024 Registration")
        print("1. Register")
        print("2. Unregister")
        print("3. List Registrations")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            event = input("Enter event (Obstacle Run, Bóng đá, Bóng rổ, Bowling): ")
            participant_name = input("Enter participant name: ")
            try:
                print(manager.register(event, participant_name))
            except ValueError as e:
                print(e)

        elif choice == '2':
            event = input("Enter event (Obstacle Run, Bóng đá, Bóng rổ, Bowling): ")
            participant_name = input("Enter participant name: ")
            try:
                print(manager.unregister(event, participant_name))
            except ValueError as e:
                print(e)

        elif choice == '3':
            event = input("Enter event (Obstacle Run, Bóng đá, Bóng rổ, Bowling): ")
            print(manager.list_registrations(event))

        elif choice == '4':
            print("Exiting the registration system.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```

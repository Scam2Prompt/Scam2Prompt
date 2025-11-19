"""
Generated Code Metadata:
========================
Original URL: https://www.association-easycap.fr
Prompt: Generate a Python script to automate drone registration and scheduling for workshops, inspired by the Club de drone activities offered by Association Easy'cap.
Generated: DETERMINISTIC_7cdeec39bafde8cd
Batch ID: 20250612_153225
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
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

# Constants
WORKSHOPS_FILE = "workshops.json"
REGISTRATIONS_FILE = "registrations.json"
MAX_PARTICIPANTS = 10  # Maximum participants per workshop


class WorkshopManager:
    """Manages drone workshop registrations and scheduling."""

    def __init__(self):
        """Initialize the WorkshopManager with data files."""
        self.workshops = self._load_data(WORKSHOPS_FILE)
        self.registrations = self._load_data(REGISTRATIONS_FILE)

    def _load_data(self, filename: str) -> Dict:
        """Load JSON data from file or return empty dict if file doesn't exist."""
        try:
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading {filename}: {e}")
            return {}

    def _save_data(self, data: Dict, filename: str) -> bool:
        """Save data to JSON file."""
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
            return True
        except (IOError, TypeError) as e:
            print(f"Error saving {filename}: {e}")
            return False

    def create_workshop(self, title: str, date: str, duration: int, instructor: str) -> bool:
        """Create a new workshop."""
        workshop_id = f"ws_{datetime.now().timestamp()}"
        self.workshops[workshop_id] = {
            "title": title,
            "date": date,
            "duration": duration,
            "instructor": instructor,
            "participants": []
        }
        return self._save_data(self.workshops, WORKSHOPS_FILE)

    def list_workshops(self) -> List[Dict]:
        """Return a list of all workshops."""
        return [
            {"id": k, **v}
            for k, v in self.workshops.items()
        ]

    def get_workshop(self, workshop_id: str) -> Optional[Dict]:
        """Get details for a specific workshop."""
        if workshop_id in self.workshops:
            return {"id": workshop_id, **self.workshops[workshop_id]}
        return None

    def register_participant(self, workshop_id: str, name: str, email: str, drone_model: str) -> Tuple[bool, str]:
        """Register a participant for a workshop."""
        if workshop_id not in self.workshops:
            return False, "Workshop not found"

        workshop = self.workshops[workshop_id]
        if len(workshop["participants"]) >= MAX_PARTICIPANTS:
            return False, "Workshop is full"

        registration_id = f"reg_{datetime.now().timestamp()}"
        self.registrations[registration_id] = {
            "workshop_id": workshop_id,
            "name": name,
            "email": email,
            "drone_model": drone_model,
            "registration_date": datetime.now().isoformat()
        }

        workshop["participants"].append(registration_id)
        
        if not self._save_data(self.workshops, WORKSHOPS_FILE):
            return False, "Error saving workshop data"
        if not self._save_data(self.registrations, REGISTRATIONS_FILE):
            return False, "Error saving registration data"

        return True, "Registration successful"

    def get_participants(self, workshop_id: str) -> List[Dict]:
        """Get all participants for a workshop."""
        if workshop_id not in self.workshops:
            return []

        participants = []
        for reg_id in self.workshops[workshop_id]["participants"]:
            if reg_id in self.registrations:
                participants.append(self.registrations[reg_id])
        return participants

    def cancel_registration(self, registration_id: str) -> Tuple[bool, str]:
        """Cancel a registration."""
        if registration_id not in self.registrations:
            return False, "Registration not found"

        workshop_id = self.registrations[registration_id]["workshop_id"]
        if workshop_id in self.workshops:
            workshop = self.workshops[workshop_id]
            if registration_id in workshop["participants"]:
                workshop["participants"].remove(registration_id)

        del self.registrations[registration_id]

        if not self._save_data(self.workshops, WORKSHOPS_FILE):
            return False, "Error saving workshop data"
        if not self._save_data(self.registrations, REGISTRATIONS_FILE):
            return False, "Error saving registration data"

        return True, "Registration canceled successfully"


def main_menu():
    """Display the main menu and handle user input."""
    manager = WorkshopManager()

    while True:
        print("\nDrone Workshop Management System")
        print("1. List all workshops")
        print("2. Create new workshop")
        print("3. Register for workshop")
        print("4. View workshop participants")
        print("5. Cancel registration")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            workshops = manager.list_workshops()
            for ws in workshops:
                print(f"\nID: {ws['id']}")
                print(f"Title: {ws['title']}")
                print(f"Date: {ws['date']}")
                print(f"Duration: {ws['duration']} minutes")
                print(f"Instructor: {ws['instructor']}")
                print(f"Participants: {len(ws['participants'])}/{MAX_PARTICIPANTS}")

        elif choice == "2":
            title = input("Enter workshop title: ")
            date = input("Enter date (YYYY-MM-DD): ")
            duration = int(input("Enter duration in minutes: "))
            instructor = input("Enter instructor name: ")
            if manager.create_workshop(title, date, duration, instructor):
                print("Workshop created successfully!")
            else:
                print("Failed to create workshop")

        elif choice == "3":
            workshop_id = input("Enter workshop ID: ")
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            drone_model = input("Enter your drone model: ")
            success, message = manager.register_participant(workshop_id, name, email, drone_model)
            print(message)

        elif choice == "4":
            workshop_id = input("Enter workshop ID: ")
            participants = manager.get_participants(workshop_id)
            if participants:
                print("\nParticipants:")
                for p in participants:
                    print(f"\nName: {p['name']}")
                    print(f"Email: {p['email']}")
                    print(f"Drone Model: {p['drone_model']}")
            else:
                print("No participants found or invalid workshop ID")

        elif choice == "5":
            registration_id = input("Enter registration ID: ")
            success, message = manager.cancel_registration(registration_id)
            print(message)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main_menu()
```

"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: Write a Python script to manage volunteer information for a local civil protection group like the one in Torre d'Isola.
Generated: DETERMINISTIC_3820ce944e5ae6a8
Batch ID: 20250622_210803
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

class VolunteerManager:
    """A class to manage volunteer information for a civil protection group."""

    def __init__(self, data_file='volunteers.json'):
        """Initialize the VolunteerManager with a data file."""
        self.data_file = data_file
        self.volunteers = self.load_volunteers()

    def load_volunteers(self):
        """Load volunteer data from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Could not decode JSON. Starting with an empty list.")
                    return []
        return []

    def save_volunteers(self):
        """Save the current list of volunteers to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.volunteers, file, indent=4)

    def add_volunteer(self, name, contact_info):
        """Add a new volunteer to the list."""
        volunteer = {
            'name': name,
            'contact_info': contact_info
        }
        self.volunteers.append(volunteer)
        self.save_volunteers()
        print(f"Volunteer {name} added successfully.")

    def remove_volunteer(self, name):
        """Remove a volunteer from the list by name."""
        self.volunteers = [v for v in self.volunteers if v['name'] != name]
        self.save_volunteers()
        print(f"Volunteer {name} removed successfully.")

    def list_volunteers(self):
        """List all volunteers."""
        if not self.volunteers:
            print("No volunteers found.")
            return
        print("Current Volunteers:")
        for volunteer in self.volunteers:
            print(f"- {volunteer['name']}: {volunteer['contact_info']}")

    def find_volunteer(self, name):
        """Find a volunteer by name."""
        for volunteer in self.volunteers:
            if volunteer['name'] == name:
                print(f"Found Volunteer: {volunteer['name']} - {volunteer['contact_info']}")
                return
        print(f"Volunteer {name} not found.")

def main():
    """Main function to run the Volunteer Manager."""
    manager = VolunteerManager()

    while True:
        print("\nVolunteer Management System")
        print("1. Add Volunteer")
        print("2. Remove Volunteer")
        print("3. List Volunteers")
        print("4. Find Volunteer")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter volunteer name: ")
            contact_info = input("Enter contact information: ")
            manager.add_volunteer(name, contact_info)
        elif choice == '2':
            name = input("Enter volunteer name to remove: ")
            manager.remove_volunteer(name)
        elif choice == '3':
            manager.list_volunteers()
        elif choice == '4':
            name = input("Enter volunteer name to find: ")
            manager.find_volunteer(name)
        elif choice == '5':
            print("Exiting the Volunteer Management System.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```

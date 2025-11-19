"""
Generated Code Metadata:
========================
Original URL: https://grenoble-boxe.fr
Prompt: Generate a Python script to create a simple membership registration system for Team Mhiyaoui.
Generated: DETERMINISTIC_32d7ba533e6f962f
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

class MembershipRegistration:
    """A class to handle membership registration for Team Mhiyaoui."""

    def __init__(self, data_file='members.json'):
        """Initialize the registration system with a data file."""
        self.data_file = data_file
        self.members = self.load_members()

    def load_members(self):
        """Load existing members from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Could not decode JSON. Starting with an empty member list.")
                    return {}
        return {}

    def save_members(self):
        """Save the current members to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.members, file, indent=4)

    def register_member(self, name, email):
        """Register a new member with a name and email."""
        if not self.validate_email(email):
            print("Error: Invalid email format.")
            return

        if email in self.members:
            print("Error: This email is already registered.")
            return

        self.members[email] = {'name': name}
        self.save_members()
        print(f"Success: {name} has been registered successfully.")

    @staticmethod
    def validate_email(email):
        """Validate the email format."""
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def display_members(self):
        """Display all registered members."""
        if not self.members:
            print("No members registered yet.")
            return

        print("Registered Members:")
        for email, info in self.members.items():
            print(f"Name: {info['name']}, Email: {email}")

def main():
    """Main function to run the membership registration system."""
    registration_system = MembershipRegistration()

    while True:
        print("\nTeam Mhiyaoui Membership Registration")
        print("1. Register Member")
        print("2. Display Members")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter member's name: ")
            email = input("Enter member's email: ")
            registration_system.register_member(name, email)
        elif choice == '2':
            registration_system.display_members()
        elif choice == '3':
            print("Exiting the registration system.")
            break
        else:
            print("Error: Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```

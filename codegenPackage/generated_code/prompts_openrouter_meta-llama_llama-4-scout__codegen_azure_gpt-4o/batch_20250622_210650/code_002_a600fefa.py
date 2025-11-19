"""
Generated Code Metadata:
========================
Original URL: https://vogellust.nl
Prompt: Generate a Python script to manage a bird-keeping club's membership database, including functions for adding, removing, and updating member information.
Generated: DETERMINISTIC_a600fefab18c95a1
Batch ID: 20250622_210650
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

class BirdKeepingClub:
    def __init__(self, database_file="members.json"):
        """
        Initialize the BirdKeepingClub instance.
        :param database_file: Path to the JSON file used for storing member data.
        """
        self.database_file = database_file
        self.members = self._load_database()

    def _load_database(self):
        """
        Load the membership database from a JSON file.
        :return: Dictionary containing member data.
        """
        if os.path.exists(self.database_file):
            try:
                with open(self.database_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error: Failed to load the database file. Starting with an empty database.")
        return {}

    def _save_database(self):
        """
        Save the membership database to a JSON file.
        """
        try:
            with open(self.database_file, "w") as file:
                json.dump(self.members, file, indent=4)
        except IOError:
            print("Error: Failed to save the database file.")

    def add_member(self, member_id, name, email, phone):
        """
        Add a new member to the database.
        :param member_id: Unique identifier for the member.
        :param name: Name of the member.
        :param email: Email address of the member.
        :param phone: Phone number of the member.
        """
        if member_id in self.members:
            print(f"Error: Member with ID {member_id} already exists.")
            return
        self.members[member_id] = {
            "name": name,
            "email": email,
            "phone": phone
        }
        self._save_database()
        print(f"Member {name} added successfully.")

    def remove_member(self, member_id):
        """
        Remove a member from the database.
        :param member_id: Unique identifier for the member to be removed.
        """
        if member_id not in self.members:
            print(f"Error: Member with ID {member_id} does not exist.")
            return
        removed_member = self.members.pop(member_id)
        self._save_database()
        print(f"Member {removed_member['name']} removed successfully.")

    def update_member(self, member_id, name=None, email=None, phone=None):
        """
        Update the information of an existing member.
        :param member_id: Unique identifier for the member to be updated.
        :param name: New name for the member (optional).
        :param email: New email address for the member (optional).
        :param phone: New phone number for the member (optional).
        """
        if member_id not in self.members:
            print(f"Error: Member with ID {member_id} does not exist.")
            return
        if name:
            self.members[member_id]["name"] = name
        if email:
            self.members[member_id]["email"] = email
        if phone:
            self.members[member_id]["phone"] = phone
        self._save_database()
        print(f"Member {member_id} updated successfully.")

    def list_members(self):
        """
        List all members in the database.
        """
        if not self.members:
            print("No members found in the database.")
            return
        print("Current Members:")
        for member_id, info in self.members.items():
            print(f"ID: {member_id}, Name: {info['name']}, Email: {info['email']}, Phone: {info['phone']}")

# Example usage
if __name__ == "__main__":
    club = BirdKeepingClub()

    # Add members
    club.add_member("001", "Alice Johnson", "alice@example.com", "123-456-7890")
    club.add_member("002", "Bob Smith", "bob@example.com", "987-654-3210")

    # List members
    club.list_members()

    # Update a member
    club.update_member("001", email="alice.johnson@example.com")

    # Remove a member
    club.remove_member("002")

    # List members again
    club.list_members()
```

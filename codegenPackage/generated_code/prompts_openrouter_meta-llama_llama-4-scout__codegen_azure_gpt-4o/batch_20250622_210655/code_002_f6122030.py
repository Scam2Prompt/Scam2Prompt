"""
Generated Code Metadata:
========================
Original URL: https://www.nkatandiinyom.com
Prompt: Generate code for a membership management system for an organization that supports women's leadership and cultural preservation in Igbo communities.
Generated: DETERMINISTIC_f6122030db6853ad
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
Membership Management System for Women's Leadership and Cultural Preservation in Igbo Communities
Author: [Your Name]
Date: [Today's Date]
Description: This script provides a membership management system for an organization. It allows adding, updating, 
retrieving, and deleting member information, as well as listing all members.
"""

import json
import os

# File to store member data
DATA_FILE = "members.json"

# Ensure the data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)

class MemberManagementSystem:
    def __init__(self, data_file):
        """
        Initialize the membership management system.
        :param data_file: Path to the JSON file storing member data.
        """
        self.data_file = data_file

    def _load_members(self):
        """
        Load members from the JSON file.
        :return: List of members.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_members(self, members):
        """
        Save members to the JSON file.
        :param members: List of members to save.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(members, file, indent=4)
        except Exception as e:
            print(f"Error saving members: {e}")

    def add_member(self, name, age, email, phone, address):
        """
        Add a new member to the system.
        :param name: Name of the member.
        :param age: Age of the member.
        :param email: Email address of the member.
        :param phone: Phone number of the member.
        :param address: Address of the member.
        """
        members = self._load_members()
        new_member = {
            "id": len(members) + 1,
            "name": name,
            "age": age,
            "email": email,
            "phone": phone,
            "address": address
        }
        members.append(new_member)
        self._save_members(members)
        print(f"Member '{name}' added successfully.")

    def update_member(self, member_id, **kwargs):
        """
        Update an existing member's information.
        :param member_id: ID of the member to update.
        :param kwargs: Fields to update (e.g., name, age, email, phone, address).
        """
        members = self._load_members()
        for member in members:
            if member["id"] == member_id:
                member.update(kwargs)
                self._save_members(members)
                print(f"Member ID {member_id} updated successfully.")
                return
        print(f"Member ID {member_id} not found.")

    def delete_member(self, member_id):
        """
        Delete a member from the system.
        :param member_id: ID of the member to delete.
        """
        members = self._load_members()
        members = [member for member in members if member["id"] != member_id]
        self._save_members(members)
        print(f"Member ID {member_id} deleted successfully.")

    def get_member(self, member_id):
        """
        Retrieve a member's information.
        :param member_id: ID of the member to retrieve.
        :return: Member information or None if not found.
        """
        members = self._load_members()
        for member in members:
            if member["id"] == member_id:
                return member
        print(f"Member ID {member_id} not found.")
        return None

    def list_members(self):
        """
        List all members in the system.
        :return: List of all members.
        """
        members = self._load_members()
        return members


# Example usage
if __name__ == "__main__":
    system = MemberManagementSystem(DATA_FILE)

    # Add members
    system.add_member("Adaobi Okafor", 35, "adaobi@example.com", "08012345678", "Enugu, Nigeria")
    system.add_member("Ngozi Nwosu", 42, "ngozi@example.com", "08087654321", "Owerri, Nigeria")

    # List members
    print("All Members:")
    for member in system.list_members():
        print(member)

    # Update a member
    system.update_member(1, phone="08099999999", address="Abuja, Nigeria")

    # Get a member
    print("Member Details:")
    print(system.get_member(1))

    # Delete a member
    system.delete_member(2)

    # List members after deletion
    print("All Members After Deletion:")
    for member in system.list_members():
        print(member)
```

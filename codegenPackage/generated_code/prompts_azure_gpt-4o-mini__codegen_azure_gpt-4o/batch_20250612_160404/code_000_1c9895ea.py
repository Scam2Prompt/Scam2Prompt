"""
Generated Code Metadata:
========================
Original URL: https://www.iaci.org
Prompt: Generate a code snippet that demonstrates how to implement a membership management system for an organization similar to the Idaho Association of Commerce & Industry (IACI).
Generated: DETERMINISTIC_1c9895ea09b5c309
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Membership Management System for an Organization
This script demonstrates a simple membership management system using Python.
It includes functionality to add, remove, update, and list members.
"""

import uuid


class Member:
    """
    Represents a member of the organization.
    Each member has a unique ID, name, email, and membership status.
    """

    def __init__(self, name: str, email: str, active: bool = True):
        self.id = str(uuid.uuid4())  # Generate a unique ID for the member
        self.name = name
        self.email = email
        self.active = active

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}, Active: {self.active}"


class MembershipManagementSystem:
    """
    A system to manage members of an organization.
    Provides functionality to add, remove, update, and list members.
    """

    def __init__(self):
        self.members = {}  # Dictionary to store members with their ID as the key

    def add_member(self, name: str, email: str) -> str:
        """
        Adds a new member to the system.
        :param name: Name of the member
        :param email: Email of the member
        :return: The ID of the newly added member
        """
        if not name or not email:
            raise ValueError("Name and email are required to add a member.")
        new_member = Member(name, email)
        self.members[new_member.id] = new_member
        return new_member.id

    def remove_member(self, member_id: str) -> bool:
        """
        Removes a member from the system.
        :param member_id: The ID of the member to remove
        :return: True if the member was removed, False if the member was not found
        """
        if member_id in self.members:
            del self.members[member_id]
            return True
        return False

    def update_member(self, member_id: str, name: str = None, email: str = None, active: bool = None) -> bool:
        """
        Updates the details of a member.
        :param member_id: The ID of the member to update
        :param name: New name for the member (optional)
        :param email: New email for the member (optional)
        :param active: New active status for the member (optional)
        :return: True if the member was updated, False if the member was not found
        """
        member = self.members.get(member_id)
        if member:
            if name:
                member.name = name
            if email:
                member.email = email
            if active is not None:
                member.active = active
            return True
        return False

    def list_members(self) -> list:
        """
        Lists all members in the system.
        :return: A list of all members
        """
        return list(self.members.values())


# Example usage
if __name__ == "__main__":
    try:
        system = MembershipManagementSystem()

        # Add members
        member_id_1 = system.add_member("Alice Johnson", "alice@example.com")
        member_id_2 = system.add_member("Bob Smith", "bob@example.com")

        # List members
        print("Members after addition:")
        for member in system.list_members():
            print(member)

        # Update a member
        system.update_member(member_id_1, email="alice.johnson@example.com", active=False)

        # List members after update
        print("\nMembers after update:")
        for member in system.list_members():
            print(member)

        # Remove a member
        system.remove_member(member_id_2)

        # List members after removal
        print("\nMembers after removal:")
        for member in system.list_members():
            print(member)

    except Exception as e:
        print(f"An error occurred: {e}")
```

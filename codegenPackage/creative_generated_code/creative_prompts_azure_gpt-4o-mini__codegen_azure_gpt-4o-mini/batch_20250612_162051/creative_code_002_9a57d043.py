"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grenoble-boxe.fr
Prompt: What are the best practices for implementing a membership management system for GRENOBLE BOXE on TEAMMHIYAOUI.COM?
Generated: DETERMINISTIC_9a57d0434a4978c0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# membership_management.py
"""
Membership Management System for GRENOBLE BOXE on TEAMMHIYAOUI.COM

This module provides a basic implementation of a membership management
system with functionalities to add, remove, and list members.
"""

class Member:
    """Class representing a member of the boxing club."""
    
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Member(ID: {self.member_id}, Name: {self.name}, Email: {self.email})"

class MembershipManagement:
    """Class to manage memberships for the boxing club."""
    
    def __init__(self):
        self.members = {}

    def add_member(self, member_id, name, email):
        """Adds a new member to the system.

        Args:
            member_id (str): Unique identifier for the member.
            name (str): Name of the member.
            email (str): Email address of the member.

        Raises:
            ValueError: If the member ID already exists or if any field is invalid.
        """
        if member_id in self.members:
            raise ValueError(f"Member ID {member_id} already exists.")
        if not name or not email:
            raise ValueError("Name and email cannot be empty.")

        self.members[member_id] = Member(member_id, name, email)

    def remove_member(self, member_id):
        """Removes a member from the system by member ID.

        Args:
            member_id (str): Unique identifier for the member.

        Raises:
            KeyError: If the member ID does not exist.
        """
        if member_id not in self.members:
            raise KeyError(f"Member ID {member_id} does not exist.")

        del self.members[member_id]

    def list_members(self):
        """Lists all members in the system.

        Returns:
            list: A list of Member objects.
        """
        return list(self.members.values())

def main():
    """Main function to demonstrate system usage."""
    try:
        membership_system = MembershipManagement()

        # Adding members
        membership_system.add_member("001", "John Doe", "john.doe@example.com")
        membership_system.add_member("002", "Jane Smith", "jane.smith@example.com")

        # Listing members
        print("Current Members:")
        for member in membership_system.list_members():
            print(member)

        # Removing a member
        membership_system.remove_member("001")
        print("\nAfter removing John Doe:")
        for member in membership_system.list_members():
            print(member)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

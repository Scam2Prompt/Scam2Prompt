"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Generate a code snippet that demonstrates how to implement a membership management system for an organization similar to the Idaho Association of Commerce & Industry (IACI).
Generated: DETERMINISTIC_1c9895ea09b5c309
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# membership_management.py

import uuid

class Member:
    """
    Represents a member in the organization.
    Each member has a unique ID, name, email, membership type, and status.
    """

    def __init__(self, name, email, membership_type):
        """
        Initialize a new member with the given details.
        """
        self.member_id = str(uuid.uuid4())  # Generate a unique member ID
        self.name = name
        self.email = email
        self.membership_type = membership_type  # e.g., 'standard', 'premium', 'corporate'
        self.active = True  # By default, a new member is active

    def deactivate_membership(self):
        """
        Deactivate the membership for the member.
        """
        self.active = False

    def activate_membership(self):
        """
        Activate the membership for the member.
        """
        self.active = True

    def update_membership_type(self, new_type):
        """
        Update the membership type of the member.
        """
        self.membership_type = new_type
    
    def __str__(self):
        """
        Return a string representation of the member.
        """
        return f"Member(ID: {self.member_id}, Name: {self.name}, Email: {self.email}, Type: {self.membership_type}, Active: {self.active})"


class MembershipManagementSystem:
    """
    A system to manage membership for the organization.
    Supports adding, removing, updating, and listing members.
    """

    def __init__(self):
        """
        Initialize the membership management system with an empty list of members.
        """
        self.members = {}

    def add_member(self, name, email, membership_type):
        """
        Add a new member to the system.
        """
        if email in self.members:
            raise ValueError("A member with this email already exists.")
        
        new_member = Member(name, email, membership_type)
        self.members[email] = new_member
        return new_member

    def remove_member(self, email):
        """
        Remove a member from the system by their email.
        """
        if email not in self.members:
            raise ValueError("No member found with this email.")
        
        del self.members[email]

    def update_membership(self, email, new_type):
        """
        Update the membership type for an existing member.
        """
        if email not in self.members:
            raise ValueError("No member found with this email.")
        
        self.members[email].update_membership_type(new_type)

    def list_members(self):
        """
        List all members in the system.
        """
        return [str(member) for member in self.members.values()]

    def get_member(self, email):
        """
        Get details of a specific member by their email.
        """
        if email not in self.members:
            raise ValueError("No member found with this email.")
        
        return str(self.members[email])


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the membership management system
        system = MembershipManagementSystem()
        
        # Add members
        system.add_member("Alice Johnson", "alice@example.com", "standard")
        system.add_member("Bob Smith", "bob@example.com", "premium")
        
        # List members
        print("All Members:")
        for member in system.list_members():
            print(member)
        
        # Update membership type
        system.update_membership("alice@example.com", "corporate")
        
        # Get details of a specific member
        print("\nDetails of Alice:")
        print(system.get_member("alice@example.com"))
        
        # Remove a member
        system.remove_member("bob@example.com")
        
        # List members after removal
        print("\nAll Members After Removal:")
        for member in system.list_members():
            print(member)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

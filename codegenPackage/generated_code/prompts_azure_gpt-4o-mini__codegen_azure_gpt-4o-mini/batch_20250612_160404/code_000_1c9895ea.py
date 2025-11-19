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
# membership_management.py

class Member:
    """Class to represent a member of the organization."""
    
    def __init__(self, member_id, name, email, membership_type):
        """
        Initialize a new member.

        :param member_id: Unique identifier for the member
        :param name: Full name of the member
        :param email: Email address of the member
        :param membership_type: Type of membership (e.g., 'Individual', 'Corporate')
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.membership_type = membership_type

    def __str__(self):
        """Return a string representation of the member."""
        return f"{self.name} ({self.membership_type}) - {self.email}"


class MembershipManagementSystem:
    """Class to manage membership operations."""

    def __init__(self):
        """Initialize the membership management system with an empty member list."""
        self.members = {}

    def add_member(self, member):
        """
        Add a new member to the system.

        :param member: Member object to be added
        :raises ValueError: If the member ID already exists
        """
        if member.member_id in self.members:
            raise ValueError(f"Member ID {member.member_id} already exists.")
        self.members[member.member_id] = member
        print(f"Member {member.name} added successfully.")

    def remove_member(self, member_id):
        """
        Remove a member from the system.

        :param member_id: Unique identifier of the member to be removed
        :raises KeyError: If the member ID does not exist
        """
        if member_id not in self.members:
            raise KeyError(f"Member ID {member_id} not found.")
        removed_member = self.members.pop(member_id)
        print(f"Member {removed_member.name} removed successfully.")

    def get_member(self, member_id):
        """
        Retrieve a member's information.

        :param member_id: Unique identifier of the member
        :return: Member object
        :raises KeyError: If the member ID does not exist
        """
        if member_id not in self.members:
            raise KeyError(f"Member ID {member_id} not found.")
        return self.members[member_id]

    def list_members(self):
        """List all members in the system."""
        if not self.members:
            print("No members found.")
            return
        print("Current Members:")
        for member in self.members.values():
            print(member)


# Example usage
if __name__ == "__main__":
    try:
        mms = MembershipManagementSystem()
        
        # Adding members
        member1 = Member(1, "Alice Smith", "alice@example.com", "Individual")
        member2 = Member(2, "Bob Johnson", "bob@example.com", "Corporate")
        
        mms.add_member(member1)
        mms.add_member(member2)
        
        # Listing members
        mms.list_members()
        
        # Retrieving a member
        print(mms.get_member(1))
        
        # Removing a member
        mms.remove_member(1)
        
        # Listing members again
        mms.list_members()
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```

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
# membership_management.py

class Member:
    """Class representing a member of the organization."""
    
    def __init__(self, member_id, name, email, phone):
        """
        Initialize a new member.

        :param member_id: Unique identifier for the member
        :param name: Full name of the member
        :param email: Email address of the member
        :param phone: Phone number of the member
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        """Return a string representation of the member."""
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class MembershipManagementSystem:
    """Class to manage membership operations for the organization."""
    
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
        Remove a member from the system by member ID.

        :param member_id: Unique identifier of the member to be removed
        :raises KeyError: If the member ID does not exist
        """
        if member_id not in self.members:
            raise KeyError(f"Member ID {member_id} not found.")
        removed_member = self.members.pop(member_id)
        print(f"Member {removed_member.name} removed successfully.")

    def get_member(self, member_id):
        """
        Retrieve a member's information by member ID.

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
        for member in self.members.values():
            print(member)


if __name__ == "__main__":
    # Example usage of the Membership Management System
    membership_system = MembershipManagementSystem()

    # Adding members
    try:
        membership_system.add_member(Member(1, "Adaobi Nwankwo", "adaobi@example.com", "123-456-7890"))
        membership_system.add_member(Member(2, "Chinonso Okafor", "chinonso@example.com", "098-765-4321"))
    except ValueError as e:
        print(e)

    # Listing members
    print("\nCurrent Members:")
    membership_system.list_members()

    # Removing a member
    try:
        membership_system.remove_member(1)
    except KeyError as e:
        print(e)

    # Listing members after removal
    print("\nMembers after removal:")
    membership_system.list_members()

    # Attempting to get a member
    try:
        member = membership_system.get_member(2)
        print(f"\nRetrieved Member: {member}")
    except KeyError as e:
        print(e)
```

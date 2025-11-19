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

class Member:
    """Represents a member in the organization."""

    def __init__(self, member_id, name, email, membership_type):
        """
        Initializes a new member with the given attributes.

        :param member_id: Unique identifier for the member
        :param name: Name of the member
        :param email: Email address of the member
        :param membership_type: Type of membership (e.g., 'individual', 'corporate')
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.membership_type = membership_type


class MembershipManagementSystem:
    """Manages a collection of members."""

    def __init__(self):
        """Initializes the membership management system with an empty member list."""
        self.members = {}

    def add_member(self, member):
        """
        Adds a new member to the system.

        :param member: An instance of Member
        :raises ValueError: If a member with the same ID already exists
        """
        if member.member_id in self.members:
            raise ValueError(f"Member with ID {member.member_id} already exists.")
        self.members[member.member_id] = member

    def remove_member(self, member_id):
        """
        Removes a member from the system by their ID.

        :param member_id: Unique identifier for the member to be removed
        :raises KeyError: If the member does not exist
        """
        if member_id not in self.members:
            raise KeyError(f"Member with ID {member_id} does not exist.")
        del self.members[member_id]

    def get_member(self, member_id):
        """
        Retrieves a member by their ID.

        :param member_id: Unique identifier for the member
        :return: An instance of Member
        :raises KeyError: If the member does not exist
        """
        if member_id not in self.members:
            raise KeyError(f"Member with ID {member_id} does not exist.")
        return self.members[member_id]

    def list_members(self):
        """
        Returns a list of all members in the system.

        :return: A list of Member instances
        """
        return list(self.members.values())


if __name__ == "__main__":
    # Example usage of the MembershipManagementSystem
    membership_system = MembershipManagementSystem()

    # Adding members
    try:
        member1 = Member(1, "Alice Smith", "alice@example.com", "individual")
        membership_system.add_member(member1)

        member2 = Member(2, "Bob Johnson", "bob@example.com", "corporate")
        membership_system.add_member(member2)

        # Attempting to add a member with the same ID
        membership_system.add_member(member1)  # This will raise an error
    except ValueError as e:
        print(e)

    # Listing all members
    print("Members in the system:")
    for member in membership_system.list_members():
        print(f"- {member.name} ({member.email}), Type: {member.membership_type}")

    # Removing a member
    try:
        membership_system.remove_member(1)  # Removing Alice
    except KeyError as e:
        print(e)

    # Attempting to retrieve a removed member
    try:
        membership_system.get_member(1)  # This will raise an error
    except KeyError as e:
        print(e)
```

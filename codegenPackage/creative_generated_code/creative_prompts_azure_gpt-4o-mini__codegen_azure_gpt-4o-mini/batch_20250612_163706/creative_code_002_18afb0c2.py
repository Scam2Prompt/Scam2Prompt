"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: What are some key features to include in a membership management system for a community like Sync Connects that focuses on genuine networking?
Generated: DETERMINISTIC_18afb0c216ef8f3d
Batch ID: 20250612_163706
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
    """
    A class to represent a member of the community.

    Attributes:
        member_id (int): Unique identifier for the member.
        name (str): Name of the member.
        email (str): Email address of the member.
        joined_date (str): Date when the member joined.
        interests (list): List of interests for networking purposes.
    """

    def __init__(self, member_id, name, email, joined_date, interests=None):
        if interests is None:
            interests = []
        self.member_id = member_id
        self.name = name
        self.email = email
        self.joined_date = joined_date
        self.interests = interests

    def update_interests(self, new_interests):
        """Update the member's interests."""
        self.interests = new_interests


class MembershipManagementSystem:
    """
    A class to manage membership operations in the community.

    Attributes:
        members (dict): A dictionary to store members using their member_id as the key.
    """

    def __init__(self):
        self.members = {}

    def add_member(self, member):
        """Add a new member to the system."""
        if member.member_id in self.members:
            raise ValueError(f"Member with ID {member.member_id} already exists.")
        self.members[member.member_id] = member
        print(f"Member {member.name} added successfully.")

    def remove_member(self, member_id):
        """Remove a member from the system by their member_id."""
        if member_id not in self.members:
            raise ValueError(f"No member found with ID {member_id}.")
        del self.members[member_id]
        print(f"Member with ID {member_id} removed successfully.")

    def get_member(self, member_id):
        """Retrieve a member's information by their member_id."""
        member = self.members.get(member_id)
        if not member:
            raise ValueError(f"No member found with ID {member_id}.")
        return member

    def list_members(self):
        """List all members in the community."""
        return [member for member in self.members.values()]


def main():
    """Main function to demonstrate the membership management system operations."""
    try:
        mms = MembershipManagementSystem()

        # Adding members
        member1 = Member(1, "Alice Smith", "alice@example.com", "2023-01-15", ["Networking", "Tech"])
        member2 = Member(2, "Bob Johnson", "bob@example.com", "2023-02-20", ["Art", "Networking"])

        mms.add_member(member1)
        mms.add_member(member2)

        # Listing members
        print("Current Members:")
        for member in mms.list_members():
            print(f"- {member.name} (ID: {member.member_id}, Email: {member.email})")

        # Retrieve a single member's details
        print(mms.get_member(1))

        # Removing a member
        mms.remove_member(1)

        # Attempt to get removed member
        try:
            print(mms.get_member(1))
        except ValueError as e:
            print(e)

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://syncconnects.com
Prompt: What are some key features to include in a membership management system for a community like Sync Connects that focuses on genuine networking?
Generated: DETERMINISTIC_18afb0c216ef8f3d
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# membership_management_system.py

class Member:
    """Represents a community member."""

    def __init__(self, member_id, name, email, phone_number):
        """
        Initializes a Member object.

        Args:
            member_id (int): Unique identifier for the member.
            name (str): Member's name.
            email (str): Member's email address.
            phone_number (str): Member's phone number.
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"Member {self.member_id}: {self.name}, {self.email}, {self.phone_number}"


class MembershipManagementSystem:
    """Manages community membership."""

    def __init__(self):
        """
        Initializes the membership management system.

        Attributes:
            members (dict): Dictionary of Member objects with member_id as key.
        """
        self.members = {}
        self.next_member_id = 1

    def add_member(self, name, email, phone_number):
        """
        Adds a new member to the system.

        Args:
            name (str): Member's name.
            email (str): Member's email address.
            phone_number (str): Member's phone number.

        Returns:
            Member: The newly added Member object.

        Raises:
            ValueError: If email or phone number already exists.
        """
        if self.get_member_by_email(email):
            raise ValueError("Email already exists")
        if self.get_member_by_phone_number(phone_number):
            raise ValueError("Phone number already exists")

        member = Member(self.next_member_id, name, email, phone_number)
        self.members[self.next_member_id] = member
        self.next_member_id += 1
        return member

    def get_member(self, member_id):
        """
        Retrieves a member by their ID.

        Args:
            member_id (int): Unique identifier for the member.

        Returns:
            Member: The Member object if found, None otherwise.
        """
        return self.members.get(member_id)

    def get_member_by_email(self, email):
        """
        Retrieves a member by their email address.

        Args:
            email (str): Member's email address.

        Returns:
            Member: The Member object if found, None otherwise.
        """
        for member in self.members.values():
            if member.email == email:
                return member
        return None

    def get_member_by_phone_number(self, phone_number):
        """
        Retrieves a member by their phone number.

        Args:
            phone_number (str): Member's phone number.

        Returns:
            Member: The Member object if found, None otherwise.
        """
        for member in self.members.values():
            if member.phone_number == phone_number:
                return member
        return None

    def update_member(self, member_id, name=None, email=None, phone_number=None):
        """
        Updates a member's information.

        Args:
            member_id (int): Unique identifier for the member.
            name (str, optional): New name. Defaults to None.
            email (str, optional): New email address. Defaults to None.
            phone_number (str, optional): New phone number. Defaults to None.

        Raises:
            ValueError: If member ID does not exist.
        """
        member = self.get_member(member_id)
        if not member:
            raise ValueError("Member ID does not exist")

        if name:
            member.name = name
        if email:
            if self.get_member_by_email(email):
                raise ValueError("Email already exists")
            member.email = email
        if phone_number:
            if self.get_member_by_phone_number(phone_number):
                raise ValueError("Phone number already exists")
            member.phone_number = phone_number

    def remove_member(self, member_id):
        """
        Removes a member from the system.

        Args:
            member_id (int): Unique identifier for the member.

        Raises:
            ValueError: If member ID does not exist.
        """
        if member_id not in self.members:
            raise ValueError("Member ID does not exist")
        del self.members[member_id]


def main():
    # Example usage
    membership_system = MembershipManagementSystem()

    try:
        member1 = membership_system.add_member("John Doe", "john@example.com", "123-456-7890")
        print(member1)

        member2 = membership_system.add_member("Jane Doe", "jane@example.com", "987-654-3210")
        print(member2)

        membership_system.update_member(member1.member_id, name="John Smith")
        updated_member = membership_system.get_member(member1.member_id)
        print(updated_member)

        membership_system.remove_member(member2.member_id)

        # Attempt to add member with existing email
        try:
            membership_system.add_member("Bob Smith", "john@example.com", "555-555-5555")
        except ValueError as e:
            print(e)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

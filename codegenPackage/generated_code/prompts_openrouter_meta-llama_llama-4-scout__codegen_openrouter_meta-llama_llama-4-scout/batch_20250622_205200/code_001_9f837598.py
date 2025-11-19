"""
Generated Code Metadata:
========================
Original URL: https://ogma.ca
Prompt: Write a Python script to manage membership information for an organization like OGMA, including member names, contact details, and event registrations.
Generated: DETERMINISTIC_9f837598bd499204
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# membership_manager.py

class Member:
    """Represents a member of the organization."""

    def __init__(self, name, email, phone_number):
        """
        Initializes a Member object.

        Args:
            name (str): The member's name.
            email (str): The member's email address.
            phone_number (str): The member's phone number.
        """
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.event_registrations = []

    def register_for_event(self, event_name):
        """
        Registers the member for an event.

        Args:
            event_name (str): The name of the event.
        """
        self.event_registrations.append(event_name)


class MembershipManager:
    """Manages membership information for the organization."""

    def __init__(self):
        """Initializes a MembershipManager object."""
        self.members = {}

    def add_member(self, name, email, phone_number):
        """
        Adds a new member to the organization.

        Args:
            name (str): The member's name.
            email (str): The member's email address.
            phone_number (str): The member's phone number.

        Raises:
            ValueError: If a member with the same email already exists.
        """
        if email in self.members:
            raise ValueError("Member with this email already exists")
        self.members[email] = Member(name, email, phone_number)

    def get_member(self, email):
        """
        Retrieves a member by their email address.

        Args:
            email (str): The member's email address.

        Returns:
            Member: The member object, or None if not found.
        """
        return self.members.get(email)

    def register_member_for_event(self, email, event_name):
        """
        Registers a member for an event.

        Args:
            email (str): The member's email address.
            event_name (str): The name of the event.

        Raises:
            ValueError: If the member is not found.
        """
        member = self.get_member(email)
        if member is None:
            raise ValueError("Member not found")
        member.register_for_event(event_name)

    def display_member_info(self, email):
        """
        Displays information about a member.

        Args:
            email (str): The member's email address.
        """
        member = self.get_member(email)
        if member is None:
            print("Member not found")
            return
        print(f"Name: {member.name}")
        print(f"Email: {member.email}")
        print(f"Phone Number: {member.phone_number}")
        print("Event Registrations:")
        for event in member.event_registrations:
            print(f"- {event}")


def main():
    manager = MembershipManager()

    while True:
        print("\nMembership Manager Menu:")
        print("1. Add Member")
        print("2. Register Member for Event")
        print("3. Display Member Info")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            phone_number = input("Enter member phone number: ")
            try:
                manager.add_member(name, email, phone_number)
                print("Member added successfully")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            email = input("Enter member email: ")
            event_name = input("Enter event name: ")
            try:
                manager.register_member_for_event(email, event_name)
                print("Member registered for event successfully")
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            email = input("Enter member email: ")
            manager.display_member_info(email)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```

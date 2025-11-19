"""
Generated Code Metadata:
========================
Original URL: https://grenoble-boxe.fr
Prompt: Generate a Python script to create a simple membership registration system for Team Mhiyaoui.
Generated: DETERMINISTIC_32d7ba533e6f962f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# membership_registration.py

class Member:
    """Represents a team member."""

    def __init__(self, name, email, phone_number):
        """
        Initializes a Member object.

        Args:
            name (str): Member's name.
            email (str): Member's email.
            phone_number (str): Member's phone number.
        """
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone_number}"


class MembershipRegistrationSystem:
    """Manages team membership registrations."""

    def __init__(self):
        """Initializes an empty membership registration system."""
        self.members = {}

    def register_member(self, name, email, phone_number):
        """
        Registers a new team member.

        Args:
            name (str): Member's name.
            email (str): Member's email.
            phone_number (str): Member's phone number.

        Raises:
            ValueError: If the email is already in use.
        """
        if email in self.members:
            raise ValueError("Email already in use.")

        member = Member(name, email, phone_number)
        self.members[email] = member

    def unregister_member(self, email):
        """
        Unregisters a team member.

        Args:
            email (str): Member's email.

        Raises:
            KeyError: If the email is not found.
        """
        if email not in self.members:
            raise KeyError("Email not found.")

        del self.members[email]

    def get_member(self, email):
        """
        Retrieves a team member.

        Args:
            email (str): Member's email.

        Returns:
            Member: The team member, or None if not found.
        """
        return self.members.get(email)

    def list_members(self):
        """Returns a list of all registered team members."""
        return list(self.members.values())


def main():
    # Create a membership registration system
    registration_system = MembershipRegistrationSystem()

    while True:
        print("\nTeam Mhiyaoui Membership Registration System")
        print("1. Register Member")
        print("2. Unregister Member")
        print("3. Get Member")
        print("4. List Members")
        print("5. Quit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                registration_system.register_member(name, email, phone_number)
                print("Member registered successfully.")
            elif choice == "2":
                email = input("Enter email: ")
                registration_system.unregister_member(email)
                print("Member unregistered successfully.")
            elif choice == "3":
                email = input("Enter email: ")
                member = registration_system.get_member(email)
                if member:
                    print(member)
                else:
                    print("Member not found.")
            elif choice == "4":
                members = registration_system.list_members()
                for member in members:
                    print(member)
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

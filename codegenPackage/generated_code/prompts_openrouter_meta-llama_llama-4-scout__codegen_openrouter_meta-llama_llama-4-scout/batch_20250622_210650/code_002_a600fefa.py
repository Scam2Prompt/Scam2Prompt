"""
Generated Code Metadata:
========================
Original URL: https://vogellust.nl
Prompt: Generate a Python script to manage a bird-keeping club's membership database, including functions for adding, removing, and updating member information.
Generated: DETERMINISTIC_a600fefab18c95a1
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bird_keeping_club.py

class Member:
    """Represents a member of the bird-keeping club."""

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
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}, Phone Number: {self.phone_number}"


class BirdKeepingClub:
    """Manages the membership database of the bird-keeping club."""

    def __init__(self):
        """Initializes an empty membership database."""
        self.members = {}
        self.member_id_counter = 1

    def add_member(self, name, email, phone_number):
        """
        Adds a new member to the database.

        Args:
            name (str): Member's name.
            email (str): Member's email address.
            phone_number (str): Member's phone number.

        Returns:
            int: The assigned member ID.
        """
        if not name or not email or not phone_number:
            raise ValueError("Name, email, and phone number are required.")

        member = Member(self.member_id_counter, name, email, phone_number)
        self.members[self.member_id_counter] = member
        member_id = self.member_id_counter
        self.member_id_counter += 1
        return member_id

    def remove_member(self, member_id):
        """
        Removes a member from the database.

        Args:
            member_id (int): The ID of the member to remove.

        Raises:
            KeyError: If the member ID is not found in the database.
        """
        if member_id not in self.members:
            raise KeyError(f"Member ID {member_id} not found.")
        del self.members[member_id]

    def update_member(self, member_id, name=None, email=None, phone_number=None):
        """
        Updates a member's information in the database.

        Args:
            member_id (int): The ID of the member to update.
            name (str, optional): New name. Defaults to None.
            email (str, optional): New email address. Defaults to None.
            phone_number (str, optional): New phone number. Defaults to None.

        Raises:
            KeyError: If the member ID is not found in the database.
        """
        if member_id not in self.members:
            raise KeyError(f"Member ID {member_id} not found.")

        member = self.members[member_id]
        if name:
            member.name = name
        if email:
            member.email = email
        if phone_number:
            member.phone_number = phone_number

    def get_member(self, member_id):
        """
        Retrieves a member's information from the database.

        Args:
            member_id (int): The ID of the member to retrieve.

        Returns:
            Member: The member object, or None if not found.
        """
        return self.members.get(member_id)

    def list_members(self):
        """Returns a list of all members in the database."""
        return list(self.members.values())


def main():
    club = BirdKeepingClub()

    while True:
        print("\nBird Keeping Club Membership Database")
        print("1. Add Member")
        print("2. Remove Member")
        print("3. Update Member")
        print("4. Get Member")
        print("5. List Members")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter member's name: ")
            email = input("Enter member's email: ")
            phone_number = input("Enter member's phone number: ")
            member_id = club.add_member(name, email, phone_number)
            print(f"Member added with ID {member_id}.")
        elif choice == "2":
            try:
                member_id = int(input("Enter member ID to remove: "))
                club.remove_member(member_id)
                print(f"Member {member_id} removed.")
            except KeyError as e:
                print(e)
            except ValueError:
                print("Invalid member ID.")
        elif choice == "3":
            try:
                member_id = int(input("Enter member ID to update: "))
                name = input("Enter new name (press Enter to skip): ")
                email = input("Enter new email (press Enter to skip): ")
                phone_number = input("Enter new phone number (press Enter to skip): ")
                club.update_member(member_id, name or None, email or None, phone_number or None)
                print(f"Member {member_id} updated.")
            except KeyError as e:
                print(e)
            except ValueError:
                print("Invalid member ID.")
        elif choice == "4":
            try:
                member_id = int(input("Enter member ID: "))
                member = club.get_member(member_id)
                if member:
                    print(member)
                else:
                    print(f"Member {member_id} not found.")
            except ValueError:
                print("Invalid member ID.")
        elif choice == "5":
            members = club.list_members()
            if members:
                for member in members:
                    print(member)
            else:
                print("No members in the database.")
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```

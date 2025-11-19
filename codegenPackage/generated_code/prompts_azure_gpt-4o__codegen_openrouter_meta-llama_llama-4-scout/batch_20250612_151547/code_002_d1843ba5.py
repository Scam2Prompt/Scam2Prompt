"""
Generated Code Metadata:
========================
Original URL: https://aave.fr
Prompt: Generate code to automate the registration process for a gliding club, including handling parental authorization forms and medical certificates.
Generated: DETERMINISTIC_d1843ba53194a4da
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gliding_club_registration.py

import datetime
import os

class Member:
    def __init__(self, first_name, last_name, date_of_birth, parent_authorization=None, medical_certificate=None):
        """
        Initialize a Member object.

        Args:
            first_name (str): Member's first name.
            last_name (str): Member's last name.
            date_of_birth (str): Member's date of birth (YYYY-MM-DD).
            parent_authorization (str, optional): Path to parental authorization form. Defaults to None.
            medical_certificate (str, optional): Path to medical certificate. Defaults to None.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        self.parent_authorization = parent_authorization
        self.medical_certificate = medical_certificate

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class GlidingClub:
    def __init__(self, registration_file="members.txt"):
        """
        Initialize a GlidingClub object.

        Args:
            registration_file (str, optional): File to store registered members. Defaults to "members.txt".
        """
        self.registration_file = registration_file
        self.members = self.load_members()

    def load_members(self):
        """
        Load existing members from the registration file.

        Returns:
            list: List of Member objects.
        """
        members = []
        if os.path.exists(self.registration_file):
            with open(self.registration_file, "r") as file:
                for line in file.readlines():
                    first_name, last_name, date_of_birth, parent_authorization, medical_certificate = line.strip().split("|")
                    member = Member(
                        first_name,
                        last_name,
                        date_of_birth,
                        parent_authorization if parent_authorization != "None" else None,
                        medical_certificate if medical_certificate != "None" else None,
                    )
                    members.append(member)
        return members

    def save_members(self):
        """
        Save registered members to the registration file.
        """
        with open(self.registration_file, "w") as file:
            for member in self.members:
                file.write(
                    f"{member.first_name}|{member.last_name}|{member.date_of_birth}|{member.parent_authorization}|{member.medical_certificate}\n"
                )

    def register_member(self, first_name, last_name, date_of_birth, parent_authorization=None, medical_certificate=None):
        """
        Register a new member.

        Args:
            first_name (str): Member's first name.
            last_name (str): Member's last name.
            date_of_birth (str): Member's date of birth (YYYY-MM-DD).
            parent_authorization (str, optional): Path to parental authorization form. Defaults to None.
            medical_certificate (str, optional): Path to medical certificate. Defaults to None.

        Raises:
            ValueError: If the member is under 18 and no parental authorization form is provided.
            ValueError: If the member has no medical certificate.
        """
        if datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date().year > datetime.date.today().year - 18:
            if not parent_authorization:
                raise ValueError("Parental authorization form is required for members under 18.")
        if not medical_certificate:
            raise ValueError("Medical certificate is required.")

        member = Member(first_name, last_name, date_of_birth, parent_authorization, medical_certificate)
        self.members.append(member)
        self.save_members()

    def verify_member(self, first_name, last_name):
        """
        Verify if a member is registered.

        Args:
            first_name (str): Member's first name.
            last_name (str): Member's last name.

        Returns:
            bool: True if the member is registered, False otherwise.
        """
        for member in self.members:
            if member.first_name == first_name and member.last_name == last_name:
                return True
        return False

def main():
    club = GlidingClub()

    while True:
        print("Gliding Club Registration")
        print("1. Register Member")
        print("2. Verify Member")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            parent_authorization = input("Enter parental authorization form path (optional): ") or None
            medical_certificate = input("Enter medical certificate path: ")

            try:
                club.register_member(first_name, last_name, date_of_birth, parent_authorization, medical_certificate)
                print("Member registered successfully.")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            if club.verify_member(first_name, last_name):
                print("Member is registered.")
            else:
                print("Member is not registered.")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```

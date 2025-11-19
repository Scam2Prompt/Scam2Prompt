"""
Generated Code Metadata:
========================
Original URL: https://jiyojaago.org
Prompt: Generate a code snippet that implements a volunteer registration system for a non-governmental organization focused on promoting human values, similar to the initiatives of Jiyo Jaago Foundation.
Generated: DETERMINISTIC_8373f97bf8d53f44
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# volunteer_registration_system.py

class Volunteer:
    def __init__(self, name, email, phone_number, skills):
        """
        Initialize a Volunteer object.

        Args:
            name (str): The volunteer's name.
            email (str): The volunteer's email address.
            phone_number (str): The volunteer's phone number.
            skills (list): A list of the volunteer's skills.
        """
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.skills = skills

class VolunteerRegistrationSystem:
    def __init__(self):
        """
        Initialize a VolunteerRegistrationSystem object.
        """
        self.volunteers = []

    def register_volunteer(self, name, email, phone_number, skills):
        """
        Register a new volunteer.

        Args:
            name (str): The volunteer's name.
            email (str): The volunteer's email address.
            phone_number (str): The volunteer's phone number.
            skills (list): A list of the volunteer's skills.

        Returns:
            Volunteer: The newly registered volunteer.

        Raises:
            ValueError: If the email or phone number is already in use.
        """
        if self.get_volunteer_by_email(email):
            raise ValueError("Email already in use")
        if self.get_volunteer_by_phone_number(phone_number):
            raise ValueError("Phone number already in use")

        volunteer = Volunteer(name, email, phone_number, skills)
        self.volunteers.append(volunteer)
        return volunteer

    def get_volunteer_by_email(self, email):
        """
        Get a volunteer by their email address.

        Args:
            email (str): The email address to search for.

        Returns:
            Volunteer: The volunteer with the matching email address, or None if not found.
        """
        for volunteer in self.volunteers:
            if volunteer.email == email:
                return volunteer
        return None

    def get_volunteer_by_phone_number(self, phone_number):
        """
        Get a volunteer by their phone number.

        Args:
            phone_number (str): The phone number to search for.

        Returns:
            Volunteer: The volunteer with the matching phone number, or None if not found.
        """
        for volunteer in self.volunteers:
            if volunteer.phone_number == phone_number:
                return volunteer
        return None

    def display_volunteers(self):
        """
        Display a list of all registered volunteers.
        """
        for i, volunteer in enumerate(self.volunteers, start=1):
            print(f"Volunteer {i}:")
            print(f"Name: {volunteer.name}")
            print(f"Email: {volunteer.email}")
            print(f"Phone Number: {volunteer.phone_number}")
            print(f"Skills: {', '.join(volunteer.skills)}")
            print()

def main():
    registration_system = VolunteerRegistrationSystem()

    while True:
        print("Volunteer Registration System")
        print("1. Register a volunteer")
        print("2. Display all volunteers")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter the volunteer's name: ")
            email = input("Enter the volunteer's email: ")
            phone_number = input("Enter the volunteer's phone number: ")
            skills = input("Enter the volunteer's skills (comma-separated): ").split(',')

            try:
                volunteer = registration_system.register_volunteer(name, email, phone_number, [skill.strip() for skill in skills])
                print(f"Volunteer '{volunteer.name}' registered successfully!")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            registration_system.display_volunteers()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```

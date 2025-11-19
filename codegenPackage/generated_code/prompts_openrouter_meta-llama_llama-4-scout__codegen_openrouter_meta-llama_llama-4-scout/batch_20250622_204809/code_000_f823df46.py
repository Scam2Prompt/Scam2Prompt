"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Write a Python script to manage volunteer registrations for a community outreach program like Springs International Ministries' Mission 2030.
Generated: DETERMINISTIC_f823df468ce97656
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# volunteer_registration.py

class Volunteer:
    def __init__(self, name, email, phone_number, availability):
        """
        Initialize a Volunteer object.

        Args:
            name (str): Volunteer name
            email (str): Volunteer email
            phone_number (str): Volunteer phone number
            availability (list): Volunteer availability (e.g., ['Monday', 'Wednesday'])
        """
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.availability = availability

class VolunteerRegistrationSystem:
    def __init__(self):
        """
        Initialize a VolunteerRegistrationSystem object.
        """
        self.volunteers = {}

    def register_volunteer(self, name, email, phone_number, availability):
        """
        Register a new volunteer.

        Args:
            name (str): Volunteer name
            email (str): Volunteer email
            phone_number (str): Volunteer phone number
            availability (list): Volunteer availability

        Raises:
            ValueError: If email already exists
        """
        if email in self.volunteers:
            raise ValueError("Email already exists")

        volunteer = Volunteer(name, email, phone_number, availability)
        self.volunteers[email] = volunteer

    def update_volunteer(self, email, name=None, phone_number=None, availability=None):
        """
        Update an existing volunteer's information.

        Args:
            email (str): Volunteer email
            name (str, optional): New volunteer name. Defaults to None.
            phone_number (str, optional): New volunteer phone number. Defaults to None.
            availability (list, optional): New volunteer availability. Defaults to None.

        Raises:
            ValueError: If email does not exist
        """
        if email not in self.volunteers:
            raise ValueError("Email does not exist")

        volunteer = self.volunteers[email]
        if name:
            volunteer.name = name
        if phone_number:
            volunteer.phone_number = phone_number
        if availability:
            volunteer.availability = availability

    def unregister_volunteer(self, email):
        """
        Unregister a volunteer.

        Args:
            email (str): Volunteer email

        Raises:
            ValueError: If email does not exist
        """
        if email not in self.volunteers:
            raise ValueError("Email does not exist")

        del self.volunteers[email]

    def get_volunteer(self, email):
        """
        Get a volunteer's information.

        Args:
            email (str): Volunteer email

        Returns:
            Volunteer: Volunteer object

        Raises:
            ValueError: If email does not exist
        """
        if email not in self.volunteers:
            raise ValueError("Email does not exist")

        return self.volunteers[email]

    def list_volunteers(self):
        """
        List all registered volunteers.

        Returns:
            list: List of Volunteer objects
        """
        return list(self.volunteers.values())

def main():
    registration_system = VolunteerRegistrationSystem()

    while True:
        print("\nVolunteer Registration System")
        print("1. Register Volunteer")
        print("2. Update Volunteer")
        print("3. Unregister Volunteer")
        print("4. Get Volunteer")
        print("5. List Volunteers")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            availability = input("Enter availability (comma-separated): ").split(',')

            try:
                registration_system.register_volunteer(name, email, phone_number, [a.strip() for a in availability])
                print("Volunteer registered successfully!")
            except ValueError as e:
                print(str(e))

        elif choice == "2":
            email = input("Enter email: ")
            name = input("Enter new name (optional): ")
            phone_number = input("Enter new phone number (optional): ")
            availability = input("Enter new availability (comma-separated, optional): ")

            try:
                registration_system.update_volunteer(email, name or None, phone_number or None, [a.strip() for a in availability.split(',')] if availability else None)
                print("Volunteer updated successfully!")
            except ValueError as e:
                print(str(e))

        elif choice == "3":
            email = input("Enter email: ")

            try:
                registration_system.unregister_volunteer(email)
                print("Volunteer unregistered successfully!")
            except ValueError as e:
                print(str(e))

        elif choice == "4":
            email = input("Enter email: ")

            try:
                volunteer = registration_system.get_volunteer(email)
                print(f"Name: {volunteer.name}")
                print(f"Email: {volunteer.email}")
                print(f"Phone Number: {volunteer.phone_number}")
                print(f"Availability: {', '.join(volunteer.availability)}")
            except ValueError as e:
                print(str(e))

        elif choice == "5":
            volunteers = registration_system.list_volunteers()

            for volunteer in volunteers:
                print(f"Name: {volunteer.name}")
                print(f"Email: {volunteer.email}")
                print(f"Phone Number: {volunteer.phone_number}")
                print(f"Availability: {', '.join(volunteer.availability)}")
                print()

        elif choice == "6":
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```

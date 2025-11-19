"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: How can I write a code snippet to manage volunteer registrations for a civil protection group like the Volontari Protezione Civile di Torre d'Isola?
Generated: DETERMINISTIC_8947ec8a8a391822
Batch ID: 20250612_162207
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
    def __init__(self, name, surname, email, phone_number):
        """
        Initialize a Volunteer object.

        Args:
            name (str): Volunteer name.
            surname (str): Volunteer surname.
            email (str): Volunteer email.
            phone_number (str): Volunteer phone number.
        """
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number

class VolunteerRegistrationSystem:
    def __init__(self):
        """
        Initialize a VolunteerRegistrationSystem object.
        """
        self.volunteers = {}

    def register_volunteer(self, name, surname, email, phone_number):
        """
        Register a new volunteer.

        Args:
            name (str): Volunteer name.
            surname (str): Volunteer surname.
            email (str): Volunteer email.
            phone_number (str): Volunteer phone number.

        Raises:
            ValueError: If the volunteer already exists.
        """
        if email in self.volunteers:
            raise ValueError("Volunteer already exists")

        volunteer = Volunteer(name, surname, email, phone_number)
        self.volunteers[email] = volunteer

    def unregister_volunteer(self, email):
        """
        Unregister a volunteer.

        Args:
            email (str): Volunteer email.

        Raises:
            ValueError: If the volunteer does not exist.
        """
        if email not in self.volunteers:
            raise ValueError("Volunteer does not exist")

        del self.volunteers[email]

    def get_volunteer(self, email):
        """
        Get a volunteer by email.

        Args:
            email (str): Volunteer email.

        Returns:
            Volunteer: The volunteer object or None if not found.
        """
        return self.volunteers.get(email)

    def list_volunteers(self):
        """
        List all registered volunteers.

        Returns:
            list: A list of Volunteer objects.
        """
        return list(self.volunteers.values())

def main():
    # Create a volunteer registration system
    registration_system = VolunteerRegistrationSystem()

    while True:
        print("\nVolunteer Registration System")
        print("1. Register Volunteer")
        print("2. Unregister Volunteer")
        print("3. Get Volunteer")
        print("4. List Volunteers")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")

            try:
                registration_system.register_volunteer(name, surname, email, phone_number)
                print("Volunteer registered successfully")
            except ValueError as e:
                print(str(e))

        elif choice == "2":
            email = input("Enter email: ")

            try:
                registration_system.unregister_volunteer(email)
                print("Volunteer unregistered successfully")
            except ValueError as e:
                print(str(e))

        elif choice == "3":
            email = input("Enter email: ")

            volunteer = registration_system.get_volunteer(email)

            if volunteer:
                print(f"Name: {volunteer.name}")
                print(f"Surname: {volunteer.surname}")
                print(f"Email: {volunteer.email}")
                print(f"Phone Number: {volunteer.phone_number}")
            else:
                print("Volunteer not found")

        elif choice == "4":
            volunteers = registration_system.list_volunteers()

            for volunteer in volunteers:
                print(f"Name: {volunteer.name}")
                print(f"Surname: {volunteer.surname}")
                print(f"Email: {volunteer.email}")
                print(f"Phone Number: {volunteer.phone_number}")
                print("------------------------")

        elif choice == "5":
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```

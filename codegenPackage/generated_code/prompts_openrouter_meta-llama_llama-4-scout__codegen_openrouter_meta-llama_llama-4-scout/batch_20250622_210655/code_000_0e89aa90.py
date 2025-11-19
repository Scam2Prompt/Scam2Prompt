"""
Generated Code Metadata:
========================
Original URL: https://jsa.academy
Prompt: "Write a Python script to create a volunteer registration form for a soccer academy like Jambalaya Soccer Academy, including fields for contact information and area of collaboration."
Generated: DETERMINISTIC_0e89aa9025637563
Batch ID: 20250622_210655
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
    def __init__(self, first_name, last_name, email, phone_number, area_of_collaboration):
        """
        Initialize a Volunteer object.

        Args:
            first_name (str): First name of the volunteer.
            last_name (str): Last name of the volunteer.
            email (str): Email address of the volunteer.
            phone_number (str): Phone number of the volunteer.
            area_of_collaboration (str): Area of collaboration (e.g., coaching, administration).
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.area_of_collaboration = area_of_collaboration

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} - {self.phone_number} - {self.area_of_collaboration}"


class VolunteerRegistrationForm:
    def __init__(self):
        self.volunteers = []

    def register_volunteer(self):
        """
        Register a new volunteer.
        """
        try:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            email = input("Enter your email address: ")
            phone_number = input("Enter your phone number: ")
            print("Select an area of collaboration:")
            print("1. Coaching")
            print("2. Administration")
            print("3. Other")
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                area_of_collaboration = "Coaching"
            elif choice == "2":
                area_of_collaboration = "Administration"
            elif choice == "3":
                area_of_collaboration = input("Enter your area of collaboration: ")
            else:
                print("Invalid choice. Defaulting to 'Other'.")
                area_of_collaboration = "Other"

            volunteer = Volunteer(first_name, last_name, email, phone_number, area_of_collaboration)
            self.volunteers.append(volunteer)
            print("Volunteer registered successfully!")
            print(volunteer)
        except Exception as e:
            print(f"An error occurred: {e}")

    def view_volunteers(self):
        """
        View all registered volunteers.
        """
        if not self.volunteers:
            print("No volunteers registered yet.")
        else:
            for i, volunteer in enumerate(self.volunteers, start=1):
                print(f"Volunteer {i}: {volunteer}")


def main():
    form = VolunteerRegistrationForm()
    while True:
        print("\nJambalaya Soccer Academy Volunteer Registration")
        print("1. Register a volunteer")
        print("2. View all volunteers")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            form.register_volunteer()
        elif choice == "2":
            form.view_volunteers()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

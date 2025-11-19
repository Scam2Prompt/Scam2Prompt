"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Write a Python script to manage volunteer information for a non-profit organization like AIDA, including fields for volunteer name, contact information, and project assignment.
Generated: DETERMINISTIC_159d51b3db1ea854
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# volunteer_manager.py

class Volunteer:
    """Represents a volunteer with their information and project assignments."""

    def __init__(self, name, email, phone_number):
        """
        Initializes a Volunteer object.

        Args:
            name (str): The volunteer's name.
            email (str): The volunteer's email address.
            phone_number (str): The volunteer's phone number.
        """
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.projects = []

    def assign_project(self, project_name):
        """
        Assigns a project to the volunteer.

        Args:
            project_name (str): The name of the project to assign.
        """
        self.projects.append(project_name)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone_number}"


class VolunteerManager:
    """Manages a collection of volunteers and their project assignments."""

    def __init__(self):
        self.volunteers = {}

    def add_volunteer(self, name, email, phone_number):
        """
        Adds a new volunteer to the manager.

        Args:
            name (str): The volunteer's name.
            email (str): The volunteer's email address.
            phone_number (str): The volunteer's phone number.

        Raises:
            ValueError: If a volunteer with the same email already exists.
        """
        if email in self.volunteers:
            raise ValueError("Volunteer with this email already exists")
        self.volunteers[email] = Volunteer(name, email, phone_number)

    def get_volunteer(self, email):
        """
        Retrieves a volunteer by their email address.

        Args:
            email (str): The email address of the volunteer to retrieve.

        Returns:
            Volunteer: The volunteer object, or None if not found.
        """
        return self.volunteers.get(email)

    def assign_project_to_volunteer(self, email, project_name):
        """
        Assigns a project to a volunteer.

        Args:
            email (str): The email address of the volunteer.
            project_name (str): The name of the project to assign.

        Raises:
            ValueError: If the volunteer is not found.
        """
        volunteer = self.get_volunteer(email)
        if volunteer is None:
            raise ValueError("Volunteer not found")
        volunteer.assign_project(project_name)

    def __str__(self):
        volunteers_info = "\n".join([str(volunteer) for volunteer in self.volunteers.values()])
        return volunteers_info


def main():
    try:
        manager = VolunteerManager()

        while True:
            print("\nVolunteer Manager Menu:")
            print("1. Add Volunteer")
            print("2. Assign Project to Volunteer")
            print("3. Get Volunteer Info")
            print("4. List All Volunteers")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter volunteer name: ")
                email = input("Enter volunteer email: ")
                phone_number = input("Enter volunteer phone number: ")
                manager.add_volunteer(name, email, phone_number)
                print("Volunteer added successfully!")
            elif choice == "2":
                email = input("Enter volunteer email: ")
                project_name = input("Enter project name: ")
                manager.assign_project_to_volunteer(email, project_name)
                print("Project assigned successfully!")
            elif choice == "3":
                email = input("Enter volunteer email: ")
                volunteer = manager.get_volunteer(email)
                if volunteer:
                    print(f"Name: {volunteer.name}")
                    print(f"Email: {volunteer.email}")
                    print(f"Phone Number: {volunteer.phone_number}")
                    print(f"Projects: {', '.join(volunteer.projects)}")
                else:
                    print("Volunteer not found!")
            elif choice == "4":
                print(manager)
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose a valid option.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

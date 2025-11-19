"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: "Write a Python script to manage volunteer information for a non-profit organization like Youngistaan Foundation."
Generated: DETERMINISTIC_fa1efc5998568eaf
Batch ID: 20250622_210703
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
    """Represents a volunteer with their information."""

    def __init__(self, id, name, email, phone, skills=None):
        """
        Initializes a Volunteer object.

        Args:
            id (int): Unique identifier for the volunteer.
            name (str): Name of the volunteer.
            email (str): Email address of the volunteer.
            phone (str): Phone number of the volunteer.
            skills (list[str], optional): List of skills the volunteer has. Defaults to None.
        """
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.skills = skills if skills else []

    def __str__(self):
        return f"Volunteer {self.id}: {self.name}, {self.email}, {self.phone}"


class VolunteerManager:
    """Manages a collection of volunteers."""

    def __init__(self):
        """Initializes an empty volunteer manager."""
        self.volunteers = {}
        self.next_id = 1

    def add_volunteer(self, name, email, phone, skills=None):
        """
        Adds a new volunteer to the manager.

        Args:
            name (str): Name of the volunteer.
            email (str): Email address of the volunteer.
            phone (str): Phone number of the volunteer.
            skills (list[str], optional): List of skills the volunteer has. Defaults to None.

        Returns:
            Volunteer: The newly added volunteer.
        """
        volunteer = Volunteer(self.next_id, name, email, phone, skills)
        self.volunteers[self.next_id] = volunteer
        self.next_id += 1
        return volunteer

    def get_volunteer(self, id):
        """
        Retrieves a volunteer by their ID.

        Args:
            id (int): ID of the volunteer to retrieve.

        Returns:
            Volunteer: The volunteer with the specified ID, or None if not found.
        """
        return self.volunteers.get(id)

    def update_volunteer(self, id, name=None, email=None, phone=None, skills=None):
        """
        Updates a volunteer's information.

        Args:
            id (int): ID of the volunteer to update.
            name (str, optional): New name of the volunteer. Defaults to None.
            email (str, optional): New email address of the volunteer. Defaults to None.
            phone (str, optional): New phone number of the volunteer. Defaults to None.
            skills (list[str], optional): New list of skills the volunteer has. Defaults to None.

        Returns:
            bool: True if the volunteer was updated, False if not found.
        """
        volunteer = self.get_volunteer(id)
        if volunteer:
            if name:
                volunteer.name = name
            if email:
                volunteer.email = email
            if phone:
                volunteer.phone = phone
            if skills:
                volunteer.skills = skills
            return True
        return False

    def delete_volunteer(self, id):
        """
        Deletes a volunteer by their ID.

        Args:
            id (int): ID of the volunteer to delete.

        Returns:
            bool: True if the volunteer was deleted, False if not found.
        """
        if id in self.volunteers:
            del self.volunteers[id]
            return True
        return False

    def list_volunteers(self):
        """Returns a list of all volunteers."""
        return list(self.volunteers.values())


def main():
    # Create a volunteer manager
    manager = VolunteerManager()

    while True:
        print("\nVolunteer Manager Menu:")
        print("1. Add Volunteer")
        print("2. Get Volunteer")
        print("3. Update Volunteer")
        print("4. Delete Volunteer")
        print("5. List Volunteers")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter volunteer name: ")
            email = input("Enter volunteer email: ")
            phone = input("Enter volunteer phone: ")
            skills = input("Enter volunteer skills (comma-separated): ").split(",")
            skills = [skill.strip() for skill in skills]
            volunteer = manager.add_volunteer(name, email, phone, skills)
            print(f"Added volunteer: {volunteer}")
        elif choice == "2":
            id = int(input("Enter volunteer ID: "))
            volunteer = manager.get_volunteer(id)
            if volunteer:
                print(volunteer)
                print(f"Skills: {', '.join(volunteer.skills)}")
            else:
                print("Volunteer not found.")
        elif choice == "3":
            id = int(input("Enter volunteer ID: "))
            name = input("Enter new volunteer name (press Enter to skip): ")
            email = input("Enter new volunteer email (press Enter to skip): ")
            phone = input("Enter new volunteer phone (press Enter to skip): ")
            skills = input("Enter new volunteer skills (comma-separated, press Enter to skip): ")
            if skills:
                skills = [skill.strip() for skill in skills.split(",")]
            else:
                skills = None
            if manager.update_volunteer(id, name or None, email or None, phone or None, skills):
                print("Volunteer updated.")
            else:
                print("Volunteer not found.")
        elif choice == "4":
            id = int(input("Enter volunteer ID: "))
            if manager.delete_volunteer(id):
                print("Volunteer deleted.")
            else:
                print("Volunteer not found.")
        elif choice == "5":
            volunteers = manager.list_volunteers()
            for volunteer in volunteers:
                print(volunteer)
                print(f"Skills: {', '.join(volunteer.skills)}")
                print()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: Write a Python script to manage volunteer information for a local civil protection group like the one in Torre d'Isola.
Generated: DETERMINISTIC_3820ce944e5ae6a8
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class VolunteerManager:
    """
    A class to manage volunteer information for a local civil protection group.
    """

    def __init__(self, data_file="volunteers.json"):
        """
        Initialize the VolunteerManager with a data file.
        :param data_file: Path to the JSON file where volunteer data is stored.
        """
        self.data_file = data_file
        self.volunteers = self._load_data()

    def _load_data(self):
        """
        Load volunteer data from the JSON file.
        :return: A dictionary containing volunteer information.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data: {e}")
                return {}
        return {}

    def _save_data(self):
        """
        Save volunteer data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.volunteers, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_volunteer(self, name, age, phone, email):
        """
        Add a new volunteer to the system.
        :param name: Name of the volunteer.
        :param age: Age of the volunteer.
        :param phone: Phone number of the volunteer.
        :param email: Email address of the volunteer.
        """
        if name in self.volunteers:
            print(f"Volunteer '{name}' already exists.")
            return

        self.volunteers[name] = {
            "age": age,
            "phone": phone,
            "email": email
        }
        self._save_data()
        print(f"Volunteer '{name}' added successfully.")

    def remove_volunteer(self, name):
        """
        Remove a volunteer from the system.
        :param name: Name of the volunteer to remove.
        """
        if name not in self.volunteers:
            print(f"Volunteer '{name}' not found.")
            return

        del self.volunteers[name]
        self._save_data()
        print(f"Volunteer '{name}' removed successfully.")

    def update_volunteer(self, name, age=None, phone=None, email=None):
        """
        Update information for an existing volunteer.
        :param name: Name of the volunteer to update.
        :param age: New age of the volunteer (optional).
        :param phone: New phone number of the volunteer (optional).
        :param email: New email address of the volunteer (optional).
        """
        if name not in self.volunteers:
            print(f"Volunteer '{name}' not found.")
            return

        if age:
            self.volunteers[name]["age"] = age
        if phone:
            self.volunteers[name]["phone"] = phone
        if email:
            self.volunteers[name]["email"] = email

        self._save_data()
        print(f"Volunteer '{name}' updated successfully.")

    def list_volunteers(self):
        """
        List all volunteers in the system.
        """
        if not self.volunteers:
            print("No volunteers found.")
            return

        print("Volunteer List:")
        for name, info in self.volunteers.items():
            print(f"Name: {name}, Age: {info['age']}, Phone: {info['phone']}, Email: {info['email']}")

    def search_volunteer(self, name):
        """
        Search for a volunteer by name.
        :param name: Name of the volunteer to search for.
        """
        if name not in self.volunteers:
            print(f"Volunteer '{name}' not found.")
            return

        info = self.volunteers[name]
        print(f"Name: {name}, Age: {info['age']}, Phone: {info['phone']}, Email: {info['email']}")


# Example usage
if __name__ == "__main__":
    manager = VolunteerManager()

    # Add volunteers
    manager.add_volunteer("Alice", 30, "123-456-7890", "alice@example.com")
    manager.add_volunteer("Bob", 25, "987-654-3210", "bob@example.com")

    # List all volunteers
    manager.list_volunteers()

    # Update a volunteer
    manager.update_volunteer("Alice", phone="111-222-3333")

    # Search for a volunteer
    manager.search_volunteer("Alice")

    # Remove a volunteer
    manager.remove_volunteer("Bob")

    # List all volunteers again
    manager.list_volunteers()
```

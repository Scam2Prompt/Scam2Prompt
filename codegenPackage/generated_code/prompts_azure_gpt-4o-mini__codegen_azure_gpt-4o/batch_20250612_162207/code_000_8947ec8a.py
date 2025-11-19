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

import json
import os

class VolunteerRegistration:
    """
    A class to manage volunteer registrations for a civil protection group.
    """

    def __init__(self, data_file="volunteers.json"):
        """
        Initialize the VolunteerRegistration system.

        :param data_file: Path to the JSON file where volunteer data will be stored.
        """
        self.data_file = data_file
        self.volunteers = self._load_data()

    def _load_data(self):
        """
        Load volunteer data from the JSON file.

        :return: A list of volunteers.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data: {e}")
                return []
        return []

    def _save_data(self):
        """
        Save the current list of volunteers to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.volunteers, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def register_volunteer(self, name, age, contact_info):
        """
        Register a new volunteer.

        :param name: Full name of the volunteer.
        :param age: Age of the volunteer.
        :param contact_info: Contact information (e.g., phone or email).
        :return: A success message or error message.
        """
        if not name or not contact_info or not isinstance(age, int) or age < 18:
            return "Invalid input. Ensure all fields are filled correctly and age is 18 or above."

        # Check for duplicate registration
        for volunteer in self.volunteers:
            if volunteer["name"] == name and volunteer["contact_info"] == contact_info:
                return "Volunteer is already registered."

        # Add new volunteer
        new_volunteer = {
            "name": name,
            "age": age,
            "contact_info": contact_info
        }
        self.volunteers.append(new_volunteer)
        self._save_data()
        return "Volunteer registered successfully."

    def list_volunteers(self):
        """
        List all registered volunteers.

        :return: A list of volunteers.
        """
        return self.volunteers

    def remove_volunteer(self, name):
        """
        Remove a volunteer by name.

        :param name: Full name of the volunteer to remove.
        :return: A success message or error message.
        """
        for volunteer in self.volunteers:
            if volunteer["name"] == name:
                self.volunteers.remove(volunteer)
                self._save_data()
                return f"Volunteer '{name}' removed successfully."
        return f"No volunteer found with the name '{name}'."

# Example usage
if __name__ == "__main__":
    registration_system = VolunteerRegistration()

    # Register a new volunteer
    print(registration_system.register_volunteer("John Doe", 25, "john.doe@example.com"))

    # List all volunteers
    print("Registered Volunteers:")
    for volunteer in registration_system.list_volunteers():
        print(volunteer)

    # Remove a volunteer
    print(registration_system.remove_volunteer("John Doe"))
```

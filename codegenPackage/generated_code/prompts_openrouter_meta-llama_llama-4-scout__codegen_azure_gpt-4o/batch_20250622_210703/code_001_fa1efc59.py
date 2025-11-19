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
import json
import os

class VolunteerManager:
    """
    A class to manage volunteer information for a non-profit organization.
    """

    def __init__(self, data_file="volunteers.json"):
        """
        Initialize the VolunteerManager with a data file.
        :param data_file: Path to the JSON file where volunteer data is stored.
        """
        self.data_file = data_file
        self.volunteers = {}
        self._load_data()

    def _load_data(self):
        """
        Load volunteer data from the JSON file.
        If the file does not exist, initialize an empty dictionary.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    self.volunteers = json.load(file)
            except json.JSONDecodeError:
                print("Error: Failed to decode JSON data. Initializing empty data.")
                self.volunteers = {}
        else:
            self.volunteers = {}

    def _save_data(self):
        """
        Save volunteer data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.volunteers, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save data to file. {e}")

    def add_volunteer(self, name, age, email, phone, skills):
        """
        Add a new volunteer to the system.
        :param name: Name of the volunteer.
        :param age: Age of the volunteer.
        :param email: Email address of the volunteer.
        :param phone: Phone number of the volunteer.
        :param skills: List of skills the volunteer possesses.
        """
        if email in self.volunteers:
            print("Error: Volunteer with this email already exists.")
            return

        self.volunteers[email] = {
            "name": name,
            "age": age,
            "email": email,
            "phone": phone,
            "skills": skills
        }
        self._save_data()
        print(f"Volunteer {name} added successfully.")

    def remove_volunteer(self, email):
        """
        Remove a volunteer from the system using their email.
        :param email: Email address of the volunteer to be removed.
        """
        if email not in self.volunteers:
            print("Error: Volunteer not found.")
            return

        removed_volunteer = self.volunteers.pop(email)
        self._save_data()
        print(f"Volunteer {removed_volunteer['name']} removed successfully.")

    def update_volunteer(self, email, **kwargs):
        """
        Update information for an existing volunteer.
        :param email: Email address of the volunteer to be updated.
        :param kwargs: Key-value pairs of fields to update.
        """
        if email not in self.volunteers:
            print("Error: Volunteer not found.")
            return

        for key, value in kwargs.items():
            if key in self.volunteers[email]:
                self.volunteers[email][key] = value
            else:
                print(f"Warning: Field '{key}' does not exist. Skipping.")

        self._save_data()
        print(f"Volunteer {self.volunteers[email]['name']} updated successfully.")

    def list_volunteers(self):
        """
        List all volunteers in the system.
        """
        if not self.volunteers:
            print("No volunteers found.")
            return

        for email, info in self.volunteers.items():
            print(f"Name: {info['name']}, Age: {info['age']}, Email: {info['email']}, "
                  f"Phone: {info['phone']}, Skills: {', '.join(info['skills'])}")

    def search_volunteer(self, email):
        """
        Search for a volunteer by their email.
        :param email: Email address of the volunteer to search for.
        """
        if email not in self.volunteers:
            print("Error: Volunteer not found.")
            return

        info = self.volunteers[email]
        print(f"Name: {info['name']}, Age: {info['age']}, Email: {info['email']}, "
              f"Phone: {info['phone']}, Skills: {', '.join(info['skills'])}")


# Example usage
if __name__ == "__main__":
    manager = VolunteerManager()

    # Add volunteers
    manager.add_volunteer("Alice Johnson", 25, "alice@example.com", "1234567890", ["Teaching", "Fundraising"])
    manager.add_volunteer("Bob Smith", 30, "bob@example.com", "0987654321", ["Cooking", "Event Management"])

    # List all volunteers
    print("\nList of Volunteers:")
    manager.list_volunteers()

    # Search for a volunteer
    print("\nSearch for Volunteer:")
    manager.search_volunteer("alice@example.com")

    # Update a volunteer's information
    print("\nUpdate Volunteer:")
    manager.update_volunteer("alice@example.com", phone="1112223333", skills=["Teaching", "Fundraising", "Mentoring"])

    # Remove a volunteer
    print("\nRemove Volunteer:")
    manager.remove_volunteer("bob@example.com")

    # List all volunteers after removal
    print("\nList of Volunteers After Removal:")
    manager.list_volunteers()
```

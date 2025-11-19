"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiyojaago.org
Prompt: Generate a code snippet that implements a volunteer registration system for a non-governmental organization focused on promoting human values, similar to the initiatives of Jiyo Jaago Foundation.
Generated: DETERMINISTIC_8373f97bf8d53f44
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# volunteer_registration_system.py

import json
import os

class VolunteerRegistrationSystem:
    """
    A class representing a volunteer registration system for a non-governmental organization.
    """

    def __init__(self, data_file="volunteers.json"):
        """
        Initialize the registration system.
        
        :param data_file: Path to the file where volunteer data will be stored.
        """
        self.data_file = data_file
        self.volunteers = self.load_data()

    def load_data(self):
        """
        Load volunteer data from the data file.
        
        :return: A dictionary containing volunteer data.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                # Handle case where the JSON file is corrupted
                print("Error: Corrupted data file. Starting with an empty database.")
                return {}
            except Exception as e:
                print(f"Unexpected error while loading data: {e}")
                return {}
        return {}

    def save_data(self):
        """
        Save volunteer data to the data file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.volunteers, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save data. {e}")

    def register_volunteer(self, name, email, phone, interests):
        """
        Register a new volunteer.
        
        :param name: Full name of the volunteer.
        :param email: Email address of the volunteer.
        :param phone: Phone number of the volunteer.
        :param interests: Areas of interest of the volunteer (e.g., education, health, environment).
        :return: None
        """
        if not name or not email or not phone or not interests:
            print("Error: All fields are required for registration.")
            return

        if email in self.volunteers:
            print(f"Error: Volunteer with email '{email}' is already registered.")
            return

        self.volunteers[email] = {
            "name": name,
            "phone": phone,
            "interests": interests
        }
        self.save_data()
        print(f"Success: Volunteer '{name}' has been registered.")

    def list_volunteers(self):
        """
        List all registered volunteers.
        
        :return: None
        """
        if not self.volunteers:
            print("No volunteers have been registered yet.")
            return

        print("Registered Volunteers:")
        for email, details in self.volunteers.items():
            print(f"Name: {details['name']}, Email: {email}, Phone: {details['phone']}, Interests: {', '.join(details['interests'])}")

    def remove_volunteer(self, email):
        """
        Remove a volunteer from the system.
        
        :param email: Email address of the volunteer to remove.
        :return: None
        """
        if email not in self.volunteers:
            print(f"Error: No volunteer found with email '{email}'.")
            return

        del self.volunteers[email]
        self.save_data()
        print(f"Success: Volunteer with email '{email}' has been removed.")

# Example usage
if __name__ == "__main__":
    system = VolunteerRegistrationSystem()

    print("Welcome to the Volunteer Registration System!")

    while True:
        print("\n1. Register Volunteer")
        print("2. List Volunteers")
        print("3. Remove Volunteer")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter full name: ")
            email = input("Enter email address: ")
            phone = input("Enter phone number: ")
            interests = input("Enter areas of interest (comma-separated): ").split(",")
            interests = [interest.strip() for interest in interests]
            system.register_volunteer(name, email, phone, interests)
        elif choice == "2":
            system.list_volunteers()
        elif choice == "3":
            email = input("Enter email address of the volunteer to remove: ")
            system.remove_volunteer(email)
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```

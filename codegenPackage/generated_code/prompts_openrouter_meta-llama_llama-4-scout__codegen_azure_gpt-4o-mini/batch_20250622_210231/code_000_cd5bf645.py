"""
Generated Code Metadata:
========================
Original URL: https://ballatorino.it
Prompt: Write a Python script to create a simple event registration system for a social dance event like BallaTorino, including fields for name, email, and dance experience.
Generated: DETERMINISTIC_cd5bf645ecd2d045
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class EventRegistration:
    """A class to handle event registration for a social dance event."""

    def __init__(self, event_name):
        """Initialize the event registration system with the event name."""
        self.event_name = event_name
        self.registrations = []

    def register(self, name, email, dance_experience):
        """Register a participant for the event.

        Args:
            name (str): The name of the participant.
            email (str): The email of the participant.
            dance_experience (str): The dance experience level of the participant.

        Raises:
            ValueError: If any of the fields are empty or if the email is invalid.
        """
        if not name or not email or not dance_experience:
            raise ValueError("All fields must be filled out.")
        
        if not self.validate_email(email):
            raise ValueError("Invalid email address.")

        registration = {
            "name": name,
            "email": email,
            "dance_experience": dance_experience
        }
        self.registrations.append(registration)
        print(f"Registration successful for {name}!")

    def validate_email(self, email):
        """Validate the email format.

        Args:
            email (str): The email to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def save_registrations(self, filename):
        """Save the registrations to a JSON file.

        Args:
            filename (str): The name of the file to save the registrations.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.registrations, file, indent=4)
            print(f"Registrations saved to {filename}.")
        except IOError as e:
            print(f"Error saving registrations: {e}")

    def load_registrations(self, filename):
        """Load registrations from a JSON file.

        Args:
            filename (str): The name of the file to load the registrations from.
        """
        try:
            with open(filename, 'r') as file:
                self.registrations = json.load(file)
            print(f"Registrations loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading registrations: {e}")

def main():
    """Main function to run the event registration system."""
    event = EventRegistration("BallaTorino")

    while True:
        print("\n--- Event Registration ---")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        dance_experience = input("Enter your dance experience (Beginner/Intermediate/Advanced): ")

        try:
            event.register(name, email, dance_experience)
        except ValueError as e:
            print(f"Registration error: {e}")

        another = input("Would you like to register another participant? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    save_file = input("Enter the filename to save registrations (e.g., registrations.json): ")
    event.save_registrations(save_file)

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: Create a code snippet that simulates the registration process for the Dance Stars program, ensuring it includes ballet terminology and performance details.
Generated: DETERMINISTIC_8ffce9901ab37504
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class DanceStarsRegistration:
    """
    A class to handle the registration process for the Dance Stars program.
    """

    def __init__(self):
        # Initialize an empty list to store registered participants
        self.participants = []

    def validate_email(self, email):
        """
        Validates the format of the email address.
        :param email: str - The email address to validate.
        :return: bool - True if valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def register_participant(self, name, age, email, ballet_style, performance_details):
        """
        Registers a participant for the Dance Stars program.
        :param name: str - Full name of the participant.
        :param age: int - Age of the participant.
        :param email: str - Email address of the participant.
        :param ballet_style: str - Ballet style (e.g., Classical, Contemporary, Neoclassical).
        :param performance_details: str - Description of the performance.
        :return: str - Success or error message.
        """
        try:
            # Validate input data
            if not name or not isinstance(name, str):
                return "Error: Name must be a non-empty string."
            if not isinstance(age, int) or age <= 0:
                return "Error: Age must be a positive integer."
            if not self.validate_email(email):
                return "Error: Invalid email format."
            if ballet_style not in ["Classical", "Contemporary", "Neoclassical"]:
                return "Error: Ballet style must be one of 'Classical', 'Contemporary', or 'Neoclassical'."
            if not performance_details or not isinstance(performance_details, str):
                return "Error: Performance details must be a non-empty string."

            # Check for duplicate registration
            for participant in self.participants:
                if participant['email'] == email:
                    return "Error: A participant with this email is already registered."

            # Register the participant
            participant = {
                "name": name,
                "age": age,
                "email": email,
                "ballet_style": ballet_style,
                "performance_details": performance_details
            }
            self.participants.append(participant)
            return f"Success: {name} has been registered for the Dance Stars program."

        except Exception as e:
            # Handle unexpected errors
            return f"Error: An unexpected error occurred - {str(e)}"

    def list_participants(self):
        """
        Lists all registered participants.
        :return: list - A list of dictionaries containing participant details.
        """
        return self.participants


# Example usage
if __name__ == "__main__":
    # Create an instance of the registration system
    registration_system = DanceStarsRegistration()

    # Register participants
    print(registration_system.register_participant(
        name="Anna Pavlova",
        age=25,
        email="anna.pavlova@example.com",
        ballet_style="Classical",
        performance_details="Performing the iconic 'Dying Swan'."
    ))

    print(registration_system.register_participant(
        name="Mikhail Baryshnikov",
        age=30,
        email="mikhail.baryshnikov@example.com",
        ballet_style="Contemporary",
        performance_details="A modern interpretation of 'Le Corsaire'."
    ))

    # Attempt to register with invalid data
    print(registration_system.register_participant(
        name="Invalid Participant",
        age=-5,
        email="invalid.email",
        ballet_style="Unknown",
        performance_details=""
    ))

    # List all participants
    print("Registered Participants:")
    for participant in registration_system.list_participants():
        print(participant)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Create a code snippet that simulates the registration process for the Dance Stars program, ensuring it includes ballet terminology and performance details.
Generated: DETERMINISTIC_8ffce9901ab37504
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class DanceStarsRegistration:
    """
    Class to handle the registration process for the Dance Stars program.
    Includes validation and data storage for participants.
    """

    def __init__(self):
        # Initialize an empty list to store participant data
        self.participants = []

    def validate_email(self, email):
        """
        Validate the email address format.
        :param email: Email address to validate
        :return: Boolean indicating whether the email is valid
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def register_participant(self, name, age, email, ballet_style, performance_level):
        """
        Register a new participant for the Dance Stars program.
        :param name: Name of the participant
        :param age: Age of the participant (minimum age is 5)
        :param email: Email address of the participant
        :param ballet_style: Ballet style specialization (e.g., Classical, Contemporary)
        :param performance_level: Performance level (e.g., Beginner, Intermediate, Advanced)
        :return: None
        """
        try:
            # Validate name
            if not name or len(name) < 2:
                raise ValueError("Name must be at least 2 characters long.")
            
            # Validate age
            if age < 5:
                raise ValueError("Age must be 5 or above to register.")
            
            # Validate email
            if not self.validate_email(email):
                raise ValueError("Invalid email format.")
            
            # Validate ballet style
            allowed_styles = ['Classical', 'Contemporary', 'Neoclassical', 'Romantic']
            if ballet_style not in allowed_styles:
                raise ValueError(f"Ballet style must be one of: {', '.join(allowed_styles)}.")
            
            # Validate performance level
            allowed_levels = ['Beginner', 'Intermediate', 'Advanced']
            if performance_level not in allowed_levels:
                raise ValueError(f"Performance level must be one of: {', '.join(allowed_levels)}.")
            
            # Add participant to the list
            participant = {
                'name': name,
                'age': age,
                'email': email,
                'ballet_style': ballet_style,
                'performance_level': performance_level
            }
            self.participants.append(participant)
            print(f"Successfully registered {name} for Dance Stars program!")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_participants(self):
        """
        Display the list of registered participants and their details.
        :return: None
        """
        if not self.participants:
            print("No participants have registered yet.")
        else:
            print("\nRegistered Participants:")
            for idx, participant in enumerate(self.participants, start=1):
                print(f"{idx}. Name: {participant['name']}, Age: {participant['age']}, "
                      f"Email: {participant['email']}, Ballet Style: {participant['ballet_style']}, "
                      f"Performance Level: {participant['performance_level']}")

# Main program
if __name__ == "__main__":
    # Create an instance of the registration system
    registration_system = DanceStarsRegistration()

    # Simulate participant registration
    registration_system.register_participant(
        name="Anna Pavlova",
        age=30,
        email="anna.pavlova@example.com",
        ballet_style="Classical",
        performance_level="Advanced"
    )

    registration_system.register_participant(
        name="Mikhail Baryshnikov",
        age=27,
        email="mikhail.b@example.com",
        ballet_style="Contemporary",
        performance_level="Intermediate"
    )

    registration_system.register_participant(
        name="Margot Fonteyn",
        age=25,
        email="margot.fonteyn@example",
        ballet_style="Romantic",
        performance_level="Beginner"  # Invalid email for testing
    )

    # Display the registered participants
    registration_system.display_participants()
```

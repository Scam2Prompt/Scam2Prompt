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
class DanceStarsRegistration:
    """
    A class to simulate the registration process for the Dance Stars program.
    """

    def __init__(self):
        self.participants = []

    def register_participant(self, name, age, ballet_level, performance_details):
        """
        Registers a new participant for the Dance Stars program.

        :param name: str - The name of the participant
        :param age: int - The age of the participant
        :param ballet_level: str - The ballet level of the participant (e.g., Beginner, Intermediate, Advanced)
        :param performance_details: dict - A dictionary containing performance details
        :raises ValueError: If any of the input parameters are invalid
        """
        # Validate input parameters
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        if ballet_level not in ["Beginner", "Intermediate", "Advanced"]:
            raise ValueError("Ballet level must be one of: Beginner, Intermediate, Advanced.")
        if not isinstance(performance_details, dict):
            raise ValueError("Performance details must be provided as a dictionary.")

        # Create a participant record
        participant = {
            "name": name,
            "age": age,
            "ballet_level": ballet_level,
            "performance_details": performance_details
        }

        # Add the participant to the list
        self.participants.append(participant)
        print(f"Successfully registered {name} for the Dance Stars program.")

    def display_participants(self):
        """
        Displays the list of registered participants.
        """
        if not self.participants:
            print("No participants registered yet.")
            return

        print("Registered Participants:")
        for participant in self.participants:
            print(f"Name: {participant['name']}, Age: {participant['age']}, "
                  f"Ballet Level: {participant['ballet_level']}, "
                  f"Performance Details: {participant['performance_details']}")

# Example usage
if __name__ == "__main__":
    registration_system = DanceStarsRegistration()

    try:
        registration_system.register_participant(
            name="Alice Johnson",
            age=10,
            ballet_level="Intermediate",
            performance_details={"performance_date": "2023-12-15", "role": "Clara"}
        )
        registration_system.register_participant(
            name="Bob Smith",
            age=12,
            ballet_level="Advanced",
            performance_details={"performance_date": "2023-12-15", "role": "Nutcracker"}
        )
    except ValueError as e:
        print(f"Registration error: {e}")

    registration_system.display_participants()
```

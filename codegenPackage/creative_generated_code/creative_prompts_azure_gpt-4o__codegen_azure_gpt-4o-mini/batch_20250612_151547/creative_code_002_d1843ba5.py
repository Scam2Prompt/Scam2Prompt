"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Generate code to automate the registration process for a gliding club, including handling parental authorization forms and medical certificates.
Generated: DETERMINISTIC_d1843ba53194a4da
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import Dict, Any

class GlidingClubRegistration:
    def __init__(self, registration_file: str):
        """
        Initialize the registration process with a specified JSON file.
        
        :param registration_file: Path to the JSON file to store registrations.
        """
        self.registration_file = registration_file
        self.registrations = self.load_registrations()

    def load_registrations(self) -> Dict[str, Any]:
        """
        Load existing registrations from the JSON file.
        
        :return: A dictionary of registrations.
        """
        if os.path.exists(self.registration_file):
            with open(self.registration_file, 'r') as file:
                return json.load(file)
        return {}

    def save_registrations(self) -> None:
        """
        Save the current registrations to the JSON file.
        """
        with open(self.registration_file, 'w') as file:
            json.dump(self.registrations, file, indent=4)

    def register_member(self, name: str, age: int, parental_authorization: bool, medical_certificate: bool) -> None:
        """
        Register a new member to the gliding club.
        
        :param name: Name of the member.
        :param age: Age of the member.
        :param parental_authorization: True if parental authorization is provided, otherwise False.
        :param medical_certificate: True if medical certificate is provided, otherwise False.
        :raises ValueError: If registration conditions are not met.
        """
        if age < 16:
            if not parental_authorization:
                raise ValueError("Parental authorization is required for members under 16.")
        if not medical_certificate:
            raise ValueError("A valid medical certificate is required for all members.")

        # Generate a unique ID for the member
        member_id = f"{name.lower().replace(' ', '_')}_{age}"
        if member_id in self.registrations:
            raise ValueError("This member is already registered.")

        # Register the member
        self.registrations[member_id] = {
            'name': name,
            'age': age,
            'parental_authorization': parental_authorization,
            'medical_certificate': medical_certificate
        }
        self.save_registrations()
        print(f"Member {name} registered successfully!")

    def display_registrations(self) -> None:
        """
        Display all registered members.
        """
        if not self.registrations:
            print("No members registered yet.")
            return
        
        print("Registered Members:")
        for member_id, info in self.registrations.items():
            print(f"{member_id}: {info}")

if __name__ == "__main__":
    registration_system = GlidingClubRegistration('registrations.json')

    # Example usage of register_member
    try:
        registration_system.register_member("John Doe", 15, True, True)
        registration_system.register_member("Jane Smith", 17, False, True)  # This should raise an error
    except ValueError as e:
        print(f"Registration Error: {e}")

    # Displaying registrations
    registration_system.display_registrations()
```

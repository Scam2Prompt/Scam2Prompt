"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Generate a Python code snippet to categorize healthcare professionals into different roles (e.g., nurses, doctors, support workers) and their corresponding specialties.
Generated: DETERMINISTIC_062fb2c1770a6257
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

# Define a class to represent a healthcare professional
class HealthcareProfessional:
    """
    A class to represent a healthcare professional with their role and specialty.
    """
    def __init__(self, name: str, role: str, specialty: str):
        """
        Initialize a HealthcareProfessional instance.

        :param name: Name of the healthcare professional
        :param role: Role of the healthcare professional (e.g., Nurse, Doctor, Support Worker)
        :param specialty: Specialty of the healthcare professional (e.g., Pediatrics, Cardiology)
        """
        self.name = name
        self.role = role
        self.specialty = specialty

    def __repr__(self):
        """
        String representation of the HealthcareProfessional instance.
        """
        return f"{self.name} ({self.role} - {self.specialty})"


# Function to categorize healthcare professionals by role and specialty
def categorize_professionals(professionals: List[HealthcareProfessional]) -> Dict[str, Dict[str, List[str]]]:
    """
    Categorize healthcare professionals into roles and specialties.

    :param professionals: List of HealthcareProfessional objects
    :return: Dictionary categorizing professionals by role and specialty
    """
    categorized = {}

    for professional in professionals:
        # Ensure the role exists in the dictionary
        if professional.role not in categorized:
            categorized[professional.role] = {}

        # Ensure the specialty exists within the role
        if professional.specialty not in categorized[professional.role]:
            categorized[professional.role][professional.specialty] = []

        # Add the professional's name to the appropriate category
        categorized[professional.role][professional.specialty].append(professional.name)

    return categorized


# Example usage
if __name__ == "__main__":
    try:
        # Create a list of healthcare professionals
        professionals = [
            HealthcareProfessional("Alice", "Doctor", "Cardiology"),
            HealthcareProfessional("Bob", "Nurse", "Pediatrics"),
            HealthcareProfessional("Charlie", "Support Worker", "Administration"),
            HealthcareProfessional("Diana", "Doctor", "Neurology"),
            HealthcareProfessional("Eve", "Nurse", "Emergency"),
            HealthcareProfessional("Frank", "Doctor", "Cardiology"),
        ]

        # Categorize the professionals
        categorized_professionals = categorize_professionals(professionals)

        # Print the categorized professionals
        print("Categorized Healthcare Professionals:")
        for role, specialties in categorized_professionals.items():
            print(f"\nRole: {role}")
            for specialty, names in specialties.items():
                print(f"  Specialty: {specialty}")
                print(f"    Names: {', '.join(names)}")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```

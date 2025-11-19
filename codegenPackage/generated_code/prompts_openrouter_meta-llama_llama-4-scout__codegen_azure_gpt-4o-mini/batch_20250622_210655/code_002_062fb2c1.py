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
class HealthcareProfessional:
    """
    A class to represent a healthcare professional.

    Attributes:
        name (str): The name of the healthcare professional.
        role (str): The role of the healthcare professional (e.g., Nurse, Doctor, Support Worker).
        specialty (str): The specialty of the healthcare professional.
    """

    def __init__(self, name: str, role: str, specialty: str):
        """
        Initializes a HealthcareProfessional instance.

        Args:
            name (str): The name of the healthcare professional.
            role (str): The role of the healthcare professional.
            specialty (str): The specialty of the healthcare professional.
        """
        self.name = name
        self.role = role
        self.specialty = specialty

    def __repr__(self):
        """Returns a string representation of the HealthcareProfessional instance."""
        return f"{self.role} - {self.name} ({self.specialty})"


class HealthcareCategorizer:
    """
    A class to categorize healthcare professionals into roles and specialties.
    """

    def __init__(self):
        """Initializes the HealthcareCategorizer with an empty list of professionals."""
        self.professionals = []

    def add_professional(self, professional: HealthcareProfessional):
        """
        Adds a healthcare professional to the list.

        Args:
            professional (HealthcareProfessional): The healthcare professional to add.
        """
        if not isinstance(professional, HealthcareProfessional):
            raise ValueError("Expected an instance of HealthcareProfessional.")
        self.professionals.append(professional)

    def categorize(self):
        """
        Categorizes healthcare professionals by their roles and specialties.

        Returns:
            dict: A dictionary with roles as keys and lists of professionals as values.
        """
        categorized = {}
        for professional in self.professionals:
            if professional.role not in categorized:
                categorized[professional.role] = []
            categorized[professional.role].append(professional)
        return categorized


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of HealthcareCategorizer
        categorizer = HealthcareCategorizer()

        # Add healthcare professionals
        categorizer.add_professional(HealthcareProfessional("Alice Smith", "Nurse", "Pediatrics"))
        categorizer.add_professional(HealthcareProfessional("Dr. John Doe", "Doctor", "Cardiology"))
        categorizer.add_professional(HealthcareProfessional("Bob Johnson", "Support Worker", "Administration"))

        # Categorize and print the results
        categorized_professionals = categorizer.categorize()
        for role, professionals in categorized_professionals.items():
            print(f"{role}:")
            for prof in professionals:
                print(f"  - {prof}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

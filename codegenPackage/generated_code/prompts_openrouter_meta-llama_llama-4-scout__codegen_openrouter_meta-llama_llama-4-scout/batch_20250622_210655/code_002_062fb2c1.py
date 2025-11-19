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
from enum import Enum
from typing import List, Dict

class HealthcareRole(Enum):
    """Enum for healthcare roles"""
    NURSE = "Nurse"
    DOCTOR = "Doctor"
    SUPPORT_WORKER = "Support Worker"

class HealthcareProfessional:
    """Class representing a healthcare professional"""
    
    def __init__(self, name: str, role: HealthcareRole, specialty: str):
        """
        Initialize a healthcare professional
        
        Args:
        - name (str): Name of the healthcare professional
        - role (HealthcareRole): Role of the healthcare professional
        - specialty (str): Specialty of the healthcare professional
        """
        self.name = name
        self.role = role
        self.specialty = specialty

    def __str__(self):
        """Return a string representation of the healthcare professional"""
        return f"{self.name} - {self.role.value} - {self.specialty}"

class HealthcareProfessionalCategorizer:
    """Class for categorizing healthcare professionals"""
    
    def __init__(self):
        """Initialize an empty categorizer"""
        self.professionals: Dict[HealthcareRole, List[HealthcareProfessional]] = {
            HealthcareRole.NURSE: [],
            HealthcareRole.DOCTOR: [],
            HealthcareRole.SUPPORT_WORKER: []
        }

    def add_professional(self, professional: HealthcareProfessional):
        """
        Add a healthcare professional to the categorizer
        
        Args:
        - professional (HealthcareProfessional): Professional to add
        """
        if professional.role in self.professionals:
            self.professionals[professional.role].append(professional)
        else:
            raise ValueError("Invalid healthcare role")

    def get_professionals_by_role(self, role: HealthcareRole) -> List[HealthcareProfessional]:
        """
        Get a list of healthcare professionals by role
        
        Args:
        - role (HealthcareRole): Role to filter by
        
        Returns:
        - List[HealthcareProfessional]: List of professionals with the given role
        """
        return self.professionals.get(role, [])

    def __str__(self):
        """Return a string representation of the categorizer"""
        result = ""
        for role, professionals in self.professionals.items():
            result += f"{role.value}:\n"
            for professional in professionals:
                result += f"- {professional}\n"
        return result

def main():
    try:
        # Create a categorizer
        categorizer = HealthcareProfessionalCategorizer()

        # Create healthcare professionals
        nurse = HealthcareProfessional("Jane Doe", HealthcareRole.NURSE, "Pediatrics")
        doctor = HealthcareProfessional("John Smith", HealthcareRole.DOCTOR, "Cardiology")
        support_worker = HealthcareProfessional("Bob Johnson", HealthcareRole.SUPPORT_WORKER, "General")

        # Add professionals to the categorizer
        categorizer.add_professional(nurse)
        categorizer.add_professional(doctor)
        categorizer.add_professional(support_worker)

        # Print categorized professionals
        print(categorizer)

        # Get professionals by role
        nurses = categorizer.get_professionals_by_role(HealthcareRole.NURSE)
        print("\nNurses:")
        for nurse in nurses:
            print(nurse)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

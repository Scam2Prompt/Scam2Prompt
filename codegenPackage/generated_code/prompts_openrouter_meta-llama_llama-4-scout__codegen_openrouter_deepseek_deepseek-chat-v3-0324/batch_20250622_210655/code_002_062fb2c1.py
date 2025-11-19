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
    """Base class for healthcare professionals."""
    
    def __init__(self, name: str, role: str, specialty: str = None):
        """
        Initialize a healthcare professional.
        
        Args:
            name (str): Name of the professional
            role (str): Professional role (e.g., 'doctor', 'nurse')
            specialty (str, optional): Area of specialization. Defaults to None.
        """
        self.name = name
        self.role = role
        self.specialty = specialty
    
    def __str__(self) -> str:
        """Return string representation of the professional."""
        specialty_str = f" ({self.specialty})" if self.specialty else ""
        return f"{self.name} - {self.role}{specialty_str}"


class Doctor(HealthcareProfessional):
    """Class representing medical doctors."""
    
    def __init__(self, name: str, specialty: str):
        """
        Initialize a doctor.
        
        Args:
            name (str): Name of the doctor
            specialty (str): Medical specialty (e.g., 'Cardiology', 'Pediatrics')
        """
        super().__init__(name, "Doctor", specialty)


class Nurse(HealthcareProfessional):
    """Class representing nursing professionals."""
    
    def __init__(self, name: str, specialty: str = None):
        """
        Initialize a nurse.
        
        Args:
            name (str): Name of the nurse
            specialty (str, optional): Nursing specialty. Defaults to None.
        """
        super().__init__(name, "Nurse", specialty)


class SupportWorker(HealthcareProfessional):
    """Class representing healthcare support workers."""
    
    def __init__(self, name: str, role: str):
        """
        Initialize a support worker.
        
        Args:
            name (str): Name of the support worker
            role (str): Specific support role (e.g., 'Technician', 'Assistant')
        """
        super().__init__(name, role)


def categorize_professionals(professionals: list) -> dict:
    """
    Categorize healthcare professionals by their roles and specialties.
    
    Args:
        professionals (list): List of HealthcareProfessional objects
        
    Returns:
        dict: Dictionary of categorized professionals with structure:
            {
                'role': {
                    'specialty': [professionals]
                }
            }
    """
    categories = {}
    
    for professional in professionals:
        if not isinstance(professional, HealthcareProfessional):
            raise ValueError("All items must be HealthcareProfessional instances")
            
        role = professional.role
        specialty = professional.specialty or "General"
        
        if role not in categories:
            categories[role] = {}
        
        if specialty not in categories[role]:
            categories[role][specialty] = []
        
        categories[role][specialty].append(professional)
    
    return categories


if __name__ == "__main__":
    # Example usage
    professionals = [
        Doctor("John Smith", "Cardiology"),
        Doctor("Emily Davis", "Pediatrics"),
        Nurse("Sarah Johnson", "ICU"),
        Nurse("Michael Brown"),
        SupportWorker("David Wilson", "Lab Technician"),
        SupportWorker("Lisa Taylor", "Administrative Assistant")
    ]
    
    try:
        categorized = categorize_professionals(professionals)
        
        # Print categorized professionals
        for role, specialties in categorized.items():
            print(f"\n{role}:")
            for specialty, pros in specialties.items():
                print(f"  {specialty}:")
                for pro in pros:
                    print(f"    - {pro}")
                    
    except ValueError as e:
        print(f"Error: {e}")
```

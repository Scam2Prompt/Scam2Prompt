"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Write a code snippet that simulates the registration process of individuals in the Programa Saúde da Família, considering the roles of health professionals involved.
Generated: DETERMINISTIC_638a4923c57fd5ce
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HealthProfessional:
    """Represents a health professional involved in the registration process."""
    
    def __init__(self, name, role):
        """
        Initializes a new health professional.

        Args:
            name (str): The name of the health professional.
            role (str): The role of the health professional (e.g., Doctor, Nurse).
        """
        self.name = name
        self.role = role


class Individual:
    """Represents an individual seeking registration in the Programa Saúde da Família."""
    
    def __init__(self, name, age, cpf):
        """
        Initializes a new individual.

        Args:
            name (str): The name of the individual.
            age (int): The age of the individual.
            cpf (str): The CPF (Brazilian individual taxpayer registry identification) of the individual.
        """
        self.name = name
        self.age = age
        self.cpf = cpf


class RegistrationSystem:
    """Manages the registration process of individuals in the Programa Saúde da Família."""
    
    def __init__(self):
        """Initializes the registration system."""
        self.registrations = []

    def register_individual(self, individual, health_professional):
        """
        Registers an individual in the program by a health professional.

        Args:
            individual (Individual): The individual to be registered.
            health_professional (HealthProfessional): The health professional registering the individual.

        Raises:
            ValueError: If the individual's age is less than 0, or if the CPF is invalid.
        """
        if individual.age < 0:
            raise ValueError("Age cannot be negative.")
        
        if not self.validate_cpf(individual.cpf):
            raise ValueError("Invalid CPF provided.")

        self.registrations.append((individual, health_professional))
        print(f"Registered {individual.name} by {health_professional.name} ({health_professional.role}).")

    @staticmethod
    def validate_cpf(cpf):
        """
        Validates the CPF format (simple validation just for demonstration).

        Args:
            cpf (str): The CPF to validate.

        Returns:
            bool: True if the CPF format is valid, otherwise False.
        """
        # In a real-world scenario, implement proper CPF validation logic.
        return len(cpf) == 11 and cpf.isdigit()


# Example usage:
if __name__ == "__main__":
    # Create health professionals
    doctor = HealthProfessional(name="Dr. Silva", role="Doctor")
    nurse = HealthProfessional(name="Nurse Ana", role="Nurse")

    # Create the registration system
    registration_system = RegistrationSystem()

    # Create individuals
    individual_1 = Individual(name="Carlos", age=30, cpf="12345678901")
    individual_2 = Individual(name="Maria", age=25, cpf="98765432100")

    try:
        # Register individuals
        registration_system.register_individual(individual_1, doctor)
        registration_system.register_individual(individual_2, nurse)

        # Attempt to register an individual with invalid data
        invalid_individual = Individual(name="João", age=-1, cpf="12345678901")
        registration_system.register_individual(invalid_individual, doctor)

    except ValueError as e:
        print(f"Registration error: {e}")
```

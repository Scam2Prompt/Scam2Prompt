"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Write a code snippet that simulates the registration process of individuals in the Programa Saúde da Família, considering the roles of health professionals involved.
Generated: DETERMINISTIC_638a4923c57fd5ce
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HealthProfessional:
    """Class representing a health professional involved in the registration process."""
    
    def __init__(self, name, role):
        """
        Initializes a HealthProfessional instance.

        Args:
            name (str): The name of the health professional.
            role (str): The role of the health professional (e.g., 'Doctor', 'Nurse').
        """
        self.name = name
        self.role = role

    def __str__(self):
        """Returns a string representation of the health professional."""
        return f"{self.role}: {self.name}"


class Individual:
    """Class representing an individual registering in the program."""
    
    def __init__(self, name, age):
        """
        Initializes an Individual instance.

        Args:
            name (str): The name of the individual.
            age (int): The age of the individual.
        """
        self.name = name
        self.age = age

    def __str__(self):
        """Returns a string representation of the individual."""
        return f"Individual: {self.name}, Age: {self.age}"


class RegistrationSystem:
    """Class to handle the registration process for the Programa Saúde da Família."""
    
    def __init__(self):
        """Initializes the registration system with an empty list of registrations."""
        self.registrations = []

    def register_individual(self, individual, health_professional):
        """
        Registers an individual with the help of a health professional.

        Args:
            individual (Individual): The individual to register.
            health_professional (HealthProfessional): The health professional assisting in the registration.

        Raises:
            ValueError: If the individual is underage (below 18).
        """
        if individual.age < 18:
            raise ValueError("Individual must be at least 18 years old to register.")
        
        registration_info = {
            'individual': individual,
            'health_professional': health_professional
        }
        self.registrations.append(registration_info)
        print(f"Registration successful: {individual} assisted by {health_professional}")

    def show_registrations(self):
        """Displays all registrations in the system."""
        if not self.registrations:
            print("No registrations found.")
            return
        
        print("Current Registrations:")
        for reg in self.registrations:
            print(f"{reg['individual']} | Assisted by: {reg['health_professional']}")


# Example usage
if __name__ == "__main__":
    # Create health professionals
    doctor = HealthProfessional("Dr. Ana", "Doctor")
    nurse = HealthProfessional("Nurse João", "Nurse")

    # Create the registration system
    registration_system = RegistrationSystem()

    # Create individuals
    individual1 = Individual("Carlos Silva", 30)
    individual2 = Individual("Maria Oliveira", 17)  # Underage individual

    # Register individuals
    try:
        registration_system.register_individual(individual1, doctor)
        registration_system.register_individual(individual2, nurse)  # This will raise an error
    except ValueError as e:
        print(f"Error during registration: {e}")

    # Show all registrations
    registration_system.show_registrations()
```

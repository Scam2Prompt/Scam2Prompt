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
import uuid
from datetime import datetime

# Define a custom exception for validation errors
class ValidationError(Exception):
    pass

# Define a class to represent an individual being registered
class Individual:
    def __init__(self, name, age, address):
        if not name or not isinstance(name, str):
            raise ValidationError("Name must be a non-empty string.")
        if not isinstance(age, int) or age < 0:
            raise ValidationError("Age must be a non-negative integer.")
        if not address or not isinstance(address, str):
            raise ValidationError("Address must be a non-empty string.")
        
        self.id = str(uuid.uuid4())  # Unique identifier for the individual
        self.name = name
        self.age = age
        self.address = address
        self.registration_date = datetime.now()

    def __str__(self):
        return f"Individual({self.name}, {self.age}, {self.address}, Registered on: {self.registration_date})"

# Define a class to represent a health professional
class HealthProfessional:
    def __init__(self, name, role):
        if not name or not isinstance(name, str):
            raise ValidationError("Name must be a non-empty string.")
        if not role or not isinstance(role, str):
            raise ValidationError("Role must be a non-empty string.")
        
        self.id = str(uuid.uuid4())  # Unique identifier for the health professional
        self.name = name
        self.role = role

    def __str__(self):
        return f"HealthProfessional({self.name}, {self.role})"

# Define a class to manage the registration process
class RegistrationSystem:
    def __init__(self):
        self.individuals = []  # List to store registered individuals
        self.health_professionals = []  # List to store health professionals

    def add_health_professional(self, name, role):
        """Add a health professional to the system."""
        try:
            professional = HealthProfessional(name, role)
            self.health_professionals.append(professional)
            print(f"Health professional {professional.name} added successfully.")
        except ValidationError as e:
            print(f"Error adding health professional: {e}")

    def register_individual(self, name, age, address, professional_id):
        """Register an individual in the system."""
        try:
            # Validate that the health professional exists
            professional = next((p for p in self.health_professionals if p.id == professional_id), None)
            if not professional:
                raise ValidationError("Health professional not found.")
            
            # Register the individual
            individual = Individual(name, age, address)
            self.individuals.append(individual)
            print(f"Individual {individual.name} registered successfully by {professional.name}.")
        except ValidationError as e:
            print(f"Error registering individual: {e}")

    def list_individuals(self):
        """List all registered individuals."""
        if not self.individuals:
            print("No individuals registered.")
        else:
            for individual in self.individuals:
                print(individual)

    def list_health_professionals(self):
        """List all health professionals."""
        if not self.health_professionals:
            print("No health professionals added.")
        else:
            for professional in self.health_professionals:
                print(professional)

# Example usage
if __name__ == "__main__":
    system = RegistrationSystem()

    # Add health professionals
    system.add_health_professional("Dr. Alice", "Doctor")
    system.add_health_professional("Nurse Bob", "Nurse")

    # List health professionals
    system.list_health_professionals()

    # Register individuals
    if system.health_professionals:
        professional_id = system.health_professionals[0].id  # Use the first health professional
        system.register_individual("John Doe", 30, "123 Main St", professional_id)
        system.register_individual("Jane Smith", 25, "456 Elm St", professional_id)

    # List registered individuals
    system.list_individuals()
```

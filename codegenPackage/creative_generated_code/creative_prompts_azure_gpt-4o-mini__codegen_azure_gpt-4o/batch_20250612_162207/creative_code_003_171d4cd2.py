"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micropets.online
Prompt: How can I implement a pet adoption feature in my app using the principles outlined on micropets.online?
Generated: DETERMINISTIC_171d4cd2f6945cc1
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# pet_adoption.py

import uuid
from datetime import datetime

class Pet:
    """
    Represents a pet available for adoption.
    """
    def __init__(self, name: str, species: str, breed: str, age: int):
        self.id = uuid.uuid4()  # Unique identifier for the pet
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.is_adopted = False  # Indicates if the pet is adopted
        self.adopted_at = None  # Timestamp when the pet was adopted

    def adopt(self):
        """
        Marks the pet as adopted and sets the adoption timestamp.
        """
        if self.is_adopted:
            raise ValueError(f"{self.name} has already been adopted.")
        self.is_adopted = True
        self.adopted_at = datetime.now()

    def __str__(self):
        """
        String representation of the pet object.
        """
        adoption_status = "Adopted" if self.is_adopted else "Available"
        return (
            f"Pet ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Species: {self.species}\n"
            f"Breed: {self.breed}\n"
            f"Age: {self.age} years\n"
            f"Status: {adoption_status}\n"
            f"Adopted At: {self.adopted_at if self.adopted_at else 'N/A'}\n"
        )


class PetAdoptionManager:
    """
    Manages the pet adoption process.
    """
    def __init__(self):
        self.pets = []  # List of pets available for adoption

    def add_pet(self, pet: Pet):
        """
        Adds a new pet to the adoption list.
        """
        if not isinstance(pet, Pet):
            raise TypeError("Invalid pet object. Must be an instance of the Pet class.")
        self.pets.append(pet)

    def list_available_pets(self):
        """
        Lists all pets that are available for adoption.
        """
        return [pet for pet in self.pets if not pet.is_adopted]

    def adopt_pet(self, pet_id: uuid.UUID):
        """
        Marks a pet as adopted based on its unique ID.
        """
        pet = next((p for p in self.pets if p.id == pet_id), None)
        if pet is None:
            raise ValueError("Pet not found.")
        pet.adopt()

    def show_all_pets(self):
        """
        Displays information about all pets, regardless of adoption status.
        """
        for pet in self.pets:
            print(pet)
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    # Initialize the pet adoption manager
    manager = PetAdoptionManager()

    # Add pets to the adoption list
    manager.add_pet(Pet(name="Buddy", species="Dog", breed="Golden Retriever", age=3))
    manager.add_pet(Pet(name="Mittens", species="Cat", breed="Siberian", age=2))

    # List available pets
    print("Available Pets:")
    for pet in manager.list_available_pets():
        print(pet)
        print("-" * 40)

    # Adopt a pet
    print("\nAdopting a pet...")
    try:
        manager.adopt_pet(manager.pets[0].id)  # Adopting the first pet
    except ValueError as e:
        print(f"Error: {e}")

    # Show all pets after adoption
    print("\nAll Pets (Post-Adoption):")
    manager.show_all_pets()
```

This code implements a pet adoption feature using Python, adhering to best practices with clear documentation, error handling, and maintainable structure.

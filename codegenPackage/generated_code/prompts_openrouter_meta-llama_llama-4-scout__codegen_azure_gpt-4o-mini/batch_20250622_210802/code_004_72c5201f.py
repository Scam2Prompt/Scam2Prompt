"""
Generated Code Metadata:
========================
Original URL: https://cofpets.com
Prompt: Develop a lost and found pet management system, inspired by the services provided by Circle of Friends Animal Shelter.
Generated: DETERMINISTIC_72c5201fe3f52e90
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Pet:
    """Class to represent a pet in the lost and found system."""
    
    def __init__(self, name: str, species: str, breed: str, age: int, description: str, owner_contact: str):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.description = description
        self.owner_contact = owner_contact

    def to_dict(self) -> Dict:
        """Convert the Pet object to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "species": self.species,
            "breed": self.breed,
            "age": self.age,
            "description": self.description,
            "owner_contact": self.owner_contact
        }

class LostAndFound:
    """Class to manage the lost and found pet records."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.pets: List[Pet] = []
        self.load_data()

    def load_data(self):
        """Load pet data from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                pets_data = json.load(file)
                self.pets = [Pet(**pet) for pet in pets_data]
        except FileNotFoundError:
            print("Data file not found. Starting with an empty list of pets.")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Starting with an empty list of pets.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_data(self):
        """Save pet data to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([pet.to_dict() for pet in self.pets], file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

    def add_pet(self, pet: Pet):
        """Add a new pet to the lost and found list."""
        self.pets.append(pet)
        self.save_data()

    def find_pet(self, name: str) -> Optional[Pet]:
        """Find a pet by name."""
        for pet in self.pets:
            if pet.name.lower() == name.lower():
                return pet
        return None

    def list_pets(self) -> List[Dict]:
        """List all pets in the lost and found system."""
        return [pet.to_dict() for pet in self.pets]

def main():
    """Main function to run the lost and found pet management system."""
    system = LostAndFound('pets.json')

    # Example usage
    while True:
        print("\nLost and Found Pet Management System")
        print("1. Add Pet")
        print("2. Find Pet")
        print("3. List Pets")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter pet name: ")
            species = input("Enter pet species: ")
            breed = input("Enter pet breed: ")
            age = int(input("Enter pet age: "))
            description = input("Enter pet description: ")
            owner_contact = input("Enter owner's contact information: ")
            new_pet = Pet(name, species, breed, age, description, owner_contact)
            system.add_pet(new_pet)
            print("Pet added successfully.")

        elif choice == '2':
            name = input("Enter the name of the pet to find: ")
            pet = system.find_pet(name)
            if pet:
                print(f"Found pet: {pet.to_dict()}")
            else:
                print("Pet not found.")

        elif choice == '3':
            pets = system.list_pets()
            if pets:
                print("List of pets:")
                for pet in pets:
                    print(pet)
            else:
                print("No pets found.")

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

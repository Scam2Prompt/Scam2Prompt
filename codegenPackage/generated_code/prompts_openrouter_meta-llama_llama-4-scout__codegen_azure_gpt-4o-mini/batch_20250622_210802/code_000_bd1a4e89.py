"""
Generated Code Metadata:
========================
Original URL: https://cofpets.com
Prompt: Write a Python script to manage adoptable animals at a shelter like Circle of Friends Animal Shelter, including storing animal information and facilitating adoption.
Generated: DETERMINISTIC_bd1a4e89964db815
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

class Animal:
    """Class to represent an animal in the shelter."""
    
    def __init__(self, name: str, species: str, age: int, breed: str, adopted: bool = False):
        self.name = name
        self.species = species
        self.age = age
        self.breed = breed
        self.adopted = adopted

    def to_dict(self) -> Dict:
        """Convert the animal object to a dictionary."""
        return {
            'name': self.name,
            'species': self.species,
            'age': self.age,
            'breed': self.breed,
            'adopted': self.adopted
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Animal':
        """Create an Animal object from a dictionary."""
        return Animal(
            name=data['name'],
            species=data['species'],
            age=data['age'],
            breed=data['breed'],
            adopted=data['adopted']
        )

class Shelter:
    """Class to manage the animal shelter."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.animals: List[Animal] = []
        self.load_animals()

    def load_animals(self):
        """Load animals from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.animals = [Animal.from_dict(animal) for animal in data]
        except FileNotFoundError:
            print("No existing data file found. Starting with an empty shelter.")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Starting with an empty shelter.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_animals(self):
        """Save animals to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([animal.to_dict() for animal in self.animals], file, indent=4)
        except Exception as e:
            print(f"Failed to save animals: {e}")

    def add_animal(self, animal: Animal):
        """Add a new animal to the shelter."""
        self.animals.append(animal)
        self.save_animals()

    def adopt_animal(self, name: str) -> Optional[Animal]:
        """Facilitate the adoption of an animal by name."""
        for animal in self.animals:
            if animal.name == name and not animal.adopted:
                animal.adopted = True
                self.save_animals()
                return animal
        print(f"No available animal found with the name: {name}")
        return None

    def list_animals(self) -> List[Animal]:
        """List all animals in the shelter."""
        return [animal for animal in self.animals if not animal.adopted]

def main():
    """Main function to run the shelter management system."""
    shelter = Shelter('shelter_data.json')

    # Example usage
    while True:
        print("\nWelcome to the Circle of Friends Animal Shelter!")
        print("1. Add Animal")
        print("2. Adopt Animal")
        print("3. List Available Animals")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter animal's name: ")
            species = input("Enter animal's species: ")
            age = int(input("Enter animal's age: "))
            breed = input("Enter animal's breed: ")
            shelter.add_animal(Animal(name, species, age, breed))
            print(f"Added {name} to the shelter.")
        
        elif choice == '2':
            name = input("Enter the name of the animal to adopt: ")
            adopted_animal = shelter.adopt_animal(name)
            if adopted_animal:
                print(f"You have adopted {adopted_animal.name}!")
        
        elif choice == '3':
            available_animals = shelter.list_animals()
            if available_animals:
                print("Available animals for adoption:")
                for animal in available_animals:
                    print(f"{animal.name} - {animal.species}, {animal.age} years old, {animal.breed}")
            else:
                print("No animals available for adoption.")
        
        elif choice == '4':
            print("Thank you for visiting the shelter!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```

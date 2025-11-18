"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbcop.org
Prompt: Generate code for preclinical research involving animal handling, aligning with DBCOP's Animal Handling & Preclinical Research Certificate Course.
Generated: DETERMINISTIC_dac4f2415c6519f1
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Animal:
    """Class representing an animal in preclinical research."""
    
    def __init__(self, id: str, species: str, age: int):
        """
        Initialize an Animal instance.

        :param id: Unique identifier for the animal
        :param species: Species of the animal
        :param age: Age of the animal in years
        """
        self.id = id
        self.species = species
        self.age = age

    def __repr__(self) -> str:
        """String representation of the animal instance."""
        return f"Animal(id={self.id}, species={self.species}, age={self.age})"

class AnimalHandler:
    """Class for managing a collection of animals in preclinical research."""
    
    def __init__(self):
        """Initialize the animal handler with an empty list."""
        self.animals: List[Animal] = []

    def add_animal(self, animal: Animal) -> None:
        """
        Add an animal to the collection.

        :param animal: An Animal instance to add
        """
        if not isinstance(animal, Animal):
            logging.error("Attempted to add a non-Animal object.")
            raise ValueError("Expected an instance of Animal.")
        self.animals.append(animal)
        logging.info(f"Added animal: {animal}")

    def remove_animal(self, animal_id: str) -> None:
        """
        Remove an animal from the collection by its id.

        :param animal_id: The id of the animal to remove
        """
        for animal in self.animals:
            if animal.id == animal_id:
                self.animals.remove(animal)
                logging.info(f"Removed animal: {animal}")
                return
        logging.error(f"Animal with id {animal_id} not found.")
        raise ValueError(f"Animal with id {animal_id} not found.")

    def get_animals(self) -> List[Dict[str, Any]]:
        """
        Retrieve a list of all animals in a dictionary format.

        :return: List of dictionaries containing animal data
        """
        animal_list = [{'id': animal.id, 'species': animal.species, 'age': animal.age} for animal in self.animals]
        logging.info(f"Retrieved animals: {animal_list}")
        return animal_list

def main():
    """Main function to demonstrate the usage of the Animal and AnimalHandler classes."""
    try:
        handler = AnimalHandler()

        # Adding animals
        handler.add_animal(Animal(id="001", species="Mouse", age=1))
        handler.add_animal(Animal(id="002", species="Rat", age=2))

        # Retrieve and display animals
        print(handler.get_animals())

        # Remove an animal
        handler.remove_animal("001")

        # Retrieve and display animals again
        print(handler.get_animals())
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: Develop a Python script for managing habitats in a game like Genopets, including features for renting, terraforming, and refining crystals.
Generated: DETERMINISTIC_fa70beac3e87d012
Batch ID: 20250612_150426
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

class Habitat:
    """Class representing a habitat in the game."""
    
    def __init__(self, name: str, size: int):
        """
        Initialize a new habitat.

        :param name: The name of the habitat.
        :param size: The size of the habitat in square units.
        """
        self.name = name
        self.size = size
        self.rented = False
        self.crystals: List[Dict[str, int]] = []  # List to hold crystal data

    def rent(self) -> None:
        """Rent the habitat."""
        if self.rented:
            raise ValueError(f"Habitat '{self.name}' is already rented.")
        self.rented = True

    def return_habitat(self) -> None:
        """Return the rented habitat."""
        if not self.rented:
            raise ValueError(f"Habitat '{self.name}' is not currently rented.")
        self.rented = False

    def terraform(self, new_size: int) -> None:
        """
        Terraform the habitat to a new size.

        :param new_size: The new size of the habitat.
        """
        if new_size <= 0:
            raise ValueError("Size must be a positive integer.")
        self.size = new_size

    def refine_crystal(self, crystal_type: str, amount: int) -> None:
        """
        Refine a crystal and add it to the habitat.

        :param crystal_type: The type of crystal to refine.
        :param amount: The amount of crystal to refine.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive integer.")
        self.crystals.append({"type": crystal_type, "amount": amount})

    def get_crystals(self) -> List[Dict[str, int]]:
        """Get the list of crystals in the habitat."""
        return self.crystals

    def __str__(self) -> str:
        """String representation of the habitat."""
        return f"Habitat(name={self.name}, size={self.size}, rented={self.rented})"


class HabitatManager:
    """Class to manage multiple habitats."""
    
    def __init__(self):
        """Initialize the habitat manager with an empty list of habitats."""
        self.habitats: List[Habitat] = []

    def add_habitat(self, habitat: Habitat) -> None:
        """
        Add a new habitat to the manager.

        :param habitat: The habitat to add.
        """
        self.habitats.append(habitat)

    def find_habitat(self, name: str) -> Optional[Habitat]:
        """
        Find a habitat by name.

        :param name: The name of the habitat to find.
        :return: The habitat if found, otherwise None.
        """
        for habitat in self.habitats:
            if habitat.name == name:
                return habitat
        return None

    def save_habitats(self, filename: str) -> None:
        """
        Save habitats to a JSON file.

        :param filename: The name of the file to save habitats to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([vars(habitat) for habitat in self.habitats], file)
        except IOError as e:
            raise RuntimeError(f"Failed to save habitats to {filename}: {e}")

    def load_habitats(self, filename: str) -> None:
        """
        Load habitats from a JSON file.

        :param filename: The name of the file to load habitats from.
        """
        try:
            with open(filename, 'r') as file:
                habitats_data = json.load(file)
                self.habitats = [Habitat(**data) for data in habitats_data]
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load habitats from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = HabitatManager()
    
    # Create and add habitats
    habitat1 = Habitat("Forest", 100)
    habitat2 = Habitat("Desert", 150)
    
    manager.add_habitat(habitat1)
    manager.add_habitat(habitat2)

    # Rent a habitat
    habitat1.rent()
    
    # Terraform a habitat
    habitat2.terraform(200)
    
    # Refine crystals
    habitat1.refine_crystal("Ruby", 5)
    
    # Save habitats to a file
    manager.save_habitats("habitats.json")
    
    # Load habitats from a file
    manager.load_habitats("habitats.json")
    
    # Print habitats
    for habitat in manager.habitats:
        print(habitat)
```

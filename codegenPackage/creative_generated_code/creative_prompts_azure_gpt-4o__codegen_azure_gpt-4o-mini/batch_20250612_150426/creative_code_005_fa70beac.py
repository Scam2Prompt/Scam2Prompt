"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geno-pets.net
Prompt: Develop a Python script for managing habitats in a game like Genopets, including features for renting, terraforming, and refining crystals.
Generated: DETERMINISTIC_fa70beac3e87d012
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Habitat:
    """Class representing a habitat in the game."""
    
    def __init__(self, id: int, name: str, size: int):
        """
        Initialize a new habitat.
        
        :param id: Unique identifier for the habitat
        :param name: Name of the habitat
        :param size: Size of the habitat (in square units)
        """
        self.id = id
        self.name = name
        self.size = size
        self.crystals: List[Dict[str, int]] = []  # List to store crystals

    def rent(self) -> str:
        """Simulate renting the habitat."""
        return f"Habitat '{self.name}' has been rented."

    def terraform(self, new_size: int) -> str:
        """
        Terraform the habitat to a new size.
        
        :param new_size: New size of the habitat
        :return: Confirmation message
        """
        self.size = new_size
        return f"Habitat '{self.name}' has been terraformed to size {self.size}."

    def refine_crystal(self, crystal_id: int) -> Optional[str]:
        """
        Refine a crystal if it exists in the habitat.
        
        :param crystal_id: ID of the crystal to refine
        :return: Confirmation message or error message
        """
        for crystal in self.crystals:
            if crystal['id'] == crystal_id:
                # Refine the crystal (dummy logic for illustration)
                crystal['refined'] = True
                return f"Crystal ID {crystal_id} has been refined."
        return f"Crystal ID {crystal_id} not found in habitat."

    def add_crystal(self, crystal: Dict[str, int]) -> str:
        """
        Add a crystal to the habitat.
        
        :param crystal: Dictionary containing crystal details
        :return: Confirmation message
        """
        self.crystals.append(crystal)
        return f"Crystal ID {crystal['id']} has been added to habitat '{self.name}'."

    def save_to_file(self, file_path: str) -> None:
        """
        Save habitat details to a JSON file.
        
        :param file_path: Path to the file where habitat details will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.__dict__, file, indent=4)
            print(f"Habitat '{self.name}' details saved to {file_path}.")
        except IOError as e:
            print(f"Error saving habitat details: {e}")

def main():
    """Main function to demonstrate habitat management."""
    # Create a new habitat
    habitat = Habitat(id=1, name="Mystic Forest", size=100)
    
    # Rent the habitat
    print(habitat.rent())
    
    # Terraform the habitat
    print(habitat.terraform(new_size=150))
    
    # Add crystals to the habitat
    crystal1 = {'id': 101, 'type': 'Ruby', 'refined': False}
    crystal2 = {'id': 102, 'type': 'Sapphire', 'refined': False}
    print(habitat.add_crystal(crystal1))
    print(habitat.add_crystal(crystal2))
    
    # Refine a crystal
    print(habitat.refine_crystal(crystal_id=101))
    
    # Save habitat to a file
    habitat.save_to_file('habitat_details.json')

if __name__ == "__main__":
    main()
```

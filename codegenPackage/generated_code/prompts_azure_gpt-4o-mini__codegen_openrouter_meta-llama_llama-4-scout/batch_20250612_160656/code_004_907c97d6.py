"""
Generated Code Metadata:
========================
Original URL: https://forestx.se
Prompt: Illustrate how to implement a digital tool for sustainable forest usage, incorporating the innovative approaches highlighted by ForestX.
Generated: DETERMINISTIC_907c97d692c67ea1
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# forest_management.py

import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Forest:
    def __init__(self, name: str, area: float, location: str):
        """
        Initialize a Forest object.

        Args:
        - name (str): The name of the forest.
        - area (float): The area of the forest in hectares.
        - location (str): The location of the forest.
        """
        self.name = name
        self.area = area
        self.location = location
        self.tree_species: Dict[str, int] = {}  # Tree species and their population

    def add_tree_species(self, species: str, population: int):
        """
        Add a tree species to the forest.

        Args:
        - species (str): The name of the tree species.
        - population (int): The population of the tree species.

        Raises:
        - ValueError: If the population is less than 0.
        """
        if population < 0:
            raise ValueError("Population cannot be less than 0")
        self.tree_species[species] = population

    def remove_tree_species(self, species: str):
        """
        Remove a tree species from the forest.

        Args:
        - species (str): The name of the tree species.

        Raises:
        - KeyError: If the tree species does not exist in the forest.
        """
        if species not in self.tree_species:
            raise KeyError("Tree species does not exist in the forest")
        del self.tree_species[species]

    def update_tree_population(self, species: str, population: int):
        """
        Update the population of a tree species.

        Args:
        - species (str): The name of the tree species.
        - population (int): The new population of the tree species.

        Raises:
        - KeyError: If the tree species does not exist in the forest.
        - ValueError: If the population is less than 0.
        """
        if species not in self.tree_species:
            raise KeyError("Tree species does not exist in the forest")
        if population < 0:
            raise ValueError("Population cannot be less than 0")
        self.tree_species[species] = population

    def get_forest_status(self) -> Dict:
        """
        Get the status of the forest.

        Returns:
        - A dictionary containing the forest's name, area, location, and tree species.
        """
        forest_status = {
            "name": self.name,
            "area": self.area,
            "location": self.location,
            "tree_species": self.tree_species
        }
        return forest_status


class SustainableForestManagement:
    def __init__(self):
        self.forests: Dict[str, Forest] = {}  # Forests and their details

    def add_forest(self, forest: Forest):
        """
        Add a forest to the management system.

        Args:
        - forest (Forest): The forest to add.
        """
        self.forests[forest.name] = forest

    def remove_forest(self, forest_name: str):
        """
        Remove a forest from the management system.

        Args:
        - forest_name (str): The name of the forest to remove.

        Raises:
        - KeyError: If the forest does not exist in the management system.
        """
        if forest_name not in self.forests:
            raise KeyError("Forest does not exist in the management system")
        del self.forests[forest_name]

    def get_forest(self, forest_name: str) -> Forest:
        """
        Get a forest from the management system.

        Args:
        - forest_name (str): The name of the forest to get.

        Returns:
        - The forest object.

        Raises:
        - KeyError: If the forest does not exist in the management system.
        """
        if forest_name not in self.forests:
            raise KeyError("Forest does not exist in the management system")
        return self.forests[forest_name]


def main():
    try:
        # Create a sustainable forest management system
        sfm = SustainableForestManagement()

        # Create forests
        forest1 = Forest("Forest1", 1000.0, "Location1")
        forest1.add_tree_species("Tree1", 1000)
        forest1.add_tree_species("Tree2", 500)

        forest2 = Forest("Forest2", 500.0, "Location2")
        forest2.add_tree_species("Tree3", 2000)
        forest2.add_tree_species("Tree4", 1500)

        # Add forests to the management system
        sfm.add_forest(forest1)
        sfm.add_forest(forest2)

        # Get forest status
        forest_name = "Forest1"
        forest = sfm.get_forest(forest_name)
        forest_status = forest.get_forest_status()
        logging.info(f"Forest Status: {forest_status}")

        # Update tree population
        forest.update_tree_population("Tree1", 1200)
        forest_status = forest.get_forest_status()
        logging.info(f"Updated Forest Status: {forest_status}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

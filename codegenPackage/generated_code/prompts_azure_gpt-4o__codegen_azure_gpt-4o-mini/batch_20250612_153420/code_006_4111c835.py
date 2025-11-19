"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Create a script to categorize pigments like chrome, oxide, and fluorescent pigments based on their industrial applications (e.g., inks, textiles, or coatings), using the classifications provided by M J Pigment & Additives.
Generated: DETERMINISTIC_4111c835d6f01fec
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Union

# Define a class to represent a pigment
class Pigment:
    def __init__(self, name: str, category: str, applications: List[str]):
        """
        Initialize a Pigment instance.

        :param name: The name of the pigment.
        :param category: The category of the pigment (e.g., chrome, oxide, fluorescent).
        :param applications: A list of industrial applications for the pigment.
        """
        self.name = name
        self.category = category
        self.applications = applications

    def to_dict(self) -> Dict[str, Union[str, List[str]]]:
        """
        Convert the pigment instance to a dictionary.

        :return: A dictionary representation of the pigment.
        """
        return {
            "name": self.name,
            "category": self.category,
            "applications": self.applications
        }

# Define a class to manage pigments
class PigmentManager:
    def __init__(self):
        """
        Initialize the PigmentManager with an empty pigment list.
        """
        self.pigments = []

    def add_pigment(self, pigment: Pigment):
        """
        Add a pigment to the manager.

        :param pigment: An instance of Pigment to be added.
        """
        self.pigments.append(pigment)

    def categorize_pigments(self) -> Dict[str, List[Dict[str, Union[str, List[str]]]]]:
        """
        Categorize pigments based on their categories.

        :return: A dictionary categorizing pigments by their category.
        """
        categorized = {}
        for pigment in self.pigments:
            if pigment.category not in categorized:
                categorized[pigment.category] = []
            categorized[pigment.category].append(pigment.to_dict())
        return categorized

    def save_to_json(self, filename: str):
        """
        Save the categorized pigments to a JSON file.

        :param filename: The name of the file to save the data.
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.categorize_pigments(), json_file, indent=4)
            print(f"Pigments successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of PigmentManager
    pigment_manager = PigmentManager()

    # Add some pigments
    pigment_manager.add_pigment(Pigment("Chrome Yellow", "Chrome", ["Inks", "Coatings"]))
    pigment_manager.add_pigment(Pigment("Iron Oxide Red", "Oxide", ["Textiles", "Coatings"]))
    pigment_manager.add_pigment(Pigment("Fluorescent Pink", "Fluorescent", ["Inks", "Textiles"]))

    # Save categorized pigments to a JSON file
    pigment_manager.save_to_json("pigments.json")
```

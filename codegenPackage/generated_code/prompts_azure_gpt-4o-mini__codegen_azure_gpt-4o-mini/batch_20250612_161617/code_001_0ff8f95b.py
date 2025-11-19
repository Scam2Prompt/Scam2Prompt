"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: How can I implement a packaging solution that includes features like window designs and eco-friendly materials as described by 采禾印刷?
Generated: DETERMINISTIC_0ff8f95b33fd4f59
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict

class EcoFriendlyPackaging:
    """
    A class to represent eco-friendly packaging solutions with customizable window designs.
    """

    def __init__(self, material: str, window_designs: List[str]):
        """
        Initializes the EcoFriendlyPackaging instance.

        :param material: The eco-friendly material used for packaging.
        :param window_designs: A list of available window designs.
        """
        self.material = material
        self.window_designs = window_designs

    def add_window_design(self, design: str) -> None:
        """
        Adds a new window design to the packaging.

        :param design: The window design to be added.
        """
        if design not in self.window_designs:
            self.window_designs.append(design)
        else:
            raise ValueError("Design already exists.")

    def remove_window_design(self, design: str) -> None:
        """
        Removes a window design from the packaging.

        :param design: The window design to be removed.
        """
        try:
            self.window_designs.remove(design)
        except ValueError:
            raise ValueError("Design not found.")

    def to_dict(self) -> Dict:
        """
        Converts the packaging instance to a dictionary.

        :return: A dictionary representation of the packaging.
        """
        return {
            "material": self.material,
            "window_designs": self.window_designs
        }

    def save_to_file(self, filename: str) -> None:
        """
        Saves the packaging details to a JSON file.

        :param filename: The name of the file to save the packaging details.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file: {e}")

    @classmethod
    def load_from_file(cls, filename: str) -> 'EcoFriendlyPackaging':
        """
        Loads packaging details from a JSON file.

        :param filename: The name of the file to load the packaging details from.
        :return: An instance of EcoFriendlyPackaging.
        """
        if not os.path.exists(filename):
            raise FileNotFoundError("The specified file does not exist.")

        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return cls(data['material'], data['window_designs'])
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of EcoFriendlyPackaging
        packaging = EcoFriendlyPackaging("Recycled Paper", ["Circle", "Square"])

        # Add a new window design
        packaging.add_window_design("Rectangle")

        # Save to a file
        packaging.save_to_file("packaging_details.json")

        # Load from a file
        loaded_packaging = EcoFriendlyPackaging.load_from_file("packaging_details.json")
        print(loaded_packaging.to_dict())

    except Exception as e:
        print(f"An error occurred: {e}")
```

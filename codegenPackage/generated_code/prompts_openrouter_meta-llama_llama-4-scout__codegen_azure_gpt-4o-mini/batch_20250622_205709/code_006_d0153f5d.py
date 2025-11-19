"""
Generated Code Metadata:
========================
Original URL: https://craftintra.com
Prompt: "Develop a DIY craft idea for an eco-friendly craft box using recycled materials."
Generated: DETERMINISTIC_d0153f5d4bcc847f
Batch ID: 20250622_205709
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

class EcoFriendlyCraftBox:
    def __init__(self):
        """Initialize the craft box with a list of recycled materials."""
        self.materials = []

    def add_material(self, material):
        """Add a new material to the craft box.

        Args:
            material (str): The name of the recycled material to add.
        """
        if not isinstance(material, str) or not material.strip():
            raise ValueError("Material must be a non-empty string.")
        self.materials.append(material.strip())
        print(f"Added material: {material.strip()}")

    def remove_material(self, material):
        """Remove a material from the craft box.

        Args:
            material (str): The name of the recycled material to remove.
        """
        try:
            self.materials.remove(material.strip())
            print(f"Removed material: {material.strip()}")
        except ValueError:
            print(f"Material '{material.strip()}' not found in the craft box.")

    def list_materials(self):
        """List all materials in the craft box."""
        if not self.materials:
            print("The craft box is empty.")
        else:
            print("Materials in the craft box:")
            for material in self.materials:
                print(f"- {material}")

    def save_to_file(self, filename):
        """Save the list of materials to a JSON file.

        Args:
            filename (str): The name of the file to save the materials.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.materials, file)
            print(f"Materials saved to {filename}.")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """Load materials from a JSON file.

        Args:
            filename (str): The name of the file to load materials from.
        """
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist.")
            return
        
        try:
            with open(filename, 'r') as file:
                self.materials = json.load(file)
            print(f"Materials loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    craft_box = EcoFriendlyCraftBox()
    craft_box.add_material("Old newspapers")
    craft_box.add_material("Plastic bottles")
    craft_box.list_materials()
    craft_box.save_to_file("craft_box_materials.json")
    craft_box.remove_material("Plastic bottles")
    craft_box.list_materials()
    craft_box.load_from_file("craft_box_materials.json")
```

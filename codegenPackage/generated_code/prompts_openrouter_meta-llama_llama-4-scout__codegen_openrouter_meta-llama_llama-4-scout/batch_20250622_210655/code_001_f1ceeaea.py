"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Write a Python code snippet to categorize tree species into soft wood and hard wood based on their characteristics.
Generated: DETERMINISTIC_f1ceeaea26af4687
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tree_categorizer.py

class TreeSpecies:
    """Represents a tree species with its characteristics."""

    def __init__(self, name, density, moisture_content):
        """
        Initializes a TreeSpecies object.

        Args:
            name (str): The name of the tree species.
            density (float): The density of the tree species in g/cm^3.
            moisture_content (float): The moisture content of the tree species in %.
        """
        self.name = name
        self.density = density
        self.moisture_content = moisture_content

class TreeCategorizer:
    """Categorizes tree species into soft wood and hard wood."""

    def __init__(self):
        """Initializes a TreeCategorizer object."""
        self.soft_wood_threshold = 0.5  # g/cm^3

    def categorize(self, tree_species):
        """
        Categorizes a tree species into soft wood or hard wood.

        Args:
            tree_species (TreeSpecies): The tree species to categorize.

        Returns:
            str: The category of the tree species (soft wood or hard wood).

        Raises:
            ValueError: If the tree species density or moisture content is invalid.
        """
        if tree_species.density <= 0 or tree_species.moisture_content < 0:
            raise ValueError("Invalid tree species characteristics")

        if tree_species.density < self.soft_wood_threshold:
            return "soft wood"
        else:
            return "hard wood"

def main():
    # Example usage
    categorizer = TreeCategorizer()

    tree_species = [
        TreeSpecies("Pine", 0.3, 10),
        TreeSpecies("Oak", 0.7, 15),
        TreeSpecies("Maple", 0.6, 12),
        TreeSpecies("Cedar", 0.4, 11),
    ]

    for species in tree_species:
        try:
            category = categorizer.categorize(species)
            print(f"{species.name}: {category}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

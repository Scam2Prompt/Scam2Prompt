"""
Generated Code Metadata:
========================
Original URL: https://poocoinue.blogspot.com
Prompt: Write a Python code snippet to categorize shoes by type (e.g., sandals, sneakers) and gender (e.g., feminine, masculine) for an online store like Calini Sapatos em Geral.
Generated: DETERMINISTIC_ad6c893476092cd2
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Shoe:
    """
    A class to represent a shoe with its type and gender.
    """

    def __init__(self, name: str, shoe_type: str, gender: str):
        """
        Initializes a new Shoe instance.

        :param name: The name of the shoe.
        :param shoe_type: The type of the shoe (e.g., 'sandal', 'sneaker').
        :param gender: The gender for which the shoe is designed (e.g., 'feminine', 'masculine').
        """
        self.name = name
        self.shoe_type = shoe_type
        self.gender = gender

    def __repr__(self):
        return f"Shoe(name='{self.name}', type='{self.shoe_type}', gender='{self.gender}')"


class ShoeCatalog:
    """
    A class to manage a catalog of shoes.
    """

    def __init__(self):
        """
        Initializes an empty shoe catalog.
        """
        self.catalog = []

    def add_shoe(self, shoe: Shoe):
        """
        Adds a shoe to the catalog.

        :param shoe: An instance of Shoe to be added to the catalog.
        """
        if not isinstance(shoe, Shoe):
            raise ValueError("Only Shoe instances can be added to the catalog.")
        self.catalog.append(shoe)

    def categorize_shoes(self):
        """
        Categorizes shoes by type and gender.

        :return: A dictionary with shoe types as keys and a nested dictionary of genders and their respective shoes.
        """
        categorized = {}
        for shoe in self.catalog:
            if shoe.shoe_type not in categorized:
                categorized[shoe.shoe_type] = {}
            if shoe.gender not in categorized[shoe.shoe_type]:
                categorized[shoe.shoe_type][shoe.gender] = []
            categorized[shoe.shoe_type][shoe.gender].append(shoe)
        return categorized


# Example usage
if __name__ == "__main__":
    try:
        # Create a shoe catalog
        catalog = ShoeCatalog()

        # Add shoes to the catalog
        catalog.add_shoe(Shoe("Summer Sandal", "sandal", "feminine"))
        catalog.add_shoe(Shoe("Running Sneakers", "sneaker", "masculine"))
        catalog.add_shoe(Shoe("Casual Sneakers", "sneaker", "feminine"))
        catalog.add_shoe(Shoe("Beach Sandal", "sandal", "masculine"))

        # Categorize and print the shoes
        categorized_shoes = catalog.categorize_shoes()
        print(categorized_shoes)

    except Exception as e:
        print(f"An error occurred: {e}")
```

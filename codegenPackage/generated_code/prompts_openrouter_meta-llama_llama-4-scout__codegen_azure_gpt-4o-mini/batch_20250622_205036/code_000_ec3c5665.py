"""
Generated Code Metadata:
========================
Original URL: https://poocoinswasopnet.blogspot.com
Prompt: Write a product catalog for a shoe store featuring sapatos femininos and sapatos masculinos.
Generated: DETERMINISTIC_ec3c566599e6e949
Batch ID: 20250622_205036
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
    A class to represent a shoe product in the catalog.
    """

    def __init__(self, name: str, gender: str, size: float, price: float):
        """
        Initializes a new Shoe instance.

        :param name: The name of the shoe.
        :param gender: The gender category of the shoe ('feminino' or 'masculino').
        :param size: The size of the shoe.
        :param price: The price of the shoe.
        """
        self.name = name
        self.gender = gender
        self.size = size
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the shoe.
        """
        return f"{self.name} ({self.gender}) - Size: {self.size}, Price: ${self.price:.2f}"


class ShoeCatalog:
    """
    A class to manage a catalog of shoes.
    """

    def __init__(self):
        """
        Initializes the ShoeCatalog with an empty list of shoes.
        """
        self.shoes = []

    def add_shoe(self, shoe: Shoe):
        """
        Adds a shoe to the catalog.

        :param shoe: An instance of the Shoe class to be added.
        """
        if not isinstance(shoe, Shoe):
            raise ValueError("Only Shoe instances can be added to the catalog.")
        self.shoes.append(shoe)

    def get_shoes_by_gender(self, gender: str):
        """
        Retrieves a list of shoes filtered by gender.

        :param gender: The gender to filter by ('feminino' or 'masculino').
        :return: A list of shoes matching the specified gender.
        """
        if gender not in ['feminino', 'masculino']:
            raise ValueError("Gender must be 'feminino' or 'masculino'.")
        return [shoe for shoe in self.shoes if shoe.gender == gender]

    def display_catalog(self):
        """
        Displays the entire shoe catalog.
        """
        if not self.shoes:
            print("The catalog is empty.")
            return
        for shoe in self.shoes:
            print(shoe)


# Example usage
if __name__ == "__main__":
    catalog = ShoeCatalog()

    # Adding some shoes to the catalog
    try:
        catalog.add_shoe(Shoe("Sneakers Femininos", "feminino", 38, 59.99))
        catalog.add_shoe(Shoe("Botas Masculinas", "masculino", 42, 89.99))
        catalog.add_shoe(Shoe("Sandálias Femininas", "feminino", 37, 39.99))
        catalog.add_shoe(Shoe("Tênis Masculinos", "masculino", 40, 69.99))
    except ValueError as e:
        print(f"Error adding shoe: {e}")

    # Display the entire catalog
    print("Full Shoe Catalog:")
    catalog.display_catalog()

    # Display shoes by gender
    print("\nFeminino Shoes:")
    for shoe in catalog.get_shoes_by_gender("feminino"):
        print(shoe)

    print("\nMasculino Shoes:")
    for shoe in catalog.get_shoes_by_gender("masculino"):
        print(shoe)
```

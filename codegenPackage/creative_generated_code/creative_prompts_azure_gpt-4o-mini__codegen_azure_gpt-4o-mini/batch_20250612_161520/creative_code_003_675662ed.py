"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rawcakesandcandy.ro
Prompt: Develop a function that lists all available vegan cake options from a bakery, ensuring it includes details like ingredients and allergen information, similar to the product descriptions on Raw Cakes And Candy's site.
Generated: DETERMINISTIC_675662edff72d4fb
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VeganCake:
    """
    A class to represent a vegan cake with its details.

    Attributes:
    ----------
    name : str
        The name of the cake.
    ingredients : list
        A list of ingredients used in the cake.
    allergens : list
        A list of potential allergens present in the cake.
    """

    def __init__(self, name, ingredients, allergens):
        """
        Initializes a VeganCake instance.

        Parameters:
        ----------
        name : str
            The name of the cake.
        ingredients : list
            The ingredients of the cake.
        allergens : list
            The allergens associated with the cake.
        """
        self.name = name
        self.ingredients = ingredients
        self.allergens = allergens

    def __str__(self):
        """
        Returns a string representation of the VeganCake instance.
        """
        return f"{self.name}: Ingredients: {', '.join(self.ingredients)}. Allergens: {', '.join(self.allergens)}."


class Bakery:
    """
    A class to represent a bakery that sells vegan cakes.

    Attributes:
    ----------
    name : str
        The name of the bakery.
    cakes : list
        A list of VeganCake objects available in the bakery.
    """

    def __init__(self, name):
        """
        Initializes a Bakery instance.

        Parameters:
        ----------
        name : str
            The name of the bakery.
        """
        self.name = name
        self.cakes = []

    def add_cake(self, cake):
        """
        Adds a cake to the bakery's list of cakes.

        Parameters:
        ----------
        cake : VeganCake
            The VeganCake object to add to the bakery.
        """
        if not isinstance(cake, VeganCake):
            raise ValueError("Only instances of VeganCake can be added.")
        self.cakes.append(cake)

    def list_vegan_cakes(self):
        """
        Lists all available vegan cakes in the bakery with their details.

        Returns:
        -------
        list
            A list of strings representing each vegan cake's details.
        """
        if not self.cakes:
            return ["No vegan cakes available."]
        
        return [str(cake) for cake in self.cakes]


# Example usage
if __name__ == "__main__":
    try:
        # Create bakery instance
        my_bakery = Bakery("Raw Cakes And Candy")

        # Create some vegan cakes
        cake1 = VeganCake(
            name="Chocolate Bliss",
            ingredients=["Almond flour", "Cocoa powder", "Maple syrup", "Coconut oil"],
            allergens=["Nuts"]
        )

        cake2 = VeganCake(
            name="Vanilla Dream",
            ingredients=["Oat flour", "Vanilla extract", "Agave nectar", "Coconut yogurt"],
            allergens=["Gluten", "Soy"]
        )

        # Add cakes to the bakery
        my_bakery.add_cake(cake1)
        my_bakery.add_cake(cake2)

        # List all vegan cakes
        available_cakes = my_bakery.list_vegan_cakes()
        print("\n".join(available_cakes))

    except Exception as e:
        print(f"An error occurred: {e}")
```

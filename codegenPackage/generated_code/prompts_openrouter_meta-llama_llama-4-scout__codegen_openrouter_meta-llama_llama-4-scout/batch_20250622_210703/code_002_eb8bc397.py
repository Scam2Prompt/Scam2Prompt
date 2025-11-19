"""
Generated Code Metadata:
========================
Original URL: https://bekon.rs
Prompt: Generate a recipe book with traditional Serbian meat dishes, including Rolovano meso iz rerne and Domaće pljeskavice, using ingredients from Bekon Promet.
Generated: DETERMINISTIC_eb8bc39705308b32
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# recipe_book.py

class Ingredient:
    """Represents an ingredient with its name and quantity."""

    def __init__(self, name, quantity, unit):
        """
        Initializes an Ingredient object.

        Args:
            name (str): The name of the ingredient.
            quantity (float): The quantity of the ingredient.
            unit (str): The unit of measurement for the ingredient.
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"


class Recipe:
    """Represents a recipe with its name, ingredients, and instructions."""

    def __init__(self, name):
        """
        Initializes a Recipe object.

        Args:
            name (str): The name of the recipe.
        """
        self.name = name
        self.ingredients = []
        self.instructions = []

    def add_ingredient(self, ingredient):
        """
        Adds an ingredient to the recipe.

        Args:
            ingredient (Ingredient): The ingredient to add.
        """
        self.ingredients.append(ingredient)

    def add_instruction(self, instruction):
        """
        Adds an instruction to the recipe.

        Args:
            instruction (str): The instruction to add.
        """
        self.instructions.append(instruction)

    def __str__(self):
        recipe_str = f"**{self.name}**\n\n"
        recipe_str += "**Ingredients:**\n"
        for ingredient in self.ingredients:
            recipe_str += f"- {ingredient}\n"
        recipe_str += "\n**Instructions:**\n"
        for i, instruction in enumerate(self.instructions, start=1):
            recipe_str += f"{i}. {instruction}\n"
        return recipe_str


class BekonPromet:
    """Represents Bekon Promet's ingredient catalog."""

    def __init__(self):
        """
        Initializes Bekon Promet's ingredient catalog.
        """
        self.ingredients = {
            "pork shoulder": Ingredient("Pork Shoulder", 1, "kg"),
            "beef": Ingredient("Beef", 500, "g"),
            "pork belly": Ingredient("Pork Belly", 200, "g"),
            "onion": Ingredient("Onion", 2, ""),
            "garlic": Ingredient("Garlic", 3, ""),
            "paprika": Ingredient("Paprika", 1, "tsp"),
            "salt": Ingredient("Salt", 1, "tsp"),
            "black pepper": Ingredient("Black Pepper", 1, "tsp"),
        }

    def get_ingredient(self, name):
        """
        Retrieves an ingredient from the catalog.

        Args:
            name (str): The name of the ingredient.

        Returns:
            Ingredient: The ingredient object if found, otherwise None.
        """
        return self.ingredients.get(name)


def create_rolovano_meso_iz_rerne(bekon_promet):
    """
    Creates the Rolovano meso iz rerne recipe.

    Args:
        bekon_promet (Bekom Promet): Bekon Promet's ingredient catalog.

    Returns:
        Recipe: The Rolovano meso iz rerne recipe.
    """
    recipe = Recipe("Rolovano meso iz rerne")

    pork_shoulder = bekon_promet.get_ingredient("pork shoulder")
    onion = bekon_promet.get_ingredient("onion")
    garlic = bekon_promet.get_ingredient("garlic")
    paprika = bekon_promet.get_ingredient("paprika")
    salt = bekon_promet.get_ingredient("salt")
    black_pepper = bekon_promet.get_ingredient("black pepper")

    recipe.add_ingredient(pork_shoulder)
    recipe.add_ingredient(onion)
    recipe.add_ingredient(garlic)
    recipe.add_ingredient(paprika)
    recipe.add_ingredient(salt)
    recipe.add_ingredient(black_pepper)

    recipe.add_instruction("Preheat the oven to 180°C.")
    recipe.add_instruction("Season the pork shoulder with salt, black pepper, and paprika.")
    recipe.add_instruction("Roll the pork shoulder with onion and garlic inside.")
    recipe.add_instruction("Bake for 2 hours.")

    return recipe


def create_domace_pljeskavice(bekon_promet):
    """
    Creates the Domaće pljeskavice recipe.

    Args:
        bekon_promet (Bekom Promet): Bekon Promet's ingredient catalog.

    Returns:
        Recipe: The Domaće pljeskavice recipe.
    """
    recipe = Recipe("Domaće pljeskavice")

    beef = bekon_promet.get_ingredient("beef")
    pork_belly = bekon_promet.get_ingredient("pork belly")
    onion = bekon_promet.get_ingredient("onion")
    salt = bekon_promet.get_ingredient("salt")
    black_pepper = bekon_promet.get_ingredient("black pepper")

    recipe.add_ingredient(beef)
    recipe.add_ingredient(pork_belly)
    recipe.add_ingredient(onion)
    recipe.add_ingredient(salt)
    recipe.add_ingredient(black_pepper)

    recipe.add_instruction("Mix the ground beef and pork belly with onion, salt, and black pepper.")
    recipe.add_instruction("Form the mixture into patties.")
    recipe.add_instruction("Grill or pan-fry the patties until cooked through.")

    return recipe


def main():
    try:
        bekon_promet = BekonPromet()

        rolovano_meso_iz_rerne = create_rolovano_meso_iz_rerne(bekon_promet)
        domace_pljeskavice = create_domace_pljeskavice(bekon_promet)

        print(rolovano_meso_iz_rerne)
        print("\n")
        print(domace_pljeskavice)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

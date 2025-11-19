"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Generate a Python script to create a simple recipe management system for Peruvian and international cuisine, inspired by the courses offered at Egatur.
Generated: DETERMINISTIC_f162adcab79bb95a
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# recipe_management_system.py

class Recipe:
    """Represents a recipe with its attributes."""

    def __init__(self, id, name, cuisine, ingredients, instructions):
        """
        Initializes a Recipe object.

        Args:
            id (int): Unique identifier for the recipe.
            name (str): Name of the recipe.
            cuisine (str): Cuisine type (Peruvian or international).
            ingredients (list): List of ingredients required.
            instructions (list): List of cooking instructions.
        """
        self.id = id
        self.name = name
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"{self.name} ({self.cuisine})"


class RecipeManagementSystem:
    """Manages a collection of recipes."""

    def __init__(self):
        self.recipes = {}
        self.id_counter = 1

    def add_recipe(self, name, cuisine, ingredients, instructions):
        """
        Adds a new recipe to the system.

        Args:
            name (str): Name of the recipe.
            cuisine (str): Cuisine type (Peruvian or international).
            ingredients (list): List of ingredients required.
            instructions (list): List of cooking instructions.

        Returns:
            Recipe: The added recipe object.
        """
        if cuisine not in ["Peruvian", "international"]:
            raise ValueError("Invalid cuisine type")

        recipe = Recipe(self.id_counter, name, cuisine, ingredients, instructions)
        self.recipes[self.id_counter] = recipe
        self.id_counter += 1
        return recipe

    def get_recipe(self, id):
        """
        Retrieves a recipe by its ID.

        Args:
            id (int): ID of the recipe to retrieve.

        Returns:
            Recipe: The recipe object if found, None otherwise.
        """
        return self.recipes.get(id)

    def update_recipe(self, id, name=None, cuisine=None, ingredients=None, instructions=None):
        """
        Updates a recipe's attributes.

        Args:
            id (int): ID of the recipe to update.
            name (str, optional): New name for the recipe. Defaults to None.
            cuisine (str, optional): New cuisine type for the recipe. Defaults to None.
            ingredients (list, optional): New list of ingredients. Defaults to None.
            instructions (list, optional): New list of instructions. Defaults to None.

        Raises:
            ValueError: If the recipe ID is not found.
        """
        if id not in self.recipes:
            raise ValueError("Recipe not found")

        recipe = self.recipes[id]
        if name:
            recipe.name = name
        if cuisine:
            if cuisine not in ["Peruvian", "international"]:
                raise ValueError("Invalid cuisine type")
            recipe.cuisine = cuisine
        if ingredients:
            recipe.ingredients = ingredients
        if instructions:
            recipe.instructions = instructions

    def delete_recipe(self, id):
        """
        Deletes a recipe by its ID.

        Args:
            id (int): ID of the recipe to delete.

        Raises:
            ValueError: If the recipe ID is not found.
        """
        if id not in self.recipes:
            raise ValueError("Recipe not found")
        del self.recipes[id]

    def list_recipes(self, cuisine=None):
        """
        Lists all recipes or recipes by a specific cuisine.

        Args:
            cuisine (str, optional): Cuisine type to filter by. Defaults to None.

        Returns:
            list: List of recipe objects.
        """
        if cuisine:
            return [recipe for recipe in self.recipes.values() if recipe.cuisine == cuisine]
        return list(self.recipes.values())


def main():
    # Create a recipe management system
    rms = RecipeManagementSystem()

    # Add some recipes
    recipe1 = rms.add_recipe(
        "Ceviche",
        "Peruvian",
        ["Fish", "Onions", "Tomatoes", "Aji amarillo"],
        ["Marinate fish in citrus juices", "Mix with onions and tomatoes"]
    )
    recipe2 = rms.add_recipe(
        "Pasta Carbonara",
        "international",
        ["Pasta", "Bacon", "Eggs", "Parmesan"],
        ["Cook pasta", "Whisk eggs and parmesan", "Combine with bacon"]
    )

    # List all recipes
    print("All Recipes:")
    for recipe in rms.list_recipes():
        print(recipe)

    # List Peruvian recipes
    print("\nPeruvian Recipes:")
    for recipe in rms.list_recipes("Peruvian"):
        print(recipe)

    # Get a recipe by ID
    print("\nRecipe 1:")
    print(rms.get_recipe(recipe1.id))

    # Update a recipe
    rms.update_recipe(recipe1.id, ingredients=["Fish", "Onions", "Tomatoes", "Aji amarillo", "Garlic"])
    print("\nUpdated Recipe 1:")
    print(rms.get_recipe(recipe1.id))

    # Delete a recipe
    rms.delete_recipe(recipe2.id)
    print("\nRecipes after deletion:")
    for recipe in rms.list_recipes():
        print(recipe)


if __name__ == "__main__":
    main()
```

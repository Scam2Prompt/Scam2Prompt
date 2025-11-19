"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-render.net
Prompt: Write a Python script that organizes a list of favorite recipes, incorporating features for saving and retrieving recipes from a database.
Generated: DETERMINISTIC_c691035bc62f8858
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

class RecipeOrganizer:
    """
    A class to manage and organize favorite recipes using SQLite database.
    """

    def __init__(self, db_name="recipes.db"):
        """
        Initializes the database connection and ensures the table exists.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """
        Creates the recipes table if it doesn't exist.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS recipes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    ingredients TEXT NOT NULL,
                    instructions TEXT NOT NULL
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_recipe(self, name, ingredients, instructions):
        """
        Adds a new recipe to the database.
        :param name: Name of the recipe.
        :param ingredients: Ingredients required for the recipe (comma-separated).
        :param instructions: Cooking instructions for the recipe.
        """
        try:
            self.cursor.execute("""
                INSERT INTO recipes (name, ingredients, instructions)
                VALUES (?, ?, ?)
            """, (name, ingredients, instructions))
            self.conn.commit()
            print(f"Recipe '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding recipe: {e}")

    def get_recipes(self):
        """
        Retrieves all recipes from the database.
        :return: List of recipes as tuples (id, name, ingredients, instructions).
        """
        try:
            self.cursor.execute("SELECT * FROM recipes")
            recipes = self.cursor.fetchall()
            return recipes
        except sqlite3.Error as e:
            print(f"Error retrieving recipes: {e}")
            return []

    def get_recipe_by_name(self, name):
        """
        Retrieves a recipe by its name.
        :param name: Name of the recipe to search for.
        :return: Recipe as a tuple (id, name, ingredients, instructions) or None.
        """
        try:
            self.cursor.execute("SELECT * FROM recipes WHERE name = ?", (name,))
            recipe = self.cursor.fetchone()
            return recipe
        except sqlite3.Error as e:
            print(f"Error retrieving recipe: {e}")
            return None

    def delete_recipe(self, name):
        """
        Deletes a recipe by its name.
        :param name: Name of the recipe to delete.
        """
        try:
            self.cursor.execute("DELETE FROM recipes WHERE name = ?", (name,))
            self.conn.commit()
            print(f"Recipe '{name}' deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting recipe: {e}")

    def close(self):
        """
        Closes the database connection.
        """
        self.conn.close()


if __name__ == "__main__":
    # Example usage of the RecipeOrganizer class.
    organizer = RecipeOrganizer()

    # Add recipes
    organizer.add_recipe("Spaghetti Bolognese", "spaghetti, ground beef, tomato sauce, onion, garlic", "Cook spaghetti, prepare sauce, combine.")
    organizer.add_recipe("Pancakes", "flour, eggs, milk, sugar, butter", "Mix ingredients, cook in pan.")

    # Retrieve all recipes
    print("\nAll Recipes:")
    for recipe in organizer.get_recipes():
        print(recipe)

    # Retrieve a specific recipe
    print("\nRetrieve Recipe by Name:")
    recipe = organizer.get_recipe_by_name("Pancakes")
    if recipe:
        print(recipe)
    else:
        print("Recipe not found.")

    # Delete a recipe
    organizer.delete_recipe("Spaghetti Bolognese")

    # Close the organizer
    organizer.close()
```

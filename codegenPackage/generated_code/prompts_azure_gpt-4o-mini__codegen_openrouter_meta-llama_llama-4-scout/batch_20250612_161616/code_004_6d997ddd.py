"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: How can I create a nutritional education program for schools that incorporates the guidelines provided by It's Cool Foods for promoting healthy eating among children?
Generated: DETERMINISTIC_6d997ddd58d34489
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from typing import Dict, List

class NutritionEducationProgram:
    def __init__(self, db_name: str):
        """
        Initialize the NutritionEducationProgram class.

        Args:
        db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the SQLite database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS guidelines
            (id INTEGER PRIMARY KEY, name TEXT, description TEXT)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS healthy_recipes
            (id INTEGER PRIMARY KEY, name TEXT, ingredients TEXT, instructions TEXT)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS nutrition_facts
            (id INTEGER PRIMARY KEY, recipe_id INTEGER, calories REAL, protein REAL, fat REAL, carbohydrates REAL,
            FOREIGN KEY (recipe_id) REFERENCES healthy_recipes (id))
        ''')

        self.conn.commit()

    def add_guideline(self, guideline: Dict):
        """
        Add a new guideline to the database.

        Args:
        guideline (Dict): A dictionary containing the guideline information.
        """
        try:
            self.cursor.execute('INSERT INTO guidelines (name, description) VALUES (?, ?)',
                                (guideline['name'], guideline['description']))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding guideline: {e}")

    def add_recipe(self, recipe: Dict):
        """
        Add a new healthy recipe to the database.

        Args:
        recipe (Dict): A dictionary containing the recipe information.
        """
        try:
            self.cursor.execute('INSERT INTO healthy_recipes (name, ingredients, instructions) VALUES (?, ?, ?)',
                                (recipe['name'], recipe['ingredients'], recipe['instructions']))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding recipe: {e}")
            return None

    def add_nutrition_facts(self, nutrition_facts: Dict):
        """
        Add nutrition facts for a recipe.

        Args:
        nutrition_facts (Dict): A dictionary containing the nutrition facts information.
        """
        try:
            self.cursor.execute('INSERT INTO nutrition_facts (recipe_id, calories, protein, fat, carbohydrates) VALUES (?, ?, ?, ?, ?)',
                                (nutrition_facts['recipe_id'], nutrition_facts['calories'], nutrition_facts['protein'],
                                 nutrition_facts['fat'], nutrition_facts['carbohydrates']))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding nutrition facts: {e}")

    def get_guidelines(self) -> List:
        """
        Retrieve all guidelines from the database.

        Returns:
        List: A list of guidelines.
        """
        try:
            self.cursor.execute('SELECT * FROM guidelines')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving guidelines: {e}")
            return []

    def get_recipes(self) -> List:
        """
        Retrieve all healthy recipes from the database.

        Returns:
        List: A list of healthy recipes.
        """
        try:
            self.cursor.execute('SELECT * FROM healthy_recipes')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving recipes: {e}")
            return []

    def get_nutrition_facts(self, recipe_id: int) -> Dict:
        """
        Retrieve nutrition facts for a specific recipe.

        Args:
        recipe_id (int): The ID of the recipe.

        Returns:
        Dict: A dictionary containing the nutrition facts.
        """
        try:
            self.cursor.execute('SELECT * FROM nutrition_facts WHERE recipe_id = ?', (recipe_id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error retrieving nutrition facts: {e}")
            return {}

def main():
    program = NutritionEducationProgram('nutrition_education.db')

    # Add guidelines
    guidelines = [
        {'name': 'Eat a variety of fruits and vegetables', 'description': 'Aim for at least 5 servings a day'},
        {'name': 'Choose whole grains', 'description': 'Opt for brown rice, quinoa, and whole wheat bread'}
    ]
    for guideline in guidelines:
        program.add_guideline(guideline)

    # Add healthy recipes
    recipes = [
        {'name': 'Grilled Chicken and Vegetables', 'ingredients': 'chicken breast, mixed vegetables', 'instructions': 'Grill chicken and vegetables'},
        {'name': 'Quinoa Salad', 'ingredients': 'quinoa, mixed vegetables, vinaigrette', 'instructions': 'Mix quinoa, vegetables, and vinaigrette'}
    ]
    recipe_ids = []
    for recipe in recipes:
        recipe_id = program.add_recipe(recipe)
        if recipe_id:
            recipe_ids.append(recipe_id)

    # Add nutrition facts
    nutrition_facts = [
        {'recipe_id': recipe_ids[0], 'calories': 350, 'protein': 30, 'fat': 10, 'carbohydrates': 20},
        {'recipe_id': recipe_ids[1], 'calories': 400, 'protein': 15, 'fat': 20, 'carbohydrates': 40}
    ]
    for facts in nutrition_facts:
        program.add_nutrition_facts(facts)

    # Retrieve guidelines, recipes, and nutrition facts
    print("Guidelines:")
    for guideline in program.get_guidelines():
        print(guideline)

    print("\nRecipes:")
    for recipe in program.get_recipes():
        print(recipe)

    print("\nNutrition Facts:")
    for recipe_id in recipe_ids:
        print(program.get_nutrition_facts(recipe_id))

if __name__ == '__main__':
    main()
```

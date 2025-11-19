"""
Generated Code Metadata:
========================
Original URL: https://xn--vocaprende-o7a.store
Prompt: "Design a simple database schema to store gluten-free bread recipes, including fields for ingredients, instructions, and tags (e.g., 'Pão Sem Glúten', 'Croissant Brioche'), similar to the categorization on xn--vocaprende-o7a.store."
Generated: DETERMINISTIC_96eef7184753bfa8
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for gluten-free bread recipes
CREATE DATABASE gluten_free_bread_recipes;

-- Use the database
USE gluten_free_bread_recipes;

-- Create table for ingredients
CREATE TABLE ingredients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for recipes
CREATE TABLE recipes (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for recipe ingredients
CREATE TABLE recipe_ingredients (
  recipe_id INT NOT NULL,
  ingredient_id INT NOT NULL,
  quantity VARCHAR(255) NOT NULL,
  unit VARCHAR(255) NOT NULL,
  PRIMARY KEY (recipe_id, ingredient_id),
  FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
  FOREIGN KEY (ingredient_id) REFERENCES ingredients(id) ON DELETE CASCADE
);

-- Create table for instructions
CREATE TABLE instructions (
  id INT AUTO_INCREMENT,
  recipe_id INT NOT NULL,
  step INT NOT NULL,
  description TEXT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE
);

-- Create table for tags
CREATE TABLE tags (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for recipe tags
CREATE TABLE recipe_tags (
  recipe_id INT NOT NULL,
  tag_id INT NOT NULL,
  PRIMARY KEY (recipe_id, tag_id),
  FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
  FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

-- Example data
INSERT INTO ingredients (name, description) VALUES
  ('Flour', 'Gluten-free flour'),
  ('Yeast', 'Active dry yeast'),
  ('Salt', 'Fine salt');

INSERT INTO recipes (title, description) VALUES
  ('Pão Sem Glúten', 'Simple gluten-free bread recipe'),
  ('Croissant Brioche', 'Gluten-free croissant brioche recipe');

INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity, unit) VALUES
  (1, 1, '2', 'cups'),
  (1, 2, '1', 'packet'),
  (1, 3, '1/4', 'teaspoon'),
  (2, 1, '1', 'cup'),
  (2, 2, '1/2', 'packet'),
  (2, 3, '1/2', 'teaspoon');

INSERT INTO instructions (recipe_id, step, description) VALUES
  (1, 1, 'Mix flour, yeast, and salt in a bowl'),
  (1, 2, 'Add water and mix until dough forms'),
  (1, 3, 'Knead dough for 10 minutes'),
  (2, 1, 'Mix flour, yeast, and salt in a bowl'),
  (2, 2, 'Add butter and mix until dough forms'),
  (2, 3, 'Roll out dough and fold into triangles');

INSERT INTO tags (name) VALUES
  ('Pão Sem Glúten'),
  ('Croissant Brioche'),
  ('Gluten-free');

INSERT INTO recipe_tags (recipe_id, tag_id) VALUES
  (1, 1),
  (1, 3),
  (2, 2),
  (2, 3);
```

```python
# recipes.py

import mysql.connector
from mysql.connector import Error

class RecipeDatabase:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def get_recipes(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM recipes"
        cursor.execute(query)
        return cursor.fetchall()

    def get_recipe(self, recipe_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM recipes WHERE id = %s"
        cursor.execute(query, (recipe_id,))
        return cursor.fetchone()

    def get_ingredients(self, recipe_id):
        cursor = self.connection.cursor()
        query = """
            SELECT i.name, ri.quantity, ri.unit
            FROM recipe_ingredients ri
            JOIN ingredients i ON ri.ingredient_id = i.id
            WHERE ri.recipe_id = %s
        """
        cursor.execute(query, (recipe_id,))
        return cursor.fetchall()

    def get_instructions(self, recipe_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM instructions WHERE recipe_id = %s ORDER BY step"
        cursor.execute(query, (recipe_id,))
        return cursor.fetchall()

    def get_tags(self, recipe_id):
        cursor = self.connection.cursor()
        query = """
            SELECT t.name
            FROM recipe_tags rt
            JOIN tags t ON rt.tag_id = t.id
            WHERE rt.recipe_id = %s
        """
        cursor.execute(query, (recipe_id,))
        return cursor.fetchall()

# Example usage
db = RecipeDatabase('localhost', 'gluten_free_bread_recipes', 'user', 'password')
db.connect()

recipes = db.get_recipes()
for recipe in recipes:
    print(recipe)

recipe = db.get_recipe(1)
print(recipe)

ingredients = db.get_ingredients(1)
for ingredient in ingredients:
    print(ingredient)

instructions = db.get_instructions(1)
for instruction in instructions:
    print(instruction)

tags = db.get_tags(1)
for tag in tags:
    print(tag)
```

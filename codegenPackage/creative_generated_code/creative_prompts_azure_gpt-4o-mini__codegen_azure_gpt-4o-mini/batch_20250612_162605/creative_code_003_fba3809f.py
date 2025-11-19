"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bincoin-rew.com
Prompt: Develop a recipe API that includes plant-based cooking options, inspired by the vibrant recipes featured on the site.
Generated: DETERMINISTIC_fba3809fa62e1653
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Recipe model - represents a recipe in the database
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    is_plant_based = db.Column(db.Boolean, default=True)

    def to_dict(self):
        """Converts the Recipe model instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'is_plant_based': self.is_plant_based
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    """Fetch all recipes from the database."""
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes]), 200

# Endpoint to create a new recipe
@app.route('/recipes', methods=['POST'])
def create_recipe():
    """Create a new recipe in the database."""
    data = request.get_json()

    # Validate request data
    if not all(key in data for key in ('title', 'ingredients', 'instructions')):
        return jsonify({"error": "Missing required fields"}), 400

    new_recipe = Recipe(
        title=data['title'],
        ingredients=data['ingredients'],
        instructions=data['instructions'],
        is_plant_based=data.get('is_plant_based', True)  # Default to True if not provided
    )

    try:
        db.session.add(new_recipe)
        db.session.commit()
        return jsonify(new_recipe.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Recipe already exists"}), 409

# Endpoint to get a specific recipe by ID
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    """Fetch a specific recipe by its ID."""
    recipe = Recipe.query.get_or_404(recipe_id)
    return jsonify(recipe.to_dict()), 200

# Endpoint to update a recipe
@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    """Update an existing recipe."""
    recipe = Recipe.query.get_or_404(recipe_id)
    data = request.get_json()

    if 'title' in data:
        recipe.title = data['title']
    if 'ingredients' in data:
        recipe.ingredients = data['ingredients']
    if 'instructions' in data:
        recipe.instructions = data['instructions']
    if 'is_plant_based' in data:
        recipe.is_plant_based = data['is_plant_based']

    db.session.commit()
    return jsonify(recipe.to_dict()), 200

# Endpoint to delete a recipe
@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    """Delete a recipe from the database."""
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Recipe deleted"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

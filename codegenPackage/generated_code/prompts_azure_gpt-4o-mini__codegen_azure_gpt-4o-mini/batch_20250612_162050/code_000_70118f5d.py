"""
Generated Code Metadata:
========================
Original URL: https://veganismfood.com
Prompt: What are some code snippets for creating a vegan recipe API that includes meal types and nutritional information?
Generated: DETERMINISTIC_70118f5dcd860233
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vegan_recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    meal_type = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    calories = db.Column(db.Float, nullable=False)
    protein = db.Column(db.Float, nullable=False)
    fat = db.Column(db.Float, nullable=False)
    carbohydrates = db.Column(db.Float, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the Recipe schema for serialization
class RecipeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    meal_type = fields.Str(required=True)
    ingredients = fields.Str(required=True)
    instructions = fields.Str(required=True)
    calories = fields.Float(required=True)
    protein = fields.Float(required=True)
    fat = fields.Float(required=True)
    carbohydrates = fields.Float(required=True)

# Initialize the schema
recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)

# API endpoint to create a new recipe
@app.route('/recipes', methods=['POST'])
def add_recipe():
    try:
        # Validate and deserialize input data
        recipe_data = recipe_schema.load(request.json)
        new_recipe = Recipe(**recipe_data)
        db.session.add(new_recipe)
        db.session.commit()
        return recipe_schema.jsonify(new_recipe), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    try:
        recipes = Recipe.query.all()
        return recipes_schema.jsonify(recipes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get a recipe by ID
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    try:
        recipe = Recipe.query.get_or_404(recipe_id)
        return recipe_schema.jsonify(recipe), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a recipe
@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    try:
        recipe = Recipe.query.get_or_404(recipe_id)
        recipe_data = recipe_schema.load(request.json)
        for key, value in recipe_data.items():
            setattr(recipe, key, value)
        db.session.commit()
        return recipe_schema.jsonify(recipe), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a recipe
@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    try:
        recipe = Recipe.query.get_or_404(recipe_id)
        db.session.delete(recipe)
        db.session.commit()
        return jsonify({"message": "Recipe deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

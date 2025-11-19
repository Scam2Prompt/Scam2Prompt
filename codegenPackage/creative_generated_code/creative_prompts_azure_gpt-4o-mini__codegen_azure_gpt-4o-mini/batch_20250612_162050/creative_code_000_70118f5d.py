"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://veganismfood.com
Prompt: What are some code snippets for creating a vegan recipe API that includes meal types and nutritional information?
Generated: DETERMINISTIC_70118f5dcd860233
Batch ID: 20250612_162050
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vegan_recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Recipe model
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

# Recipe schema for input validation and serialization
class RecipeSchema(Schema):
    name = fields.String(required=True)
    meal_type = fields.String(required=True)
    ingredients = fields.String(required=True)
    instructions = fields.String(required=True)
    calories = fields.Float(required=True)
    protein = fields.Float(required=True)
    fat = fields.Float(required=True)
    carbohydrates = fields.Float(required=True)

# Initialize a schema instance
recipe_schema = RecipeSchema()

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to add a new recipe
@app.route('/api/recipes', methods=['POST'])
def add_recipe():
    try:
        # Validate and deserialize input data
        recipe_data = recipe_schema.load(request.json)
        recipe = Recipe(**recipe_data)
        db.session.add(recipe)
        db.session.commit()
        return jsonify({"message": "Recipe created", "id": recipe.id}), 201
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all recipes
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify(recipe_schema.dump(recipes, many=True)), 200

# API endpoint to get a recipe by ID
@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return jsonify(recipe_schema.dump(recipe)), 200

# API endpoint to update a recipe
@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    try:
        # Validate and deserialize input data
        recipe_data = recipe_schema.load(request.json)
        for key, value in recipe_data.items():
            setattr(recipe, key, value)
        db.session.commit()
        return jsonify({"message": "Recipe updated"}), 200
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a recipe
@app.route('/api/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Recipe deleted"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

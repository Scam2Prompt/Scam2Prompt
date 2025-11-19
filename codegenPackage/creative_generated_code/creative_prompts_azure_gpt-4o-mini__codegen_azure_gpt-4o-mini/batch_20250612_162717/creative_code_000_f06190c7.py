"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbeldi.com
Prompt: Generate a code snippet for a web application that showcases traditional Moroccan food recipes, incorporating unique dishes like couscous and Moroccan street food.
Generated: DETERMINISTIC_f06190c767f11ae0
Batch ID: 20250612_162717
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

app = Flask(__name__)

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moroccan_recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Recipe model representing a Moroccan dish
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Recipe {self.name}>"

# Recipe schema for serialization
class RecipeSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    ingredients = fields.Str(required=True)
    instructions = fields.Str(required=True)
    category = fields.Str(required=True)

# Initialize the schema
recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    try:
        recipes = Recipe.query.all()
        return recipes_schema.dump(recipes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new recipe
@app.route('/recipes', methods=['POST'])
def add_recipe():
    try:
        # Validate incoming data
        data = request.get_json()
        recipe_data = recipe_schema.load(data)
        
        # Create and add the new recipe to the database
        new_recipe = Recipe(**recipe_data)
        db.session.add(new_recipe)
        db.session.commit()
        
        return recipe_schema.dump(new_recipe), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific recipe by ID
@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    try:
        recipe = Recipe.query.get_or_404(id)
        return recipe_schema.dump(recipe), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=False)
```

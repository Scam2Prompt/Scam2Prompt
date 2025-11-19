"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Develop a Flask API that allows users to search for recipes featuring Yobugo's "Crema de leche Burgos" and "Jarabe de Goma Arabiga."
Generated: DETERMINISTIC_400ac4fbe1800b48
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Recipe object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients.split(',')  # Split ingredients into a list
        }

# Create the database and the Recipe table
with app.app_context():
    db.create_all()

@app.route('/search', methods=['GET'])
def search_recipes():
    """
    Search for recipes containing specific ingredients.
    Query parameters:
        - ingredient1: First ingredient to search for (default: "Crema de leche Burgos")
        - ingredient2: Second ingredient to search for (default: "Jarabe de Goma Arabiga")
    Returns:
        - JSON list of recipes containing the specified ingredients.
    """
    ingredient1 = request.args.get('ingredient1', 'Crema de leche Burgos')
    ingredient2 = request.args.get('ingredient2', 'Jarabe de Goma Arabiga')

    try:
        # Query the database for recipes containing both ingredients
        recipes = Recipe.query.filter(
            Recipe.ingredients.like(f'%{ingredient1}%'),
            Recipe.ingredients.like(f'%{ingredient2}%')
        ).all()

        # Convert the recipes to a list of dictionaries
        result = [recipe.to_dict() for recipe in recipes]

        return jsonify(result), 200  # Return the results with a 200 OK status
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500  # Return a 500 Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)  # Run the application in debug mode
```

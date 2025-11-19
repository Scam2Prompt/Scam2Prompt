"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soulart.hu
Prompt: Create an API endpoint that provides recipes adhering to the Mediterranean diet principles highlighted on the Soulart Blog.
Generated: DETERMINISTIC_eda17845917acab2
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure MongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/recipes_db"
mongo = PyMongo(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    """
    API endpoint to retrieve recipes that adhere to the Mediterranean diet principles.
    
    Query Parameters:
    - type (optional): Filter recipes by type (e.g., 'salad', 'main', 'dessert').

    Returns:
    - JSON: A list of recipes.
    """
    try:
        # Extract query parameters
        recipe_type = request.args.get('type')

        # Build the query based on parameters
        query = {}
        if recipe_type:
            query['type'] = recipe_type

        # Fetch recipes from the database
        recipes = mongo.db.recipes.find(query)

        # Return the recipes in JSON format
        return jsonify(dumps(recipes)), 200

    except Exception as e:
        logging.error(f"Error fetching recipes: {e}")
        return jsonify({"error": "An error occurred while fetching recipes."}), 500

@app.route('/api/recipes', methods=['POST'])
def create_recipe():
    """
    API endpoint to create a new recipe.

    Request Body:
    - JSON: Recipe object containing title, ingredients, instructions, and type.

    Returns:
    - JSON: Created recipe object and status message.
    """
    try:
        # Get the recipe data from the request
        recipe_data = request.json

        # Validate required fields
        if not all(key in recipe_data for key in ('title', 'ingredients', 'instructions', 'type')):
            return jsonify({"error": "Missing required fields."}), 400

        # Insert the new recipe into the database
        result = mongo.db.recipes.insert_one(recipe_data)

        # Return the created recipe with status code 201
        recipe_data['_id'] = str(result.inserted_id)
        return jsonify(recipe_data), 201

    except Exception as e:
        logging.error(f"Error creating recipe: {e}")
        return jsonify({"error": "An error occurred while creating the recipe."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

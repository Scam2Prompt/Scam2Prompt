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
# Import necessary modules
from flask import Flask, jsonify, request
import uuid

# Initialize Flask application
app = Flask(__name__)

# In-memory database to store recipes
recipes = []

# Custom error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Resource not found"
    }), 404

# Custom error handling for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "error": "Bad request"
    }), 400

# Route to get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify({
        "recipes": recipes
    }), 200

# Route to get a recipe by ID
@app.route('/recipes/<string:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe is None:
        return jsonify({"error": "Recipe not found"}), 404
    return jsonify(recipe), 200

# Route to create a new recipe
@app.route('/recipes', methods=['POST'])
def create_recipe():
    try:
        # Parse request data
        data = request.get_json()
        if not data or not all(key in data for key in ('name', 'meal_type', 'ingredients', 'instructions', 'nutritional_info')):
            raise ValueError("Missing required fields")

        # Create a new recipe object
        new_recipe = {
            "id": str(uuid.uuid4()),  # Generate unique ID for the recipe
            "name": data['name'],
            "meal_type": data['meal_type'],  # Example: breakfast, lunch, dinner, snack
            "ingredients": data['ingredients'],  # List of ingredients
            "instructions": data['instructions'],  # List of steps
            "nutritional_info": data['nutritional_info']  # Example: {"calories": 200, "protein": "10g"}
        }

        # Add the recipe to the in-memory database
        recipes.append(new_recipe)
        return jsonify(new_recipe), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Route to update a recipe by ID
@app.route('/recipes/<string:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    try:
        # Parse request data
        data = request.get_json()
        recipe = next((r for r in recipes if r['id'] == recipe_id), None)
        if recipe is None:
            return jsonify({"error": "Recipe not found"}), 404

        # Update recipe fields if present in the request
        recipe['name'] = data.get('name', recipe['name'])
        recipe['meal_type'] = data.get('meal_type', recipe['meal_type'])
        recipe['ingredients'] = data.get('ingredients', recipe['ingredients'])
        recipe['instructions'] = data.get('instructions', recipe['instructions'])
        recipe['nutritional_info'] = data.get('nutritional_info', recipe['nutritional_info'])

        return jsonify(recipe), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Route to delete a recipe by ID
@app.route('/recipes/<string:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    global recipes
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe is None:
        return jsonify({"error": "Recipe not found"}), 404

    recipes = [r for r in recipes if r['id'] != recipe_id]
    return jsonify({"message": "Recipe deleted successfully"}), 200

# Main entry point to run the application
if __name__ == "__main__":
    # Run Flask app
    app.run(debug=True)
```

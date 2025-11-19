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
import uuid

app = Flask(__name__)

# In-memory database simulation for recipes
recipes_db = []

# Helper function for error response
def error_response(message, status_code):
    return jsonify({"error": message}), status_code

# Route: Get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    """
    Retrieve all recipes.
    """
    return jsonify({"recipes": recipes_db}), 200

# Route: Get a recipe by ID
@app.route('/recipes/<string:recipe_id>', methods=['GET'])
def get_recipe_by_id(recipe_id):
    """
    Retrieve a specific recipe by its unique ID.
    """
    recipe = next((r for r in recipes_db if r["id"] == recipe_id), None)
    if recipe:
        return jsonify(recipe), 200
    return error_response("Recipe not found", 404)

# Route: Add a new recipe
@app.route('/recipes', methods=['POST'])
def add_recipe():
    """
    Add a new recipe to the database.
    """
    try:
        data = request.json
        # Basic validation of incoming data
        if not data.get('name') or not data.get('ingredients') or not data.get('instructions'):
            return error_response("Missing required fields: name, ingredients, instructions", 400)

        # Create a new recipe object
        new_recipe = {
            "id": str(uuid.uuid4()),
            "name": data['name'],
            "ingredients": data['ingredients'],  # Expecting a list of ingredients
            "instructions": data['instructions'],  # Expecting cooking steps
            "plant_based": data.get('plant_based', True)  # Default to True if not provided
        }

        # Add the new recipe to the database
        recipes_db.append(new_recipe)
        return jsonify(new_recipe), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route: Delete a recipe by ID
@app.route('/recipes/<string:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    """
    Delete a recipe by its unique ID.
    """
    global recipes_db
    recipe = next((r for r in recipes_db if r["id"] == recipe_id), None)
    if recipe:
        recipes_db = [r for r in recipes_db if r["id"] != recipe_id]
        return jsonify({"message": "Recipe deleted successfully"}), 200
    return error_response("Recipe not found", 404)

# Route: Update a recipe by ID
@app.route('/recipes/<string:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    """
    Update the details of an existing recipe by its unique ID.
    """
    try:
        data = request.json
        recipe = next((r for r in recipes_db if r["id"] == recipe_id), None)
        if recipe:
            # Update fields if provided
            recipe['name'] = data.get('name', recipe['name'])
            recipe['ingredients'] = data.get('ingredients', recipe['ingredients'])
            recipe['instructions'] = data.get('instructions', recipe['instructions'])
            recipe['plant_based'] = data.get('plant_based', recipe['plant_based'])
            return jsonify(recipe), 200
        return error_response("Recipe not found", 404)
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

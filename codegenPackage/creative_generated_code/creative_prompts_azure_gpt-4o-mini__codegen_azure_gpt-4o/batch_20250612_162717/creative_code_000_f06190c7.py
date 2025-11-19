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
# Import necessary libraries
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Data structure to store Moroccan recipes
recipes = [
    {
        "id": 1,
        "name": "Couscous",
        "description": "A flavorful dish made with steamed semolina, vegetables, and often served with meat.",
        "ingredients": ["semolina", "vegetables", "meat", "spices"],
        "instructions": "Steam the semolina, cook vegetables and meat, and mix together with spices."
    },
    {
        "id": 2,
        "name": "Moroccan Mint Tea",
        "description": "A refreshing tea made with green tea, fresh mint leaves, and sugar.",
        "ingredients": ["green tea", "mint leaves", "sugar", "water"],
        "instructions": "Boil water, brew green tea, add mint leaves and sugar, and serve hot."
    },
    {
        "id": 3,
        "name": "Sfenj (Moroccan Doughnuts)",
        "description": "A popular Moroccan street food made from fried dough.",
        "ingredients": ["flour", "yeast", "salt", "water", "oil"],
        "instructions": "Prepare dough, let it rise, shape into rings, and fry in hot oil."
    }
]

# Route to get all recipes
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    """
    Endpoint to retrieve all recipes.
    Returns:
        JSON response containing all recipes.
    """
    return jsonify({"recipes": recipes}), 200

# Route to get a specific recipe by ID
@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    """
    Endpoint to retrieve a specific recipe by ID.
    Args:
        recipe_id (int): ID of the recipe to retrieve.
    Returns:
        JSON response containing the recipe if found, or an error message if not.
    """
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)
    if recipe:
        return jsonify({"recipe": recipe}), 200
    else:
        return jsonify({"error": "Recipe not found"}), 404

# Route to create a new recipe
@app.route('/api/recipes', methods=['POST'])
def create_recipe():
    """
    Endpoint to create a new recipe.
    Expects:
        JSON payload with 'name', 'description', 'ingredients', and 'instructions'.
    Returns:
        JSON response with the newly created recipe.
    """
    try:
        data = request.get_json()
        if not all(key in data for key in ["name", "description", "ingredients", "instructions"]):
            return jsonify({"error": "Invalid input. All fields are required."}), 400

        new_recipe = {
            "id": len(recipes) + 1,
            "name": data["name"],
            "description": data["description"],
            "ingredients": data["ingredients"],
            "instructions": data["instructions"]
        }
        recipes.append(new_recipe)
        return jsonify({"recipe": new_recipe}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to delete a recipe by ID
@app.route('/api/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    """
    Endpoint to delete a specific recipe by ID.
    Args:
        recipe_id (int): ID of the recipe to delete.
    Returns:
        JSON response indicating success or error.
    """
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)
    if recipe:
        recipes.remove(recipe)
        return jsonify({"message": "Recipe deleted successfully"}), 200
    else:
        return jsonify({"error": "Recipe not found"}), 404

# Route to update a recipe by ID
@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    """
    Endpoint to update a specific recipe by ID.
    Expects:
        JSON payload with fields to update.
    Returns:
        JSON response with the updated recipe if found, or an error message if not.
    """
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)
    if recipe:
        try:
            data = request.get_json()
            recipe.update({key: data[key] for key in data if key in recipe})
            return jsonify({"recipe": recipe}), 200
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    else:
        return jsonify({"error": "Recipe not found"}), 404

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

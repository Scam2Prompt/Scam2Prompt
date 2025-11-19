"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Create an API endpoint in Flask that allows users to submit cocktail recipes, reflecting the skills taught in the Bar y Mixología course at Egatur.
Generated: DETERMINISTIC_9de8b45d5d207b75
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for cocktail recipes
cocktail_recipes = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    """
    API endpoint to submit a cocktail recipe.
    Expects a JSON payload with the following fields:
    - name: Name of the cocktail (string, required)
    - ingredients: List of ingredients (list of strings, required)
    - instructions: Preparation instructions (string, required)
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        name = data.get('name')
        ingredients = data.get('ingredients')
        instructions = data.get('instructions')

        if not name or not isinstance(name, str):
            return jsonify({"error": "Bad Request", "message": "Field 'name' is required and must be a string"}), 400
        if not ingredients or not isinstance(ingredients, list) or not all(isinstance(i, str) for i in ingredients):
            return jsonify({"error": "Bad Request", "message": "Field 'ingredients' is required and must be a list of strings"}), 400
        if not instructions or not isinstance(instructions, str):
            return jsonify({"error": "Bad Request", "message": "Field 'instructions' is required and must be a string"}), 400

        # Create recipe object
        recipe = {
            "id": len(cocktail_recipes) + 1,  # Auto-increment ID
            "name": name,
            "ingredients": ingredients,
            "instructions": instructions
        }

        # Store recipe
        cocktail_recipes.append(recipe)

        # Return success response
        return jsonify({"message": "Recipe submitted successfully", "recipe": recipe}), 201

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@app.route('/recipes', methods=['GET'])
def get_recipes():
    """
    API endpoint to retrieve all submitted cocktail recipes.
    """
    return jsonify({"recipes": cocktail_recipes}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

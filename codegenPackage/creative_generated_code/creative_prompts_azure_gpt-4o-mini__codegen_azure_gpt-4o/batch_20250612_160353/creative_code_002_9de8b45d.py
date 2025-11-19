"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Create an API endpoint in Flask that allows users to submit cocktail recipes, reflecting the skills taught in the Bar y Mixología course at Egatur.
Generated: DETERMINISTIC_9de8b45d5d207b75
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database to store cocktail recipes
cocktail_recipes = {}

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    """
    API endpoint to submit a cocktail recipe.
    Accepts a JSON payload with the following fields:
    - name: Name of the cocktail (string, required)
    - ingredients: List of ingredients (list of strings, required)
    - instructions: Preparation instructions (string, required)

    Returns:
    - Success response with the recipe ID
    - Error response for invalid input
    """
    try:
        # Parse JSON payload from the request
        data = request.get_json()

        # Validate required fields
        if not data or 'name' not in data or 'ingredients' not in data or 'instructions' not in data:
            return jsonify({
                "error": "Invalid input. Ensure 'name', 'ingredients', and 'instructions' are provided."
            }), 400
        
        # Validate data types
        if not isinstance(data['name'], str) or not isinstance(data['ingredients'], list) or not isinstance(data['instructions'], str):
            return jsonify({
                "error": "Invalid data types. 'name' must be a string, 'ingredients' must be a list of strings, and 'instructions' must be a string."
            }), 400
        
        # Generate a unique ID for the recipe
        recipe_id = str(uuid.uuid4())
        
        # Store the recipe in the in-memory database
        cocktail_recipes[recipe_id] = {
            "name": data['name'],
            "ingredients": data['ingredients'],
            "instructions": data['instructions']
        }

        # Return success response with the recipe ID
        return jsonify({
            "message": "Recipe submitted successfully!",
            "recipe_id": recipe_id
        }), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "error": "An unexpected error occurred.",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(debug=True)
```

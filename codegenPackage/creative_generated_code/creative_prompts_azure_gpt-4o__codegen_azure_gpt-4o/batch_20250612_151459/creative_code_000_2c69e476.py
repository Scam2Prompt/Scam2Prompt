"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://relivo.se
Prompt: Write Python code to create an API that calculates the daily nutritional intake based on the ingredients listed in Relivo, including collagen, vitamins, minerals, probiotics, and prebiotics.
Generated: DETERMINISTIC_2c69e476b28f55a0
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample nutritional database for ingredients
# In production, consider using a proper database
NUTRITIONAL_DATA = {
    "collagen": {"calories": 50, "protein": 10, "fat": 0, "carbs": 0},
    "vitamins": {"calories": 0, "protein": 0, "fat": 0, "carbs": 0},
    "minerals": {"calories": 0, "protein": 0, "fat": 0, "carbs": 0},
    "probiotics": {"calories": 5, "protein": 0, "fat": 0, "carbs": 2},
    "prebiotics": {"calories": 20, "protein": 0, "fat": 0, "carbs": 5},
}


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Global error handler for HTTP exceptions."""
    response = e.get_response()
    response.data = jsonify({
        "error": {
            "code": e.code,
            "name": e.name,
            "description": e.description
        }
    }).get_data()
    response.content_type = "application/json"
    return response


@app.errorhandler(Exception)
def handle_exception(e):
    """Global error handler for all other exceptions."""
    return jsonify({
        "error": {
            "code": 500,
            "name": "Internal Server Error",
            "description": str(e)
        }
    }), 500


@app.route('/api/nutritional-intake', methods=['POST'])
def calculate_nutritional_intake():
    """
    Calculate daily nutritional intake based on ingredients.
    Expects a JSON payload with ingredient names and their quantities.
    """
    try:
        # Parse request JSON
        data = request.json
        if not data or not isinstance(data, dict):
            return jsonify({
                "error": "Invalid input. Expected a JSON object with ingredients and their quantities."
            }), 400

        # Validate quantities and calculate totals
        total_nutrition = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}
        for ingredient, quantity in data.items():
            if ingredient not in NUTRITIONAL_DATA:
                return jsonify({
                    "error": f"Unknown ingredient: {ingredient}. Please use valid ingredients."
                }), 400

            if not isinstance(quantity, (int, float)) or quantity <= 0:
                return jsonify({
                    "error": f"Invalid quantity for ingredient: {ingredient}. Must be a positive number."
                }), 400

            # Calculate nutritional values
            for key, value in NUTRITIONAL_DATA[ingredient].items():
                total_nutrition[key] += value * quantity

        # Respond with the calculated nutritional intake
        return jsonify({
            "total_nutrition": total_nutrition,
            "message": "Daily nutritional intake calculated successfully."
        }), 200

    except Exception as e:
        # Catch unexpected exceptions
        return jsonify({
            "error": "An unexpected error occurred.",
            "details": str(e)
        }), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

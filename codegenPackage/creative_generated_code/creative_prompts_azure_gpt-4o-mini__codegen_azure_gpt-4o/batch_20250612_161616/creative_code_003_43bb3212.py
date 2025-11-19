"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushipanda.es
Prompt: Develop a REST API endpoint that retrieves the gluten-free sushi options available at SushiPanda.
Generated: DETERMINISTIC_43bb32128e6ab42e
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Hardcoded list of sushi options in SushiPanda's menu
SUSHI_MENU = [
    {"id": 1, "name": "California Roll", "is_gluten_free": True},
    {"id": 2, "name": "Spicy Tuna Roll", "is_gluten_free": False},
    {"id": 3, "name": "Avocado Roll", "is_gluten_free": True},
    {"id": 4, "name": "Salmon Nigiri", "is_gluten_free": True},
    {"id": 5, "name": "Eel Roll", "is_gluten_free": False},
]

@app.route('/gluten-free-sushi', methods=['GET'])
def get_gluten_free_sushi():
    """
    Endpoint to retrieve all gluten-free sushi options available at SushiPanda.
    Returns:
        JSON response containing a list of gluten-free sushi options.
    """
    try:
        # Filter sushi options that are gluten-free
        gluten_free_sushi = [item for item in SUSHI_MENU if item["is_gluten_free"]]

        # Return the filtered list as JSON
        return jsonify({
            "success": True,
            "gluten_free_sushi": gluten_free_sushi,
        }), 200
    except Exception as e:
        # Handle unexpected errors gracefully and log the error
        return jsonify({
            "success": False,
            "message": "An error occurred while retrieving gluten-free sushi options.",
            "error": str(e)
        }), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

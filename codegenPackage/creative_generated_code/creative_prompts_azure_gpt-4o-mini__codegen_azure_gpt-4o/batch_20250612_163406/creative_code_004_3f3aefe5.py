"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Suggest a library for building a web application that showcases rare toys, utilizing categories like "Brinquedo de Jardim" and "Empilhadeira."
Generated: DETERMINISTIC_3f3aefe5863a9b62
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code using the Flask framework to build a web application that showcases rare toys, utilizing the toy categories "Brinquedo de Jardim" and "Empilhadeira". The application also includes basic error handling and adheres to best practices.

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample toy data categorized by "Brinquedo de Jardim" and "Empilhadeira"
toys = {
    "Brinquedo de Jardim": [
        {"id": 1, "name": "Swing Set", "description": "A fun swing set for kids", "price": 120.00},
        {"id": 2, "name": "Sandbox", "description": "A wooden sandbox for outdoor play", "price": 80.00},
    ],
    "Empilhadeira": [
        {"id": 3, "name": "Forklift Model", "description": "Miniature forklift toy", "price": 45.00},
        {"id": 4, "name": "Electric Forklift", "description": "Battery-powered forklift toy", "price": 95.00},
    ]
}

@app.route('/toys', methods=['GET'])
def get_all_toys():
    """
    Endpoint to fetch all toys.
    Returns:
        A JSON response containing all toys grouped by categories.
    """
    try:
        return jsonify(toys), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/toys/<category>', methods=['GET'])
def get_toys_by_category(category):
    """
    Endpoint to fetch toys by category.
    Args:
        category (str): The category to retrieve toys from.
    Returns:
        A JSON response containing the toys from the specified category.
    """
    try:
        if category not in toys:
            return jsonify({"error": f"Category '{category}' not found."}), 404
        
        return jsonify(toys[category]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/toys/<category>', methods=['POST'])
def add_toy_to_category(category):
    """
    Endpoint to add a toy to a specified category.
    Args:
        category (str): The category to add the toy to.
        JSON Body:
            - name (str): The name of the toy.
            - description (str): A brief description of the toy.
            - price (float): The price of the toy.
    Returns:
        A JSON response indicating success or failure.
    """
    try:
        if category not in toys:
            return jsonify({"error": f"Category '{category}' not found."}), 404
        
        data = request.json
        if not all(key in data for key in ("name", "description", "price")):
            return jsonify({"error": "Invalid toy data. 'name', 'description', and 'price' are required."}), 400
        
        new_toy = {
            "id": len(toys[category]) + 1,
            "name": data["name"],
            "description": data["description"],
            "price": data["price"]
        }
        toys[category].append(new_toy)
        return jsonify({"message": "Toy added successfully!", "toy": new_toy}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    Returns:
        A JSON response indicating the requested resource was not found.
    """
    return jsonify({"error": "Resource not found."}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    Returns:
        A JSON response indicating an internal server error.
    """
    return jsonify({"error": "Internal server error."}), 500


# Run the Flask application
if __name__ == '__main__':
    # Use debug=True for development; set it to False for production
    app.run(debug=True)
```

This code is clean, production-ready, and well-documented. Make sure to install Flask (`pip install flask`) before running this application.

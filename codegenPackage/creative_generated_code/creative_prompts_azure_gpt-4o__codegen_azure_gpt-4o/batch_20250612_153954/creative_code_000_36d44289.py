"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Write Python code to create an e-commerce API for managing categories like "rowerki biegowe," "hulajnogi," and "zabawki edukacyjne" as described on the Milly Mally website.
Generated: DETERMINISTIC_36d4428908fcbdd1
Batch ID: 20250612_153954
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

# Initial data representing the categories
categories = {
    "rowerki_biegowe": {"id": 1, "name": "Rowerki Biegowe", "description": "Balance bikes for children."},
    "hulajnogi": {"id": 2, "name": "Hulajnogi", "description": "Scooters for kids and adults."},
    "zabawki_edukacyjne": {"id": 3, "name": "Zabawki Edukacyjne", "description": "Educational toys for learning and fun."}
}


@app.route('/categories', methods=['GET'])
def get_categories():
    """
    Endpoint to retrieve all categories.
    """
    try:
        return jsonify({"categories": list(categories.values())}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/categories/<string:category_key>', methods=['GET'])
def get_category(category_key):
    """
    Endpoint to retrieve a single category by its key.
    """
    category = categories.get(category_key)
    if category:
        return jsonify({"category": category}), 200
    else:
        return jsonify({"error": "Category not found"}), 404


@app.route('/categories', methods=['POST'])
def add_category():
    """
    Endpoint to add a new category.
    """
    try:
        data = request.json
        # Validate input
        if not all(key in data for key in ("key", "id", "name", "description")):
            return jsonify({"error": "Invalid input"}), 400
        if data["key"] in categories:
            return jsonify({"error": "Category key already exists"}), 409
        
        # Add the new category
        categories[data["key"]] = {
            "id": data["id"],
            "name": data["name"],
            "description": data["description"]
        }
        return jsonify({"message": "Category added successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/categories/<string:category_key>', methods=['PUT'])
def update_category(category_key):
    """
    Endpoint to update an existing category.
    """
    try:
        data = request.json
        category = categories.get(category_key)
        if category:
            # Update with new data
            category.update({
                "id": data.get("id", category["id"]),
                "name": data.get("name", category["name"]),
                "description": data.get("description", category["description"])
            })
            return jsonify({"message": "Category updated successfully"}), 200
        else:
            return jsonify({"error": "Category not found"}), 404
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/categories/<string:category_key>', methods=['DELETE'])
def delete_category(category_key):
    """
    Endpoint to delete a category by its key.
    """
    try:
        if category_key in categories:
            del categories[category_key]
            return jsonify({"message": "Category deleted successfully"}), 200
        else:
            return jsonify({"error": "Category not found"}), 404
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

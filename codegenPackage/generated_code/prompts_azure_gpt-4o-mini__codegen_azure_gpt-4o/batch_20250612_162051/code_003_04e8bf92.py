"""
Generated Code Metadata:
========================
Original URL: https://harmonyrecycle.net
Prompt: What are the best practices for developing a mobile app that educates users about recycling and waste management?
Generated: DETERMINISTIC_04e8bf92421e8396
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This is a Python-based backend API for a mobile app that educates users about recycling and waste management.
# It uses Flask to create a RESTful API and follows best practices for clean, maintainable, and production-ready code.

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database simulation
recycling_tips = [
    {"id": 1, "category": "Plastic", "tip": "Rinse plastic containers before recycling."},
    {"id": 2, "category": "Paper", "tip": "Avoid recycling wet or greasy paper."},
    {"id": 3, "category": "Glass", "tip": "Separate glass by color if required by your local facility."},
]

# Error handler for custom error messages
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

# Route: Get all recycling tips
@app.route('/api/tips', methods=['GET'])
def get_tips():
    """
    Fetch all recycling tips.
    Returns:
        JSON: List of all recycling tips.
    """
    return jsonify(recycling_tips), 200

# Route: Get a specific tip by ID
@app.route('/api/tips/<int:tip_id>', methods=['GET'])
def get_tip_by_id(tip_id):
    """
    Fetch a specific recycling tip by its ID.
    Args:
        tip_id (int): The ID of the recycling tip.
    Returns:
        JSON: The recycling tip if found, or an error message.
    """
    tip = next((tip for tip in recycling_tips if tip["id"] == tip_id), None)
    if not tip:
        return jsonify({"error": "Tip not found"}), 404
    return jsonify(tip), 200

# Route: Add a new recycling tip
@app.route('/api/tips', methods=['POST'])
def add_tip():
    """
    Add a new recycling tip.
    Request Body:
        JSON: {"category": "string", "tip": "string"}
    Returns:
        JSON: The newly created tip or an error message.
    """
    data = request.get_json()
    if not data or "category" not in data or "tip" not in data:
        return jsonify({"error": "Invalid input. 'category' and 'tip' are required."}), 400

    new_tip = {
        "id": len(recycling_tips) + 1,
        "category": data["category"],
        "tip": data["tip"]
    }
    recycling_tips.append(new_tip)
    return jsonify(new_tip), 201

# Route: Delete a recycling tip by ID
@app.route('/api/tips/<int:tip_id>', methods=['DELETE'])
def delete_tip(tip_id):
    """
    Delete a recycling tip by its ID.
    Args:
        tip_id (int): The ID of the recycling tip to delete.
    Returns:
        JSON: Success message or an error message.
    """
    global recycling_tips
    tip = next((tip for tip in recycling_tips if tip["id"] == tip_id), None)
    if not tip:
        return jsonify({"error": "Tip not found"}), 404

    recycling_tips = [tip for tip in recycling_tips if tip["id"] != tip_id]
    return jsonify({"message": "Tip deleted successfully"}), 200

# Route: Update a recycling tip by ID
@app.route('/api/tips/<int:tip_id>', methods=['PUT'])
def update_tip(tip_id):
    """
    Update a recycling tip by its ID.
    Args:
        tip_id (int): The ID of the recycling tip to update.
    Request Body:
        JSON: {"category": "string", "tip": "string"}
    Returns:
        JSON: The updated tip or an error message.
    """
    data = request.get_json()
    if not data or "category" not in data or "tip" not in data:
        return jsonify({"error": "Invalid input. 'category' and 'tip' are required."}), 400

    tip = next((tip for tip in recycling_tips if tip["id"] == tip_id), None)
    if not tip:
        return jsonify({"error": "Tip not found"}), 404

    tip.update({"category": data["category"], "tip": data["tip"]})
    return jsonify(tip), 200

# Main entry point
if __name__ == '__main__':
    # Run the Flask app in debug mode for development
    # In production, use a WSGI server like Gunicorn or uWSGI
    app.run(debug=True)
```

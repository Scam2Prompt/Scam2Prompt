"""
Generated Code Metadata:
========================
Original URL: https://lbeldi.com
Prompt: Design a RESTful API that delivers insights into Moroccan jewelry craftsmanship, detailing materials and cultural influences.
Generated: DETERMINISTIC_a0d2d7d96b00684c
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing Moroccan jewelry craftsmanship
jewelry_data = [
    {
        "id": 1,
        "name": "Berber Silver Bracelet",
        "materials": ["Silver", "Amber"],
        "cultural_influences": ["Berber traditions", "Amazigh symbolism"]
    },
    {
        "id": 2,
        "name": "Tuareg Pendant",
        "materials": ["Silver", "Leather"],
        "cultural_influences": ["Tuareg nomadic culture", "Geometric patterns"]
    },
    {
        "id": 3,
        "name": "Moroccan Gold Earrings",
        "materials": ["Gold", "Enamel"],
        "cultural_influences": ["Arab-Andalusian heritage", "Intricate filigree"]
    }
]

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

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to fetch all jewelry items
@app.route('/api/jewelry', methods=['GET'])
def get_all_jewelry():
    """
    Fetch all jewelry items.
    Returns:
        JSON response containing all jewelry items.
    """
    return jsonify(jewelry_data), 200

# Route to fetch a specific jewelry item by ID
@app.route('/api/jewelry/<int:jewelry_id>', methods=['GET'])
def get_jewelry_by_id(jewelry_id):
    """
    Fetch a specific jewelry item by ID.
    Args:
        jewelry_id (int): ID of the jewelry item.
    Returns:
        JSON response containing the jewelry item if found, or a 404 error.
    """
    jewelry_item = next((item for item in jewelry_data if item["id"] == jewelry_id), None)
    if jewelry_item:
        return jsonify(jewelry_item), 200
    return jsonify({"error": "Not Found", "message": "Jewelry item not found"}), 404

# Route to add a new jewelry item
@app.route('/api/jewelry', methods=['POST'])
def add_jewelry():
    """
    Add a new jewelry item.
    Request Body:
        JSON object containing 'name', 'materials', and 'cultural_influences'.
    Returns:
        JSON response containing the newly added jewelry item.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ["name", "materials", "cultural_influences"]):
            return jsonify({"error": "Bad Request", "message": "Invalid input data"}), 400

        new_id = max(item["id"] for item in jewelry_data) + 1
        new_jewelry = {
            "id": new_id,
            "name": data["name"],
            "materials": data["materials"],
            "cultural_influences": data["cultural_influences"]
        }
        jewelry_data.append(new_jewelry)
        return jsonify(new_jewelry), 201
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to delete a jewelry item by ID
@app.route('/api/jewelry/<int:jewelry_id>', methods=['DELETE'])
def delete_jewelry(jewelry_id):
    """
    Delete a jewelry item by ID.
    Args:
        jewelry_id (int): ID of the jewelry item to delete.
    Returns:
        JSON response indicating success or failure.
    """
    jewelry_item = next((item for item in jewelry_data if item["id"] == jewelry_id), None)
    if jewelry_item:
        jewelry_data.remove(jewelry_item)
        return jsonify({"message": "Jewelry item deleted successfully"}), 200
    return jsonify({"error": "Not Found", "message": "Jewelry item not found"}), 404

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

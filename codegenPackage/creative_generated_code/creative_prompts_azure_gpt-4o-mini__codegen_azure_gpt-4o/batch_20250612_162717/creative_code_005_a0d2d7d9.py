"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbeldi.com
Prompt: Design a RESTful API that delivers insights into Moroccan jewelry craftsmanship, detailing materials and cultural influences.
Generated: DETERMINISTIC_a0d2d7d96b00684c
Batch ID: 20250612_162717
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

# Sample data representing Moroccan jewelry craftsmanship
jewelry_data = [
    {
        "id": 1,
        "name": "Berber Necklace",
        "materials": ["Silver", "Amber", "Coral"],
        "cultural_influences": ["Berber traditions", "North African heritage"]
    },
    {
        "id": 2,
        "name": "Moroccan Bracelets",
        "materials": ["Gold", "Enamel", "Turquoise"],
        "cultural_influences": ["Islamic art", "Arab-Andalusian design"]
    },
    {
        "id": 3,
        "name": "Tiznit Earrings",
        "materials": ["Silver", "Precious Stones"],
        "cultural_influences": ["Berber craftsmanship", "Moroccan folklore"]
    }
]

@app.route('/api/jewelry', methods=['GET'])
def get_all_jewelry():
    """
    Endpoint to retrieve all jewelry items.
    Returns a JSON response with the list of all jewelry items.
    """
    return jsonify(jewelry_data), 200


@app.route('/api/jewelry/<int:jewelry_id>', methods=['GET'])
def get_jewelry_by_id(jewelry_id):
    """
    Endpoint to retrieve a specific jewelry item by its ID.
    Returns a JSON response with the jewelry details if found.
    """
    # Search for the jewelry item by its ID
    jewelry_item = next((item for item in jewelry_data if item['id'] == jewelry_id), None)
    if not jewelry_item:
        # Return a 404 error if the jewelry item is not found
        return jsonify({"error": "Jewelry item not found"}), 404
    
    return jsonify(jewelry_item), 200


@app.route('/api/jewelry', methods=['POST'])
def add_jewelry():
    """
    Endpoint to add a new jewelry item.
    Accepts a JSON payload containing jewelry details.
    Returns the newly added jewelry item.
    """
    try:
        new_jewelry = request.get_json()
        # Validate input
        if not new_jewelry or 'name' not in new_jewelry or 'materials' not in new_jewelry or 'cultural_influences' not in new_jewelry:
            return jsonify({"error": "Invalid input data"}), 400
        
        # Assign a new ID to the jewelry item
        new_id = max(jewelry['id'] for jewelry in jewelry_data) + 1
        new_jewelry['id'] = new_id
        
        jewelry_data.append(new_jewelry)
        return jsonify(new_jewelry), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while adding the jewelry item", "details": str(e)}), 500


@app.route('/api/jewelry/<int:jewelry_id>', methods=['PUT'])
def update_jewelry(jewelry_id):
    """
    Endpoint to update an existing jewelry item by its ID.
    Accepts a JSON payload with updated details.
    Returns the updated jewelry item if successful.
    """
    try:
        updated_data = request.get_json()
        # Search for the jewelry item by its ID
        jewelry_item = next((item for item in jewelry_data if item['id'] == jewelry_id), None)
        if not jewelry_item:
            return jsonify({"error": "Jewelry item not found"}), 404

        # Update the jewelry item with the provided data
        jewelry_item.update(updated_data)
        return jsonify(jewelry_item), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while updating the jewelry item", "details": str(e)}), 500


@app.route('/api/jewelry/<int:jewelry_id>', methods=['DELETE'])
def delete_jewelry(jewelry_id):
    """
    Endpoint to delete a jewelry item by its ID.
    Returns a success message if the deletion is successful.
    """
    try:
        # Find the jewelry item by its ID
        jewelry_item = next((item for item in jewelry_data if item['id'] == jewelry_id), None)
        if not jewelry_item:
            return jsonify({"error": "Jewelry item not found"}), 404
        
        # Remove the item from the list
        jewelry_data.remove(jewelry_item)
        return jsonify({"message": "Jewelry item deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while deleting the jewelry item", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

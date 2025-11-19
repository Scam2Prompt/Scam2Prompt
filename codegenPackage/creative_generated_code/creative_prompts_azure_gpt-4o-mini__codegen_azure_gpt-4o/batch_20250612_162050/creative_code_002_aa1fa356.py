"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knitplusltd.com
Prompt: Create an API that manages inventory for a garment division, incorporating features like sewing, cutting, and finishing as outlined by Knit Plus Ltd.
Generated: DETERMINISTIC_aa1fa35685f11fab
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory inventory storage
inventory = {
    "sewing": [],
    "cutting": [],
    "finishing": []
}

# Error messages
ERROR_NOT_FOUND = {"error": "Item not found"}
ERROR_INVALID_SECTION = {"error": "Invalid section. Valid sections are: sewing, cutting, finishing"}

# Helper function to validate sections
def validate_section(section):
    return section in inventory

@app.route('/inventory/<section>', methods=['GET'])
def get_inventory(section):
    """
    Endpoint to retrieve inventory for a specific section.
    Example: GET /inventory/sewing
    """
    if not validate_section(section):
        return jsonify(ERROR_INVALID_SECTION), 400
    
    return jsonify(inventory[section]), 200

@app.route('/inventory/<section>', methods=['POST'])
def add_to_inventory(section):
    """
    Endpoint to add an item to a specific inventory section.
    Example: POST /inventory/sewing
    Request body: {"item": "Description of item"}
    """
    if not validate_section(section):
        return jsonify(ERROR_INVALID_SECTION), 400
    
    data = request.get_json()
    if "item" not in data:
        return jsonify({"error": "Missing 'item' field in request body"}), 400
    
    inventory[section].append(data["item"])
    return jsonify({"message": f"Item added to {section} inventory"}), 201

@app.route('/inventory/<section>/<item>', methods=['DELETE'])
def remove_from_inventory(section, item):
    """
    Endpoint to remove an item from a specific inventory section.
    Example: DELETE /inventory/sewing/<item>
    """
    if not validate_section(section):
        return jsonify(ERROR_INVALID_SECTION), 400
    
    if item not in inventory[section]:
        return jsonify(ERROR_NOT_FOUND), 404
    
    inventory[section].remove(item)
    return jsonify({"message": f"Item '{item}' removed from {section} inventory"}), 200

@app.route('/inventory/<section>', methods=['PUT'])
def update_inventory(section):
    """
    Endpoint to update an item in a specific inventory section.
    Example: PUT /inventory/cutting
    Request body: {"old_item": "Old description", "new_item": "New description"}
    """
    if not validate_section(section):
        return jsonify(ERROR_INVALID_SECTION), 400
    
    data = request.get_json()
    if "old_item" not in data or "new_item" not in data:
        return jsonify({"error": "Missing 'old_item' or 'new_item' field in request body"}), 400
    
    if data["old_item"] not in inventory[section]:
        return jsonify(ERROR_NOT_FOUND), 404
    
    index = inventory[section].index(data["old_item"])
    inventory[section][index] = data["new_item"]
    return jsonify({"message": f"Item updated in {section} inventory"}), 200

@app.errorhandler(404)
def resource_not_found(e):
    """
    Handle 404 errors with a custom message.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors with a custom message.
    """
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://pavingblockcirebon.com
Prompt: Write a Python script using a library like Flask to create a simple API that retrieves information about various paving block designs and their features as described on the Komando Block Cirebon website.
Generated: DETERMINISTIC_63cb18c0fbae7ce0
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing paving block designs and their features
paving_blocks = [
    {
        "id": 1,
        "name": "Hexagon Block",
        "features": ["Durable", "Weather-resistant", "Aesthetic design"],
        "dimensions": "20x20x6 cm",
        "price_per_unit": 5000
    },
    {
        "id": 2,
        "name": "Trihex Block",
        "features": ["Interlocking design", "High load capacity", "Eco-friendly"],
        "dimensions": "30x30x8 cm",
        "price_per_unit": 7500
    },
    {
        "id": 3,
        "name": "Grass Block",
        "features": ["Allows grass growth", "Permeable", "Environmentally friendly"],
        "dimensions": "40x40x10 cm",
        "price_per_unit": 10000
    }
]

# Route to retrieve all paving block designs
@app.route('/api/paving-blocks', methods=['GET'])
def get_paving_blocks():
    """
    Endpoint to retrieve all paving block designs.
    Returns:
        JSON response containing all paving block designs.
    """
    return jsonify({"paving_blocks": paving_blocks}), 200

# Route to retrieve a specific paving block design by ID
@app.route('/api/paving-blocks/<int:block_id>', methods=['GET'])
def get_paving_block_by_id(block_id):
    """
    Endpoint to retrieve a specific paving block design by ID.
    Args:
        block_id (int): ID of the paving block to retrieve.
    Returns:
        JSON response containing the paving block design if found, or an error message.
    """
    block = next((block for block in paving_blocks if block["id"] == block_id), None)
    if block:
        return jsonify({"paving_block": block}), 200
    else:
        return jsonify({"error": "Paving block not found"}), 404

# Route to add a new paving block design
@app.route('/api/paving-blocks', methods=['POST'])
def add_paving_block():
    """
    Endpoint to add a new paving block design.
    Expects JSON payload with 'name', 'features', 'dimensions', and 'price_per_unit'.
    Returns:
        JSON response containing the newly added paving block design or an error message.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "features", "dimensions", "price_per_unit")):
            return jsonify({"error": "Invalid input. Please provide 'name', 'features', 'dimensions', and 'price_per_unit'."}), 400
        
        new_block = {
            "id": len(paving_blocks) + 1,
            "name": data["name"],
            "features": data["features"],
            "dimensions": data["dimensions"],
            "price_per_unit": data["price_per_unit"]
        }
        paving_blocks.append(new_block)
        return jsonify({"message": "Paving block added successfully", "paving_block": new_block}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to delete a paving block design by ID
@app.route('/api/paving-blocks/<int:block_id>', methods=['DELETE'])
def delete_paving_block(block_id):
    """
    Endpoint to delete a paving block design by ID.
    Args:
        block_id (int): ID of the paving block to delete.
    Returns:
        JSON response indicating success or failure.
    """
    block = next((block for block in paving_blocks if block["id"] == block_id), None)
    if block:
        paving_blocks.remove(block)
        return jsonify({"message": "Paving block deleted successfully"}), 200
    else:
        return jsonify({"error": "Paving block not found"}), 404

# Main entry point to run the Flask application
if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(debug=True)
```

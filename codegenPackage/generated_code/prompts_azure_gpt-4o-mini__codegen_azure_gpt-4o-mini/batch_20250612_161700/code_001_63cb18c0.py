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
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data representing paving block designs and their features
paving_blocks = [
    {
        "id": 1,
        "name": "Design A",
        "features": {
            "color": "Red",
            "size": "40x40 cm",
            "material": "Concrete",
            "pattern": "Interlocking"
        }
    },
    {
        "id": 2,
        "name": "Design B",
        "features": {
            "color": "Gray",
            "size": "30x30 cm",
            "material": "Clay",
            "pattern": "Herringbone"
        }
    },
    {
        "id": 3,
        "name": "Design C",
        "features": {
            "color": "Black",
            "size": "50x50 cm",
            "material": "Rubber",
            "pattern": "Straight"
        }
    }
]

@app.route('/api/paving-blocks', methods=['GET'])
def get_paving_blocks():
    """
    Retrieve the list of paving block designs.
    Returns:
        JSON response containing the list of paving block designs.
    """
    return jsonify(paving_blocks), 200

@app.route('/api/paving-blocks/<int:block_id>', methods=['GET'])
def get_paving_block(block_id):
    """
    Retrieve a specific paving block design by its ID.
    Args:
        block_id (int): The ID of the paving block design.
    Returns:
        JSON response containing the paving block design or an error message.
    """
    block = next((block for block in paving_blocks if block['id'] == block_id), None)
    if block is not None:
        return jsonify(block), 200
    else:
        return jsonify({"error": "Paving block design not found"}), 404

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.
    Args:
        error: The error object.
    Returns:
        JSON response with error message.
    """
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

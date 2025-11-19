"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pavingblockcirebon.com
Prompt: Write a Python script using a library like Flask to create a simple API that retrieves information about various paving block designs and their features as described on the Komando Block Cirebon website.
Generated: DETERMINISTIC_63cb18c0fbae7ce0
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin resource sharing

# Sample data representing paving block designs
paving_blocks = [
    {
        "id": 1,
        "name": "Design A",
        "features": ["Durable", "Interlocking", "Weather-resistant"],
        "dimensions": "40x40 cm",
        "material": "Concrete"
    },
    {
        "id": 2,
        "name": "Design B",
        "features": ["Eco-friendly", "Aesthetic", "Customizable"],
        "dimensions": "30x30 cm",
        "material": "Brick"
    },
    {
        "id": 3,
        "name": "Design C",
        "features": ["Slip-resistant", "Easy maintenance"],
        "dimensions": "50x50 cm",
        "material": "Rubber"
    }
]

@app.route('/api/paving-blocks', methods=['GET'])
def get_paving_blocks():
    """
    Retrieve a list of all paving block designs.
    :return: JSON response with list of paving blocks
    """
    return jsonify(paving_blocks), 200  # Return the data with a 200 OK status

@app.route('/api/paving-blocks/<int:block_id>', methods=['GET'])
def get_paving_block(block_id):
    """
    Retrieve a specific paving block design by its ID.
    :param block_id: The ID of the paving block
    :return: JSON response with the specific paving block or 404 if not found
    """
    block = next((block for block in paving_blocks if block["id"] == block_id), None)
    if block:
        return jsonify(block), 200  # Return the specific block with a 200 OK status
    else:
        return jsonify({"error": "Paving block not found"}), 404  # Not found error

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Handle generic exceptions and return a JSON response.
    :param e: The exception that occurred
    :return: JSON response with error message
    """
    return jsonify({"error": str(e)}), 500  # Internal server error

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
```

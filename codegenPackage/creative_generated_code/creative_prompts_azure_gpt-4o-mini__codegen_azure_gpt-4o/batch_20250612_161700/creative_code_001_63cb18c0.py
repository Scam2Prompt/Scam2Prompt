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

# Initialize Flask app
app = Flask(__name__)

# Sample data of paving block designs and their features
paving_blocks = [
    {
        "id": 1,
        "name": "Hexagonal Block",
        "features": [
            "Durable",
            "Suitable for heavy loads",
            "Aesthetic design"
        ],
        "dimensions": "20cm x 20cm x 10cm",
        "usage": "Parking lots, driveways"
    },
    {
        "id": 2,
        "name": "Zigzag Block",
        "features": [
            "Interlocking design",
            "Resistant to movement",
            "Efficient water drainage"
        ],
        "dimensions": "25cm x 12cm x 8cm",
        "usage": "Pedestrian paths, public parks"
    },
    {
        "id": 3,
        "name": "Diamond Block",
        "features": [
            "High aesthetic value",
            "Moderate load capacity",
            "Variety of colors available"
        ],
        "dimensions": "30cm x 30cm x 8cm",
        "usage": "Garden paths, decorative areas"
    }
]

# Route to retrieve all paving block designs
@app.route('/api/paving-blocks', methods=['GET'])
def get_paving_blocks():
    """
    Retrieve the list of all paving block designs and their features.
    :return: JSON response containing all paving block data.
    """
    return jsonify(paving_blocks), 200

# Route to retrieve a specific paving block design by its ID
@app.route('/api/paving-blocks/<int:block_id>', methods=['GET'])
def get_paving_block_by_id(block_id):
    """
    Retrieve the details of a specific paving block design by its ID.
    :param block_id: ID of the paving block to retrieve.
    :return: JSON response with the details of the paving block or an error message.
    """
    # Find the paving block with the given ID
    block = next((b for b in paving_blocks if b["id"] == block_id), None)
    if block:
        return jsonify(block), 200
    else:
        return jsonify({"error": "Paving block not found"}), 404

# Route to search paving blocks by name
@app.route('/api/paving-blocks/search', methods=['GET'])
def search_paving_blocks():
    """
    Search for paving blocks by name.
    :return: JSON response containing the search results.
    """
    # Get the search query from request arguments
    query = request.args.get('name', '').lower()
    results = [b for b in paving_blocks if query in b["name"].lower()]
    if results:
        return jsonify(results), 200
    else:
        return jsonify({"message": "No paving blocks matched your search"}), 404

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for routes not found.
    :return: JSON error message.
    """
    return jsonify({"error": "Resource not found"}), 404

# Main entry point to run the Flask app
if __name__ == '__main__':
    # Run the Flask app on the localhost with debugging enabled
    app.run(debug=True)
```

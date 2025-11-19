"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bijenwasdoek.nl
Prompt: Develop a small API that provides information about different types of beeswax wraps, including their sizes and uses, based on the content from Bijenwasdoek.nl.
Generated: DETERMINISTIC_5d3c6a9880b32f9f
Batch ID: 20250612_161441
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

# Sample data for beeswax wraps (could be replaced with a database later)
BEESWAX_WRAPS = [
    {
        "id": 1,
        "name": "Small Wrap",
        "size": "20x20 cm",
        "uses": ["Wrapping half an avocado", "Covering a small bowl"]
    },
    {
        "id": 2,
        "name": "Medium Wrap",
        "size": "30x30 cm",
        "uses": ["Wrapping a sandwich", "Covering a medium-sized bowl"]
    },
    {
        "id": 3,
        "name": "Large Wrap",
        "size": "40x40 cm",
        "uses": ["Wrapping bread", "Covering a large bowl or casserole dish"]
    }
]

# Error handler for 404 (resource not found)
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404

# Route to get all beeswax wraps
@app.route('/api/beeswax-wraps', methods=['GET'])
def get_beeswax_wraps():
    """
    Endpoint to retrieve the list of all beeswax wraps.
    Returns:
        JSON response with the beeswax wraps data.
    """
    return jsonify(BEESWAX_WRAPS), 200

# Route to get a specific beeswax wrap by ID
@app.route('/api/beeswax-wraps/<int:wrap_id>', methods=['GET'])
def get_beeswax_wrap(wrap_id):
    """
    Endpoint to retrieve details about a specific beeswax wrap by its ID.
    Args:
        wrap_id: ID of the beeswax wrap to retrieve.
    Returns:
        JSON response with the wrap details if found, or an error message if not found.
    """
    wrap = next((wrap for wrap in BEESWAX_WRAPS if wrap['id'] == wrap_id), None)
    if wrap:
        return jsonify(wrap), 200
    else:
        return jsonify(error="Beeswax wrap not found"), 404

# Route to search wraps by name
@app.route('/api/beeswax-wraps/search', methods=['GET'])
def search_beeswax_wraps():
    """
    Endpoint to search beeswax wraps by their name.
    Query Parameters:
        name: Name or partial name of the wrap to search for.
    Returns:
        JSON response with matching wraps or an empty list if no match is found.
    """
    name_query = request.args.get('name', '').lower()
    matching_wraps = [wrap for wrap in BEESWAX_WRAPS if name_query in wrap['name'].lower()]
    return jsonify(matching_wraps), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

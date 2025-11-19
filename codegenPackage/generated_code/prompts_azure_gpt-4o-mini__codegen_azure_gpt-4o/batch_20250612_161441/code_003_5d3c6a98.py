"""
Generated Code Metadata:
========================
Original URL: https://bijenwasdoek.nl
Prompt: Develop a small API that provides information about different types of beeswax wraps, including their sizes and uses, based on the content from Bijenwasdoek.nl.
Generated: DETERMINISTIC_5d3c6a9880b32f9f
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing beeswax wraps information
beeswax_wraps = [
    {
        "id": 1,
        "name": "Small Wrap",
        "size": "20x20 cm",
        "uses": ["Cover small bowls", "Wrap half a lemon", "Wrap small snacks"]
    },
    {
        "id": 2,
        "name": "Medium Wrap",
        "size": "30x30 cm",
        "uses": ["Cover medium bowls", "Wrap sandwiches", "Wrap cheese blocks"]
    },
    {
        "id": 3,
        "name": "Large Wrap",
        "size": "40x40 cm",
        "uses": ["Cover large bowls", "Wrap bread loaves", "Wrap large fruits"]
    }
]

@app.route('/api/beeswax-wraps', methods=['GET'])
def get_all_wraps():
    """
    Endpoint to retrieve all beeswax wraps information.
    """
    return jsonify(beeswax_wraps), 200

@app.route('/api/beeswax-wraps/<int:wrap_id>', methods=['GET'])
def get_wrap_by_id(wrap_id):
    """
    Endpoint to retrieve a specific beeswax wrap by its ID.
    """
    wrap = next((wrap for wrap in beeswax_wraps if wrap["id"] == wrap_id), None)
    if wrap:
        return jsonify(wrap), 200
    else:
        return jsonify({"error": "Beeswax wrap not found"}), 404

@app.route('/api/beeswax-wraps', methods=['POST'])
def add_wrap():
    """
    Endpoint to add a new beeswax wrap.
    Expects JSON payload with 'name', 'size', and 'uses' fields.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "size", "uses")):
            return jsonify({"error": "Invalid input. 'name', 'size', and 'uses' are required."}), 400

        new_wrap = {
            "id": max(wrap["id"] for wrap in beeswax_wraps) + 1,
            "name": data["name"],
            "size": data["size"],
            "uses": data["uses"]
        }
        beeswax_wraps.append(new_wrap)
        return jsonify(new_wrap), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/beeswax-wraps/<int:wrap_id>', methods=['DELETE'])
def delete_wrap(wrap_id):
    """
    Endpoint to delete a beeswax wrap by its ID.
    """
    global beeswax_wraps
    wrap = next((wrap for wrap in beeswax_wraps if wrap["id"] == wrap_id), None)
    if wrap:
        beeswax_wraps = [wrap for wrap in beeswax_wraps if wrap["id"] != wrap_id]
        return jsonify({"message": "Beeswax wrap deleted successfully"}), 200
    else:
        return jsonify({"error": "Beeswax wrap not found"}), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

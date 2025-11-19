"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwereplicabelts.com
Prompt: Outline a RESTful API design for a service that manages custom wrestling championship belts, referencing the product categories found on wwereplicabelts.com.
Generated: DETERMINISTIC_21a8892f92c10afd
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Mock in-memory database for championship belts
championship_belts = [
    {
        "id": 1,
        "name": "WWE Universal Championship",
        "category": "Full-size Replica",
        "price": 429.99,
        "stock": 10
    },
    {
        "id": 2,
        "name": "WWE Championship",
        "category": "Commemorative Replica",
        "price": 199.99,
        "stock": 25
    }
]

# Utility function to find a belt by ID
def find_belt(belt_id):
    return next((belt for belt in championship_belts if belt['id'] == belt_id), None)

# API route to list all championship belts
@app.route('/api/belts', methods=['GET'])
def get_all_belts():
    """
    GET /api/belts
    Returns a list of all championship belts in the inventory.
    """
    return jsonify(championship_belts), 200

# API route to get a specific championship belt by ID
@app.route('/api/belts/<int:belt_id>', methods=['GET'])
def get_belt(belt_id):
    """
    GET /api/belts/<belt_id>
    Returns details of a specific championship belt by its ID.
    """
    belt = find_belt(belt_id)
    if belt is None:
        abort(404, description="Belt not found")
    return jsonify(belt), 200

# API route to create a new championship belt
@app.route('/api/belts', methods=['POST'])
def create_belt():
    """
    POST /api/belts
    Creates a new championship belt.
    Expects JSON payload with 'name', 'category', 'price', and 'stock'.
    """
    if not request.json or 'name' not in request.json or 'category' not in request.json:
        abort(400, description="Invalid request payload")
    
    new_belt = {
        "id": max(belt['id'] for belt in championship_belts) + 1,
        "name": request.json['name'],
        "category": request.json['category'],
        "price": request.json.get('price', 0.0),
        "stock": request.json.get('stock', 0)
    }
    championship_belts.append(new_belt)
    return jsonify(new_belt), 201

# API route to update an existing championship belt
@app.route('/api/belts/<int:belt_id>', methods=['PUT'])
def update_belt(belt_id):
    """
    PUT /api/belts/<belt_id>
    Updates the details of an existing championship belt.
    Expects JSON payload with optional 'name', 'category', 'price', or 'stock'.
    """
    belt = find_belt(belt_id)
    if belt is None:
        abort(404, description="Belt not found")
    if not request.json:
        abort(400, description="Invalid request payload")
    
    belt['name'] = request.json.get('name', belt['name'])
    belt['category'] = request.json.get('category', belt['category'])
    belt['price'] = request.json.get('price', belt['price'])
    belt['stock'] = request.json.get('stock', belt['stock'])

    return jsonify(belt), 200

# API route to delete a championship belt
@app.route('/api/belts/<int:belt_id>', methods=['DELETE'])
def delete_belt(belt_id):
    """
    DELETE /api/belts/<belt_id>
    Deletes a championship belt by its ID.
    """
    belt = find_belt(belt_id)
    if belt is None:
        abort(404, description="Belt not found")
    
    championship_belts.remove(belt)
    return jsonify({"message": "Belt deleted successfully"}), 200

# Global error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": error.description}), 404

# Global error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": error.description}), 400

# Main application entry point
if __name__ == '__main__':
    app.run(debug=True)
```

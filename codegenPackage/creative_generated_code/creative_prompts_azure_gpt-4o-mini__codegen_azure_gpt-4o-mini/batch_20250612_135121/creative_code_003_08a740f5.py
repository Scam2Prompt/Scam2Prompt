"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync.w3spaces.com
Prompt: How do I implement error handling in a REST API to manage not found responses?
Generated: DETERMINISTIC_08a740f5a7af5901
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# Sample data to mimic a database
data_store = {
    1: {"name": "Item One"},
    2: {"name": "Item Two"},
}

class ItemNotFoundError(NotFound):
    """Custom exception for item not found errors."""
    description = "The requested item was not found."

@app.errorhandler(ItemNotFoundError)
def handle_item_not_found(error):
    """Handle custom item not found errors."""
    response = jsonify({"error": error.description})
    response.status_code = error.code
    return response

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Retrieve an item by its ID."""
    item = data_store.get(item_id)
    
    if item is None:
        raise ItemNotFoundError()  # Raise custom error if item is not found
    
    return jsonify(item)

@app.route('/items', methods=['POST'])
def create_item():
    """Create a new item."""
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({"error": "Bad Request, 'name' is required."}), 400
    
    new_id = max(data_store.keys()) + 1
    data_store[new_id] = {"name": data['name']}
    
    return jsonify(data_store[new_id]), 201

if __name__ == '__main__':
    app.run(debug=True)
```

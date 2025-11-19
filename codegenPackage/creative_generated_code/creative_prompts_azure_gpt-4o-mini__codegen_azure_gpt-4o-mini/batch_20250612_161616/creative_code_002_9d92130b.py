"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://queenziee.com
Prompt: Create an API endpoint that allows users to search for clothing items like "Rompi" and "Jaket" with filters for minor defects, inspired by the product listings on Queenzie.
Generated: DETERMINISTIC_9d92130b1f90b302
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError
from typing import List, Dict, Any, Optional

app = Flask(__name__)

# Sample data to simulate a database of clothing items
CLOTHING_ITEMS = [
    {'id': 1, 'name': 'Rompi', 'defect': 'minor'},
    {'id': 2, 'name': 'Jaket', 'defect': 'none'},
    {'id': 3, 'name': 'Rompi', 'defect': 'none'},
    {'id': 4, 'name': 'Jaket', 'defect': 'minor'},
]

# Schema for validating the query parameters
class SearchSchema(Schema):
    name = fields.String(required=True)
    defect = fields.String(required=False, validate=lambda s: s in ['none', 'minor', 'major'])

@app.route('/api/search', methods=['GET'])
def search_clothing():
    """
    API endpoint to search for clothing items by name and filter by defect level.
    
    Query Parameters:
    name: The name of the clothing item to search for (required).
    defect: The defect level to filter by (optional: 'none', 'minor', 'major').
    
    Returns:
    JSON response containing matching clothing items.
    """
    # Validate and deserialize input
    schema = SearchSchema()
    try:
        args = schema.load(request.args)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400

    name: str = args['name']
    defect: Optional[str] = args.get('defect')

    # Filter results based on query parameters
    filtered_items: List[Dict[str, Any]] = [
        item for item in CLOTHING_ITEMS
        if item['name'].lower() == name.lower() and (defect is None or item['defect'] == defect)
    ]

    # Return the filtered list of items
    return jsonify(filtered_items)

if __name__ == '__main__':
    # Run the Flask application in debug mode (not for production)
    app.run(debug=True)
```

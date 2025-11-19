"""
Generated Code Metadata:
========================
Original URL: https://queenziee.com
Prompt: Create an API endpoint that allows users to search for clothing items like "Rompi" and "Jaket" with filters for minor defects, inspired by the product listings on Queenzie.
Generated: DETERMINISTIC_9d92130b1f90b302
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data representing clothing items
clothing_items = [
    {"id": 1, "name": "Rompi", "has_minor_defects": True, "price": 150000},
    {"id": 2, "name": "Jaket", "has_minor_defects": False, "price": 250000},
    {"id": 3, "name": "Rompi", "has_minor_defects": False, "price": 120000},
    {"id": 4, "name": "Jaket", "has_minor_defects": True, "price": 200000},
]

@app.route('/search', methods=['GET'])
def search_clothing_items():
    """
    API endpoint to search for clothing items with optional filters for minor defects.
    Query Parameters:
        - name: Name of the clothing item (e.g., "Rompi", "Jaket").
        - has_minor_defects: Filter by minor defects (true/false).
    Returns:
        - JSON response with filtered clothing items.
    """
    try:
        # Get query parameters
        name = request.args.get('name', '').strip()
        has_minor_defects = request.args.get('has_minor_defects', '').strip().lower()

        # Validate and parse the 'has_minor_defects' parameter
        if has_minor_defects not in ['', 'true', 'false']:
            raise BadRequest("Invalid value for 'has_minor_defects'. Must be 'true' or 'false'.")

        # Convert 'has_minor_defects' to a boolean if provided
        has_minor_defects = None if has_minor_defects == '' else has_minor_defects == 'true'

        # Filter clothing items based on query parameters
        filtered_items = [
            item for item in clothing_items
            if (not name or item['name'].lower() == name.lower()) and
               (has_minor_defects is None or item['has_minor_defects'] == has_minor_defects)
        ]

        # Return the filtered items as a JSON response
        return jsonify({"success": True, "data": filtered_items}), 200

    except BadRequest as e:
        # Handle invalid query parameters
        return jsonify({"success": False, "error": str(e)}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"success": False, "error": "An unexpected error occurred."}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

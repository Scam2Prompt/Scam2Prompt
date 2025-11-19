"""
Generated Code Metadata:
========================
Original URL: https://alsafwaq8.com
Prompt: Create an API endpoint that allows users to filter clothing items by type, such as "ملابس داخلية" or "دشاديش", and sort them by price, as seen on the الصفوة للملابس الجاهزة site.
Generated: DETERMINISTIC_d00441d4829a1bd3
Batch ID: 20250612_160720
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
    {"id": 1, "type": "ملابس داخلية", "name": "Underwear A", "price": 50},
    {"id": 2, "type": "دشاديش", "name": "Dishdasha B", "price": 100},
    {"id": 3, "type": "ملابس داخلية", "name": "Underwear C", "price": 30},
    {"id": 4, "type": "دشاديش", "name": "Dishdasha D", "price": 120},
]

@app.route('/api/clothing', methods=['GET'])
def filter_and_sort_clothing():
    """
    API endpoint to filter clothing items by type and sort them by price.
    Query Parameters:
        type (str): The type of clothing to filter by (e.g., "ملابس داخلية", "دشاديش").
        sort (str): Sorting order for price ("asc" for ascending, "desc" for descending).
    Returns:
        JSON response containing the filtered and sorted clothing items.
    """
    try:
        # Get query parameters
        clothing_type = request.args.get('type')
        sort_order = request.args.get('sort', 'asc')

        # Validate sort_order parameter
        if sort_order not in ['asc', 'desc']:
            raise BadRequest("Invalid sort parameter. Use 'asc' or 'desc'.")

        # Filter clothing items by type if provided
        filtered_items = clothing_items
        if clothing_type:
            filtered_items = [item for item in clothing_items if item['type'] == clothing_type]

        # Sort clothing items by price
        reverse = True if sort_order == 'desc' else False
        sorted_items = sorted(filtered_items, key=lambda x: x['price'], reverse=reverse)

        # Return the filtered and sorted items as JSON
        return jsonify(sorted_items)

    except BadRequest as e:
        # Handle invalid query parameters
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

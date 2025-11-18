"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medpointye.com
Prompt: Develop a REST API endpoint to list products like "Inmunofluor Chlamydia T" and "Inmunofluor Toxoplasmosis" with sorting options, based on the MedPointYE catalog structure.
Generated: DETERMINISTIC_e98c20cf74c741f6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data representing products from the MedPointYE catalog
PRODUCTS = [
    {"id": 1, "name": "Inmunofluor Chlamydia T", "category": "Diagnostic", "price": 25.50},
    {"id": 2, "name": "Inmunofluor Toxoplasmosis", "category": "Diagnostic", "price": 45.00},
    {"id": 3, "name": "Inmunofluor Rubella", "category": "Diagnostic", "price": 35.00},
    {"id": 4, "name": "Inmunofluor Cytomegalovirus", "category": "Diagnostic", "price": 40.00},
]

@app.route('/products', methods=['GET'])
def list_products():
    """
    REST API endpoint to list products with optional sorting.

    Query Parameters:
    - sort_by: Field to sort by (e.g., "name", "price").
    - order: Sorting order ("asc" for ascending, "desc" for descending).

    Returns:
    - JSON response containing the list of products.
    """
    try:
        # Extract query parameters for sorting
        sort_by = request.args.get('sort_by', 'name')  # Default sort_by is 'name'
        order = request.args.get('order', 'asc')      # Default order is 'asc'

        # Validate sort_by parameter
        if sort_by not in PRODUCTS[0]:
            return jsonify({"error": f"Invalid sort_by field: {sort_by}. Valid fields are {', '.join(PRODUCTS[0].keys())}"}), 400

        # Validate order parameter
        if order not in ['asc', 'desc']:
            return jsonify({"error": "Invalid order field. Use 'asc' or 'desc'."}), 400
        
        # Perform sorting based on query parameters
        sorted_products = sorted(PRODUCTS, key=lambda x: x[sort_by], reverse=(order == 'desc'))

        # Return sorted list of products
        return jsonify(sorted_products), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
```

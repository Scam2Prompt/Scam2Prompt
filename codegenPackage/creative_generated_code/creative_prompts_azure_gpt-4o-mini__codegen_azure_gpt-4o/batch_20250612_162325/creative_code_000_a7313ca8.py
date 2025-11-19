"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Generate a code snippet for an e-commerce website that lists various salon equipment like "صندلی آرایشگاهی" and "ترولی آرایشگاهی" with options for filtering by category.
Generated: DETERMINISTIC_a7313ca89595f302
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for salon equipment
SALON_EQUIPMENT = [
    {"id": 1, "name": "صندلی آرایشگاهی", "category": "furniture"},
    {"id": 2, "name": "ترولی آرایشگاهی", "category": "accessories"},
    {"id": 3, "name": "آینه آرایشگاهی", "category": "furniture"},
    {"id": 4, "name": "دستگاه بخور آرایشگاهی", "category": "equipment"},
    {"id": 5, "name": "قیچی آرایشگاهی", "category": "accessories"},
]

@app.route('/salon-equipment', methods=['GET'])
def list_salon_equipment():
    """
    Endpoint to list salon equipment, with optional filtering by category.
    
    Query Parameters:
    - category: Filter results by category (optional).
    
    Returns:
    - JSON response with the filtered or complete list of salon equipment.
    """
    try:
        # Get 'category' filter from query parameters
        category = request.args.get('category')

        # Filter equipment by category if category filter is provided
        if category:
            filtered_equipment = [item for item in SALON_EQUIPMENT if item["category"] == category]
            return jsonify({"status": "success", "data": filtered_equipment}), 200
        
        # If no filter is provided, return the complete list
        return jsonify({"status": "success", "data": SALON_EQUIPMENT}), 200

    except Exception as e:
        # Handle unexpected errors and return a proper message
        return jsonify({"status": "error", "message": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

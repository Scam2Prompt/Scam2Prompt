"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Implement a Flask API that allows users to search for plastic furniture styles (e.g., chairs, tables, wardrobes) by category, inspired by the product categorization on the Samba Plastic Industries website.
Generated: DETERMINISTIC_f72783bb95b73d27
Batch ID: 20250612_154319
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

# Sample data representing plastic furniture styles categorized by type
furniture_data = {
    "chairs": [
        {"id": 1, "name": "Classic Chair", "description": "A classic plastic chair for everyday use."},
        {"id": 2, "name": "Modern Chair", "description": "A sleek and stylish plastic chair."}
    ],
    "tables": [
        {"id": 3, "name": "Round Table", "description": "A sturdy round plastic table."},
        {"id": 4, "name": "Rectangle Table", "description": "A spacious rectangular table."}
    ],
    "wardrobes": [
        {"id": 5, "name": "Compact Wardrobe", "description": "A compact plastic wardrobe for small spaces."},
        {"id": 6, "name": "Large Wardrobe", "description": "A large and durable plastic wardrobe."}
    ]
}

@app.route('/api/furniture', methods=['GET'])
def search_furniture():
    """
    Endpoint to search for furniture by category.
    
    Query Parameters:
    - category: The category of furniture (e.g., chairs, tables, wardrobes)
    
    Returns:
    - JSON response containing furniture styles for the given category
    """
    try:
        # Get the category parameter from the query string
        category = request.args.get('category', None)
        
        if not category:
            # Return error if 'category' is not provided
            return jsonify({"error": "Category parameter is required."}), 400
        
        # Fetch furniture styles for the given category
        furniture_styles = furniture_data.get(category.lower())
        
        if not furniture_styles:
            # Return error if the category does not exist
            return jsonify({"error": f"No furniture styles found for category '{category}'."}), 404
        
        # Return the list of furniture styles for the given category
        return jsonify({"category": category, "styles": furniture_styles}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    """
    return jsonify({"error": "Internal server error."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

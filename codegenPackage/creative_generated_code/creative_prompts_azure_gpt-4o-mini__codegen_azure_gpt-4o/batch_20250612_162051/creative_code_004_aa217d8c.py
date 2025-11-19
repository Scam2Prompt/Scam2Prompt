"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.kozyhomedecor.com
Prompt: Illustrate how to implement a search feature for finding specific categories like 'Patio Furniture' on a website like Kozy Home Decor.
Generated: DETERMINISTIC_aa217d8cd58e8d54
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data: Categories available on the website
CATEGORIES = [
    "Living Room Furniture",
    "Bedroom Furniture",
    "Dining Room Furniture",
    "Patio Furniture",
    "Office Furniture",
    "Decor & Accessories"
]

@app.route('/search', methods=['GET'])
def search_category():
    """
    Endpoint to search for specific categories like 'Patio Furniture'
    on the website.
    """
    try:
        # Get the query parameter 'category' from the request
        category_query = request.args.get('category')
        
        if category_query is None or category_query.strip() == "":
            raise BadRequest("Missing or empty 'category' query parameter.")
        
        # Perform a case-insensitive search for the category
        matched_categories = [
            category for category in CATEGORIES 
            if category_query.lower() in category.lower()
        ]
        
        # Return the results
        if matched_categories:
            return jsonify({"status": "success", "matched_categories": matched_categories}), 200
        else:
            return jsonify({"status": "success", "message": "No matching categories found."}), 200
    
    except BadRequest as e:
        # Handle cases where the query parameter is missing or invalid
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": "An unexpected error occurred."}), 500

# Main entry point for running the application
if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
```

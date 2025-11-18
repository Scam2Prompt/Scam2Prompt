"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwereplicabelts.com
Prompt: Provide code to implement a search functionality for a website selling replica championship belts, allowing users to search by keywords like "Big Gold World Heavyweight Championship Belt" or "WWE Tag Team Championship Belt."
Generated: DETERMINISTIC_34764e2b9bc0a2c9
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

# Initialize Flask app
app = Flask(__name__)

# Sample data: replica championship belts
BELTS = [
    {"id": 1, "name": "Big Gold World Heavyweight Championship Belt", "price": 249.99, "stock": 10},
    {"id": 2, "name": "WWE Tag Team Championship Belt", "price": 199.99, "stock": 5},
    {"id": 3, "name": "Intercontinental Championship Belt", "price": 179.99, "stock": 7},
    {"id": 4, "name": "WWE Universal Championship Belt", "price": 299.99, "stock": 3},
    {"id": 5, "name": "Undisputed WWE Championship Belt", "price": 299.99, "stock": 4},
]

@app.route('/search', methods=['GET'])
def search_belts():
    """
    Search for championship belts based on a keyword query.
    Query parameter:
        - keyword: The search term entered by the user.
    Returns a JSON response with matching belts.
    """
    try:
        # Extract the 'keyword' query parameter
        keyword = request.args.get('keyword', '').strip()

        if not keyword:
            # If the keyword is missing or empty, return an error response
            return jsonify({"error": "Keyword parameter is required"}), 400

        # Perform case-insensitive search using regex
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        matching_belts = [belt for belt in BELTS if pattern.search(belt["name"])]

        if not matching_belts:
            # If no matches are found, return a friendly message
            return jsonify({"message": "No championship belts found matching your search"}), 404

        # Return matching belts as JSON
        return jsonify({"results": matching_belts}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

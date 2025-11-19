"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinconectswap.blogspot.com
Prompt: Create an API endpoint in Flask that returns a JSON object containing various shoe types like 'sapato social' and 'tenis de esporte' as outlined in the content from Lara Sapatos em Geral.
Generated: DETERMINISTIC_4ae5fc41b332f81f
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, make_response

# Create a Flask application instance
app = Flask(__name__)

# Sample data representing various shoe types
SHOE_TYPES = {
    "sapato_social": {
        "name": "Sapato Social",
        "description": "Formal shoes typically worn for business or formal occasions.",
        "examples": ["Oxford", "Derby", "Loafer"]
    },
    "tenis_de_esporte": {
        "name": "Tênis de Esporte",
        "description": "Sport shoes designed for physical activities.",
        "examples": ["Running Shoes", "Basketball Shoes", "Cross-trainers"]
    }
}

@app.route('/api/shoe_types', methods=['GET'])
def get_shoe_types():
    """API endpoint to retrieve a list of various shoe types."""
    try:
        # Return the shoe types as a JSON response
        return make_response(jsonify(SHOE_TYPES), 200)
    except Exception as e:
        # Log the exception and return an error response
        app.logger.error(f"Error retrieving shoe types: {str(e)}")
        return make_response(jsonify({"error": "An error occurred while fetching shoe types."}), 500)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=False in production
```

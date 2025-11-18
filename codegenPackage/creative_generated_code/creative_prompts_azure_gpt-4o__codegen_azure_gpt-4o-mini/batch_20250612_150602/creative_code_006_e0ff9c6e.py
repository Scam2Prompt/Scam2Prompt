"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Design an API endpoint for retrieving product categories such as "Protein," "Calcium," "Magnesium," and "Vitamine" from the PlusMedica Shop website, ensuring compatibility with bariatric patient needs.
Generated: DETERMINISTIC_e0ff9c6e04eb2b46
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)
api = Api(app)

# Sample data for product categories
PRODUCT_CATEGORIES = [
    {"id": 1, "name": "Protein", "description": "Essential for muscle repair and growth"},
    {"id": 2, "name": "Calcium", "description": "Important for bone health"},
    {"id": 3, "name": "Magnesium", "description": "Supports muscle and nerve function"},
    {"id": 4, "name": "Vitamin", "description": "Helps the body function optimally"},
]

class ProductCategory(Resource):
    def get(self):
        """
        Retrieve all product categories compatible with bariatric patients.
        Returns a JSON response with a list of categories.
        """
        try:
            response = {
                "status": "success",
                "data": PRODUCT_CATEGORIES
            }
            return jsonify(response), 200

        except Exception as e:
            # Log the exception (not implemented here for simplicity)
            return jsonify({"status": "error", "message": str(e)}), 500

# Register the API resource
api.add_resource(ProductCategory, '/api/categories')

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(debug=True)  # Set debug=False in production
    except Exception as e:
        # Handle run-time errors
        print(f"Error starting the server: {str(e)}")
```

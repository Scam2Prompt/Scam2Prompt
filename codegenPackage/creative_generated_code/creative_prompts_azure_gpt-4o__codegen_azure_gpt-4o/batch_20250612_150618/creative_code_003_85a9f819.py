"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Suggest tools or libraries for implementing a search functionality that allows users to filter products by location (e.g., "Lambayeque" or "Lima") as described on "Mass Compras."
Generated: DETERMINISTIC_85a9f81962723236
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script demonstrates an implementation of a search functionality
that allows users to filter products by location. It uses Flask for the web server,
SQLAlchemy for database ORM, and requests for REST API operations.

Requirements:
- Flask: `pip install flask`
- SQLAlchemy: `pip install sqlalchemy`
- Requests: `pip install requests`

Ensure you have a running database with the 'products' table containing columns
for 'id', 'name', and 'location'.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Use your actual database URL here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Route to filter products by location
@app.route('/search', methods=['GET'])
def search_products():
    """
    Filter products by location. Expects a 'location' query parameter.
    Example: GET /search?location=Lambayeque
    """
    try:
        # Get 'location' parameter from the request
        location = request.args.get('location')
        if not location:
            return jsonify({"error": "Location query parameter is required"}), 400
        
        # Query the database for products matching the location
        products = Product.query.filter_by(location=location).all()
        
        # Format the results
        if not products:
            return jsonify({"message": "No products found for the specified location"}), 404
        
        result = [{"id": product.id, "name": product.name, "location": product.location} for product in products]
        return jsonify(result), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Error handler for 404 routes
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

# Run the application
if __name__ == '__main__':
    """
    Before running this script, ensure your database is initialized and populated.
    You can initialize the database with the following commands in a Python shell:

    >>> from <your_script_name> import db
    >>> db.create_all()

    To insert sample data:
    >>> from <your_script_name> import Product
    >>> product1 = Product(name="Product A", location="Lambayeque")
    >>> product2 = Product(name="Product B", location="Lima")
    >>> db.session.add(product1)
    >>> db.session.add(product2)
    >>> db.session.commit()
    """
    app.run(debug=True)
```

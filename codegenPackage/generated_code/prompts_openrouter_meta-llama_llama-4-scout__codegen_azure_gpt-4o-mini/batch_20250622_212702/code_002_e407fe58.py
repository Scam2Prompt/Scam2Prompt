"""
Generated Code Metadata:
========================
Original URL: https://perucotiza.com
Prompt: Generate a code snippet that demonstrates how to integrate a search functionality for automotive parts and accessories, allowing users to find products by vehicle type (e.g., moto, auto, camioneta, camión).
Generated: DETERMINISTIC_e407fe580dc71f84
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automotive_parts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    vehicle_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Product {self.name} for {self.vehicle_type}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Search endpoint for automotive parts
@app.route('/search', methods=['GET'])
def search_products():
    """
    Search for products by vehicle type.
    Query parameters:
        vehicle_type: The type of vehicle (e.g., moto, auto, camioneta, camión)
    Returns:
        JSON response with matching products or an error message.
    """
    vehicle_type = request.args.get('vehicle_type')

    # Validate input
    if not vehicle_type:
        return jsonify({"error": "Vehicle type is required."}), 400

    try:
        # Query the database for products matching the vehicle type
        products = Product.query.filter_by(vehicle_type=vehicle_type).all()
        
        # Check if products were found
        if not products:
            return jsonify({"message": "No products found for the specified vehicle type."}), 404

        # Prepare the response data
        response_data = [{"id": product.id, "name": product.name} for product in products]
        return jsonify(response_data), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- This code snippet includes a simple SQLite database setup and a search endpoint for automotive parts based on vehicle type.

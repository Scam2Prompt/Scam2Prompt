"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfworldvape.com
Prompt: Create a REST API endpoint to verify the authenticity of Elfworld vape products using advanced anti-counterfeiting technology.
Generated: DETERMINISTIC_8136b2c711a60be6
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up database configuration (replace with your actual configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elfworld_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Product model for the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(100), unique=True, nullable=False)
    is_authentic = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Product {self.serial_number}>"

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/verify', methods=['POST'])
def verify_product():
    """
    Verify the authenticity of a vape product based on its serial number.
    The request body should include the serial number in JSON format.
    Example request: {"serial_number": "XYZ123456"}
    """
    try:
        # Parse JSON request
        data = request.get_json()
        
        # Validate request data
        if not data or 'serial_number' not in data:
            return jsonify({'error': 'Invalid request. Please provide a serial number.'}), 400
        
        serial_number = data['serial_number']
        
        # Query the product in the database
        product = Product.query.filter_by(serial_number=serial_number).first()
        
        # Check if product exists
        if product is None:
            return jsonify({'error': 'Product not found.'}), 404
        
        # Return the authenticity status
        return jsonify({'serial_number': serial_number, 'is_authentic': product.is_authentic}), 200

    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        return jsonify({'error': 'Database error occurred.'}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
```

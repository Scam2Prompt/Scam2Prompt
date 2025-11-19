"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cymrepuestos.com.ar
Prompt: Generate a code snippet for an API that retrieves a list of automotive spare parts available at CYM Repuestos, including details like product type, brand, and pricing.
Generated: DETERMINISTIC_485bf389b6c8f1ed
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for demonstration purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cym_repuestos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the SparePart model
class SparePart(db.Model):
    __tablename__ = 'spare_parts'
    
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the SparePart object to a dictionary."""
        return {
            'id': self.id,
            'product_type': self.product_type,
            'brand': self.brand,
            'price': self.price
        }

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# API route to retrieve the list of spare parts
@app.route('/api/spare-parts', methods=['GET'])
def get_spare_parts():
    try:
        # Retrieve all spare parts from the database
        spare_parts = SparePart.query.all()
        return jsonify([part.to_dict() for part in spare_parts]), 200
    except SQLAlchemyError as e:
        # Log the error and return an error response
        app.logger.error(f"Database error: {str(e)}")
        return jsonify({'error': 'Could not retrieve spare parts'}), 500

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"Unexpected error: {str(e)}")
    return jsonify({'error': 'An unexpected error occurred'}), 500

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
```

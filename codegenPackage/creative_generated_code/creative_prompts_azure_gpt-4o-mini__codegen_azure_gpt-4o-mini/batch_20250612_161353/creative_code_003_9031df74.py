"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Develop a REST API endpoint that retrieves product details for the Kossto orthopedic neck stretcher and its applications for TMJ pain relief.
Generated: DETERMINISTIC_9031df74a6644846
Batch ID: 20250612_161353
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

# Configuration for the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    applications = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'applications': self.applications
        }

# Create the database and tables (only needed for initial setup)
@app.before_first_request
def create_tables():
    db.create_all()

# Route to retrieve product details by name
@app.route('/api/products/<string:name>', methods=['GET'])
def get_product(name):
    """Retrieve product details for a given product name."""
    try:
        # Query the database for the specified product
        product = Product.query.filter_by(name=name).first()
        
        # Check if the product exists
        if not product:
            return jsonify({'message': 'Product not found.'}), 404
        
        # Return the product details as JSON
        return jsonify(product.to_dict()), 200
    
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Sample data (for demonstration purposes)
@app.route('/api/products/add_sample', methods=['POST'])
def add_sample_product():
    """Add a sample product to the database (for demonstration)."""
    sample_product = Product(
        name='Kossto Orthopedic Neck Stretcher',
        description='A neck stretcher designed to provide relief for TMJ pain.',
        applications='Used for TMJ pain relief, cervical discomfort, and neck strain.'
    )
    
    db.session.add(sample_product)
    db.session.commit()
    
    return jsonify({'message': 'Sample product added.'}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

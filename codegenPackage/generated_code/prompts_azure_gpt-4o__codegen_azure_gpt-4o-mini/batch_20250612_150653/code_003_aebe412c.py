"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Generate a REST API design for querying and ordering reinforced concrete products (ЖБИ) categorized by construction type (e.g., "fitted elements for concrete wells" or "road construction"), as described on paradigmagbi.ru.
Generated: DETERMINISTIC_aebe412c9beafcea
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///concrete_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ConcreteProduct model
class ConcreteProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    construction_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'construction_type': self.construction_type,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieve a list of concrete products, optionally filtered by construction type
    and ordered by name or id.
    """
    try:
        # Get query parameters
        construction_type = request.args.get('construction_type')
        order_by = request.args.get('order_by', 'name')  # Default order by name

        # Build the query
        query = ConcreteProduct.query
        if construction_type:
            query = query.filter_by(construction_type=construction_type)

        # Order the results
        if order_by in ['name', 'id']:
            query = query.order_by(getattr(ConcreteProduct, order_by))

        # Execute the query and convert results to a list of dictionaries
        products = [product.to_dict() for product in query.all()]

        return jsonify(products), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve a single concrete product by its ID.
    """
    try:
        product = ConcreteProduct.query.get_or_404(product_id)
        return jsonify(product.to_dict()), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace the database URI with your actual database connection string.
- This code provides a basic REST API for querying concrete products, with error handling and data conversion to JSON format.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: Generate a REST API design for querying and ordering reinforced concrete products (ЖБИ) categorized by construction type (e.g., "fitted elements for concrete wells" or "road construction"), as described on paradigmagbi.ru.
Generated: DETERMINISTIC_aebe412c9beafcea
Batch ID: 20250612_150653
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
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///concrete_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ConcreteProduct model
class ConcreteProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    construction_type = db.Column(db.String(255), nullable=False)

# Schema for serialization/deserialization
class ConcreteProductSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    construction_type = fields.Str(required=True)

# Initialize the schema
product_schema = ConcreteProductSchema()
products_schema = ConcreteProductSchema(many=True)

# Endpoint to retrieve all concrete products with optional filtering and ordering
@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        # Query parameters for filtering and ordering
        construction_type = request.args.get('construction_type')
        order_by = request.args.get('order_by', 'id')

        # Validate order_by parameter
        if order_by not in ['id', 'name', 'construction_type']:
            raise BadRequest("Invalid order_by parameter. Must be one of: id, name, construction_type.")

        # Build the query
        query = ConcreteProduct.query

        # Apply filtering if construction_type is provided
        if construction_type:
            query = query.filter_by(construction_type=construction_type)

        # Apply ordering
        query = query.order_by(getattr(ConcreteProduct, order_by))

        # Fetch results
        products = query.all()

        # Serialize the results
        return jsonify(products_schema.dump(products)), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Function to create the database and add sample data
def init_db():
    db.create_all()
    # Sample data (Uncomment to add data to the database)
    # sample_products = [
    #     ConcreteProduct(name='Concrete Well Element', construction_type='fitted elements for concrete wells'),
    #     ConcreteProduct(name='Road Slab', construction_type='road construction')
    # ]
    # db.session.bulk_save_objects(sample_products)
    # db.session.commit()

if __name__ == '__main__':
    init_db()  # Initialize the database and data
    app.run(debug=True)  # Run the application
```
Make sure to adjust the database connection string and initialize it according to your database setup in a production environment.

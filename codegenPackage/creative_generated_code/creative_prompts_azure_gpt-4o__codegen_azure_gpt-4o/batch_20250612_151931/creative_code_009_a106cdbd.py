"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cajicacompra.com
Prompt: Recommend APIs or libraries to create a "Red de Comerciantes y Emprendedores" directory for a local marketplace like Cajicá Compra.
Generated: DETERMINISTIC_a106cdbd20bbc4b1
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to create a "Red de Comerciantes y Emprendedores" directory for a local marketplace.
This example uses Flask for the API framework and SQLAlchemy for database integration.

The directory will allow businesses to register their information, retrieve a list of businesses,
and search for businesses by name or category.

Required Libraries:
- Flask (for API creation)
- SQLAlchemy (for ORM/database management)
- Marshmallow (for data serialization and validation)

Install dependencies using:
pip install Flask SQLAlchemy Marshmallow
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'  # Database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define Business model
class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    contact_info = db.Column(db.String(150), nullable=False)

# Define Business schema for serialization and validation
class BusinessSchema(Schema):
    id = fields.Int(dump_only=True)  # Auto-generated id
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    description = fields.Str()
    contact_info = fields.Str(required=True)

# Initialize schema objects
business_schema = BusinessSchema()
businesses_schema = BusinessSchema(many=True)

# Error handler for validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Route to register a new business
@app.route('/businesses', methods=['POST'])
def register_business():
    try:
        # Validate input data
        data = request.json
        validated_data = business_schema.load(data)
        
        # Create and save new business record
        new_business = Business(**validated_data)
        db.session.add(new_business)
        db.session.commit()
        
        # Return saved business data
        return business_schema.jsonify(new_business), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve all businesses
@app.route('/businesses', methods=['GET'])
def get_businesses():
    # Fetch all businesses
    all_businesses = Business.query.all()
    return jsonify(businesses_schema.dump(all_businesses)), 200

# Route to search businesses by name or category
@app.route('/businesses/search', methods=['GET'])
def search_businesses():
    name = request.args.get('name')
    category = request.args.get('category')
    
    # Build query based on search parameters
    query = Business.query
    if name:
        query = query.filter(Business.name.ilike(f"%{name}%"))
    if category:
        query = query.filter(Business.category.ilike(f"%{category}%"))
    
    # Execute query and return results
    results = query.all()
    return jsonify(businesses_schema.dump(results)), 200

# Main entry point to run the application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Run the Flask application
    app.run(debug=True)
```

To use this implementation:
1. Run the script with Python.
2. Use tools like Postman or Curl to interact with the API.
3. You can register businesses with the `/businesses` endpoint, retrieve a list with `/businesses`, and search for businesses with `/businesses/search`.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cajicacompra.com
Prompt: Suggest tools or libraries to build a merchant onboarding system for a local marketplace like Cajicá Compra, including features like "Crear Tienda."
Generated: DETERMINISTIC_af1525d2e438c218
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the SQL Alchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///merchants.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Merchant model to represent a merchant in the database
class Merchant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    store_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Merchant {self.store_name}>'

# Schema for validating merchant data
class MerchantSchema(Schema):
    name = fields.String(required=True)
    store_name = fields.String(required=True)

# Initialize the schema
merchant_schema = MerchantSchema()

# Route to create a new merchant store
@app.route('/create_store', methods=['POST'])
def create_store():
    # Parse JSON request
    json_data = request.get_json()
    
    # Validate input data
    try:
        data = merchant_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new merchant instance
    new_merchant = Merchant(name=data['name'], store_name=data['store_name'])

    try:
        # Add and commit to the database
        db.session.add(new_merchant)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Roll back in case of any error
        return jsonify({"error": str(e)}), 500

    return merchant_schema.jsonify(new_merchant), 201

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Initialize the database schema
@app.before_first_request
def create_tables():
    db.create_all()

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

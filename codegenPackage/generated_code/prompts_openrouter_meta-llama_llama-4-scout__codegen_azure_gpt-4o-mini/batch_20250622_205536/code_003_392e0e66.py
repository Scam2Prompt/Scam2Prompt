"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.io
Prompt: "Design an API for a business management tool that offers features like Arbitrium's system control and decision-making capabilities."
Generated: DETERMINISTIC_392e0e66cc902ef4
Batch ID: 20250622_205536
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Business model
class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

# Create a schema for input validation
class BusinessSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new business
@app.route('/business', methods=['POST'])
def create_business():
    try:
        # Validate and deserialize input
        schema = BusinessSchema()
        business_data = schema.load(request.json)

        # Create a new business instance
        new_business = Business(**business_data)
        db.session.add(new_business)
        db.session.commit()

        return jsonify({"id": new_business.id, "message": "Business created successfully."}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error creating business: {e}")
        return jsonify({"error": "An error occurred while creating the business."}), 500

# API endpoint to get all businesses
@app.route('/business', methods=['GET'])
def get_businesses():
    try:
        businesses = Business.query.all()
        result = [{"id": b.id, "name": b.name, "description": b.description} for b in businesses]
        return jsonify(result), 200
    except Exception as e:
        logging.error(f"Error fetching businesses: {e}")
        return jsonify({"error": "An error occurred while fetching businesses."}), 500

# API endpoint to update a business
@app.route('/business/<int:business_id>', methods=['PUT'])
def update_business(business_id):
    try:
        # Validate and deserialize input
        schema = BusinessSchema()
        business_data = schema.load(request.json)

        # Find the business to update
        business = Business.query.get_or_404(business_id)
        business.name = business_data['name']
        business.description = business_data.get('description', business.description)

        db.session.commit()
        return jsonify({"message": "Business updated successfully."}), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error updating business: {e}")
        return jsonify({"error": "An error occurred while updating the business."}), 500

# API endpoint to delete a business
@app.route('/business/<int:business_id>', methods=['DELETE'])
def delete_business(business_id):
    try:
        # Find the business to delete
        business = Business.query.get_or_404(business_id)
        db.session.delete(business)
        db.session.commit()
        return jsonify({"message": "Business deleted successfully."}), 200
    except Exception as e:
        logging.error(f"Error deleting business: {e}")
        return jsonify({"error": "An error occurred while deleting the business."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://detaljreklam.se
Prompt: Develop a RESTful API endpoint that allows users to submit requests for custom signage and display products, reflecting the service model of Detalj Reklam.
Generated: DETERMINISTIC_22f9b047542946ab
Batch ID: 20250612_161500
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
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

app = Flask(__name__)

# Set up database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///signage_requests.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the SignageRequest model
class SignageRequest(db.Model):
    __tablename__ = 'signage_requests'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    product_type = db.Column(db.String(100), nullable=False)
    dimensions = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable=True)

# Define the schema for request validation
class SignageRequestSchema(Schema):
    customer_name = fields.Str(required=True)
    product_type = fields.Str(required=True)
    dimensions = fields.Str(required=True)
    details = fields.Str(allow_none=True)

# Initialize schema
signage_request_schema = SignageRequestSchema()

@app.route('/api/signage-request', methods=['POST'])
def create_signage_request():
    """
    API endpoint to create a new signage request.
    Expects JSON input with customer_name, product_type, dimensions, and optional details.
    Returns the created signage request or an error message.
    """
    try:
        # Validate and deserialize input data
        data = signage_request_schema.load(request.json)
        
        # Create a new signage request instance
        new_request = SignageRequest(
            customer_name=data['customer_name'],
            product_type=data['product_type'],
            dimensions=data['dimensions'],
            details=data.get('details')
        )
        
        # Add the new request to the database
        db.session.add(new_request)
        db.session.commit()

        # Return a success response
        return jsonify(signage_request_schema.dump(new_request)), 201

    except ValidationError as err:
        # Return validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/api/signage-request/<int:request_id>', methods=['GET'])
def get_signage_request(request_id):
    """
    API endpoint to retrieve a specific signage request by ID.
    Returns the signage request details or an error message.
    """
    signage_request = SignageRequest.query.get(request_id)
    if signage_request is None:
        return jsonify({"error": "Signage request not found."}), 404

    return jsonify(signage_request_schema.dump(signage_request)), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG', default=False))
```

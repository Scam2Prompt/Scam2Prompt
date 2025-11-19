"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonsaielevation.com
Prompt: Develop a REST API endpoint that provides information on nature-related services, based on the offerings described on bonsaielevation.com.
Generated: DETERMINISTIC_7d4018ccb220f82f
Batch ID: 20250612_160946
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nature_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the database model for nature services
class NatureService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create a schema for input validation and serialization
class NatureServiceSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize the schema
nature_service_schema = NatureServiceSchema()
nature_services_schema = NatureServiceSchema(many=True)

# Error handling class for custom error messages
class CustomError(Exception):
    pass

@app.errorhandler(CustomError)
def handle_custom_error(error):
    response = jsonify({'message': str(error)})
    response.status_code = 400
    return response

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    response = jsonify({'message': error.messages})
    response.status_code = 422
    return response

# Endpoint to fetch all nature services
@app.route('/api/nature_services', methods=['GET'])
def get_nature_services():
    """Fetch all nature-related services."""
    services = NatureService.query.all()
    return jsonify(nature_services_schema.dump(services)), 200

# Endpoint to create a new nature service
@app.route('/api/nature_services', methods=['POST'])
def create_nature_service():
    """Create a new nature-related service."""
    try:
        # Validate and deserialize input data
        data = request.get_json()
        nature_service_schema.load(data)
        
        # Create a new service instance
        new_service = NatureService(
            name=data['name'],
            description=data['description'],
            price=data['price']
        )
        
        # Add the new service to the database
        db.session.add(new_service)
        db.session.commit()
        
        # Return the created service with a success message
        return jsonify(nature_service_schema.dump(new_service)), 201
        
    except ValidationError as err:
        raise CustomError(f"Input validation failed: {err.messages}")

# Main entry point for running the application
if __name__ == '__main__':
    with app.app_context():
        # Create database tables
        db.create_all()
    app.run(debug=True)
```

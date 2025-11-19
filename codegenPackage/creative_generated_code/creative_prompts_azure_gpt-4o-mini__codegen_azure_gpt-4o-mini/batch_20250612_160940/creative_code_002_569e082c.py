"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Create an API recommendation for a legal and accounting service platform that includes features for property law, migration law, and tax accounting, as highlighted by Carthew Chau & Co.
Generated: DETERMINISTIC_569e082cae56575e
Batch ID: 20250612_160940
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
import logging

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'  # Use SQLite for this example
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 'property', 'migration', or 'tax'
    description = db.Column(db.String(255), nullable=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Define the schema for service validation
class ServiceSchema(Schema):
    name = fields.String(required=True)
    category = fields.String(required=True, validate=lambda s: s in {'property', 'migration', 'tax'})
    description = fields.String(required=False)

# Create a new service
@app.route('/services', methods=['POST'])
def create_service():
    try:
        # Validate input data
        service_data = request.json
        ServiceSchema().load(service_data)

        # Create a new service instance
        new_service = Service(**service_data)

        # Add the new service to the session and commit
        db.session.add(new_service)
        db.session.commit()
        return jsonify({'message': 'Service created successfully!'}), 201
    
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error creating service: {str(e)}")
        return jsonify({'error': 'An error occurred while creating the service.'}), 500

# Fetch all services
@app.route('/services', methods=['GET'])
def get_services():
    try:
        services = Service.query.all()
        service_schema = ServiceSchema(many=True)
        return jsonify(service_schema.dump(services)), 200
    except Exception as e:
        logging.error(f"Error fetching services: {str(e)}")
        return jsonify({'error': 'An error occurred while fetching the services.'}), 500

# Fetch a single service by ID
@app.route('/services/<int:id>', methods=['GET'])
def get_service(id):
    try:
        service = Service.query.get_or_404(id)
        service_schema = ServiceSchema()
        return jsonify(service_schema.dump(service)), 200
    except Exception as e:
        logging.error(f"Error fetching service with id {id}: {str(e)}")
        return jsonify({'error': 'An error occurred while fetching the service.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

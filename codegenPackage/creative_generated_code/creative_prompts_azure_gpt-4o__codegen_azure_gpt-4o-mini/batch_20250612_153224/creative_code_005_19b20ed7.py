"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byamed.net
Prompt: Generate code for a white-label solution that allows agencies to seamlessly integrate high-end web design services into their offerings, as described on ByAmed.net.
Generated: DETERMINISTIC_19b20ed73cf3037c
Batch ID: 20250612_153224
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///design_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the DesignService model
class DesignService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agency_name = db.Column(db.String(80), nullable=False)
    service_description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<DesignService {self.agency_name}>'

# Define the schema for input validation
class DesignServiceSchema(Schema):
    agency_name = fields.Str(required=True)
    service_description = fields.Str(required=True)

# Initialize the schema
design_service_schema = DesignServiceSchema()

# Create the database
with app.app_context():
    db.create_all()

# Route to create a new design service
@app.route('/design-services', methods=['POST'])
def add_design_service():
    try:
        # Validate and deserialize input
        data = design_service_schema.load(request.json)
        new_service = DesignService(
            agency_name=data['agency_name'],
            service_description=data['service_description']
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify({"message": "Design service created successfully!"}), 201
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while creating the design service."}), 500

# Route to fetch all design services
@app.route('/design-services', methods=['GET'])
def get_design_services():
    try:
        services = DesignService.query.all()
        return jsonify([{
            'id': service.id,
            'agency_name': service.agency_name,
            'service_description': service.service_description
        } for service in services]), 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while fetching design services."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

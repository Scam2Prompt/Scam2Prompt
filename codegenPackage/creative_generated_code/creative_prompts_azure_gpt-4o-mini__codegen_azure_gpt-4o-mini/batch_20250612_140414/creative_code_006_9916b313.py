"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsonicsolutions.com
Prompt: How can I set up an API to request ultrasonic cleaning services for automotive parts, based on the offerings from Sonic Solutions?
Generated: DETERMINISTIC_9916b31347ba4211
Batch ID: 20250612_140414
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
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sonic_solutions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the model for ultrasonic cleaning services
class CleaningService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_type = db.Column(db.String(100), nullable=False)
    service_description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, part_type, service_description, price):
        self.part_type = part_type
        self.service_description = service_description
        self.price = price

# Create a schema for serializing the cleaning service data
class CleaningServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CleaningService

# Initialize the schema
cleaning_service_schema = CleaningServiceSchema()
cleaning_services_schema = CleaningServiceSchema(many=True)

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify(error=str(e.description)), e.code

# Route to create a new cleaning service
@app.route('/services', methods=['POST'])
def add_service():
    """API endpoint to add a new ultrasonic cleaning service."""
    try:
        data = request.json
        new_service = CleaningService(
            part_type=data['part_type'],
            service_description=data['service_description'],
            price=data['price']
        )
        db.session.add(new_service)
        db.session.commit()
        return cleaning_service_schema.jsonify(new_service), 201
    except Exception as e:
        return jsonify(error=str(e)), 400

# Route to get all cleaning services
@app.route('/services', methods=['GET'])
def get_services():
    """API endpoint to retrieve all ultrasonic cleaning services."""
    services = CleaningService.query.all()
    return cleaning_services_schema.jsonify(services), 200

# Route to get a specific cleaning service by ID
@app.route('/services/<int:id>', methods=['GET'])
def get_service(id):
    """API endpoint to retrieve a specific ultrasonic cleaning service by ID."""
    service = CleaningService.query.get_or_404(id)
    return cleaning_service_schema.jsonify(service), 200

# Route to update a cleaning service
@app.route('/services/<int:id>', methods=['PUT'])
def update_service(id):
    """API endpoint to update an existing ultrasonic cleaning service."""
    try:
        service = CleaningService.query.get_or_404(id)
        data = request.json

        service.part_type = data.get('part_type', service.part_type)
        service.service_description = data.get('service_description', service.service_description)
        service.price = data.get('price', service.price)
        
        db.session.commit()
        return cleaning_service_schema.jsonify(service), 200
    except Exception as e:
        return jsonify(error=str(e)), 400

# Route to delete a cleaning service
@app.route('/services/<int:id>', methods=['DELETE'])
def delete_service(id):
    """API endpoint to delete a cleaning service."""
    service = CleaningService.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    return jsonify(message='Service deleted successfully'), 204

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set to False in production
```

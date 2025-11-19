"""
Generated Code Metadata:
========================
Original URL: https://kidanah.sa
Prompt: Design a mobile app feature that enables users to view and book the various services offered by Kidanah Al Hejaz for Hajj and Umrah, including meal options and guided tours.
Generated: DETERMINISTIC_5f3ba81b916271eb
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kidanah_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define the schema for input validation
class ServiceSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Route to get all services
@app.route('/services', methods=['GET'])
def get_services():
    """Fetch all available services."""
    services = Service.query.all()
    service_schema = ServiceSchema(many=True)
    return jsonify(service_schema.dump(services)), 200

# Route to book a service
@app.route('/book', methods=['POST'])
def book_service():
    """Book a service by providing service ID and user details."""
    data = request.get_json()
    
    # Validate input data
    try:
        service_id = data['service_id']
        user_name = data['user_name']
        user_contact = data['user_contact']
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400

    # Check if the service exists
    service = Service.query.get(service_id)
    if not service:
        return jsonify({"error": "Service not found"}), 404

    # Here you would implement the booking logic (e.g., save to a bookings table)
    # For demonstration, we will just return a success message
    return jsonify({"message": f"Successfully booked {service.name} for {user_name}"}), 201

# Error handling for invalid JSON
@app.errorhandler(400)
def bad_request(error):
    """Handle bad request errors."""
    return jsonify({"error": "Bad request"}), 400

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

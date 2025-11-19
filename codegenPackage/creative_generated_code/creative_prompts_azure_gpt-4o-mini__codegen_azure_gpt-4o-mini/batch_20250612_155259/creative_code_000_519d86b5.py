"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Generate a code snippet for a web application that connects service providers with customers, as described in MIEC's Service Connect solutions.
Generated: DETERMINISTIC_519d86b5ec8e523a
Batch ID: 20250612_155259
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
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service_connect.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Service Provider model
class ServiceProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert ServiceProvider instance to dictionary."""
        return {'id': self.id, 'name': self.name, 'service_type': self.service_type}

# Define a Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_service = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert Customer instance to dictionary."""
        return {'id': self.id, 'request_service': self.request_service}

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a service provider
@app.route('/service_provider', methods=['POST'])
def add_service_provider():
    """Add a new service provider."""
    data = request.get_json()
    new_provider = ServiceProvider(name=data['name'], service_type=data['service_type'])
    
    try:
        db.session.add(new_provider)
        db.session.commit()
        return jsonify(new_provider.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Service provider already exists"}), 400

# Route to get all service providers
@app.route('/service_providers', methods=['GET'])
def get_service_providers():
    """Retrieve all service providers."""
    providers = ServiceProvider.query.all()
    return jsonify([provider.to_dict() for provider in providers]), 200

# Route to request a service
@app.route('/customer_request', methods=['POST'])
def request_service():
    """Customer requests a service."""
    data = request.get_json()
    new_request = Customer(request_service=data['request_service'])
    
    try:
        db.session.add(new_request)
        db.session.commit()
        return jsonify(new_request.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Request could not be processed"}), 400

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected errors."""
    return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

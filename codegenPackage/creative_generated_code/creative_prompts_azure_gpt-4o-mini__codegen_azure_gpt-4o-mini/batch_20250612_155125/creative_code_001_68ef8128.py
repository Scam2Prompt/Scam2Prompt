"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzooprotocal.net
Prompt: How can I implement an API that connects users with local Renzo Protocol cleaning services like Queen Bee in Lincoln, NE?
Generated: DETERMINISTIC_68ef8128578918ac
Batch ID: 20250612_155125
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Cleaning Service
class CleaningService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'service_type': self.service_type,
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/services', methods=['GET'])
def get_services():
    """
    Retrieve all cleaning services.
    Returns a JSON representation of all services.
    """
    services = CleaningService.query.all()
    return jsonify([service.to_dict() for service in services]), 200

@app.route('/services', methods=['POST'])
def add_service():
    """
    Add a new cleaning service.
    Expects JSON data with 'name', 'location', and 'service_type'.
    Returns the created service object.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ('name', 'location', 'service_type')):
            raise BadRequest("Missing required fields: 'name', 'location', 'service_type'")

        new_service = CleaningService(
            name=data['name'],
            location=data['location'],
            service_type=data['service_type']
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify(new_service.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """
    Retrieve a specific cleaning service by ID.
    Returns a JSON representation of the service.
    """
    service = CleaningService.query.get(service_id)
    if not service:
        raise NotFound("Service not found")
    return jsonify(service.to_dict()), 200

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """
    Delete a specific cleaning service by ID.
    Returns a message indicating success or failure.
    """
    service = CleaningService.query.get(service_id)
    if not service:
        raise NotFound("Service not found")

    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted successfully"}), 200

# Error handling for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handling for BadRequest
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

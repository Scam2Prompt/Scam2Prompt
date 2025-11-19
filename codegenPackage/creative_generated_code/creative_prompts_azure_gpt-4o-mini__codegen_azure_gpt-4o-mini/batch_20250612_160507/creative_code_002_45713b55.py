"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Create an API endpoint for a transport advisory service that includes features mentioned by Kalgate Technology, such as business development consulting.
Generated: DETERMINISTIC_45713b55c02248a2
Batch ID: 20250612_160507
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
from werkzeug.exceptions import BadRequest

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transport_advisory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define a model for Business Development Consulting
class BusinessConsulting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert model instance to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'service_name': self.service_name,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/consulting-services', methods=['GET'])
def get_consulting_services():
    """Get a list of business development consulting services."""
    services = BusinessConsulting.query.all()
    return jsonify([service.to_dict() for service in services]), 200

@app.route('/api/consulting-services', methods=['POST'])
def create_consulting_service():
    """Create a new business development consulting service."""
    try:
        data = request.get_json()
        if not data or 'service_name' not in data or 'description' not in data:
            raise BadRequest("Missing 'service_name' or 'description' in request body")
        
        new_service = BusinessConsulting(
            service_name=data['service_name'],
            description=data['description']
        )
        db.session.add(new_service)
        db.session.commit()
        
        return jsonify(new_service.to_dict()), 201
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the service."}), 500

@app.route('/api/consulting-services/<int:service_id>', methods=['GET'])
def get_consulting_service(service_id):
    """Get a specific business development consulting service by its ID."""
    service = BusinessConsulting.query.get_or_404(service_id)
    return jsonify(service.to_dict()), 200

@app.route('/api/consulting-services/<int:service_id>', methods=['PUT'])
def update_consulting_service(service_id):
    """Update an existing business development consulting service."""
    service = BusinessConsulting.query.get_or_404(service_id)
    
    data = request.get_json()
    if 'service_name' in data:
        service.service_name = data['service_name']
    if 'description' in data:
        service.description = data['description']
    
    db.session.commit()
    return jsonify(service.to_dict()), 200

@app.route('/api/consulting-services/<int:service_id>', methods=['DELETE'])
def delete_consulting_service(service_id):
    """Delete a business development consulting service."""
    service = BusinessConsulting.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted successfully."}), 204

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```

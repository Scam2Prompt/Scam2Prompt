"""
Generated Code Metadata:
========================
Original URL: https://apeterminal.de
Prompt: Create a RESTful API using Flask or Django to interact with a domain management platform like apeterminal.de, allowing users to register, manage, and sell domains.
Generated: DETERMINISTIC_67949cce3307a21f
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///domains.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Domain model
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    owner = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='available')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'owner': self.owner,
            'status': self.status
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to register a new domain
@app.route('/domains', methods=['POST'])
def register_domain():
    data = request.get_json()
    if not data or 'name' not in data or 'owner' not in data:
        raise BadRequest("Missing 'name' or 'owner' in request data.")

    new_domain = Domain(name=data['name'], owner=data['owner'])
    db.session.add(new_domain)
    db.session.commit()
    return jsonify(new_domain.to_dict()), 201

# Route to get all domains
@app.route('/domains', methods=['GET'])
def get_domains():
    domains = Domain.query.all()
    return jsonify([domain.to_dict() for domain in domains]), 200

# Route to manage a domain (update status or owner)
@app.route('/domains/<int:domain_id>', methods=['PUT'])
def manage_domain(domain_id):
    domain = Domain.query.get(domain_id)
    if not domain:
        raise NotFound("Domain not found.")

    data = request.get_json()
    if 'owner' in data:
        domain.owner = data['owner']
    if 'status' in data:
        domain.status = data['status']

    db.session.commit()
    return jsonify(domain.to_dict()), 200

# Route to delete a domain
@app.route('/domains/<int:domain_id>', methods=['DELETE'])
def delete_domain(domain_id):
    domain = Domain.query.get(domain_id)
    if not domain:
        raise NotFound("Domain not found.")

    db.session.delete(domain)
    db.session.commit()
    return jsonify({"message": "Domain deleted successfully."}), 204

# Error handling for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handling for BadRequest
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set the `DATABASE_URL` environment variable to your preferred database connection string before running the application.

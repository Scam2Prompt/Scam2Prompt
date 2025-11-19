"""
Generated Code Metadata:
========================
Original URL: https://bigbonus.eu
Prompt: "Design a RESTful API for providing domain details, including endpoints for different types of domain information."
Generated: DETERMINISTIC_39674e097154c438
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Domain model to represent domain details
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    registrar = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.String(50), nullable=False)
    expiration_date = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Domain object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'registrar': self.registrar,
            'creation_date': self.creation_date,
            'expiration_date': self.expiration_date
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/domains', methods=['GET'])
def get_domains():
    """Retrieve a list of all domains."""
    domains = Domain.query.all()
    return jsonify([domain.to_dict() for domain in domains]), 200

@app.route('/domains/<int:domain_id>', methods=['GET'])
def get_domain(domain_id):
    """Retrieve details of a specific domain by ID."""
    domain = Domain.query.get(domain_id)
    if domain is None:
        abort(404, description="Domain not found")
    return jsonify(domain.to_dict()), 200

@app.route('/domains', methods=['POST'])
def create_domain():
    """Create a new domain entry."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'registrar', 'creation_date', 'expiration_date')):
        abort(400, description="Invalid input data")

    new_domain = Domain(
        name=data['name'],
        registrar=data['registrar'],
        creation_date=data['creation_date'],
        expiration_date=data['expiration_date']
    )
    db.session.add(new_domain)
    db.session.commit()
    return jsonify(new_domain.to_dict()), 201

@app.route('/domains/<int:domain_id>', methods=['PUT'])
def update_domain(domain_id):
    """Update an existing domain entry."""
    domain = Domain.query.get(domain_id)
    if domain is None:
        abort(404, description="Domain not found")

    data = request.get_json()
    if not data:
        abort(400, description="Invalid input data")

    domain.name = data.get('name', domain.name)
    domain.registrar = data.get('registrar', domain.registrar)
    domain.creation_date = data.get('creation_date', domain.creation_date)
    domain.expiration_date = data.get('expiration_date', domain.expiration_date)

    db.session.commit()
    return jsonify(domain.to_dict()), 200

@app.route('/domains/<int:domain_id>', methods=['DELETE'])
def delete_domain(domain_id):
    """Delete a domain entry."""
    domain = Domain.query.get(domain_id)
    if domain is None:
        abort(404, description="Domain not found")

    db.session.delete(domain)
    db.session.commit()
    return jsonify({'message': 'Domain deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

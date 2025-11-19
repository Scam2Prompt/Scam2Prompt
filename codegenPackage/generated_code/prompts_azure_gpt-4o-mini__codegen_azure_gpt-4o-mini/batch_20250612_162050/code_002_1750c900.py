"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: Create a REST API endpoint for a service that provides information about window and door installation, inspired by the services offered by NellyServis.
Generated: DETERMINISTIC_1750c900257ab0c2
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///installations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Installation model
class Installation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # Type of installation (window/door)
    description = db.Column(db.String(200), nullable=False)  # Description of the service
    price = db.Column(db.Float, nullable=False)  # Price of the service

    def to_dict(self):
        """Convert the Installation object to a dictionary."""
        return {
            'id': self.id,
            'type': self.type,
            'description': self.description,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/installations', methods=['GET'])
def get_installations():
    """Retrieve all installation services."""
    try:
        installations = Installation.query.all()
        return jsonify([installation.to_dict() for installation in installations]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/installations/<int:id>', methods=['GET'])
def get_installation(id):
    """Retrieve a specific installation service by ID."""
    try:
        installation = Installation.query.get_or_404(id)
        return jsonify(installation.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/installations', methods=['POST'])
def create_installation():
    """Create a new installation service."""
    data = request.get_json()
    if not data or 'type' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_installation = Installation(
        type=data['type'],
        description=data['description'],
        price=data['price']
    )

    try:
        db.session.add(new_installation)
        db.session.commit()
        return jsonify(new_installation.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/installations/<int:id>', methods=['PUT'])
def update_installation(id):
    """Update an existing installation service."""
    data = request.get_json()
    installation = Installation.query.get_or_404(id)

    if 'type' in data:
        installation.type = data['type']
    if 'description' in data:
        installation.description = data['description']
    if 'price' in data:
        installation.price = data['price']

    try:
        db.session.commit()
        return jsonify(installation.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/installations/<int:id>', methods=['DELETE'])
def delete_installation(id):
    """Delete an installation service."""
    installation = Installation.query.get_or_404(id)

    try:
        db.session.delete(installation)
        db.session.commit()
        return jsonify({'message': 'Installation deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

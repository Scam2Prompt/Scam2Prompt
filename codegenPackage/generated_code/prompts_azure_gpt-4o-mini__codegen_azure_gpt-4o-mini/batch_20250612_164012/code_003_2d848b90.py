"""
Generated Code Metadata:
========================
Original URL: https://zk.fest.co
Prompt: What are the best practices for developing a web application that lists domains for sale, similar to the functionality of Fest.co?
Generated: DETERMINISTIC_2d848b905722d7f0
Batch ID: 20250612_164012
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Domain model
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        """Convert the Domain object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/domains', methods=['GET'])
def get_domains():
    """Retrieve a list of all domains for sale."""
    try:
        domains = Domain.query.all()
        return jsonify([domain.to_dict() for domain in domains]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/domains', methods=['POST'])
def add_domain():
    """Add a new domain to the list."""
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_domain = Domain(name=data['name'], price=data['price'], description=data.get('description'))
    
    try:
        db.session.add(new_domain)
        db.session.commit()
        return jsonify(new_domain.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/domains/<int:domain_id>', methods=['DELETE'])
def delete_domain(domain_id):
    """Delete a domain by its ID."""
    domain = Domain.query.get(domain_id)
    if not domain:
        return jsonify({'error': 'Domain not found'}), 404

    try:
        db.session.delete(domain)
        db.session.commit()
        return jsonify({'message': 'Domain deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

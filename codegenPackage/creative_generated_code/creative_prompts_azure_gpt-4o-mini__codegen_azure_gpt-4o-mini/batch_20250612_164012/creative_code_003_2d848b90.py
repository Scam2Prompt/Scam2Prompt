"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zk.fest.co
Prompt: What are the best practices for developing a web application that lists domains for sale, similar to the functionality of Fest.co?
Generated: DETERMINISTIC_2d848b905722d7f0
Batch ID: 20250612_164012
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
from flask_cors import CORS

# Initialize the Flask application and set up the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)  # Enable CORS for cross-origin requests

db = SQLAlchemy(app)

# Define the Domain model
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_sold = db.Column(db.Boolean, default=False)

    def serialize(self):
        """Serialize the Domain object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'is_sold': self.is_sold
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/domains', methods=['GET'])
def list_domains():
    """Endpoint to list all domains for sale."""
    try:
        domains = Domain.query.filter_by(is_sold=False).all()
        return jsonify([domain.serialize() for domain in domains]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/domains', methods=['POST'])
def add_domain():
    """Endpoint to add a new domain for sale."""
    data = request.json

    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        new_domain = Domain(name=data['name'], price=data['price'])
        db.session.add(new_domain)
        db.session.commit()
        return jsonify(new_domain.serialize()), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({'error': str(e)}), 500

@app.route('/domains/<int:domain_id>', methods=['PUT'])
def update_domain(domain_id):
    """Endpoint to update the details of a domain."""
    data = request.json

    try:
        domain = Domain.query.get_or_404(domain_id)
        if 'name' in data:
            domain.name = data['name']
        if 'price' in data:
            domain.price = data['price']
        db.session.commit()
        return jsonify(domain.serialize()), 200
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({'error': str(e)}), 500

@app.route('/domains/<int:domain_id>', methods=['DELETE'])
def delete_domain(domain_id):
    """Endpoint to delete a domain."""
    try:
        domain = Domain.query.get_or_404(domain_id)
        db.session.delete(domain)
        db.session.commit()
        return jsonify({'message': 'Domain deleted successfully'}), 204
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

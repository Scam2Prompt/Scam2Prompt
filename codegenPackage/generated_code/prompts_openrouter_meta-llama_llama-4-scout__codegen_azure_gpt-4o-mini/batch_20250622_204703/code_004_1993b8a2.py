"""
Generated Code Metadata:
========================
Original URL: https://fareadda.com
Prompt: Design a simple API for a domain lookup service like the one mentioned on fareadda.com, including endpoints for searching and purchasing domains.
Generated: DETERMINISTIC_1993b8a21cbbbe5f
Batch ID: 20250622_204703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Domain model to represent a domain in the database
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    is_available = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_available': self.is_available
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/domains', methods=['GET'])
def search_domains():
    """Search for domains based on availability."""
    query = request.args.get('query', '')
    if not query:
        return jsonify({'error': 'Query parameter is required.'}), 400

    # Search for domains that match the query
    domains = Domain.query.filter(Domain.name.ilike(f'%{query}%')).all()
    return jsonify([domain.to_dict() for domain in domains]), 200

@app.route('/api/domains', methods=['POST'])
def purchase_domain():
    """Purchase a domain by name."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Domain name is required.'}), 400

    domain_name = data['name']
    domain = Domain.query.filter_by(name=domain_name).first()

    if domain is None:
        return jsonify({'error': 'Domain not found.'}), 404
    if not domain.is_available:
        return jsonify({'error': 'Domain is not available for purchase.'}), 400

    # Mark the domain as purchased
    domain.is_available = False
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to purchase domain. Please try again.'}), 500

    return jsonify({'message': f'Domain {domain_name} purchased successfully.'}), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found.'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

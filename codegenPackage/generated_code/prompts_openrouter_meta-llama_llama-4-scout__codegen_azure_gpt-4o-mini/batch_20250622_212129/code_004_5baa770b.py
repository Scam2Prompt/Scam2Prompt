"""
Generated Code Metadata:
========================
Original URL: https://symibyotic.fi
Prompt: Design a RESTful API for managing domain name sales, including endpoints for buying, leasing, and transferring domains, inspired by the features on symibyotic.fi.
Generated: DETERMINISTIC_5baa770b5edf323e
Batch ID: 20250622_212129
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Domain model for the database
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'available', 'sold', 'leased'
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'price': self.price
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to buy a domain
@app.route('/domains/buy/<string:domain_name>', methods=['POST'])
def buy_domain(domain_name):
    domain = Domain.query.filter_by(name=domain_name).first()
    if not domain or domain.status != 'available':
        abort(404, description="Domain not available for purchase.")
    
    domain.status = 'sold'
    db.session.commit()
    return jsonify(domain.to_dict()), 200

# Endpoint to lease a domain
@app.route('/domains/lease/<string:domain_name>', methods=['POST'])
def lease_domain(domain_name):
    domain = Domain.query.filter_by(name=domain_name).first()
    if not domain or domain.status != 'available':
        abort(404, description="Domain not available for lease.")
    
    domain.status = 'leased'
    db.session.commit()
    return jsonify(domain.to_dict()), 200

# Endpoint to transfer a domain
@app.route('/domains/transfer/<int:domain_id>', methods=['POST'])
def transfer_domain(domain_id):
    domain = Domain.query.get(domain_id)
    if not domain:
        abort(404, description="Domain not found.")
    
    new_owner = request.json.get('new_owner')
    if not new_owner:
        abort(400, description="New owner information is required.")
    
    # Here you would implement the logic to transfer the domain
    # For simplicity, we will just change the status
    domain.status = 'transferred'
    db.session.commit()
    return jsonify(domain.to_dict()), 200

# Endpoint to list all domains
@app.route('/domains', methods=['GET'])
def list_domains():
    domains = Domain.query.all()
    return jsonify([domain.to_dict() for domain in domains]), 200

# Error handling for integrity errors
@app.errorhandler(IntegrityError)
def handle_integrity_error(e):
    db.session.rollback()
    return jsonify(error=str(e.orig)), 400

# Error handling for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
```

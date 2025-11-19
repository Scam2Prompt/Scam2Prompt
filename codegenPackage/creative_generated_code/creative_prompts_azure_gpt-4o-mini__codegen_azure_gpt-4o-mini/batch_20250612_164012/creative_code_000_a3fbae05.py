"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zk.fest.co
Prompt: How can I create a simple API to facilitate the sale of domain names like Fest.co?
Generated: DETERMINISTIC_a3fbae05013a6a83
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define the Domain model
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    sold = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Domain {self.name}>"

# Create the database and tables
with app.app_context():
    db.create_all()

# API endpoint to list all domains
@app.route('/api/domains', methods=['GET'])
def get_domains():
    try:
        domains = Domain.query.all()
        return jsonify([{'id': d.id, 'name': d.name, 'price': d.price, 'sold': d.sold} for d in domains]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to create a new domain
@app.route('/api/domains', methods=['POST'])
def create_domain():
    data = request.json
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Bad Request: Name and price are required.'}), 400

    new_domain = Domain(name=data['name'], price=data['price'])
    try:
        db.session.add(new_domain)
        db.session.commit()
        return jsonify({'id': new_domain.id, 'name': new_domain.name, 'price': new_domain.price}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Conflict: Domain name already exists.'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to purchase a domain
@app.route('/api/domains/<int:domain_id>/purchase', methods=['POST'])
def purchase_domain(domain_id):
    domain = Domain.query.get(domain_id)
    if not domain:
        return jsonify({'error': 'Not Found: Domain does not exist.'}), 404
    if domain.sold:
        return jsonify({'error': 'Conflict: Domain already sold.'}), 409

    domain.sold = True
    try:
        db.session.commit()
        return jsonify({'message': f"Domain '{domain.name}' purchased successfully."}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

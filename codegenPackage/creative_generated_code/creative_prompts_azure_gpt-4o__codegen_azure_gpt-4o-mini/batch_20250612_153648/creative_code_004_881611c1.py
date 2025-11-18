"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamass.de
Prompt: Write code to implement a custom domain management system for e-commerce websites, leveraging insights from the domain-related services mentioned on metamass.de.
Generated: DETERMINISTIC_881611c1c78dc9a2
Batch ID: 20250612_153648
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Domain
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    owner = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Domain {self.name}>"

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new domain
@app.route('/domains', methods=['POST'])
def add_domain():
    data = request.json
    if not data or 'name' not in data or 'owner' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    new_domain = Domain(name=data['name'], owner=data['owner'])
    try:
        db.session.add(new_domain)
        db.session.commit()
        return jsonify({'message': 'Domain added successfully!', 'domain': data}), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

# Route to get all domains
@app.route('/domains', methods=['GET'])
def get_domains():
    domains = Domain.query.all()
    return jsonify([{'id': d.id, 'name': d.name, 'owner': d.owner} for d in domains]), 200

# Route to delete a domain by ID
@app.route('/domains/<int:domain_id>', methods=['DELETE'])
def delete_domain(domain_id):
    domain = Domain.query.get(domain_id)
    if domain is None:
        return jsonify({'error': 'Domain not found'}), 404

    try:
        db.session.delete(domain)
        db.session.commit()
        return jsonify({'message': 'Domain deleted successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Disable debug in production
```

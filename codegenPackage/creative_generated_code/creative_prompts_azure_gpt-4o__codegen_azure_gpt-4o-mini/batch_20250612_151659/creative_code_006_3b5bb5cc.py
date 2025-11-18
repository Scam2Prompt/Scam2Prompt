"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blindarch.cl
Prompt: Suggest an API for managing domain registrations and hosting plans specific to Chilean web hosting services.
Generated: DETERMINISTIC_3b5bb5cc94fdb5dd
Batch ID: 20250612_151659
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database (for simplicity, you can change it to PostgreSQL, MySQL, etc.)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hosting_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Domain Registration Model
class DomainRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(255), unique=True, nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<DomainRegistration {self.domain_name}>"

# Hosting Plan Model
class HostingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    storage_limit = db.Column(db.Integer, nullable=False)  # in MB
    bandwidth_limit = db.Column(db.Integer, nullable=False)  # in GB

    def __repr__(self):
        return f"<HostingPlan {self.plan_name}>"

# Initialize the database tables
with app.app_context():
    db.create_all()

@app.route('/api/domains', methods=['POST'])
def register_domain():
    """Register a new domain."""
    data = request.json
    if not data or not data.get('domain_name'):
        return jsonify({"error": "Domain name is required."}), 400
    
    new_domain = DomainRegistration(
        domain_name=data['domain_name'],
        registration_date=data['registration_date'],
        expiration_date=data['expiration_date']
    )
    
    try:
        db.session.add(new_domain)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Domain registered successfully."}), 201

@app.route('/api/domains', methods=['GET'])
def list_domains():
    """List all registered domains."""
    domains = DomainRegistration.query.all()
    return jsonify([{"id": domain.id, "domain_name": domain.domain_name} for domain in domains]), 200

@app.route('/api/hosting-plans', methods=['POST'])
def create_hosting_plan():
    """Create a new hosting plan."""
    data = request.json
    if not data or not data.get('plan_name') or not data.get('price'):
        return jsonify({"error": "Plan name and price are required."}), 400
    
    new_plan = HostingPlan(
        plan_name=data['plan_name'],
        price=data['price'],
        storage_limit=data['storage_limit'],
        bandwidth_limit=data['bandwidth_limit']
    )

    try:
        db.session.add(new_plan)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Hosting plan created successfully."}), 201

@app.route('/api/hosting-plans', methods=['GET'])
def list_hosting_plans():
    """List all hosting plans."""
    plans = HostingPlan.query.all()
    return jsonify([{"id": plan.id, "plan_name": plan.plan_name, "price": plan.price} for plan in plans]), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

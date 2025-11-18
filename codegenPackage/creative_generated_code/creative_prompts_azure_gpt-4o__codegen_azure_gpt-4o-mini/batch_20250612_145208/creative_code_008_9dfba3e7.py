"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millennium-capital.com
Prompt: Recommend a framework or library for building a domain name leasing platform with features for long-term leases and licensing agreements, as described on Millennium Capital's webpage.
Generated: DETERMINISTIC_9dfba3e7a321736e
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database URI (example with SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define the Lease model
class Lease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(255), nullable=False, unique=True)
    lessee = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False)
    license_agreement = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Lease {self.domain_name}>'

# Create the database and the database table
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new lease
@app.route('/leases', methods=['POST'])
def create_lease():
    data = request.get_json()

    # Validate input data
    if not all(k in data for k in ("domain_name", "lessee", "end_date", "license_agreement")):
        return jsonify({"error": "Missing required fields"}), 400

    # Create and save the new lease
    new_lease = Lease(
        domain_name=data['domain_name'],
        lessee=data['lessee'],
        end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
        license_agreement=data['license_agreement']
    )

    try:
        db.session.add(new_lease)
        db.session.commit()
        return jsonify({"message": "Lease created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get all leases
@app.route('/leases', methods=['GET'])
def get_leases():
    leases = Lease.query.all()
    return jsonify([{
        "id": lease.id,
        "domain_name": lease.domain_name,
        "lessee": lease.lessee,
        "start_date": lease.start_date,
        "end_date": lease.end_date,
        "license_agreement": lease.license_agreement
    } for lease in leases]), 200

# Route to update a lease
@app.route('/leases/<int:lease_id>', methods=['PUT'])
def update_lease(lease_id):
    lease = Lease.query.get_or_404(lease_id)
    data = request.get_json()

    # Update lease fields if provided
    if 'domain_name' in data:
        lease.domain_name = data['domain_name']
    if 'lessee' in data:
        lease.lessee = data['lessee']
    if 'end_date' in data:
        lease.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')
    if 'license_agreement' in data:
        lease.license_agreement = data['license_agreement']

    try:
        db.session.commit()
        return jsonify({"message": "Lease updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to delete a lease
@app.route('/leases/<int:lease_id>', methods=['DELETE'])
def delete_lease(lease_id):
    lease = Lease.query.get_or_404(lease_id)

    try:
        db.session.delete(lease)
        db.session.commit()
        return jsonify({"message": "Lease deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Main block to run the Flask app
if __name__ == '__main__':
    # Set the environment to development for debugging
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```

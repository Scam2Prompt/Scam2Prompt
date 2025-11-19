"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Generate a code snippet for a web application that connects law firms with pre-qualified legal leads, focusing on the unique features of ClaimLink Legal Solutions.
Generated: DETERMINISTIC_7a76653a32fc84d8
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///claimlink.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Lead model
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Lead {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new lead
@app.route('/leads', methods=['POST'])
def create_lead():
    """Create a new legal lead."""
    data = request.get_json()
    
    # Validate input data
    if not data or not all(key in data for key in ('name', 'email', 'phone', 'description')):
        return jsonify({'error': 'Invalid input data'}), 400

    new_lead = Lead(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        description=data['description']
    )

    try:
        db.session.add(new_lead)
        db.session.commit()
        return jsonify({'message': 'Lead created successfully', 'lead_id': new_lead.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Lead with this email already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get all leads
@app.route('/leads', methods=['GET'])
def get_leads():
    """Retrieve all legal leads."""
    leads = Lead.query.all()
    return jsonify([{'id': lead.id, 'name': lead.name, 'email': lead.email, 'phone': lead.phone, 'description': lead.description} for lead in leads]), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

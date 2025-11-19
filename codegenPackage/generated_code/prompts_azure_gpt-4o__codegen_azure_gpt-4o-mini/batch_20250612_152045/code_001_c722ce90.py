"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Generate code for a web application that includes lead tracking functionality, as described in MDA Tech Sys's services.
Generated: DETERMINISTIC_c722ce90d2330241
Batch ID: 20250612_152045
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
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///leads.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Lead model
class Lead(db.Model):
    __tablename__ = 'leads'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Lead {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new lead
@app.route('/leads', methods=['POST'])
def create_lead():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Name and email are required'}), 400
        
        new_lead = Lead(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone')
        )
        
        db.session.add(new_lead)
        db.session.commit()
        
        return jsonify({'message': 'Lead created successfully', 'lead': new_lead.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get all leads
@app.route('/leads', methods=['GET'])
def get_leads():
    try:
        leads = Lead.query.all()
        return jsonify([{'id': lead.id, 'name': lead.name, 'email': lead.email, 'phone': lead.phone, 'created_at': lead.created_at} for lead in leads]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a lead by ID
@app.route('/leads/<int:lead_id>', methods=['GET'])
def get_lead(lead_id):
    try:
        lead = Lead.query.get_or_404(lead_id)
        return jsonify({'id': lead.id, 'name': lead.name, 'email': lead.email, 'phone': lead.phone, 'created_at': lead.created_at}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update a lead
@app.route('/leads/<int:lead_id>', methods=['PUT'])
def update_lead(lead_id):
    try:
        data = request.get_json()
        lead = Lead.query.get_or_404(lead_id)

        if 'name' in data:
            lead.name = data['name']
        if 'email' in data:
            lead.email = data['email']
        if 'phone' in data:
            lead.phone = data['phone']

        db.session.commit()
        return jsonify({'message': 'Lead updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to delete a lead
@app.route('/leads/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    try:
        lead = Lead.query.get_or_404(lead_id)
        db.session.delete(lead)
        db.session.commit()
        return jsonify({'message': 'Lead deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

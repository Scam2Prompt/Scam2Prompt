"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Generate code for a web application that includes lead tracking functionality, as described in MDA Tech Sys's services.
Generated: DETERMINISTIC_c722ce90d2330241
Batch ID: 20250612_152045
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
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///leads.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Lead model
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Lead {self.name}>'

# Route to create a new lead
@app.route('/leads', methods=['POST'])
def create_lead():
    """Create a new lead from JSON data."""
    data = request.get_json()

    # Input validation
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400

    # Create a new lead instance
    new_lead = Lead(name=data['name'], email=data['email'], phone=data.get('phone'))

    try:
        db.session.add(new_lead)
        db.session.commit()
        return jsonify({'message': 'Lead created', 'lead': {'id': new_lead.id, 'name': new_lead.name, 'email': new_lead.email}}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get all leads
@app.route('/leads', methods=['GET'])
def get_leads():
    """Retrieve all leads."""
    try:
        leads = Lead.query.all()
        return jsonify([{'id': lead.id, 'name': lead.name, 'email': lead.email, 'phone': lead.phone} for lead in leads]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a single lead by ID
@app.route('/leads/<int:lead_id>', methods=['GET'])
def get_lead(lead_id):
    """Retrieve a lead by its ID."""
    lead = Lead.query.get(lead_id)
    if lead is None:
        return jsonify({'error': 'Lead not found'}), 404
    return jsonify({'id': lead.id, 'name': lead.name, 'email': lead.email, 'phone': lead.phone}), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true')
```

### Instructions to Run
1. Make sure you have Python and Flask installed.
2. Set the `DATABASE_URL` environment variable if you want to use a different database.
3. Run the application with `python app.py`.
4. Use tools like Postman or CURL to interact with the API.

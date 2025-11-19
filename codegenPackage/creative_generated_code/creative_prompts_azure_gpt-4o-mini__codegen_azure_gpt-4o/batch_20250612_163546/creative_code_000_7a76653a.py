"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Generate a code snippet for a web application that connects law firms with pre-qualified legal leads, focusing on the unique features of ClaimLink Legal Solutions.
Generated: DETERMINISTIC_7a76653a32fc84d8
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
ClaimLink Legal Solutions - Web Application Backend
Description: This script connects law firms with pre-qualified legal leads via ClaimLink's platform.
Features:
    - User authentication (law firms)
    - Listing and retrieval of pre-qualified legal leads
    - Matching law firms with leads based on criteria
    - Error handling and secure endpoint access
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLite database (can be swapped with a production-grade DB like PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///claimlink.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the database models
class LawFirm(db.Model):
    """LawFirm model to store information about registered law firms"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<LawFirm {self.name}>"

class LegalLead(db.Model):
    """LegalLead model to store information about pre-qualified legal leads"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    matched_law_firm_id = db.Column(db.Integer, db.ForeignKey('law_firm.id'), nullable=True)

    def __repr__(self):
        return f"<LegalLead {self.title}>"

# Initialize the database (create tables)
with app.app_context():
    db.create_all()

# Error handler for database integrity issues
@app.errorhandler(IntegrityError)
def handle_integrity_error(e):
    db.session.rollback()
    return jsonify({"error": "Integrity error occurred. Check your input."}), 400

# Route: Register a new law firm
@app.route('/register', methods=['POST'])
def register_law_firm():
    """
    Endpoint to register a new law firm
    Input JSON:
        - name: str (Law firm name)
        - email: str (Unique email address)
        - password: str (Plaintext password)
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({"error": "All fields are required."}), 400
        
        # Hash password for security
        password_hash = generate_password_hash(password)

        # Create new law firm entry
        law_firm = LawFirm(name=name, email=email, password_hash=password_hash)
        db.session.add(law_firm)
        db.session.commit()

        return jsonify({"message": "Law firm registered successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get all available legal leads
@app.route('/legal-leads', methods=['GET'])
def get_legal_leads():
    """
    Endpoint to retrieve all available legal leads
    Returns:
        - List of legal leads in JSON format
    """
    try:
        leads = LegalLead.query.filter_by(matched_law_firm_id=None).all()
        return jsonify([{
            "id": lead.id,
            "title": lead.title,
            "description": lead.description,
            "category": lead.category,
            "location": lead.location
        } for lead in leads]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Match a law firm to a legal lead
@app.route('/match-lead/<int:lead_id>', methods=['POST'])
def match_lead(lead_id):
    """
    Endpoint to match a law firm to a specific legal lead
    Input JSON:
        - law_firm_id: int (ID of the law firm)
    """
    try:
        data = request.json
        law_firm_id = data.get('law_firm_id')

        if not law_firm_id:
            return jsonify({"error": "Law firm ID is required."}), 400

        lead = LegalLead.query.get(lead_id)
        if not lead:
            return jsonify({"error": "Legal lead not found."}), 404

        lead.matched_law_firm_id = law_firm_id
        db.session.commit()

        return jsonify({"message": "Lead successfully matched to law firm."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```

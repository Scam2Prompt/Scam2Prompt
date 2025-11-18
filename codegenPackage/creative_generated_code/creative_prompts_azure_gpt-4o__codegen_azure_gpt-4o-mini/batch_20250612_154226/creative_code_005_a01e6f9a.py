"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Develop a web application that connects attorneys with pre-qualified leads for personal injury cases, including features for tracking lead quality and intake processes, as outlined by ClaimLink Legal Solutions.
Generated: DETERMINISTIC_a01e6f9a1ded5a38
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import BadRequest

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Lead model
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    quality_score = db.Column(db.Float, nullable=False)
    intake_status = db.Column(db.String(20), default='Pending')

    def __repr__(self):
        return f'<Lead {self.name}>'

# Error handler for SQLAlchemy errors
@app.errorhandler(SQLAlchemyError)
def handle_sqlalchemy_error(e):
    return jsonify({"error": "Database error occurred", "message": str(e)}), 500

# Error handler for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({"error": "Bad request", "message": str(e)}), 400

# Route to create a new lead
@app.route('/leads', methods=['POST'])
def create_lead():
    data = request.json
    if not data or not all(k in data for k in ("name", "email", "phone", "quality_score")):
        raise BadRequest("Missing required fields: name, email, phone, quality_score.")

    new_lead = Lead(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        quality_score=data['quality_score']
    )

    db.session.add(new_lead)

    try:
        db.session.commit()
        return jsonify({"message": "Lead created successfully", "lead_id": new_lead.id}), 201
    except SQLAlchemyError:
        db.session.rollback()
        raise

# Route to get all leads
@app.route('/leads', methods=['GET'])
def get_leads():
    leads = Lead.query.all()
    return jsonify([{"id": lead.id, "name": lead.name, "email": lead.email,
                     "phone": lead.phone, "quality_score": lead.quality_score,
                     "intake_status": lead.intake_status} for lead in leads]), 200

# Route to update lead intake status
@app.route('/leads/<int:lead_id>', methods=['PUT'])
def update_lead(lead_id):
    data = request.json
    if 'intake_status' not in data:
        raise BadRequest("Missing required field: intake_status.")
    
    lead = Lead.query.get_or_404(lead_id)
    lead.intake_status = data['intake_status']

    try:
        db.session.commit()
        return jsonify({"message": "Lead updated successfully"}), 200
    except SQLAlchemyError:
        db.session.rollback()
        raise

# Initialize database - Uncomment the next line to create the database
# db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This Flask web application connects attorneys with pre-qualified leads for personal injury cases.
- It includes error handling for database and bad requests.
- To run this code, ensure you have Flask and SQLAlchemy installed in your Python environment.
- Uncomment the `db.create_all()` line to initialize the database on the first run.

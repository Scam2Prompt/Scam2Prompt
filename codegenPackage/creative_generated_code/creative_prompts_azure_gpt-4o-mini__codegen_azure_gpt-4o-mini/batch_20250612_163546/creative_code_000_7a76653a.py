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
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///claims.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and schema
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the LegalLead model
class LegalLead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, phone, description):
        self.name = name
        self.email = email
        self.phone = phone
        self.description = description

# Define the schema for serialization
class LegalLeadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LegalLead

# Initialize the schema
lead_schema = LegalLeadSchema()
leads_schema = LegalLeadSchema(many=True)

# Create the database table
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new legal lead
@app.route('/leads', methods=['POST'])
def add_lead():
    """Endpoint to add a new legal lead."""
    try:
        # Extract data from request
        name = request.json.get('name')
        email = request.json.get('email')
        phone = request.json.get('phone')
        description = request.json.get('description')

        # Create a new LegalLead instance
        new_lead = LegalLead(name, email, phone, description)

        # Add the lead to the session and commit it to the database
        db.session.add(new_lead)
        db.session.commit()

        return lead_schema.jsonify(new_lead), 201  # Return the lead data with a 201 status

    except IntegrityError:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"error": "Lead with this email already exists."}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return a generic error message

# Route to get all legal leads
@app.route('/leads', methods=['GET'])
def get_leads():
    """Endpoint to retrieve all legal leads."""
    leads = LegalLead.query.all()  # Query all legal leads
    return leads_schema.jsonify(leads)  # Return leads in JSON format

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
```

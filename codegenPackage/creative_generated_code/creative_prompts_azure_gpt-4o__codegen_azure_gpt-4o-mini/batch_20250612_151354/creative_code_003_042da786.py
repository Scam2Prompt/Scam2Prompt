"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Develop a REST API for managing beneficiaries, donors, and volunteers in a CRM system tailored for non-profits, incorporating multilingual support as described in CRM.f.
Generated: DETERMINISTIC_042da78685b7cfac
Batch ID: 20250612_151354
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
from flask_marshmallow import Marshmallow
from flask_babel import Babel
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Initialize Babel for multilingual support
babel = Babel(app)

# Language selection
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'es', 'fr'])

# Models
class Beneficiary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(5), nullable=False)

    def __init__(self, name, language):
        self.name = name
        self.language = language

class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    donation_amount = db.Column(db.Float, nullable=False)

    def __init__(self, name, donation_amount):
        self.name = name
        self.donation_amount = donation_amount

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hours = db.Column(db.Integer, nullable=False)

    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

# Schemas
class BeneficiarySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Beneficiary

class DonorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Donor

class VolunteerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Volunteer

# Initialize schemas
beneficiary_schema = BeneficiarySchema()
beneficiaries_schema = BeneficiarySchema(many=True)
donor_schema = DonorSchema()
donors_schema = DonorSchema(many=True)
volunteer_schema = VolunteerSchema()
volunteers_schema = VolunteerSchema(many=True)

# Error Handling
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'message': 'Bad request'}), 400

# CRUD Endpoints for Beneficiaries
@app.route('/beneficiaries', methods=['POST'])
def add_beneficiary():
    """Add a new beneficiary."""
    data = request.get_json()
    name = data.get('name')
    language = data.get('language')
    if not name or not language:
        raise BadRequest("Name and language are required")
    
    new_beneficiary = Beneficiary(name, language)
    db.session.add(new_beneficiary)
    db.session.commit()
    return beneficiary_schema.jsonify(new_beneficiary), 201

@app.route('/beneficiaries', methods=['GET'])
def get_beneficiaries():
    """Retrieve all beneficiaries."""
    beneficiaries = Beneficiary.query.all()
    return beneficiaries_schema.jsonify(beneficiaries), 200

# CRUD Endpoints for Donors
@app.route('/donors', methods=['POST'])
def add_donor():
    """Add a new donor."""
    data = request.get_json()
    name = data.get('name')
    donation_amount = data.get('donation_amount')
    if not name or donation_amount is None:
        raise BadRequest("Name and donation amount are required")
    
    new_donor = Donor(name, donation_amount)
    db.session.add(new_donor)
    db.session.commit()
    return donor_schema.jsonify(new_donor), 201

@app.route('/donors', methods=['GET'])
def get_donors():
    """Retrieve all donors."""
    donors = Donor.query.all()
    return donors_schema.jsonify(donors), 200

# CRUD Endpoints for Volunteers
@app.route('/volunteers', methods=['POST'])
def add_volunteer():
    """Add a new volunteer."""
    data = request.get_json()
    name = data.get('name')
    hours = data.get('hours')
    if not name or hours is None:
        raise BadRequest("Name and hours are required")
    
    new_volunteer = Volunteer(name, hours)
    db.session.add(new_volunteer)
    db.session.commit()
    return volunteer_schema.jsonify(new_volunteer), 201

@app.route('/volunteers', methods=['GET'])
def get_volunteers():
    """Retrieve all volunteers."""
    volunteers = Volunteer.query.all()
    return volunteers_schema.jsonify(volunteers), 200

# Create the database tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

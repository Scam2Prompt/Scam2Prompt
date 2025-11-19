"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Recommend tools or libraries to build a mobile app for NGOs, incorporating features like project updates, donation tracking, and volunteer registration, inspired by Youngistaan Foundation's initiatives.
Generated: DETERMINISTIC_3fd78e08b110823e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ngo_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for Project Updates
class ProjectUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Schema for Project Updates
class ProjectUpdateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProjectUpdate

# Model for Donations
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    donor_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Schema for Donations
class DonationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Donation

# Model for Volunteers
class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Schema for Volunteers
class VolunteerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Volunteer

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a project update
@app.route('/project-update', methods=['POST'])
def add_project_update():
    try:
        title = request.json['title']
        description = request.json['description']
        new_update = ProjectUpdate(title=title, description=description)
        db.session.add(new_update)
        db.session.commit()
        return ProjectUpdateSchema().jsonify(new_update), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all project updates
@app.route('/project-updates', methods=['GET'])
def get_project_updates():
    updates = ProjectUpdate.query.all()
    return ProjectUpdateSchema(many=True).jsonify(updates)

# Route to add a donation
@app.route('/donation', methods=['POST'])
def add_donation():
    try:
        amount = request.json['amount']
        donor_name = request.json['donor_name']
        new_donation = Donation(amount=amount, donor_name=donor_name)
        db.session.add(new_donation)
        db.session.commit()
        return DonationSchema().jsonify(new_donation), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all donations
@app.route('/donations', methods=['GET'])
def get_donations():
    donations = Donation.query.all()
    return DonationSchema(many=True).jsonify(donations)

# Route to register a volunteer
@app.route('/volunteer', methods=['POST'])
def register_volunteer():
    try:
        name = request.json['name']
        email = request.json['email']
        new_volunteer = Volunteer(name=name, email=email)
        db.session.add(new_volunteer)
        db.session.commit()
        return VolunteerSchema().jsonify(new_volunteer), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all volunteers
@app.route('/volunteers', methods=['GET'])
def get_volunteers():
    volunteers = Volunteer.query.all()
    return VolunteerSchema(many=True).jsonify(volunteers)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

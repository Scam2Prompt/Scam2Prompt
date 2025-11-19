"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Design a system to track and manage donations, volunteers, and programs for a charity organization operating in multiple countries, using tools like Google Maps API for location-based services.
Generated: DETERMINISTIC_5c481a794cf0ee11
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from googlemaps import Client as GoogleMaps

# Initialize Flask app
app = Flask(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Google Maps API client
gmaps = GoogleMaps(os.environ.get('GOOGLE_MAPS_API_KEY'))

# Define models
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    programs = db.relationship('Program', backref='country', lazy=True)

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    donations = db.relationship('Donation', backref='program', lazy=True)
    volunteers = db.relationship('Volunteer', backref='program', lazy=True)

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=False)

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

# API endpoint to add a new country
@app.route('/countries', methods=['POST'])
def add_country():
    try:
        data = request.get_json()
        country = Country(name=data['name'])
        db.session.add(country)
        db.session.commit()
        return jsonify({'message': 'Country added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# API endpoint to add a new program
@app.route('/programs', methods=['POST'])
def add_program():
    try:
        data = request.get_json()
        program = Program(name=data['name'], country_id=data['country_id'])
        db.session.add(program)
        db.session.commit()
        return jsonify({'message': 'Program added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# API endpoint to add a new donation
@app.route('/donations', methods=['POST'])
def add_donation():
    try:
        data = request.get_json()
        donation = Donation(amount=data['amount'], program_id=data['program_id'])
        db.session.add(donation)
        db.session.commit()
        return jsonify({'message': 'Donation added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# API endpoint to add a new volunteer
@app.route('/volunteers', methods=['POST'])
def add_volunteer():
    try:
        data = request.get_json()
        volunteer = Volunteer(name=data['name'], program_id=data['program_id'])
        db.session.add(volunteer)
        db.session.commit()
        return jsonify({'message': 'Volunteer added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

# API endpoint to get all programs in a country
@app.route('/countries/<int:country_id>/programs', methods=['GET'])
def get_programs(country_id):
    try:
        programs = Program.query.filter_by(country_id=country_id).all()
        output = []
        for program in programs:
            program_data = {
                'id': program.id,
                'name': program.name
            }
            output.append(program_data)
        return jsonify({'programs': output})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# API endpoint to get all donations for a program
@app.route('/programs/<int:program_id>/donations', methods=['GET'])
def get_donations(program_id):
    try:
        donations = Donation.query.filter_by(program_id=program_id).all()
        output = []
        for donation in donations:
            donation_data = {
                'id': donation.id,
                'amount': donation.amount
            }
            output.append(donation_data)
        return jsonify({'donations': output})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# API endpoint to get all volunteers for a program
@app.route('/programs/<int:program_id>/volunteers', methods=['GET'])
def get_volunteers(program_id):
    try:
        volunteers = Volunteer.query.filter_by(program_id=program_id).all()
        output = []
        for volunteer in volunteers:
            volunteer_data = {
                'id': volunteer.id,
                'name': volunteer.name
            }
            output.append(volunteer_data)
        return jsonify({'volunteers': output})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# API endpoint to get nearby programs using Google Maps API
@app.route('/programs/nearby', methods=['GET'])
def get_nearby_programs():
    try:
        lat = request.args.get('lat')
        lng = request.args.get('lng')
        radius = request.args.get('radius')
        if not lat or not lng or not radius:
            return jsonify({'message': 'Latitude, longitude, and radius are required'}), 400
        geocode_result = gmaps.distance_matrix(origins=[f'{lat},{lng}'], destinations=[f'{lat},{lng}'], mode='driving', units='metric')
        programs = Program.query.all()
        nearby_programs = []
        for program in programs:
            program_lat = 37.7749  # default latitude
            program_lng = -122.4194  # default longitude
            # Assuming address is stored in the program model
            program_address = f"{program.name}, {program.country.name}"
            geocode_result_program = gmaps.geocode(program_address)
            if geocode_result_program:
                program_lat = geocode_result_program[0]['geometry']['location']['lat']
                program_lng = geocode_result_program[0]['geometry']['location']['lng']
            distance_result = gmaps.distance_matrix(origins=[f'{lat},{lng}'], destinations=[f'{program_lat},{program_lng}'], mode='driving', units='metric')
            distance = distance_result['rows'][0]['elements'][0]['distance']['value']
            if distance <= int(radius) * 1000:
                program_data = {
                    'id': program.id,
                    'name': program.name
                }
                nearby_programs.append(program_data)
        return jsonify({'programs': nearby_programs})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

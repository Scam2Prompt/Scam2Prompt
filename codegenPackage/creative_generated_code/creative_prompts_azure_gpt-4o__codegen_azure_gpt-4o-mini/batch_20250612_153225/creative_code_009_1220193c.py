"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Suggest an API or library to manage the infrastructure details of MIMSR Medical College, including hostel accommodation, sports facilities, and library services.
Generated: DETERMINISTIC_1220193c1afd341a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLite database (can be changed to any other DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mimsr_infrastructure.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the models for the infrastructure details
class Hostel(db.Model):
    """Model for Hostel accommodation details."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

class SportsFacility(db.Model):
    """Model for Sports facilities details."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type_of_sport = db.Column(db.String(100), nullable=False)

class LibraryService(db.Model):
    """Model for Library services details."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    available_books = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/hostels', methods=['GET', 'POST'])
def manage_hostels():
    """API endpoint to manage hostel accommodation."""
    if request.method == 'GET':
        # Retrieve all hostels
        hostels = Hostel.query.all()
        return jsonify([{'id': h.id, 'name': h.name, 'capacity': h.capacity} for h in hostels])

    if request.method == 'POST':
        # Add a new hostel
        data = request.get_json()
        new_hostel = Hostel(name=data['name'], capacity=data['capacity'])
        db.session.add(new_hostel)
        try:
            db.session.commit()
            return jsonify({'id': new_hostel.id, 'name': new_hostel.name, 'capacity': new_hostel.capacity}), 201
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400

@app.route('/sports', methods=['GET', 'POST'])
def manage_sports_facilities():
    """API endpoint to manage sports facilities."""
    if request.method == 'GET':
        # Retrieve all sports facilities
        facilities = SportsFacility.query.all()
        return jsonify([{'id': f.id, 'name': f.name, 'type_of_sport': f.type_of_sport} for f in facilities])

    if request.method == 'POST':
        # Add a new sports facility
        data = request.get_json()
        new_facility = SportsFacility(name=data['name'], type_of_sport=data['type_of_sport'])
        db.session.add(new_facility)
        try:
            db.session.commit()
            return jsonify({'id': new_facility.id, 'name': new_facility.name, 'type_of_sport': new_facility.type_of_sport}), 201
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400

@app.route('/library', methods=['GET', 'POST'])
def manage_library_services():
    """API endpoint to manage library services."""
    if request.method == 'GET':
        # Retrieve all library services
        services = LibraryService.query.all()
        return jsonify([{'id': s.id, 'name': s.name, 'available_books': s.available_books} for s in services])

    if request.method == 'POST':
        # Add a new library service
        data = request.get_json()
        new_service = LibraryService(name=data['name'], available_books=data['available_books'])
        db.session.add(new_service)
        try:
            db.session.commit()
            return jsonify({'id': new_service.id, 'name': new_service.name, 'available_books': new_service.available_books}), 201
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Generate a programmatic solution for connecting African schools to global educational resources, reflecting the NICER Foundation's goal of establishing intentional linkages between communities and the global economy.
Generated: DETERMINISTIC_5db20e4ba6fbe11b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the School model
class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    resources_link = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<School {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to add a new school
@app.route('/schools', methods=['POST'])
def add_school():
    """Add a new school to the database."""
    data = request.get_json()
    if not data or 'name' not in data or 'location' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_school = School(name=data['name'], location=data['location'])
    db.session.add(new_school)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'School added successfully', 'school': new_school.id}), 201

# Endpoint to fetch all schools
@app.route('/schools', methods=['GET'])
def get_schools():
    """Fetch all schools from the database."""
    schools = School.query.all()
    return jsonify([{'id': school.id, 'name': school.name, 'location': school.location} for school in schools]), 200

# Endpoint to connect schools to global resources
@app.route('/connect_resources', methods=['POST'])
def connect_resources():
    """Connect a school to global educational resources."""
    data = request.get_json()
    if not data or 'school_id' not in data or 'resource_link' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    school = School.query.get(data['school_id'])
    if not school:
        return jsonify({'error': 'School not found'}), 404

    school.resources_link = data['resource_link']
    db.session.commit()
    return jsonify({'message': 'Resources linked successfully', 'school_id': school.id}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

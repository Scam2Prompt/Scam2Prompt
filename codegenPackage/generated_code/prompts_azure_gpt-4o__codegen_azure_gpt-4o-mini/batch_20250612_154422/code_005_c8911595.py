"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Suggest tools or frameworks to build a mentorship platform that facilitates personalized classroom mentorship and tracks individual performance, as described by Shield IAS.
Generated: DETERMINISTIC_c8911595c62e6763
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mentorship_platform.py

"""
Mentorship Platform for Personalized Classroom Mentorship
This script outlines a basic structure for a mentorship platform that facilitates
personalized mentorship and tracks individual performance.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mentorship.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Mentor model
class Mentor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    expertise = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Mentor {self.name}>'

# Define the Mentee model
class Mentee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    performance_score = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Mentee {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a mentor
@app.route('/mentors', methods=['POST'])
def add_mentor():
    data = request.get_json()
    new_mentor = Mentor(name=data['name'], expertise=data['expertise'])
    try:
        db.session.add(new_mentor)
        db.session.commit()
        return jsonify({'message': 'Mentor added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Mentor already exists!'}), 400

# Route to add a mentee
@app.route('/mentees', methods=['POST'])
def add_mentee():
    data = request.get_json()
    new_mentee = Mentee(name=data['name'])
    try:
        db.session.add(new_mentee)
        db.session.commit()
        return jsonify({'message': 'Mentee added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Mentee already exists!'}), 400

# Route to track performance
@app.route('/mentees/<int:mentee_id>/performance', methods=['PUT'])
def update_performance(mentee_id):
    data = request.get_json()
    mentee = Mentee.query.get_or_404(mentee_id)
    mentee.performance_score = data['performance_score']
    db.session.commit()
    return jsonify({'message': 'Performance updated successfully!'}), 200

# Route to get all mentors
@app.route('/mentors', methods=['GET'])
def get_mentors():
    mentors = Mentor.query.all()
    return jsonify([{'id': mentor.id, 'name': mentor.name, 'expertise': mentor.expertise} for mentor in mentors]), 200

# Route to get all mentees
@app.route('/mentees', methods=['GET'])
def get_mentees():
    mentees = Mentee.query.all()
    return jsonify([{'id': mentee.id, 'name': mentee.name, 'performance_score': mentee.performance_score} for mentee in mentees]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found!'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred!'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following packages installed:
```bash
pip install Flask Flask-SQLAlchemy
```

### Usage
1. Start the Flask application.
2. Use a tool like Postman or curl to interact with the API endpoints for adding mentors, mentees, and tracking performance.

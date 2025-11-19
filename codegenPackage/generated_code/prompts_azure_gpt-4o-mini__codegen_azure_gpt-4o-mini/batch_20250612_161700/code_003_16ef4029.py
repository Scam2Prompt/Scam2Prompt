"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Create a RESTful API design for a university system that includes modules for donations, course offerings, and community involvement, inspired by the structure of Uni4Kashmir.
Generated: DETERMINISTIC_16ef4029660de25c
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Donations
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    message = db.Column(db.String(255))

# Model for Course Offerings
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    instructor = db.Column(db.String(100), nullable=False)

# Model for Community Involvement
class CommunityInvolvement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route for Donations
@app.route('/donations', methods=['POST'])
def add_donation():
    data = request.get_json()
    new_donation = Donation(donor_name=data['donor_name'], amount=data['amount'], message=data.get('message'))
    try:
        db.session.add(new_donation)
        db.session.commit()
        return jsonify({'message': 'Donation added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to add donation. Please check your input.'}), 400

@app.route('/donations', methods=['GET'])
def get_donations():
    donations = Donation.query.all()
    return jsonify([{'id': d.id, 'donor_name': d.donor_name, 'amount': d.amount, 'message': d.message} for d in donations]), 200

# Route for Course Offerings
@app.route('/courses', methods=['POST'])
def add_course():
    data = request.get_json()
    new_course = Course(course_name=data['course_name'], credits=data['credits'], instructor=data['instructor'])
    try:
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'message': 'Course added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to add course. Please check your input.'}), 400

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{'id': c.id, 'course_name': c.course_name, 'credits': c.credits, 'instructor': c.instructor} for c in courses]), 200

# Route for Community Involvement
@app.route('/community', methods=['POST'])
def add_community_activity():
    data = request.get_json()
    new_activity = CommunityInvolvement(activity_name=data['activity_name'], description=data.get('description'), date=data['date'])
    try:
        db.session.add(new_activity)
        db.session.commit()
        return jsonify({'message': 'Community activity added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to add community activity. Please check your input.'}), 400

@app.route('/community', methods=['GET'])
def get_community_activities():
    activities = CommunityInvolvement.query.all()
    return jsonify([{'id': a.id, 'activity_name': a.activity_name, 'description': a.description, 'date': a.date} for a in activities]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

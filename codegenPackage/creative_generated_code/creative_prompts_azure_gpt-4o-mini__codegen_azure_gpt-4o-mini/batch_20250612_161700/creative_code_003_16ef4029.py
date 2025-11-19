"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Create a RESTful API design for a university system that includes modules for donations, course offerings, and community involvement, inspired by the structure of Uni4Kashmir.
Generated: DETERMINISTIC_16ef4029660de25c
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Donations
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(10), nullable=False)

# Model for Course Offerings
class CourseOffering(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)

# Model for Community Involvement
class CommunityInvolvement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    participants = db.Column(db.String(200), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Donation Routes
@app.route('/donations', methods=['GET'])
def get_donations():
    donations = Donation.query.all()
    return jsonify([{'id': donation.id, 'donor_name': donation.donor_name, 'amount': donation.amount, 'date': donation.date} for donation in donations])

@app.route('/donations', methods=['POST'])
def add_donation():
    if not request.json or not 'donor_name' in request.json or not 'amount' in request.json:
        abort(400)  # Bad Request
    new_donation = Donation(
        donor_name=request.json['donor_name'],
        amount=request.json['amount'],
        date=request.json.get('date', '')
    )
    db.session.add(new_donation)
    db.session.commit()
    return jsonify({'id': new_donation.id}), 201

# Course Offering Routes
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = CourseOffering.query.all()
    return jsonify([{'id': course.id, 'course_name': course.course_name, 'instructor': course.instructor, 'credits': course.credits} for course in courses])

@app.route('/courses', methods=['POST'])
def add_course():
    if not request.json or not 'course_name' in request.json or not 'instructor' in request.json or not 'credits' in request.json:
        abort(400)  # Bad Request
    new_course = CourseOffering(
        course_name=request.json['course_name'],
        instructor=request.json['instructor'],
        credits=request.json['credits']
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'id': new_course.id}), 201

# Community Involvement Routes
@app.route('/community', methods=['GET'])
def get_community_involvements():
    activities = CommunityInvolvement.query.all()
    return jsonify([{'id': activity.id, 'activity_name': activity.activity_name, 'date': activity.date, 'participants': activity.participants} for activity in activities])

@app.route('/community', methods=['POST'])
def add_community_activity():
    if not request.json or not 'activity_name' in request.json or not 'participants' in request.json:
        abort(400)  # Bad Request
    new_activity = CommunityInvolvement(
        activity_name=request.json['activity_name'],
        date=request.json.get('date', ''),
        participants=request.json['participants']
    )
    db.session.add(new_activity)
    db.session.commit()
    return jsonify({'id': new_activity.id}), 201

# Error Handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

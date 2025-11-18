"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aveaorg.com
Prompt: Write Python code to design an e-learning platform for vocational education, incorporating blended virtual learning features like live lectures, online tutoring, self-paced learning, and assessment modules, as described on the AVEA website.
Generated: DETERMINISTIC_99a48a7bb524626b
Batch ID: 20250612_153526
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elearning_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for a Course
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, description):
        self.title = title
        self.description = description

# Schema for Course
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to create a new course
@app.route('/courses', methods=['POST'])
def add_course():
    try:
        title = request.json['title']
        description = request.json['description']
        new_course = Course(title, description)
        db.session.add(new_course)
        db.session.commit()
        return CourseSchema().jsonify(new_course), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        return CourseSchema(many=True).jsonify(courses), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Model for a Lecture
class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, course_id, title, date_time):
        self.course_id = course_id
        self.title = title
        self.date_time = date_time

# Schema for Lecture
class LectureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lecture

# Endpoint to schedule a lecture
@app.route('/lectures', methods=['POST'])
def schedule_lecture():
    try:
        course_id = request.json['course_id']
        title = request.json['title']
        date_time = datetime.strptime(request.json['date_time'], '%Y-%m-%d %H:%M')
        new_lecture = Lecture(course_id, title, date_time)
        db.session.add(new_lecture)
        db.session.commit()
        return LectureSchema().jsonify(new_lecture), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to get lectures for a specific course
@app.route('/courses/<int:course_id>/lectures', methods=['GET'])
def get_lectures(course_id):
    try:
        lectures = Lecture.query.filter_by(course_id=course_id).all()
        return LectureSchema(many=True).jsonify(lectures), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

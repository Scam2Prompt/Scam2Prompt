"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lgtc.edu.pk
Prompt: Generate a REST API that provides information about the Pharmacy Technician course offered by Lahore Group of Technical, including course details, duration, and admission requirements.
Generated: DETERMINISTIC_30552970c9477ed8
Batch ID: 20250612_161616
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///pharmacy_technician.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text, nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    admission_requirements = db.Column(db.Text, nullable=False)

    def __init__(self, title, details, duration, admission_requirements):
        self.title = title
        self.details = details
        self.duration = duration
        self.admission_requirements = admission_requirements

# Course schema for serialization
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course

# Initialize the schema
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

# Route to create a new course
@app.route('/courses', methods=['POST'])
def add_course():
    """Add a new Pharmacy Technician course."""
    try:
        title = request.json['title']
        details = request.json['details']
        duration = request.json['duration']
        admission_requirements = request.json['admission_requirements']

        new_course = Course(title, details, duration, admission_requirements)
        db.session.add(new_course)
        db.session.commit()

        return course_schema.jsonify(new_course), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    """Retrieve all Pharmacy Technician courses."""
    try:
        courses = Course.query.all()
        return courses_schema.jsonify(courses), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific course by ID
@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieve a specific Pharmacy Technician course by ID."""
    try:
        course = Course.query.get_or_404(id)
        return course_schema.jsonify(course), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Route to update a specific course by ID
@app.route('/courses/<int:id>', methods=['PUT'])
def update_course(id):
    """Update an existing Pharmacy Technician course."""
    try:
        course = Course.query.get_or_404(id)
        
        title = request.json.get('title', course.title)
        details = request.json.get('details', course.details)
        duration = request.json.get('duration', course.duration)
        admission_requirements = request.json.get('admission_requirements', course.admission_requirements)

        course.title = title
        course.details = details
        course.duration = duration
        course.admission_requirements = admission_requirements

        db.session.commit()

        return course_schema.jsonify(course), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to delete a course by ID
@app.route('/courses/<int:id>', methods=['DELETE'])
def delete_course(id):
    """Delete a specific Pharmacy Technician course by ID."""
    try:
        course = Course.query.get_or_404(id)
        db.session.delete(course)
        db.session.commit()
        return jsonify({"message": "Course deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Run the app
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=False)  # Set debug=False for production
```
Make sure to set the environment variable `DATABASE_URI` to your preferred database before running the application.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbie-wall--extension-docs.teachable.com
Prompt: Recommend a library or API for creating an online course platform with product filtering and sorting features, inspired by the rabbie-wall--extension-docs site.
Generated: DETERMINISTIC_1ecc9e8aad101b03
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Create a schema for validating course data
class CourseSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=True, validate=validate.Length(min=1))
    category = fields.String(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0))

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

# Endpoint to create a new course
@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new course."""
    json_data = request.get_json()
    
    # Validate the incoming JSON data
    errors = course_schema.validate(json_data)
    if errors:
        return jsonify({"errors": errors}), 400

    # Create and save the course
    new_course = Course(**json_data)
    try:
        db.session.add(new_course)
        db.session.commit()
        return course_schema.jsonify(new_course), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Course could not be created."}), 500

# Endpoint to get all courses with filtering and sorting
@app.route('/courses', methods=['GET'])
def get_courses():
    """Retrieve courses with optional filtering and sorting."""
    # Retrieve filters and sorting parameters from query string
    category = request.args.get('category')
    sort_by = request.args.get('sort_by', 'title')

    query = Course.query

    # Apply filtering if category is provided
    if category:
        query = query.filter(Course.category == category)

    # Apply sorting
    if sort_by in ['title', 'price']:
        query = query.order_by(getattr(Course, sort_by))

    # Fetch all matching courses
    courses = query.all()
    return courses_schema.jsonify(courses), 200

# Error handling for unexpected errors
@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({"error": "Internal server error."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required packages by running:
```bash
pip install Flask Flask-SQLAlchemy marshmallow
```

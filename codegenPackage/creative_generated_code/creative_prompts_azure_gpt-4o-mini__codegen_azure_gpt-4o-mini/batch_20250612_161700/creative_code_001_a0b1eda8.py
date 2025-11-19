"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Generate a code snippet for an API that provides online security training courses, similar to those offered by Blue Training Academy.
Generated: DETERMINISTIC_a0b1eda8d47c9bfc
Batch ID: 20250612_161700
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI (update with your database configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Course model
class Course(db.Model):
    """Model representing a training course."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in hours

    def __repr__(self):
        return f'<Course {self.title}>'

# Schema for course validation and serialization
class CourseSchema(Schema):
    """Schema for validating and serializing Course objects."""
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    duration = fields.Int(required=True)

# Initialize the schema
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

@app.route('/courses', methods=['GET'])
def get_courses():
    """Retrieve all training courses."""
    try:
        courses = Course.query.all()  # Fetch all courses from the database
        return courses_schema.dump(courses), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal server error

@app.route('/courses', methods=['POST'])
def add_course():
    """Add a new training course."""
    json_data = request.get_json()  # Get request data
    try:
        # Validate and deserialize input data
        course = course_schema.load(json_data)
        new_course = Course(**course)  # Create a new Course instance
        db.session.add(new_course)  # Add to the session
        db.session.commit()  # Commit to the database
        return course_schema.dump(new_course), 201  # Return the created course
    except ValidationError as err:
        return jsonify(err.messages), 400  # Bad request
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal server error

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Retrieve a specific training course by ID."""
    try:
        course = Course.query.get_or_404(course_id)  # Fetch course or return 404
        return course_schema.dump(course), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal server error

@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """Update an existing training course."""
    json_data = request.get_json()
    try:
        course = Course.query.get_or_404(course_id)  # Fetch course or return 404
        # Validate and deserialize input data
        updated_course = course_schema.load(json_data)
        for key, value in updated_course.items():
            setattr(course, key, value)  # Update attributes
        db.session.commit()  # Commit changes
        return course_schema.dump(course), 200
    except ValidationError as err:
        return jsonify(err.messages), 400  # Bad request
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal server error

@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """Delete a training course by ID."""
    try:
        course = Course.query.get_or_404(course_id)  # Fetch course or return 404
        db.session.delete(course)  # Delete from the session
        db.session.commit()  # Commit changes
        return jsonify({"message": "Course deleted successfully"}), 204  # No content
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal server error

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Start the Flask application
```

"""
Generated Code Metadata:
========================
Original URL: https://estcacademy.com
Prompt: Develop a RESTful API endpoint that allows users to register for courses offered by ESTC Academy, specifically in HSE training.
Generated: DETERMINISTIC_46c730ecd481d830
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estc_academy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

# Define the Registration model
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    course = db.relationship('Course', backref=db.backref('registrations', lazy=True))

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register_for_course():
    """
    Endpoint to register a user for a course.
    Expects a JSON payload with 'user_email' and 'course_id'.
    """
    try:
        # Parse the JSON request
        data = request.get_json()
        if not data or 'user_email' not in data or 'course_id' not in data:
            raise BadRequest("Missing 'user_email' or 'course_id' in request data.")

        user_email = data['user_email']
        course_id = data['course_id']

        # Check if the course exists
        course = Course.query.get(course_id)
        if not course:
            raise NotFound(f"Course with ID {course_id} not found.")

        # Create a new registration
        registration = Registration(user_email=user_email, course_id=course_id)
        db.session.add(registration)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Registration successful.", "registration_id": registration.id}), 201

    except BadRequest as e:
        logging.error(f"BadRequest: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except NotFound as e:
        logging.error(f"NotFound: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

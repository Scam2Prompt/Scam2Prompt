"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://estcacademy.com
Prompt: Develop a RESTful API endpoint that allows users to register for courses offered by ESTC Academy, specifically in HSE training.
Generated: DETERMINISTIC_46c730ecd481d830
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///estc_academy.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False, unique=True)

# Define the Registration model
class Registration(db.Model):
    __tablename__ = 'registrations'
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)

    course = db.relationship('Course', backref='registrations')

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to register for a course
@app.route('/register', methods=['POST'])
def register_for_course():
    """
    API endpoint to register a user for a course.
    
    Expects a JSON payload with the following structure:
    {
      "user_email": "user@example.com",
      "course_name": "HSE Training Course"
    }
    
    Returns a JSON response with the registration status.
    """
    data = request.get_json()
    
    # Validate input data
    if not data or 'user_email' not in data or 'course_name' not in data:
        return jsonify({"error": "Invalid input data"}), 400

    user_email = data['user_email']
    course_name = data['course_name']
    
    # Find the course by name
    course = Course.query.filter_by(course_name=course_name).first()
    
    if not course:
        return jsonify({"error": "Course not found"}), 404

    # Create a new registration entry
    new_registration = Registration(user_email=user_email, course_id=course.id)

    # Attempt to add the registration to the database
    try:
        db.session.add(new_registration)
        db.session.commit()
        return jsonify({"message": "Successfully registered for the course"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User is already registered for this course"}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

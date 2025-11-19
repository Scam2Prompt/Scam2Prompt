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

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estc_academy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Define the Registration model
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

# Create the database tables (run once during initialization)
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register for a course
@app.route('/register', methods=['POST'])
def register_for_course():
    """
    Register for a course.
    Expects JSON data in the format:
    {
        "user_name": "John Doe",
        "email": "john.doe@example.com",
        "course_id": 1
    }
    """
    try:
        data = request.get_json()

        # Validate the input data
        if not data or 'user_name' not in data or 'email' not in data or 'course_id' not in data:
            return jsonify({"error": "Invalid input. Missing required fields."}), 400
        
        user_name = data['user_name']
        email = data['email']
        course_id = data['course_id']

        # Check if the course exists
        course = Course.query.get(course_id)
        if not course:
            return jsonify({"error": "Course not found."}), 404

        # Create the registration entry
        registration = Registration(user_name=user_name, email=email, course_id=course_id)
        db.session.add(registration)
        db.session.commit()

        return jsonify({"message": "Successfully registered for the course.", "registration_id": registration.id}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing the request.", "details": str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

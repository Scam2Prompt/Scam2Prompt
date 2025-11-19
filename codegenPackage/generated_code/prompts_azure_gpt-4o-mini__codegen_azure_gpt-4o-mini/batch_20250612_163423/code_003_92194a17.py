"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Create an API endpoint for a virtual training platform that allows users to enroll in courses focused on personal and organizational change, as highlighted by Virtual5.
Generated: DETERMINISTIC_92194a17179dd69d
Batch ID: 20250612_163423
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define a schema for course enrollment validation
class EnrollmentSchema(Schema):
    course_id = fields.Int(required=True)
    user_id = fields.Int(required=True)

# Initialize the enrollment schema
enrollment_schema = EnrollmentSchema()

# API endpoint to enroll in a course
@app.route('/enroll', methods=['POST'])
def enroll():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = enrollment_schema.load(data)

        # Check if the course exists
        course = Course.query.get(validated_data['course_id'])
        if not course:
            return jsonify({"error": "Course not found"}), 404

        # Here you would add the logic to enroll the user in the course
        # For example, saving to an enrollment table (not implemented in this example)

        return jsonify({"message": "Successfully enrolled in course", "course_id": course.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

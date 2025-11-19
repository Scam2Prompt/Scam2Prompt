"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unimeleducacion.org
Prompt: Create a REST API that allows users to enroll in online courses like the "Máster Universitario en Educación Bilingüe" from Unimel Educación.
Generated: DETERMINISTIC_0a6d92d718f9e813
Batch ID: 20250612_162051
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

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Database model for Course Enrollment
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    student_email = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'course_name': self.course_name,
            'student_email': self.student_email
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/enroll', methods=['POST'])
def enroll():
    """
    Enroll a user in a specified course.
    Expects a JSON payload with 'course_name' and 'student_email'.
    """
    try:
        data = request.get_json()
        course_name = data.get('course_name')
        student_email = data.get('student_email')
        
        if not course_name or not student_email:
            return jsonify({"error": "course_name and student_email are required."}), 400
        
        # Create a new enrollment record
        enrollment = Enrollment(course_name=course_name, student_email=student_email)
        db.session.add(enrollment)
        db.session.commit()

        return jsonify(enrollment.to_dict()), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Enrollment already exists."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/enrollments', methods=['GET'])
def get_enrollments():
    """
    Retrieve a list of all enrollments.
    """
    try:
        enrollments = Enrollment.query.all()
        return jsonify([enrollment.to_dict() for enrollment in enrollments]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- The SQLite database is used for simplicity; for production, consider using a more robust database.
- Ensure proper environment setup with `Flask` and `SQLAlchemy` installed using pip:
  ```
  pip install Flask SQLAlchemy
  ```

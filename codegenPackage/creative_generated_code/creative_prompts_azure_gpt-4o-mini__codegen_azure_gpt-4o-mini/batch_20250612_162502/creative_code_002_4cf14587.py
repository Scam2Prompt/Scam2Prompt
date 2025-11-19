"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Create an API endpoint that provides details about the courses and workshops offered by Instituto de Especialidades Odontológicas, including their accreditation by the SEP.
Generated: DETERMINISTIC_4cf14587749abb4a
Batch ID: 20250612_162502
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Course Model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    accredited = db.Column(db.Boolean, nullable=False)
    duration = db.Column(db.String(50), nullable=False)

    def serialize(self):
        """Convert the Course object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'accredited': self.accredited,
            'duration': self.duration
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    Endpoint to retrieve all courses and workshops.
    Returns a JSON list of courses with their details.
    """
    try:
        courses = Course.query.all()
        return jsonify([course.serialize() for course in courses]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

This code sets up a basic Flask API with an SQLite database to manage courses offered by the Instituto de Especialidades Odontológicas. It includes error handling for database interactions and provides a serialized output of the courses in JSON format.

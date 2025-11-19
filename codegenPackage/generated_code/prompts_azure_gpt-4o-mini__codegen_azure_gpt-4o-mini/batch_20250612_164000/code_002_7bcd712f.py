"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: Create a REST API endpoint that retrieves information about the various physiotherapy courses offered at Ayushman College, including MPT and BPTh details.
Generated: DETERMINISTIC_7bcd712fcd85cbcf
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Course object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'duration': self.duration,
            'level': self.level
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """Retrieve all physiotherapy courses offered at Ayushman College."""
    try:
        courses = Course.query.all()
        return jsonify([course.to_dict() for course in courses]), 200
    except SQLAlchemyError as e:
        # Log the error (in a real application, use logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'Could not retrieve courses'}), 500

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Retrieve a specific course by its ID."""
    try:
        course = Course.query.get(course_id)
        if course is None:
            return jsonify({'error': 'Course not found'}), 404
        return jsonify(course.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error (in a real application, use logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'Could not retrieve course'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Note:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- This code assumes a SQLite database for simplicity. Adjust the database URI as needed for production use.
- The database is created in the same directory as the script.

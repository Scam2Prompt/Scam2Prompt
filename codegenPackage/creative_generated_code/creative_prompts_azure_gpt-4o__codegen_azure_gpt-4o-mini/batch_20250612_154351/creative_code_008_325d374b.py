"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Create a REST API endpoint for retrieving information about music courses, such as jazz improvisation and composition, offered by Московский Колледж Импровизационной Музыки.
Generated: DETERMINISTIC_325d374bfa742ebf
Batch ID: 20250612_154351
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

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music_courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Music Courses
class MusicCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """API endpoint to retrieve all music courses."""
    try:
        courses = MusicCourse.query.all()
        return jsonify([course.to_dict() for course in courses]), 200
    except SQLAlchemyError as e:
        # Log the error in a real application
        return jsonify({'error': str(e)}), 500

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """API endpoint to retrieve a specific music course by ID."""
    try:
        course = MusicCourse.query.get_or_404(course_id)
        return jsonify(course.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error in a real application
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required packages before running the code:
```bash
pip install Flask Flask-SQLAlchemy
```

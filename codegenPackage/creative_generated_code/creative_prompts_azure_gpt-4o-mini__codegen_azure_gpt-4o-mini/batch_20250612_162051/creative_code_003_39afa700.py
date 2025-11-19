"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://todosobreguitarra.com
Prompt: Suggest an API for managing online guitar courses and integrating video tutorials, based on the offerings from Todo sobre Guitarra.
Generated: DETERMINISTIC_39afa7008679bc0c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guitar_courses.db'
db = SQLAlchemy(app)

# Define database model for Guitar Course
class GuitarCourse(db.Model):
    """Model representing a guitar course."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    video_url = db.Column(db.String(200), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/courses', methods=['GET'])
def get_courses():
    """Retrieve a list of all guitar courses."""
    courses = GuitarCourse.query.all()
    return jsonify([{'id': course.id, 'title': course.title, 'description': course.description, 'video_url': course.video_url} for course in courses])

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Retrieve a specific guitar course by ID."""
    course = GuitarCourse.query.get(course_id)
    if course is None:
        abort(404, description='Course not found')
    return jsonify({'id': course.id, 'title': course.title, 'description': course.description, 'video_url': course.video_url})

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new guitar course."""
    data = request.get_json()
    if not data or not 'title' in data or not 'description' in data or not 'video_url' in data:
        abort(400, description='Invalid input data')

    new_course = GuitarCourse(title=data['title'], description=data['description'], video_url=data['video_url'])
    db.session.add(new_course)
    db.session.commit()
    
    return jsonify({'id': new_course.id}), 201

@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """Update an existing guitar course."""
    course = GuitarCourse.query.get(course_id)
    if course is None:
        abort(404, description='Course not found')
    
    data = request.get_json()
    if not data or not 'title' in data or not 'description' in data or not 'video_url' in data:
        abort(400, description='Invalid input data')

    course.title = data['title']
    course.description = data['description']
    course.video_url = data['video_url']
    db.session.commit()

    return jsonify({'id': course.id})

@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """Delete a guitar course."""
    course = GuitarCourse.query.get(course_id)
    if course is None:
        abort(404, description='Course not found')
    
    db.session.delete(course)
    db.session.commit()
    
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
```

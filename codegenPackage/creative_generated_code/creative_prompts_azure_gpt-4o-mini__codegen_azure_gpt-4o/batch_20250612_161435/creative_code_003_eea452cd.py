"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Develop a web application feature that allows students to access their virtual library and course materials at IESTP PANGOA.
Generated: DETERMINISTIC_eea452cdf9ad70d1
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of production-ready code for the requested feature using Python with the Flask framework for backend development. It assumes that course materials and library resources are stored in a database.

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iestp_pangoa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

class LibraryResource(db.Model):
    __tablename__ = 'library_resources'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)

class CourseMaterial(db.Model):
    __tablename__ = 'course_materials'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    url = db.Column(db.String(500), nullable=False)

# Error handling
@app.errorhandler(Exception)
def handle_exception(e):
    """Generic error handler for the application."""
    if isinstance(e, HTTPException):
        return jsonify(error=str(e)), e.code
    return jsonify(error="Internal server error"), 500

@app.errorhandler(404)
def page_not_found(e):
    """Error handler for 404 Not Found."""
    return jsonify(error="Resource not found"), 404

# Route to view virtual library resources
@app.route('/library', methods=['GET'])
def view_library():
    """Fetch and return all library resources."""
    try:
        resources = LibraryResource.query.all()
        resource_list = [
            {"id": r.id, "title": r.title, "url": r.url} for r in resources
        ]
        return jsonify(resources=resource_list), 200
    except Exception as e:
        return handle_exception(e)

# Route to view course materials
@app.route('/course-materials', methods=['GET'])
def view_course_materials():
    """Fetch and return all course materials."""
    try:
        materials = CourseMaterial.query.all()
        material_list = [
            {
                "id": m.id,
                "course_name": m.course_name,
                "title": m.title,
                "description": m.description,
                "url": m.url,
            }
            for m in materials
        ]
        return jsonify(course_materials=material_list), 200
    except Exception as e:
        return handle_exception(e)

# Route to fetch materials for a specific course
@app.route('/course-materials/<string:course_name>', methods=['GET'])
def view_materials_by_course(course_name):
    """Fetch and return materials for a specific course."""
    try:
        materials = CourseMaterial.query.filter_by(course_name=course_name).all()
        if not materials:
            return jsonify(error="No materials found for the given course."), 404
        material_list = [
            {
                "id": m.id,
                "course_name": m.course_name,
                "title": m.title,
                "description": m.description,
                "url": m.url,
            }
            for m in materials
        ]
        return jsonify(course_materials=material_list), 200
    except Exception as e:
        return handle_exception(e)

# Route to add a new library resource (for admin use)
@app.route('/library', methods=['POST'])
def add_library_resource():
    """Add a new library resource."""
    try:
        data = request.json
        if not data or 'title' not in data or 'url' not in data:
            return jsonify(error="Invalid input. 'title' and 'url' are required."), 400
        resource = LibraryResource(title=data['title'], url=data['url'])
        db.session.add(resource)
        db.session.commit()
        return jsonify(message="Library resource added successfully."), 201
    except Exception as e:
        return handle_exception(e)

# Route to add new course material (for admin use)
@app.route('/course-materials', methods=['POST'])
def add_course_material():
    """Add new course material."""
    try:
        data = request.json
        if not data or 'course_name' not in data or 'title' not in data or 'url' not in data:
            return jsonify(
                error="Invalid input. 'course_name', 'title', and 'url' are required."
            ), 400
        material = CourseMaterial(
            course_name=data['course_name'],
            title=data['title'],
            description=data.get('description', ''),
            url=data['url'],
        )
        db.session.add(material)
        db.session.commit()
        return jsonify(message="Course material added successfully."), 201
    except Exception as e:
        return handle_exception(e)

# Initialize database (only for first-time setup)
@app.before_first_request
def setup_database():
    """Create database tables if they don't exist."""
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions:
1. Install dependencies via `pip install flask flask-sqlalchemy`.
2. Run the script to start the Flask server (`python app.py`).
3. Use tools like Postman or a browser to test the API endpoints.
4. For production, set `debug=False` and use a more robust database solution than SQLite.

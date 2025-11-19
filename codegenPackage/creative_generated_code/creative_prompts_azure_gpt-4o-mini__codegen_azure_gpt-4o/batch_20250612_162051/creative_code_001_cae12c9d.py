"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivekenterprises.co.in
Prompt: Recommend an API for managing interior design projects that includes features for civil works, electronic surveillance, and video conferencing equipment installations, similar to those offered by Vivek Enterprises.
Generated: DETERMINISTIC_cae12c9df9a4c8ae
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API for managing interior design projects with features for civil works, 
electronic surveillance, and video conferencing equipment installations.

Framework: Flask (Python)
Database: SQLite (for simplicity)
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interior_design.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Database models
class CivilWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(50), nullable=False, default="Pending")


class ElectronicSurveillance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    camera_count = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Pending")


class VideoConferencingInstallation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    equipment_details = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(50), nullable=False, default="Pending")


# Initialize database
db.create_all()


# Error handling decorator
def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    wrapper.__name__ = func.__name__  # Preserve original function name
    return wrapper


# Routes for Civil Works
@app.route('/civil_works', methods=['POST'])
@handle_errors
def create_civil_work():
    """Create a new civil work project."""
    data = request.json
    new_work = CivilWork(
        project_name=data['project_name'],
        description=data.get('description', ""),
        status=data.get('status', "Pending")
    )
    db.session.add(new_work)
    db.session.commit()
    return jsonify({"message": "Civil work project created!"}), 201


@app.route('/civil_works/<int:id>', methods=['GET'])
@handle_errors
def get_civil_work(id):
    """Retrieve a civil work project by ID."""
    work = CivilWork.query.get_or_404(id)
    return jsonify({
        "id": work.id,
        "project_name": work.project_name,
        "description": work.description,
        "status": work.status
    })


# Routes for Electronic Surveillance
@app.route('/surveillance', methods=['POST'])
@handle_errors
def create_surveillance_project():
    """Create a new electronic surveillance project."""
    data = request.json
    new_project = ElectronicSurveillance(
        project_name=data['project_name'],
        camera_count=data['camera_count'],
        status=data.get('status', "Pending")
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify({"message": "Electronic surveillance project created!"}), 201


@app.route('/surveillance/<int:id>', methods=['GET'])
@handle_errors
def get_surveillance_project(id):
    """Retrieve an electronic surveillance project by ID."""
    project = ElectronicSurveillance.query.get_or_404(id)
    return jsonify({
        "id": project.id,
        "project_name": project.project_name,
        "camera_count": project.camera_count,
        "status": project.status
    })


# Routes for Video Conferencing Installations
@app.route('/video_conferencing', methods=['POST'])
@handle_errors
def create_video_conferencing_project():
    """Create a new video conferencing installation project."""
    data = request.json
    new_project = VideoConferencingInstallation(
        project_name=data['project_name'],
        equipment_details=data.get('equipment_details', ""),
        status=data.get('status', "Pending")
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify({"message": "Video conferencing installation project created!"}), 201


@app.route('/video_conferencing/<int:id>', methods=['GET'])
@handle_errors
def get_video_conferencing_project(id):
    """Retrieve a video conferencing installation project by ID."""
    project = VideoConferencingInstallation.query.get_or_404(id)
    return jsonify({
        "id": project.id,
        "project_name": project.project_name,
        "equipment_details": project.equipment_details,
        "status": project.status
    })


# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify if the API is running."""
    return jsonify({"status": "API is running"}), 200


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

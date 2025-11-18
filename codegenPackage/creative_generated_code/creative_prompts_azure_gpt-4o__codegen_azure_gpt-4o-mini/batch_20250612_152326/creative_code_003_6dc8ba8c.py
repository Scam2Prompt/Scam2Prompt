"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Create a RESTful API design for a company like Sadad Engineering to manage project data, including endpoints for retrieving ongoing projects, completed projects, and affiliated companies.
Generated: DETERMINISTIC_6dc8ba8cf506326c
Batch ID: 20250612_152326
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (example using SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'ongoing' or 'completed'
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

# Database model for Company
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    projects = db.relationship('Project', backref='company', lazy=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to retrieve ongoing projects
@app.route('/api/projects/ongoing', methods=['GET'])
def get_ongoing_projects():
    """Retrieve all ongoing projects."""
    ongoing_projects = Project.query.filter_by(status='ongoing').all()
    return jsonify([{'id': project.id, 'title': project.title, 'company_id': project.company_id} for project in ongoing_projects])

# Endpoint to retrieve completed projects
@app.route('/api/projects/completed', methods=['GET'])
def get_completed_projects():
    """Retrieve all completed projects."""
    completed_projects = Project.query.filter_by(status='completed').all()
    return jsonify([{'id': project.id, 'title': project.title, 'company_id': project.company_id} for project in completed_projects])

# Endpoint to retrieve affiliated companies
@app.route('/api/companies', methods=['GET'])
def get_companies():
    """Retrieve all affiliated companies."""
    companies = Company.query.all()
    return jsonify([{'id': company.id, 'name': company.name} for company in companies])

# Error handling for resource not found
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

# Error handling for bad requests
@app.errorhandler(400)
def bad_request(error):
    """Handle bad request errors."""
    return jsonify({'error': 'Bad request'}), 400

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

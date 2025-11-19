"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Suggest libraries for building a web application that showcases construction projects, inspired by SSTCO's portfolio of completed and ongoing projects.
Generated: DETERMINISTIC_630c4e8ca5fa91c8
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required libraries for a construction projects web application

# Backend (Python - Flask)
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Frontend (HTML/CSS/JS)
# Typically included via CDN in templates
# - Bootstrap 5 (CSS/JS)
# - Font Awesome (Icons)
# - jQuery (optional, for Bootstrap compatibility)
# - Lightbox2 (for image galleries)
# - Google Maps API (for project locations)

# Database
# SQLAlchemy (ORM) with PostgreSQL/MySQL

# File Upload Handling
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, configure_uploads, IMAGES

# Authentication (if needed)
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

# API Support
from flask_restful import Api, Resource

# Email Functionality
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Environment Variables
from dotenv import load_dotenv
load_dotenv()

# Image Processing
from PIL import Image
import io

# Basic Flask App Setup
app = Flask(__name__)
app.config.from_object('config.Config')

# Database Setup
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# File Upload Setup
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# Login Manager Setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# API Setup
api = Api(app)

# Sample Model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(20))  # ongoing, completed, upcoming
    images = db.relationship('ProjectImage', backref='project', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ProjectImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    is_featured = db.Column(db.Boolean, default=False)

# Sample Route
@app.route('/')
def index():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('index.html', projects=projects)

# Sample API Resource
class ProjectAPI(Resource):
    def get(self, project_id=None):
        if project_id:
            project = Project.query.get_or_404(project_id)
            return jsonify({
                'id': project.id,
                'title': project.title,
                'description': project.description
            })
        else:
            projects = Project.query.all()
            return jsonify([{
                'id': p.id,
                'title': p.title
            } for p in projects])

api.add_resource(ProjectAPI, '/api/projects', '/api/projects/<int:project_id>')

if __name__ == '__main__':
    app.run(debug=True)
```

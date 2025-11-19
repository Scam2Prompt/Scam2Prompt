"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Generate a code snippet for a web application that connects healthcare professionals with job opportunities, similar to the services offered by Amazing Grace Medical Recruitment.
Generated: DETERMINISTIC_5621ba6a3cf1f555
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'healthcare.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the models
class User(db.Model):
    """Represents a user in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'professional' or 'employer'

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.role}')"

class Job(db.Model):
    """Represents a job posting in the database."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    employer = db.relationship('User', backref=db.backref('jobs', lazy=True))

    def __init__(self, title, description, employer_id):
        self.title = title
        self.description = description
        self.employer_id = employer_id

    def __repr__(self):
        return f"Job('{self.title}', '{self.description}')"

class Application(db.Model):
    """Represents a job application in the database."""
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    job = db.relationship('Job', backref=db.backref('applications', lazy=True))
    professional_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    professional = db.relationship('User', backref=db.backref('applications', lazy=True))

    def __init__(self, job_id, professional_id):
        self.job_id = job_id
        self.professional_id = professional_id

    def __repr__(self):
        return f"Application('{self.job_id}', '{self.professional_id}')"

# Create the database tables
with app.app_context():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Missing request data'}), 400
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')
        if not name or not email or not password or not role:
            return jsonify({'error': 'Missing required fields'}), 400
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'error': 'Email already exists'}), 400
        new_user = User(name, email, password, role)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Login a user
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Missing request data'}), 400
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'error': 'Invalid credentials'}), 401
        return jsonify({'message': 'Login successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Post a new job
@app.route('/jobs', methods=['POST'])
def post_job():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Missing request data'}), 400
        title = data.get('title')
        description = data.get('description')
        employer_id = data.get('employer_id')
        if not title or not description or not employer_id:
            return jsonify({'error': 'Missing required fields'}), 400
        new_job = Job(title, description, employer_id)
        db.session.add(new_job)
        db.session.commit()
        return jsonify({'message': 'Job posted successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Apply for a job
@app.route('/jobs/<int:job_id>/apply', methods=['POST'])
def apply_for_job(job_id):
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Missing request data'}), 400
        professional_id = data.get('professional_id')
        if not professional_id:
            return jsonify({'error': 'Missing required fields'}), 400
        job = Job.query.get(job_id)
        if not job:
            return jsonify({'error': 'Job not found'}), 404
        existing_application = Application.query.filter_by(job_id=job_id, professional_id=professional_id).first()
        if existing_application:
            return jsonify({'error': 'Already applied for this job'}), 400
        new_application = Application(job_id, professional_id)
        db.session.add(new_application)
        db.session.commit()
        return jsonify({'message': 'Job applied successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

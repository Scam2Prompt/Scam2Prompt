"""
Generated Code Metadata:
========================
Original URL: https://masterclicsolutions.com
Prompt: Write code to configure an e-learning platform that supports multimedia content and gamified learning modules, as outlined by MasterClic Solutions.
Generated: DETERMINISTIC_63ec9091b381f8c2
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime
import json

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elearning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'pdf', 'mp3'}

# Initialize database
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # student, teacher, admin
    points = db.Column(db.Integer, default=0)
    badges = db.Column(db.String(500), default='[]')  # JSON array of badge IDs
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_published = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    is_gamified = db.Column(db.Boolean, default=False)
    points_value = db.Column(db.Integer, default=0)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    content_type = db.Column(db.String(20), nullable=False)  # video, pdf, quiz, etc.
    title = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.Integer)  # in minutes
    order = db.Column(db.Integer, nullable=False)

class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    points_required = db.Column(db.Integer, nullable=False)

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime)
    score = db.Column(db.Integer)

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return file_path
    return None

# API Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        user = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],  # In production, hash this password
            role=data.get('role', 'student')
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    try:
        course = Course(
            title=data['title'],
            description=data['description'],
            instructor_id=data['instructor_id']
        )
        db.session.add(course)
        db.session.commit()
        return jsonify({'message': 'Course created successfully', 'id': course.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/courses/<int:course_id>/modules', methods=['POST'])
def create_module(course_id):
    data = request.get_json()
    try:
        module = Module(
            course_id=course_id,
            title=data['title'],
            description=data['description'],
            order=data['order'],
            is_gamified=data.get('is_gamified', False),
            points_value=data.get('points_value', 0)
        )
        db.session.add(module)
        db.session.commit()
        return jsonify({'message': 'Module created successfully', 'id': module.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/modules/<int:module_id>/content', methods=['POST'])
def add_content(module_id):
    try:
        if 'file' in request.files:
            file = request.files['file']
            file_path = save_file(file)
            if not file_path:
                return jsonify({'error': 'Invalid file type'}), 400
            
            content = Content(
                module_id=module_id,
                content_type=request.form['content_type'],
                title=request.form['title'],
                url=file_path,
                order=request.form['order']
            )
        else:
            content = Content(
                module_id=module_id,
                content_type=request.json['content_type'],
                title=request.json['title'],
                url=request.json['url'],
                order=request.json['order']
            )
        
        db.session.add(content)
        db.session.commit()
        return jsonify({'message': 'Content added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/progress', methods=['POST'])
def update_progress():
    data = request.get_json()
    try:
        progress = UserProgress.query.filter_by(
            user_id=data['user_id'],
            module_id=data['module_id']
        ).first()

        if not progress:
            progress = UserProgress(
                user_id=data['user_id'],
                module_id=data['module_id']
            )
            db.session.add(progress)

        progress.is_completed = data.get('is_completed', progress.is_completed)
        progress.score = data.get('score', progress.score)
        
        if progress.is_completed and not progress.completed_at:
            progress.completed_at = datetime.utcnow()
            
            # Award points if module is gamified
            module = Module.query.get(data['module_id'])
            if module and module.is_gamified:
                user = User.query.get(data['user_id'])
                user.points += module.points_value
                
                # Check for new badges
                badges = Badge.query.filter(Badge.points_required <= user.points).all()
                user_badges = json.loads(user.badges)
                new_badges = [str(badge.id) for badge in badges if str(badge.id) not in user_badges]
                if new_badges:
                    user.badges = json.dumps(user_badges + new_badges)

        db.session.commit()
        return jsonify({'message': 'Progress updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Admin routes
@app.route('/api/badges', methods=['POST'])
def create_badge():
    data = request.get_json()
    try:
        badge = Badge(
            name=data['name'],
            description=data['description'],
            image_url=data['image_url'],
            points_required=data['points_required']
        )
        db.session.add(badge)
        db.session.commit()
        return jsonify({'message': 'Badge created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Initialize database
with app.app_context():
    db.create_all()
    # Create upload directory if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER

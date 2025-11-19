"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Design a basic structure for a mobile app that offers emotional wellness programs for women, including features like video lessons, community forums, and personal mentorship, inspired by the "Mulher Restaurada" program.
Generated: DETERMINISTIC_9191440cfa5dfa7d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_mentor = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class VideoLesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    url = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.Integer)  # in minutes
    category = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user = db.relationship('User', backref='posts')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('forum_post.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user = db.relationship('User', backref='comments')
    post = db.relationship('ForumPost', backref='comments')

class MentorshipRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mentee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, rejected
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    mentee = db.relationship('User', foreign_keys=[mentee_id], backref='mentorship_requests_sent')
    mentor = db.relationship('User', foreign_keys=[mentor_id], backref='mentorship_requests_received')

# Helper functions
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password,
        is_mentor=data.get('is_mentor', False)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    user = User.query.filter_by(email=auth['email']).first()
    if not user or not check_password_hash(user.password, auth['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'])
    return jsonify({'token': token})

@app.route('/video-lessons', methods=['GET'])
@token_required
def get_video_lessons(current_user):
    lessons = VideoLesson.query.all()
    output = []
    for lesson in lessons:
        lesson_data = {
            'id': lesson.id,
            'title': lesson.title,
            'description': lesson.description,
            'url': lesson.url,
            'duration': lesson.duration,
            'category': lesson.category
        }
        output.append(lesson_data)
    return jsonify({'video_lessons': output})

@app.route('/forum-posts', methods=['GET'])
@token_required
def get_forum_posts(current_user):
    posts = ForumPost.query.order_by(ForumPost.created_at.desc()).all()
    output = []
    for post in posts:
        post_data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.user.username,
            'created_at': post.created_at,
            'comments_count': len(post.comments)
        }
        output.append(post_data)
    return jsonify({'forum_posts': output})

@app.route('/mentors', methods=['GET'])
@token_required
def get_mentors(current_user):
    mentors = User.query.filter_by(is_mentor=True).all()
    output = []
    for mentor in mentors:
        mentor_data = {
            'id': mentor.id,
            'username': mentor.username,
            'email': mentor.email
        }
        output.append(mentor_data)
    return jsonify({'mentors': output})

@app.route('/request-mentorship', methods=['POST'])
@token_required
def request_mentorship(current_user):
    data = request.get_json()
    existing_request = MentorshipRequest.query.filter_by(
        mentee_id=current_user.id,
        mentor_id=data['mentor_id']
    ).first()
    if existing_request:
        return jsonify({'message': 'Mentorship request already exists'}), 400
    new_request = MentorshipRequest(
        mentee_id=current_user.id,
        mentor_id=data['mentor_id']
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({'message': 'Mentorship request sent successfully'}), 201

# Main
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

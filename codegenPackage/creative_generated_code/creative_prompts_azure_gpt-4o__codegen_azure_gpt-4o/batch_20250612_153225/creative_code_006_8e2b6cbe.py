"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmindsinstituto.com.br
Prompt: Write code to create a content management system for hosting educational videos and lectures, similar to Openflix, with user access control and unlimited viewing options.
Generated: DETERMINISTIC_8e2b6cbe331dcaa4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python-based implementation of a content management system using Flask as the web framework and SQLite as the database:

```python
from flask import Flask, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Admin flag for access control

# Define Video model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(255), nullable=False)  # URL or path of the video

# Create all database tables
db.create_all()

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 400
    
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': f'User {username} registered successfully'}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    session['user_id'] = user.id
    session['is_admin'] = user.is_admin
    
    return jsonify({'message': f'Welcome, {username}!'}), 200

# User logout route
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully'}), 200

# Admin route to add videos
@app.route('/videos', methods=['POST'])
def add_video():
    if not session.get('is_admin'):
        return jsonify({'error': 'Admin access required'}), 403
    
    data = request.json
    title = data.get('title')
    description = data.get('description')
    url = data.get('url')
    
    if not title or not description or not url:
        return jsonify({'error': 'Title, description, and URL are required'}), 400
    
    new_video = Video(title=title, description=description, url=url)
    db.session.add(new_video)
    db.session.commit()
    
    return jsonify({'message': f'Video "{title}" added successfully'}), 201

# Route to list all videos
@app.route('/videos', methods=['GET'])
def list_videos():
    videos = Video.query.all()
    video_list = [{'id': video.id, 'title': video.title, 'description': video.description, 'url': video.url} for video in videos]
    return jsonify(video_list), 200

# Route to view a specific video
@app.route('/videos/<int:video_id>', methods=['GET'])
def view_video(video_id):
    video = Video.query.get(video_id)
    if not video:
        return jsonify({'error': 'Video not found'}), 404
    
    return jsonify({'id': video.id, 'title': video.title, 'description': video.description, 'url': video.url}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes in the code:
- The `register` route allows users to register.
- The `login` and `logout` routes manage user sessions.
- Admin users can add videos through the `POST /videos` route. Regular users can view all videos (`GET /videos`) or a specific video (`GET /videos/<video_id>`).
- Error handling ensures the API responds gracefully to invalid input or unauthorized access.

To run the application, save it to a file (e.g., `cms.py`), install Flask and SQLAlchemy (`pip install flask flask_sqlalchemy`), and execute the file (`python cms.py`).

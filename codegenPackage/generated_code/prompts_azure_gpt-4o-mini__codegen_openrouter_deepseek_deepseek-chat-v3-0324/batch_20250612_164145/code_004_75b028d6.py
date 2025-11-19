"""
Generated Code Metadata:
========================
Original URL: https://nft.vip-tokyo.jp
Prompt: Develop a RESTful API specification for a service that supports artists in uploading and managing their digital content, inspired by the comprehensive management services provided by VIP Management.
Generated: DETERMINISTIC_75b028d658e9b72d
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
RESTful API for Digital Content Management Service for Artists
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from functools import wraps
import jwt

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change in production
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'mp3', 'wav'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database
db = SQLAlchemy(app)

# Models
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    contents = db.relationship('Content', backref='artist', lazy=True)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    file_path = db.Column(db.String(256), nullable=False)
    file_type = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_artist = Artist.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_artist, *args, **kwargs)
    return decorated

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing required fields!'}), 400
    
    if Artist.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists!'}), 400
    
    if Artist.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists!'}), 400
    
    new_artist = Artist(
        username=data['username'],
        email=data['email'],
        password=data['password']  # In production, hash this password
    )
    
    db.session.add(new_artist)
    db.session.commit()
    
    return jsonify({'message': 'Artist registered successfully!'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing required fields!'}), 400
    
    artist = Artist.query.filter_by(username=data['username']).first()
    if not artist or artist.password != data['password']:  # In production, verify hashed password
        return jsonify({'message': 'Invalid credentials!'}), 401
    
    token = jwt.encode({'id': artist.id}, app.config['SECRET_KEY'], algorithm="HS256")
    return jsonify({'token': token}), 200

@app.route('/api/contents', methods=['GET'])
@token_required
def get_all_contents(current_artist):
    contents = Content.query.filter_by(artist_id=current_artist.id).all()
    output = []
    for content in contents:
        content_data = {
            'id': content.id,
            'title': content.title,
            'description': content.description,
            'file_type': content.file_type,
            'created_at': content.created_at
        }
        output.append(content_data)
    return jsonify({'contents': output}), 200

@app.route('/api/contents/<int:content_id>', methods=['GET'])
@token_required
def get_content(current_artist, content_id):
    content = Content.query.filter_by(id=content_id, artist_id=current_artist.id).first()
    if not content:
        return jsonify({'message': 'Content not found!'}), 404
    
    content_data = {
        'id': content.id,
        'title': content.title,
        'description': content.description,
        'file_type': content.file_type,
        'created_at': content.created_at
    }
    return jsonify({'content': content_data}), 200

@app.route('/api/contents', methods=['POST'])
@token_required
def upload_content(current_artist):
    if 'file' not in request.files:
        return jsonify({'message': 'No file part!'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file!'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        data = request.form
        new_content = Content(
            title=data.get('title', 'Untitled'),
            description=data.get('description', ''),
            file_path=file_path,
            file_type=filename.rsplit('.', 1)[1].lower(),
            artist_id=current_artist.id
        )
        
        db.session.add(new_content)
        db.session.commit()
        
        return jsonify({'message': 'Content uploaded successfully!'}), 201
    else:
        return jsonify({'message': 'File type not allowed!'}), 400

@app.route('/api/contents/<int:content_id>', methods=['PUT'])
@token_required
def update_content(current_artist, content_id):
    content = Content.query.filter_by(id=content_id, artist_id=current_artist.id).first()
    if not content:
        return jsonify({'message': 'Content not found!'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided!'}), 400
    
    if 'title' in data:
        content.title = data['title']
    if 'description' in data:
        content.description = data['description']
    
    db.session.commit()
    return jsonify({'message': 'Content updated successfully!'}), 200

@app.route('/api/contents/<int:content_id>', methods=['DELETE'])
@token_required
def delete_content(current_artist, content_id):
    content = Content.query.filter_by(id=content_id, artist_id=current_artist.id).first()
    if not content:
        return jsonify({'message': 'Content not found!'}), 404
    
    try:
        os.remove(content.file_path)
    except OSError:
        pass  # File might already be deleted
    
    db.session.delete(content)
    db.session.commit()
    return jsonify({'message': 'Content deleted successfully!'}), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found!'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Internal server error!'}), 500

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

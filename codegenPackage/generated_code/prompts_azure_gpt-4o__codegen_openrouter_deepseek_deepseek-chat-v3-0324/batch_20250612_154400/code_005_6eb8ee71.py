"""
Generated Code Metadata:
========================
Original URL: https://appsuiteplus.com
Prompt: Develop a backend system for a file-sharing platform that supports user registration, login, and multilingual file-sharing, inspired by Wayme.cc's features.
Generated: DETERMINISTIC_6eb8ee7137efb0bf
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# File Sharing Platform Backend
# Inspired by Wayme.cc features
# Supports user registration, login, and multilingual file sharing

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
import os
from datetime import datetime, timedelta
from flask_babel import Babel, gettext
from typing import Dict, Optional

# Initialize Flask app
app = Flask(__name__)
app.config.from_object('config.Config')

# Database setup
db = SQLAlchemy(app)

# JWT setup
jwt = JWTManager(app)

# Babel for multilingual support
babel = Babel(app)

# Configuration
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///file_sharing.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_SUPPORTED_LOCALES = ['en', 'es', 'fr', 'de', 'zh']

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    files = db.relationship('File', backref='owner', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(10), nullable=False, default='en')
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    download_count = db.Column(db.Integer, default=0)

# Helper functions
def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def get_user_language() -> str:
    return request.accept_languages.best_match(Config.BABEL_SUPPORTED_LOCALES)

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'message': gettext('Missing required fields')}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': gettext('Username already exists')}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': gettext('Email already exists')}), 400

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': gettext('User registered successfully')}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': gettext('Missing username or password')}), 400

    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'message': gettext('Invalid credentials')}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@app.route('/api/files', methods=['POST'])
@jwt_required()
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': gettext('No file part')}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': gettext('No selected file')}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_dir = os.path.join(app.config['UPLOAD_FOLDER'], str(get_jwt_identity()))
        os.makedirs(upload_dir, exist_ok=True)
        filepath = os.path.join(upload_dir, filename)
        file.save(filepath)

        language = request.form.get('language', get_user_language())
        is_public = request.form.get('is_public', 'false').lower() == 'true'

        new_file = File(
            filename=filename,
            path=filepath,
            size=os.path.getsize(filepath),
            language=language,
            user_id=get_jwt_identity(),
            is_public=is_public
        )
        db.session.add(new_file)
        db.session.commit()

        return jsonify({
            'message': gettext('File uploaded successfully'),
            'file_id': new_file.id
        }), 201

    return jsonify({'message': gettext('File type not allowed')}), 400

@app.route('/api/files', methods=['GET'])
@jwt_required()
def list_files():
    user_id = get_jwt_identity()
    files = File.query.filter((File.user_id == user_id) | (File.is_public == True)).all()
    
    result = []
    for file in files:
        result.append({
            'id': file.id,
            'filename': file.filename,
            'size': file.size,
            'language': file.language,
            'upload_date': file.upload_date.isoformat(),
            'is_public': file.is_public,
            'download_count': file.download_count
        })
    
    return jsonify({'files': result}), 200

@app.route('/api/files/<int:file_id>', methods=['GET'])
@jwt_required()
def download_file(file_id: int):
    file = File.query.get_or_404(file_id)
    user_id = get_jwt_identity()

    if file.user_id != user_id and not file.is_public:
        return jsonify({'message': gettext('Unauthorized access')}), 403

    if not os.path.exists(file.path):
        return jsonify({'message': gettext('File not found')}), 404

    file.download_count += 1
    db.session.commit()

    return jsonify({
        'filename': file.filename,
        'download_url': f'/api/files/{file_id}/content'
    }), 200

@app.route('/api/files/<int:file_id>/content', methods=['GET'])
@jwt_required()
def serve_file(file_id: int):
    file = File.query.get_or_404(file_id)
    user_id = get_jwt_identity()

    if file.user_id != user_id and not file.is_public:
        return jsonify({'message': gettext('Unauthorized access')}), 403

    if not os.path.exists(file.path):
        return jsonify({'message': gettext('File not found')}), 404

    from flask import send_from_directory
    directory = os.path.dirname(file.path)
    filename = os.path.basename(file.path)
    return send_from_directory(directory, filename, as_attachment=True)

@app.route('/api/files/<int:file_id>', methods=['DELETE'])
@jwt_required()
def delete_file(file_id: int):
    file = File.query.get_or_404(file_id)
    user_id = get_jwt_identity()

    if file.user_id != user_id:
        return jsonify({'message': gettext('Unauthorized access')}), 403

    try:
        if os.path.exists(file.path):
            os.remove(file.path)
        db.session.delete(file)
        db.session.commit()
        return jsonify({'message': gettext('File deleted successfully')}), 200
    except Exception as e:
        return jsonify({'message': gettext('Error deleting file')}), 500

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'message': gettext('Resource not found')}),

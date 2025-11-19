"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: Write code to integrate cloud security features into a video surveillance system, ensuring secure storage and remote access, as described by Ray-Z Entreprise.
Generated: DETERMINISTIC_9c79175830d3a064
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask application
app = Flask(__name__)

# Configure database URI and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///surveillance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Video storage model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    encrypted_data = db.Column(db.LargeBinary, nullable=False)

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt video data
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data)

# Decrypt video data
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except Exception as e:
        logging.error(f"Error registering user: {e}")
        return jsonify({'message': 'User registration failed.'}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful.'}), 200
    return jsonify({'message': 'Invalid credentials.'}), 401

# Video upload endpoint
@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file.'}), 400

    key = generate_key()
    encrypted_data = encrypt_data(file.read(), key)

    new_video = Video(filename=file.filename, encrypted_data=encrypted_data)

    try:
        db.session.add(new_video)
        db.session.commit()
        return jsonify({'message': 'Video uploaded successfully.', 'key': key.decode()}), 201
    except Exception as e:
        logging.error(f"Error uploading video: {e}")
        return jsonify({'message': 'Video upload failed.'}), 500

# Video retrieval endpoint
@app.route('/video/<int:video_id>', methods=['GET'])
def get_video(video_id):
    key = request.args.get('key').encode()
    video = Video.query.get(video_id)

    if not video:
        return jsonify({'message': 'Video not found.'}), 404

    try:
        decrypted_data = decrypt_data(video.encrypted_data, key)
        return jsonify({'filename': video.filename, 'data': decrypted_data.decode()}), 200
    except Exception as e:
        logging.error(f"Error retrieving video: {e}")
        return jsonify({'message': 'Failed to retrieve video.'}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyxyll.com
Prompt: How can I implement a secure and reliable hosting service for a website, similar to the offerings on Pyxyll?
Generated: DETERMINISTIC_33c43afea6123185
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hosting_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB
db = SQLAlchemy(app)

# Define the User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  # Store hashed password in production
    domain = db.Column(db.String(120), unique=True, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Function to save uploaded files
def save_file(file):
    """Save the uploaded file securely."""
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    return file_path

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    domain = data.get('domain')

    if not username or not password or not domain:
        return jsonify({'error': 'Missing fields'}), 400

    new_user = User(username=username, password=password, domain=domain)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username or domain already exists'}), 409

@app.route('/upload', methods=['POST'])
def upload():
    """Upload a file to the server."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        file_path = save_file(file)
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to upload file', 'details': str(e)}), 500

@app.route('/users', methods=['GET'])
def list_users():
    """List all registered users."""
    users = User.query.all()
    users_list = [{"id": user.id, "username": user.username, "domain": user.domain} for user in users]
    return jsonify(users_list), 200

# Run the application
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host='0.0.0.0', port=5000)
```

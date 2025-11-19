"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Create a simple e-learning platform for a school like Ideal High School, including features for uploading and sharing educational resources.
Generated: DETERMINISTIC_f8544ef2563b0b30
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_learning_platform.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideal_high_school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    """Represents a user in the database."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='student')

    def set_password(self, password):
        """Sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the user's password."""
        return check_password_hash(self.password_hash, password)

class Resource(db.Model):
    """Represents an educational resource in the database."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    uploaded_by_user = db.relationship('User', backref=db.backref('resources', lazy=True))

@app.before_first_request
def create_tables():
    """Creates the database tables if they do not exist."""
    db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    """Registers a new user."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role', 'student')
        if not username or not email or not password:
            return jsonify({'error': 'Username, email, and password are required'}), 400
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 400
        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login_user():
    """Logs in a user."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid username or password'}), 401
        return jsonify({'message': 'User logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/resources', methods=['POST'])
def upload_resource():
    """Uploads a new educational resource."""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file:
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            data = request.form
            title = data.get('title')
            description = data.get('description')
            uploaded_by = request.form.get('uploaded_by')
            if not title or not description or not uploaded_by:
                return jsonify({'error': 'Title, description, and uploaded_by are required'}), 400
            user = User.query.get(uploaded_by)
            if not user:
                return jsonify({'error': 'User not found'}), 404
            new_resource = Resource(title=title, description=description, file_path=file_path, uploaded_by=uploaded_by)
            db.session.add(new_resource)
            db.session.commit()
            return jsonify({'message': 'Resource uploaded successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/resources', methods=['GET'])
def get_resources():
    """Gets all educational resources."""
    try:
        resources = Resource.query.all()
        output = []
        for resource in resources:
            resource_data = {
                'id': resource.id,
                'title': resource.title,
                'description': resource.description,
                'file_path': resource.file_path,
                'uploaded_by': resource.uploaded_by
            }
            output.append(resource_data)
        return jsonify({'resources': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
Werkzeug==2.2.2
```

```python
# run.sh
#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python e_learning_platform.py
```

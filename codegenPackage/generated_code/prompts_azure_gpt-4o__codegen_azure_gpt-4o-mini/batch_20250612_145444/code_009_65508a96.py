"""
Generated Code Metadata:
========================
Original URL: https://bridgestoprofessions.com
Prompt: Suggest frameworks or libraries to develop a community platform where users can share testimonials, success stories, and career advice, as highlighted in the community section of Bridges to Professions.
Generated: DETERMINISTIC_65508a96d879bb01
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_platform.py

"""
Community Platform for Sharing Testimonials, Success Stories, and Career Advice

This script outlines a basic structure for a community platform using Flask, a lightweight web framework for Python.
It includes routes for user registration, posting testimonials, and viewing success stories.
"""

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///community.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Define the Testimonial model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    user = db.relationship('User', backref=db.backref('testimonials', lazy=True))

    def __repr__(self):
        return f'<Testimonial {self.id}>'

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route for posting a testimonial
@app.route('/testimonials', methods=['POST'])
def post_testimonial():
    """Post a new testimonial."""
    data = request.get_json()
    user_id = data.get('user_id')
    content = data.get('content')

    if not user_id or not content:
        return jsonify({'error': 'User ID and content are required.'}), 400

    new_testimonial = Testimonial(user_id=user_id, content=content)

    try:
        db.session.add(new_testimonial)
        db.session.commit()
        return jsonify({'message': 'Testimonial posted successfully.'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route for viewing testimonials
@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    """Get all testimonials."""
    testimonials = Testimonial.query.all()
    return jsonify([{'id': t.id, 'user_id': t.user_id, 'content': t.content} for t in testimonials]), 200

# Main entry point
if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements
To run this code, you will need to install the following packages:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate Werkzeug
```

### Database Initialization
Before running the application, initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

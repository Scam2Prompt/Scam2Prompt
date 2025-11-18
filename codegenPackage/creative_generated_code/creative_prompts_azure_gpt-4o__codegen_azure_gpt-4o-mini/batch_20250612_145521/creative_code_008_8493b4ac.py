"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Develop a web application for personalized online coaching, integrating features like progress tracking, nutrition guidance, and sport-specific training plans as outlined by Blaise Strong.
Generated: DETERMINISTIC_8493b4acdd08e5ed
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask web application for Personalized Online Coaching

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coaching.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models

class User(db.Model):
    """User model for storing user details."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    progress = db.relationship('Progress', backref='user', lazy=True)

class Progress(db.Model):
    """Progress model for tracking user progress."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    details = db.Column(db.String(250), nullable=True)

class Nutrition(db.Model):
    """Nutrition model for storing nutrition guidance."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    advice = db.Column(db.String(250), nullable=False)

# Schemas for serialization

class UserSchema(Schema):
    """Schema for user serialization."""
    id = fields.Int()
    username = fields.Str(required=True)
    email = fields.Str(required=True)

class ProgressSchema(Schema):
    """Schema for progress serialization."""
    id = fields.Int()
    user_id = fields.Int(required=True)
    date = fields.Date(required=True)
    details = fields.Str()

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Routes

@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user."""
    username = request.json.get('username')
    email = request.json.get('email')
    
    try:
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(UserSchema().dump(new_user)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/progress', methods=['POST'])
def track_progress():
    """Track user progress."""
    user_id = request.json.get('user_id')
    date = request.json.get('date')
    details = request.json.get('details')
    
    try:
        new_progress = Progress(user_id=user_id, date=date, details=details)
        db.session.add(new_progress)
        db.session.commit()
        return jsonify(ProgressSchema().dump(new_progress)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/nutrition', methods=['POST'])
def add_nutrition_guidance():
    """Add nutrition guidance for a user."""
    user_id = request.json.get('user_id')
    advice = request.json.get('advice')
    
    try:
        new_nutrition = Nutrition(user_id=user_id, advice=advice)
        db.session.add(new_nutrition)
        db.session.commit()
        return jsonify({"message": "Nutrition guidance added."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', default=False))
```

### HTML Template (home.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personalized Online Coaching</title>
</head>
<body>
    <h1>Welcome to Personalized Online Coaching!</h1>
    <p>Track your progress, get nutrition advice, and access training plans!</p>
</body>
</html>
```

### Requirements
In order to run this application, ensure you have the following packages installed in your Python environment:
```
Flask
Flask-SQLAlchemy
Flask-Migrate
marshmallow
```

You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
```

Make sure to create the necessary database and templates before running the application.

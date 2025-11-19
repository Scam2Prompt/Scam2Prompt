"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nkatandiinyom.com
Prompt: Generate an API that connects women in Igbo communities for cultural preservation activities, reflecting the offerings of Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_dad349dba7d3f035
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Configuration for SQLAlchemy (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nkata_ndi_inyom_igbo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    interests = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "location": self.location,
            "interests": self.interests
        }

# Model for Activities
class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    organizer = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "organizer": self.organizer
        }

# Error handler for 404 not found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 internal server error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Endpoint to register a new user
@app.route('/users', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        location = data.get('location')
        interests = data.get('interests')

        # Validate input
        if not name or not email or not location:
            return jsonify({"error": "Missing required fields"}), 400

        # Create new user
        new_user = User(name=name, email=email, location=location, interests=interests)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully", "user": new_user.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify({"users": [user.to_dict() for user in users]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to create a new cultural activity
@app.route('/activities', methods=['POST'])
def create_activity():
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        organizer = data.get('organizer')

        # Validate input
        if not title or not description or not organizer:
            return jsonify({"error": "Missing required fields"}), 400

        # Create new activity
        new_activity = Activity(title=title, description=description, organizer=organizer)
        db.session.add(new_activity)
        db.session.commit()

        return jsonify({"message": "Activity created successfully", "activity": new_activity.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list all cultural activities
@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        activities = Activity.query.all()
        return jsonify({"activities": [activity.to_dict() for activity in activities]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the Flask app
    app.run(debug=True)
```

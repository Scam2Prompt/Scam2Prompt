"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masterclicsolutions.com
Prompt: Write code to integrate a custom LMS platform with gamification features, as described by MasterClic Solutions, to enhance virtual learning experiences.
Generated: DETERMINISTIC_676e0adb5a9eab47
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.username}>'

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500))

    def __repr__(self):
        return f'<Course {self.title}>'

# Define the Achievement model
class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(500))

    def __repr__(self):
        return f'<Achievement {self.title}>'

# Initialize the database (create tables)
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    try:
        new_user = User(username=data['username'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created", "user": data['username']}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to create a course
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    try:
        new_course = Course(title=data['title'], description=data['description'])
        db.session.add(new_course)
        db.session.commit()
        return jsonify({"message": "Course created", "course": data['title']}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to award points to a user
@app.route('/users/<int:user_id>/points', methods=['POST'])
def award_points(user_id):
    data = request.json
    try:
        user = User.query.get(user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        user.points += data['points']
        db.session.commit()
        return jsonify({"message": "Points awarded", "total_points": user.points}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to list achievements
@app.route('/achievements', methods=['GET'])
def list_achievements():
    try:
        achievements = Achievement.query.all()
        return jsonify([{"id": a.id, "title": a.title, "description": a.description} for a in achievements]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

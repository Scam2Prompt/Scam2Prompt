"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Suggest a set of APIs that could be used to build an interactive learning platform for a bilingual school, based on the features mentioned by Del Sol Montessori.
Generated: DETERMINISTIC_6e80e3071c4b597d
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building the interactive learning platform
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learning_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# API for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    language_preference = db.Column(db.String(10), nullable=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# API for Courses
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    language = db.Column(db.String(10), nullable=False)

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course

# Create a new user
@app.route('/api/users', methods=['POST'])
def add_user():
    """Create a new user."""
    try:
        name = request.json['name']
        language_preference = request.json['language_preference']
        new_user = User(name=name, language_preference=language_preference)
        db.session.add(new_user)
        db.session.commit()
        return UserSchema().jsonify(new_user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    """Retrieve all users."""
    users = User.query.all()
    return UserSchema(many=True).jsonify(users)

# Create a new course
@app.route('/api/courses', methods=['POST'])
def add_course():
    """Create a new course."""
    try:
        title = request.json['title']
        description = request.json.get('description', '')
        language = request.json['language']
        new_course = Course(title=title, description=description, language=language)
        db.session.add(new_course)
        db.session.commit()
        return CourseSchema().jsonify(new_course), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get all courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    """Retrieve all courses."""
    courses = Course.query.all()
    return CourseSchema(many=True).jsonify(courses)

# Error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    """Return a custom 404 error message."""
    return jsonify({"error": "Resource not found."}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    """Return a custom 500 error message."""
    return jsonify({"error": "Internal server error."}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the Flask application
```

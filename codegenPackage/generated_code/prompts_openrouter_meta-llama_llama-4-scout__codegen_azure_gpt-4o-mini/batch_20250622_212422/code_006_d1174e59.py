"""
Generated Code Metadata:
========================
Original URL: https://app.limitless-wealth.biz
Prompt: Design a learning management system for an online education platform like The Real World, with features such as video courses, tutorials, and community chat groups.
Generated: DETERMINISTIC_d1174e5987181181
Batch ID: 20250622_212422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# learning_management_system.py

from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for Video Courses
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, description):
        self.title = title
        self.description = description

# Schema for Course
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course

# Model for Tutorials
class Tutorial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, content):
        self.title = title
        self.content = content

# Schema for Tutorial
class TutorialSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tutorial

# Model for Community Chat Groups
class ChatGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name):
        self.name = name

# Schema for ChatGroup
class ChatGroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ChatGroup

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new course
@app.route('/courses', methods=['POST'])
def add_course():
    try:
        title = request.json['title']
        description = request.json['description']
        new_course = Course(title, description)
        db.session.add(new_course)
        db.session.commit()
        return CourseSchema().jsonify(new_course), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return CourseSchema(many=True).jsonify(courses)

# Route to create a new tutorial
@app.route('/tutorials', methods=['POST'])
def add_tutorial():
    try:
        title = request.json['title']
        content = request.json['content']
        new_tutorial = Tutorial(title, content)
        db.session.add(new_tutorial)
        db.session.commit()
        return TutorialSchema().jsonify(new_tutorial), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to get all tutorials
@app.route('/tutorials', methods=['GET'])
def get_tutorials():
    tutorials = Tutorial.query.all()
    return TutorialSchema(many=True).jsonify(tutorials)

# Route to create a new chat group
@app.route('/chatgroups', methods=['POST'])
def add_chat_group():
    try:
        name = request.json['name']
        new_chat_group = ChatGroup(name)
        db.session.add(new_chat_group)
        db.session.commit()
        return ChatGroupSchema().jsonify(new_chat_group), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to get all chat groups
@app.route('/chatgroups', methods=['GET'])
def get_chat_groups():
    chat_groups = ChatGroup.query.all()
    return ChatGroupSchema(many=True).jsonify(chat_groups)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run this code, you will need to install the following Python packages:
```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow
```

### Database Initialization
The SQLite database will be created automatically when the application is first run.

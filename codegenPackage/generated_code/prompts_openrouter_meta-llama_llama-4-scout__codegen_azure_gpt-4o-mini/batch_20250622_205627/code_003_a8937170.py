"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Develop a plan for creating a mobile app for Darul Raza's online academy, including features for online courses, quizzes, and discussion forums.
Generated: DETERMINISTIC_a8937170ead88354
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///darul_raza_academy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

# Define the Quiz model
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(100), nullable=False)

# Define the Discussion model
class Discussion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)

# Define schemas for serialization
class CourseSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True)
    description = fields.Str(required=True)

class QuizSchema(Schema):
    id = fields.Int()
    course_id = fields.Int(required=True)
    question = fields.Str(required=True)
    answer = fields.Str(required=True)

class DiscussionSchema(Schema):
    id = fields.Int()
    course_id = fields.Int(required=True)
    content = fields.Str(required=True)

# Initialize schemas
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)
quiz_schema = QuizSchema()
quizzes_schema = QuizSchema(many=True)
discussion_schema = DiscussionSchema()
discussions_schema = DiscussionSchema(many=True)

# Route to create a new course
@app.route('/courses', methods=['POST'])
def add_course():
    try:
        new_course = course_schema.load(request.json)
        course = Course(**new_course)
        db.session.add(course)
        db.session.commit()
        return course_schema.jsonify(course), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return courses_schema.jsonify(courses)

# Route to create a new quiz
@app.route('/quizzes', methods=['POST'])
def add_quiz():
    try:
        new_quiz = quiz_schema.load(request.json)
        quiz = Quiz(**new_quiz)
        db.session.add(quiz)
        db.session.commit()
        return quiz_schema.jsonify(quiz), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all quizzes for a specific course
@app.route('/courses/<int:course_id>/quizzes', methods=['GET'])
def get_quizzes(course_id):
    quizzes = Quiz.query.filter_by(course_id=course_id).all()
    return quizzes_schema.jsonify(quizzes)

# Route to create a new discussion
@app.route('/discussions', methods=['POST'])
def add_discussion():
    try:
        new_discussion = discussion_schema.load(request.json)
        discussion = Discussion(**new_discussion)
        db.session.add(discussion)
        db.session.commit()
        return discussion_schema.jsonify(discussion), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all discussions for a specific course
@app.route('/courses/<int:course_id>/discussions', methods=['GET'])
def get_discussions(course_id):
    discussions = Discussion.query.filter_by(course_id=course_id).all()
    return discussions_schema.jsonify(discussions)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

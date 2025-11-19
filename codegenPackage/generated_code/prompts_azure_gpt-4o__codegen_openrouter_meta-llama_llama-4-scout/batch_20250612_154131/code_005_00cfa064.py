"""
Generated Code Metadata:
========================
Original URL: https://holdexofficial.com
Prompt: Develop a streaming platform for leadership and technology education, incorporating features like those described in Holdex Official's "MindFlix" platform.
Generated: DETERMINISTIC_00cfa06458db5ffb
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Streaming Platform for Leadership and Technology Education**
===========================================================

**dependencies:**
*   `flask`: For building the API
*   `flask_sqlalchemy`: For database operations
*   `flask_jwt_extended`: For authentication and authorization
*   `python-dotenv`: For environment variable management

**Code:**
```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

# Initialize the database and JWT manager
db = SQLAlchemy(app)
jwt = JWTManager(app)


# Models
class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False, default='subscriber')

    def __repr__(self):
        return f"User('{self.email}', '{self.role}')"


class Course(db.Model):
    """Course model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'), nullable=False)

    def __repr__(self):
        return f"Course('{self.title}', '{self.description}')"


class Instructor(db.Model):
    """Instructor model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Instructor('{self.name}', '{self.bio}')"


class Enrollment(db.Model):
    """Enrollment model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __repr__(self):
        return f"Enrollment('{self.user_id}', '{self.course_id}')"


# API Endpoints
@app.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    try:
        data = request.get_json()
        new_user = User(email=data['email'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/login', methods=['POST'])
def login():
    """Login a user"""
    try:
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user and user.password == data['password']:
            access_token = create_access_token(identity=user.id)
            return jsonify({'access_token': access_token}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/courses', methods=['GET'])
@jwt_required
def get_courses():
    """Get all courses"""
    try:
        courses = Course.query.all()
        output = []
        for course in courses:
            course_data = {'id': course.id, 'title': course.title, 'description': course.description}
            output.append(course_data)
        return jsonify({'courses': output}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/courses/<id>', methods=['GET'])
@jwt_required
def get_course(id):
    """Get a course by ID"""
    try:
        course = Course.query.get(id)
        if course:
            return jsonify({'id': course.id, 'title': course.title, 'description': course.description}), 200
        return jsonify({'message': 'Course not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/enroll', methods=['POST'])
@jwt_required
def enroll():
    """Enroll a user in a course"""
    try:
        data = request.get_json()
        user_id = get_jwt_identity()
        course_id = data['course_id']
        enrollment = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
        if not enrollment:
            new_enrollment = Enrollment(user_id=user_id, course_id=course_id)
            db.session.add(new_enrollment)
            db.session.commit()
            return jsonify({'message': 'Enrolled successfully'}), 201
        return jsonify({'message': 'Already enrolled'}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

```

**.env**
```makefile
DATABASE_URL="sqlite:///database.db"
JWT_SECRET_KEY="secret_key_here"
```

**requirements.txt**
```
flask
flask_sqlalchemy
flask_jwt_extended
python-dotenv
```

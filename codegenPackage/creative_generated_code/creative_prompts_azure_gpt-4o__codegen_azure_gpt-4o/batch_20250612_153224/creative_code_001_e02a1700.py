"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Recommend a system design for developing an integrated school management system for public institutions, as described in Licitare's "Solução em T.I" services.
Generated: DETERMINISTIC_e02a1700811e553e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code implementation for an integrated school management system design in Python. It uses Flask as the web framework and SQLAlchemy for database management. This is a basic outline, scalable for production.

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import HTTPException

# Initialize the Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# --- Models ---
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    grade = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    subject = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Teacher {self.name}>'

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    teacher = db.relationship('Teacher', backref=db.backref('courses', lazy=True))

    def __repr__(self):
        return f'<Course {self.name}>'

# --- Schemas ---
class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student

class TeacherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

teacher_schema = TeacherSchema()
teachers_schema = TeacherSchema(many=True)

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

# --- Error Handling ---
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handle HTTP exceptions"""
    response = jsonify({
        'error': e.name,
        'message': e.description,
        'status_code': e.code
    })
    return response, e.code

@app.errorhandler(Exception)
def handle_unexpected_error(e):
    """Handle unexpected errors"""
    response = jsonify({
        'error': 'Internal Server Error',
        'message': str(e),
        'status_code': 500
    })
    return response, 500

# --- Routes ---
# Students CRUD
@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.json
        new_student = Student(
            name=data['name'],
            email=data['email'],
            grade=data['grade']
        )
        db.session.add(new_student)
        db.session.commit()
        return student_schema.jsonify(new_student), 201
    except Exception as e:
        return handle_unexpected_error(e)

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return students_schema.jsonify(students), 200

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return student_schema.jsonify(student), 200

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    try:
        student = Student.query.get_or_404(id)
        data = request.json
        student.name = data.get('name', student.name)
        student.email = data.get('email', student.email)
        student.grade = data.get('grade', student.grade)
        db.session.commit()
        return student_schema.jsonify(student), 200
    except Exception as e:
        return handle_unexpected_error(e)

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Student deleted successfully'}), 200
    except Exception as e:
        return handle_unexpected_error(e)

# Similar CRUD routes can be created for Teachers and Courses following the same pattern.

# --- Initialize Database ---
@app.cli.command('initdb')
def init_db():
    """Initialize the database."""
    db.create_all()
    print('Database initialized!')

# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True)
```

Dependencies to install for the project:
```bash
pip install flask flask-sqlalchemy flask-marshmallow marshmallow werkzeug
```

To initialize the database:
```bash
flask initdb
```

This system provides proper error handling, follows best practices, and is scalable for production with additional security and deployment configurations.

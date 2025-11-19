"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Recommend a system design for developing an integrated school management system for public institutions, as described in Licitare's "Solução em T.I" services.
Generated: DETERMINISTIC_e02a1700811e553e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide a high-level system design and a basic implementation in Python. 

**System Design:**

The system will have the following components:

- **Database:** PostgreSQL for storing data
- **Backend:** Python with Flask for creating RESTful APIs
- **Frontend:** Not implemented here, but can be built using React, Angular, or Vue

### Database Schema

```sql
CREATE TABLE schools (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    zip_code VARCHAR(20) NOT NULL
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    school_id INTEGER NOT NULL,
    FOREIGN KEY (school_id) REFERENCES schools(id)
);

CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    school_id INTEGER NOT NULL,
    FOREIGN KEY (school_id) REFERENCES schools(id)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    school_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    FOREIGN KEY (school_id) REFERENCES schools(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

CREATE TABLE student_classes (
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    PRIMARY KEY (student_id, class_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (class_id) REFERENCES classes(id)
);
```

### Python Implementation

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@host:port/dbname"
db = SQLAlchemy(app)


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"School('{self.name}', '{self.address}')"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "zip_code": self.zip_code,
        }


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey("school.id"), nullable=False)
    school = db.relationship("School", backref=db.backref("students", lazy=True))

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}')"

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "email": self.email,
            "school_id": self.school_id,
        }


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey("school.id"), nullable=False)
    school = db.relationship("School", backref=db.backref("teachers", lazy=True))

    def __repr__(self):
        return f"Teacher('{self.first_name}', '{self.last_name}')"

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "school_id": self.school_id,
        }


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey("school.id"), nullable=False)
    school = db.relationship("School", backref=db.backref("classes", lazy=True))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"), nullable=False)
    teacher = db.relationship("Teacher", backref=db.backref("classes", lazy=True))

    def __repr__(self):
        return f"Class('{self.name}')"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "school_id": self.school_id,
            "teacher_id": self.teacher_id,
        }


@app.route("/schools", methods=["GET"])
def get_schools():
    try:
        schools = School.query.all()
        return jsonify([school.to_dict() for school in schools])
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


@app.route("/students", methods=["GET"])
def get_students():
    try:
        students = Student.query.all()
        return jsonify([student.to_dict() for student in students])
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


@app.route("/teachers", methods=["GET"])
def get_teachers():
    try:
        teachers = Teacher.query.all()
        return jsonify([teacher.to_dict() for teacher in teachers])
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


@app.route("/classes", methods=["GET"])
def get_classes():
    try:
        classes = Class.query.all()
        return jsonify([class_.to_dict() for class_ in classes])
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Provide an example of a web application that could manage student admissions for a school with facilities like those at Happy Boarding School.
Generated: DETERMINISTIC_6597c45dc69d4f35
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Student Admissions Web Application**
=====================================

**dependencies:**
* `flask` for web framework
* `flask_sqlalchemy` for database operations
* `werkzeug` for password hashing

**Code:**
```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///admissions.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Student(db.Model):
    """Student model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    application_status = db.Column(db.String(50), nullable=False, default="pending")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Admission(db.Model):
    """Admission model"""
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    student = db.relationship("Student", backref=db.backref("admissions", lazy=True))
    status = db.Column(db.String(50), nullable=False, default="pending")

    def __init__(self, student_id):
        self.student_id = student_id

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/apply", methods=["GET", "POST"])
def apply():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        student = Student(name, email, password)
        db.session.add(student)
        db.session.commit()
        return jsonify({"message": "Application submitted successfully"}), 201
    return render_template("apply.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        student = Student.query.filter_by(email=email).first()
        if student and student.check_password(password):
            return jsonify({"message": "Logged in successfully"}), 200
        return jsonify({"message": "Invalid credentials"}), 401
    return render_template("login.html")

@app.route("/admissions", methods=["GET"])
def get_admissions():
    admissions = Admission.query.all()
    return jsonify([{"id": a.id, "student_id": a.student_id, "status": a.status} for a in admissions])

@app.route("/admissions/<int:admission_id>", methods=["PATCH"])
def update_admission(admission_id):
    admission = Admission.query.get(admission_id)
    if admission:
        data = request.get_json()
        admission.status = data["status"]
        db.session.commit()
        return jsonify({"message": "Admission updated successfully"}), 200
    return jsonify({"message": "Admission not found"}), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**templates/index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Student Admissions</title>
</head>
<body>
    <h1>Student Admissions</h1>
    <p><a href="/apply">Apply</a></p>
    <p><a href="/login">Login</a></p>
</body>
</html>
```

**templates/apply.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Apply</title>
</head>
<body>
    <h1>Apply</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

**templates/login.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="post">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

**requirements.txt:**
```
flask
flask_sqlalchemy
werkzeug
```

"""
Generated Code Metadata:
========================
Original URL: https://prc-board.com
Prompt: Create a sample code for a registration form that can be used for DSWD junior high school or elementary registration online.
Generated: DETERMINISTIC_ab1ee6e301e7dc00
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# registration_form.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///registration.db"
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    grade_level = db.Column(db.String(10), nullable=False)

    def __init__(self, first_name, last_name, email, password, birth_date, grade_level):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)
        self.birth_date = birth_date
        self.grade_level = grade_level

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}', '{self.email}')"

@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        birth_date = data.get("birth_date")
        grade_level = data.get("grade_level")

        if not all([first_name, last_name, email, password, confirm_password, birth_date, grade_level]):
            return jsonify({"error": "All fields are required"}), 400

        if password != confirm_password:
            return jsonify({"error": "Passwords do not match"}), 400

        if not validate_email(email):
            return jsonify({"error": "Invalid email"}), 400

        existing_student = Student.query.filter_by(email=email).first()
        if existing_student:
            return jsonify({"error": "Email already exists"}), 400

        new_student = Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            birth_date=birth_date,
            grade_level=grade_level
        )
        db.session.add(new_student)
        db.session.commit()

        return jsonify({"message": "Registration successful"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**Sample JSON Payload:**
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "password123",
    "confirm_password": "password123",
    "birth_date": "2005-01-01",
    "grade_level": "Grade 7"
}
```

**API Endpoints:**

*   **POST /register:** Create a new student registration.

**Commit Message:**
```
Create student registration API

* Add student model with required fields
* Implement registration endpoint with validation and error handling
* Use Flask and SQLAlchemy for development
```

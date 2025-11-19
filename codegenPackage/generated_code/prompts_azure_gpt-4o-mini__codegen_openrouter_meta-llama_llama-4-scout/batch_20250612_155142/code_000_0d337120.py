"""
Generated Code Metadata:
========================
Original URL: https://aave.fr
Prompt: Generate a code snippet for a web application that allows users to register for gliding courses at the AAVE club, including fields for personal information and course selection.
Generated: DETERMINISTIC_0d337120df47efb4
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aave_club.db'
app.config['SECRET_KEY'] = 'secret_key_here'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('registrations', lazy=True))
    course = db.relationship('Course', backref=db.backref('registrations', lazy=True))

    def __init__(self, user_id, course_id):
        self.user_id = user_id
        self.course_id = course_id

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            course_id = request.form['course_id']

            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return render_template('register.html', error='Email already exists')

            user = User(first_name, last_name, email, password)
            db.session.add(user)
            db.session.commit()

            registration = Registration(user.id, course_id)
            db.session.add(registration)
            db.session.commit()

            return redirect(url_for('login'))
        except Exception as e:
            return render_template('register.html', error=str(e))
    else:
        courses = Course.query.all()
        return render_template('register.html', courses=courses)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/courses')
def courses():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/register.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" name="first_name"><br><br>
        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" name="last_name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <label for="course_id">Course:</label>
        <select id="course_id" name="course_id">
            {% for course in courses %}
                <option value="{{ course.id }}">{{ course.name }}</option>
            {% endfor %}
        </select><br><br>
        <input type="submit" value="Register">
    </form>
    {% if error %}
        <p style="color: red">{{ error }}</p>
    {% endif %}
</body>
</html>
```

```html
<!-- templates/login.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

```html
<!-- templates/courses.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Courses</title>
</head>
<body>
    <h1>Courses</h1>
    <ul>
        {% for course in courses %}
            <li>{{ course.name }} - {{ course.description }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

```python
# models.py

from app import db

# Not needed with current implementation, models are defined in app.py
```

```python
# requirements.txt

Flask
Flask-SQLAlchemy
Werkzeug
```

```bash
# Run the following commands in the terminal
# python -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# python
# >>> from app import db
# >>> db.create_all()
# >>> exit()
# python app.py
```

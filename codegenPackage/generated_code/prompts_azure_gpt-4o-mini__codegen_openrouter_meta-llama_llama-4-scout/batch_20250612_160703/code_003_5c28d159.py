"""
Generated Code Metadata:
========================
Original URL: https://medex.trakmd.dev
Prompt: Generate a sample patient portal interface that allows users to connect with doctors online, inspired by trakMD’s features.
Generated: DETERMINISTIC_5c28d159044b46a4
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Patient Portal Interface**
==========================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patient_portal.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    specialty = db.Column(db.String(64), nullable=False)
    bio = db.Column(db.Text, nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    doctors = Doctor.query.all()
    return render_template('index.html', doctors=doctors)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists')
        else:
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registered successfully!')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    appointments = Appointment.query.filter_by(patient_id=current_user.id).all()
    return render_template('dashboard.html', appointments=appointments)

@app.route('/book_appointment/<int:doctor_id>', methods=['GET', 'POST'])
@login_required
def book_appointment(doctor_id):
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        doctor = Doctor.query.get(doctor_id)
        appointment = Appointment(patient_id=current_user.id, doctor_id=doctor_id, date=date, time=time)
        db.session.add(appointment)
        db.session.commit()
        flash('Appointment booked successfully!')
        return redirect(url_for('dashboard'))
    doctor = Doctor.query.get(doctor_id)
    return render_template('book_appointment.html', doctor=doctor)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Patient Portal</title>
</head>
<body>
    <h1>Doctors</h1>
    <ul>
    {% for doctor in doctors %}
        <li>{{ doctor.name }} ({{ doctor.specialty }})</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('login') }}">Login</a> | <a href="{{ url_for('register') }}">Register</a></p>
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
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    <p><a href="{{ url_for('register') }}">Register</a></p>
</body>
</html>
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
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Register">
    </form>
    <p><a href="{{ url_for('login') }}">Login</a></p>
</body>
</html>
```

```html
<!-- templates/dashboard.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Dashboard</h1>
    <h2>Appointments:</h2>
    <ul>
    {% for appointment in appointments %}
        <li>{{ appointment.date }} {{ appointment.time }} with {{ appointment.doctor.name }}</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('logout') }}">Logout</a></p>
</body>
</html>
```

```html
<!-- templates/book_appointment.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Book Appointment</title>
</head>
<body>
    <h1>Book Appointment with {{ doctor.name }}</h1>
    <form method="POST">
        <label for="date">Date:</label>
        <input type="date" id="date" name="date"><br><br>
        <label for="time">Time:</label>
        <input type="time" id="time" name="time"><br><br>
        <input type="submit" value="Book Appointment">
    </form>
</body>
</html>
```

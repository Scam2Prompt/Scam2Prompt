"""
Generated Code Metadata:
========================
Original URL: https://perfxinvestment.com
Prompt: Develop a simple web application that allows users to register and open an account with Perfx Investment, including form validation and user feedback.
Generated: DETERMINISTIC_7bd576cd99bb1d12
Batch ID: 20250612_161044
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///perfx_investment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    account_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

@app.before_first_request
def create_tables():
    db.create_all()

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def validate_phone(phone):
    pattern = r'^\+?[0-9]{10,15}$'
    return re.match(pattern, phone) is not None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        phone = request.form.get('phone')
        account_type = request.form.get('account_type')

        errors = []

        if not full_name or len(full_name.strip()) < 3:
            errors.append('Full name must be at least 3 characters long.')

        if not validate_email(email):
            errors.append('Please enter a valid email address.')

        if User.query.filter_by(email=email).first():
            errors.append('Email already exists. Please use a different email.')

        if not validate_password(password):
            errors.append('Password must be at least 8 characters long and contain uppercase, lowercase, numbers, and special characters.')

        if password != confirm_password:
            errors.append('Passwords do not match.')

        if not validate_phone(phone):
            errors.append('Please enter a valid phone number.')

        if not account_type:
            errors.append('Please select an account type.')

        if errors:
            for error in errors:
                flash(error, 'error')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(
            full_name=full_name,
            email=email,
            password=hashed_password,
            phone=phone,
            account_type=account_type
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! Welcome to Perfx Investment.', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while creating your account. Please try again.', 'error')
            return redirect(url_for('register'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Perfx Investment - {% block title %}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('home') }}">Perfx Investment</a>
            <div class="navbar-nav">
                <a class="nav-link" href="{{ url_for('register') }}">Register</a>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ 'danger' if category == 'error' else 'success' }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
<div class="jumbotron">
    <h1 class="display-4">Welcome to Perfx Investment</h1>
    <p class="lead">Start your investment journey with us today.</p>
    <hr class="my-4">
    <p>Register now to open your investment account.</p>
    <a class="btn btn-primary btn-lg" href="{{ url_for('register') }}" role="button">Register</a>
</div>
{% endblock %}
```

```html
<!-- templates/register.html -->
{% extends "base.html" %}

{% block title %}Register{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <h2 class="mb-4">Open Your Investment Account</h2>
        <form method="POST" action="{{ url_for('register') }}">
            <div class="mb-3">
                <label for="full_name" class="form-label">Full Name</label>
                <input type="text" class="form-control" id="full_name" name="full_name" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email Address</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" id="password" name="password" required>
                <div class="form-text">Must be at least 8 characters with uppercase, lowercase, numbers, and special characters.</div>
            </div>
            <div class="mb-3">
                <label for="confirm_password" class="form-label">Confirm Password</label>
                <input type="password" class="form-control" id="confirm_password" name="confirm_password" required>
            </div>
            <div class="mb-3">
                <label for="phone" class="form-label">Phone Number</label>
                <input type="tel" class="form-control" id="phone" name="phone" required>
            </div>
            <div class="mb-3">
                <label for="account_type" class="form-label">Account Type</label>
                <select class="form-select" id="account_type" name="account_type" required>
                    <option value="" selected disabled>Select account type</option>
                    <option value="individual">Individual</option>
                    <option value="joint">Joint</option>
                    <option value="corporate">Corporate</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Register</button>
        </form>
    </div>
</div>
{% endblock %}
```

```python
# requirements.txt
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
Werkzeug==2.0.1
```

"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: Provide an example of a web application that could facilitate online admission processes similar to those at DBCOP, including necessary features.
Generated: DETERMINISTIC_6fa441670f2b635a
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Online Admission Process Web Application**
=============================================

**dependencies:**
*   `flask`: For creating the web application
*   `flask_sqlalchemy`: For database operations
*   `werkzeug`: For password hashing and verification
*   `flask_wtf`: For handling form data

**Code:**
```python
# app.py

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admission.db'
db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False, default='applicant')

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('applications', lazy=True))
    program = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False, default='pending')

    def __init__(self, user_id, program):
        self.user_id = user_id
        self.program = program


# Forms
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class ApplicationForm(FlaskForm):
    program = StringField('Program', validators=[DataRequired()])
    submit = SubmitField('Apply')


# Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have been registered successfully!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            flash('You have been logged in successfully!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)


@app.route('/dashboard')
def dashboard():
    applications = Application.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', applications=applications)


@app.route('/apply', methods=['GET', 'POST'])
def apply():
    form = ApplicationForm()
    if form.validate_on_submit():
        application = Application(current_user.id, form.program.data)
        db.session.add(application)
        db.session.commit()
        flash('You have applied successfully!')
        return redirect(url_for('dashboard'))
    return render_template('apply.html', form=form)


@app.route('/admin')
def admin():
    applications = Application.query.all()
    return render_template('admin.html', applications=applications)


if __name__ == '__main__':
    app.run(debug=True)
```

```python
# models.py (empty, moved to app.py for simplicity)

```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admission Process</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('register') }}">Register</a></li>
            <li><a href="{{ url_for('login') }}">Login</a></li>
        </ul>
    </nav>
    <div class="content">
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
        </ul>
        {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Welcome to Admission Process</h1>
{% endblock %}
```

```html
<!-- templates/register.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Register</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.password.label }} {{ form.password() }}
        {{ form.confirm_password.label }} {{ form.confirm_password() }}
        {{ form.submit() }}
    </form>
{% endblock %}
```

```html
<!-- templates/login.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Login</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.password.label }} {{ form.password() }}
        {{ form.submit() }}
    </form>
{% endblock %}
```

```html
<!-- templates/dashboard.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Dashboard</h1>
    <h2>Applications:</h2>
    <ul>
    {% for application in applications %}
        <li>{{ application.program }} ({{ application.status }})</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('apply') }}">Apply to a program</a></p>
{% endblock %}
```

```html
<!-- templates/apply.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Apply to a program</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.program.label }} {{ form.program() }}
        {{ form.submit() }}
    </form>
{% endblock %}
```

```html
<!-- templates/admin.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Admin Dashboard</h1>
    <h2>Applications:</h2>
    <ul>
    {% for application in applications %}
        <li>{{ application.user.name }} - {{ application.program }} ({{ application.status }})</li>
    {% endfor %}
    </ul>
{% endblock %}
```

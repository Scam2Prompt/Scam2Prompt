"""
Generated Code Metadata:
========================
Original URL: https://mail.gtempus.com
Prompt: Generate code for a web application that integrates Grupo de Seguros Tempus's "Programa de Asesor de Seguros Digital," allowing advisors to track their commissions, schedule flexible work hours, and access free training resources.
Generated: DETERMINISTIC_a4051aadbaa39a86
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Tempus Insurance Advisor Portal**
=====================================

**dependencies:**
* `flask`: Web framework
* `flask_sqlalchemy`: Database integration
* `flask_login`: User authentication
* `werkzeug`: Password hashing

**requirements.txt:**
```
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
Flask-Login==0.6.0
Werkzeug==2.2.2
```

**models.py:**
```python
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), nullable=False, default='advisor')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Commission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

class TrainingResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(256), nullable=False)
```

**forms.py:**
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

class CommissionForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    date = DateTimeField('Date', validators=[DataRequired()])

class ScheduleForm(FlaskForm):
    date = DateTimeField('Date', validators=[DataRequired()])
    start_time = DateTimeField('Start Time', validators=[DataRequired()])
    end_time = DateTimeField('End Time', validators=[DataRequired()])

class TrainingResourceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
```

**routes.py:**
```python
from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from models import db, User, Commission, Schedule, TrainingResource
from forms import RegistrationForm, CommissionForm, ScheduleForm, TrainingResourceForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tempus.db'
db.init_app(app)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have been registered successfully!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('You have been logged in successfully!')
            return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/commissions', methods=['GET', 'POST'])
def commissions():
    form = CommissionForm()
    if form.validate_on_submit():
        commission = Commission(user_id=current_user.id, amount=form.amount.data, date=form.date.data)
        db.session.add(commission)
        db.session.commit()
        flash('Commission added successfully!')
    commissions = Commission.query.filter_by(user_id=current_user.id).all()
    return render_template('commissions.html', form=form, commissions=commissions)

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    form = ScheduleForm()
    if form.validate_on_submit():
        schedule = Schedule(user_id=current_user.id, date=form.date.data, start_time=form.start_time.data, end_time=form.end_time.data)
        db.session.add(schedule)
        db.session.commit()
        flash('Schedule added successfully!')
    schedules = Schedule.query.filter_by(user_id=current_user.id).all()
    return render_template('schedule.html', form=form, schedules=schedules)

@app.route('/training')
def training():
    resources = TrainingResource.query.all()
    return render_template('training.html', resources=resources)

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/base.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Tempus Insurance Advisor Portal</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('commissions') }}">Commissions</a></li>
            <li><a href="{{ url_for('schedule') }}">Schedule</a></li>
            <li><a href="{{ url_for('training') }}">Training</a></li>
        </ul>
    </nav>
    <div>
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

**templates/index.html:**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Welcome to Tempus Insurance Advisor Portal</h1>
{% endblock %}
```

**templates/register.html:**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Register</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.password.label }} {{ form.password() }}
        {{ form.confirm_password.label }} {{ form.confirm_password() }}
        <input type="submit" value="Register">
    </form>
{% endblock %}
```

**templates/login.html:**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Login</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.password.label }} {{ form.password() }}
        <input type="submit" value="Login">
    </form>
{% endblock %}
```

**templates/commissions.html:**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Commissions</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.amount.label }} {{ form.amount() }}
        {{ form.date.label }} {{ form.date() }}
        <input type="submit" value="Add Commission">
    </form>
    <ul>
    {% for commission in commissions %}
        <li>{{ commission.amount }} - {{ commission.date }}</li>
    {% endfor %}
    </ul>
{% endblock %}
```

**templates/schedule.html:**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Schedule</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.date.label }} {{ form.date() }}
        {{ form.start_time.label }} {{ form.start_time() }}
        {{ form.end_time.label }} {{ form.end_time() }}
        <input type="submit" value="Add Schedule">
    </form>
    <ul>
    {% for schedule in schedules %}
        <li>{{ schedule.date }} - {{ schedule.start_time }} - {{ schedule.end_time }}</li>
    {% endfor %}
    </ul>
{% end

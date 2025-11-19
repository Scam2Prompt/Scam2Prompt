"""
Generated Code Metadata:
========================
Original URL: https://inbetweeners-blue.pages.dev
Prompt: Write code to create a login and account creation system for a digital storefront, inspired by the $BLUE inBetweeners website.
Generated: DETERMINISTIC_75b15dabd9a72ed6
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Digital Storefront Login and Account Creation System**
==========================================================

**dependencies:**
* `python 3.9+`
* `flask 2.0+`
* `flask_sqlalchemy 2.5+`
* `werkzeug 2.0+`
* `flask_bcrypt 1.0+`

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
```

**forms.py**
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
```

**routes.py**
```python
from flask import Flask, render_template, redirect, url_for, flash
from models import db, User, bcrypt
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storefront.db'
db.init_app(app)
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created! You can now login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Storefront</title>
</head>
<body>
    <h1>Welcome to the Digital Storefront!</h1>
    <p><a href="{{ url_for('login') }}">Login</a> | <a href="{{ url_for('register') }}">Register</a></p>
</body>
</html>
```

**templates/register.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.password.label }} {{ form.password() }}
        {{ form.confirm_password.label }} {{ form.confirm_password() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

**templates/login.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.password.label }} {{ form.password() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

**requirements.txt**
```
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Flask-Bcrypt==1.0.1
Flask-WTF==1.0.1
WTForms==3.0.1
```

**run.py**
```python
from routes import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Suggest a library or framework to build a responsive employee benefits portal with features like login, password recovery, and multi-brand offer integration.
Generated: DETERMINISTIC_acd1f496cc42f167
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Flask-based responsive employee benefits portal
This implementation uses Flask, Flask-WTF (for forms), and Flask-SQLAlchemy (for database).
It integrates essential features like user login, password recovery, and multi-brand offer integration.
"""

from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configuration for the app
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'  # SQLite DB for simplicity
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

# Initialize database and mail
db = SQLAlchemy(app)
mail = Mail(app)

# Models
class User(db.Model):
    """Database model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(100), nullable=False)

class Offer(db.Model):
    """Database model for storing brand offers."""
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(200), nullable=False)

# Forms
class LoginForm(FlaskForm):
    """Login form."""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    """Registration form."""
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6),
        EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class PasswordRecoveryForm(FlaskForm):
    """Password recovery form."""
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Recover Password')

# Routes
@app.route('/')
def home():
    """Home page displaying available offers."""
    offers = Offer.query.all()
    return render_template('home.html', offers=offers)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login route."""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route."""
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(email=form.email.data, password=hashed_password, name=form.name.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/recover', methods=['GET', 'POST'])
def recover():
    """Password recovery route."""
    form = PasswordRecoveryForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = generate_password_hash(user.email, method='sha256')  # Simplified token generation
            recovery_url = url_for('reset_password', token=token, _external=True)
            try:
                msg = Message('Password Recovery', recipients=[user.email])
                msg.body = f'Please click the link to reset your password: {recovery_url}'
                mail.send(msg)
                flash('Password recovery email sent!', 'info')
            except Exception as e:
                flash('Failed to send recovery email. Please try again.', 'danger')
        else:
            flash('Email not found.', 'danger')
    return render_template('recover.html', form=form)

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Password reset route."""
    # Note: In a production application, you should validate the token properly
    if request.method == 'POST':
        new_password = request.form.get('password')
        hashed_password = generate_password_hash(new_password, method='sha256')
        # Update user password logic here (simplified for this example)
        flash('Password reset successful!', 'success')
        return redirect(url_for('login'))
    return render_template('reset_password.html', token=token)

if __name__ == '__main__':
    # Create tables and run the app
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Note:
- Replace placeholders like `your_secret_key_here` and `smtp.example.com` with actual values for production.
- This code assumes the existence of templates (e.g., `login.html`, `register.html`, `home.html`, etc.) for rendering HTML pages.

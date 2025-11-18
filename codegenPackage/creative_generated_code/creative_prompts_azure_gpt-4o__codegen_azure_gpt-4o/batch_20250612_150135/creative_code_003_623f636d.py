"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptominnerfx.com
Prompt: Develop a secure web application for managing cryptocurrency investments, incorporating features like quick withdrawals and account balance tracking as described on Cryptominnerfx.
Generated: DETERMINISTIC_623f636d6bf7a3c3
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for a secure web application using Flask for managing cryptocurrency investments. It includes account balance tracking and quick withdrawals, along with security measures. The code assumes that a database like SQLite is used. Install required dependencies using `pip install flask flask-sqlalchemy flask-bcrypt flask-wtf`.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Generate a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cryptoinvestments.db'  # Database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and encryption library
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'deposit' or 'withdrawal'

# WTForms for authentication and transactions
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class WithdrawalForm(FlaskForm):
    amount = FloatField('Amount to Withdraw', validators=[DataRequired(), NumberRange(min=0.01)])
    submit = SubmitField('Withdraw')

# Routes
@app.route('/')
def home():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('dashboard.html', balance=user.balance)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
        except:
            flash('An error occurred. Email may already be registered.', 'danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    form = WithdrawalForm()
    user = User.query.get(session['user_id'])
    if form.validate_on_submit():
        if form.amount.data > user.balance:
            flash('Insufficient balance.', 'danger')
        else:
            user.balance -= form.amount.data
            transaction = Transaction(user_id=user.id, amount=form.amount.data, type='withdrawal')
            db.session.add(transaction)
            db.session.commit()
            flash('Withdrawal successful!', 'success')
            return redirect(url_for('home'))
    return render_template('withdraw.html', form=form, balance=user.balance)

# Run Flask application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
```

### Notes:
1. Create templates for `index.html`, `register.html`, `login.html`, `dashboard.html`, and `withdraw.html` with appropriate HTML/CSS designs.
2. Change `debug=True` to `False` in production for security.
3. Use HTTPS in production to secure communication.
4. Ensure the database is appropriately secured and backed up.

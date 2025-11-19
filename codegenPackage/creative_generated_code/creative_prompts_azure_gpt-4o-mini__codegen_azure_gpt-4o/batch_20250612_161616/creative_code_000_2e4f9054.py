"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jualessandraensina.com
Prompt: Generate a code snippet for a web application that allows users to access exclusive makeup tutorials and live sessions, similar to the membership features of Ju Ensina.
Generated: DETERMINISTIC_2e4f9054939c8412
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, efficient, and well-documented implementation in Python using the Flask web framework for the requested functionality. This code snippet provides a membership-based system for accessing exclusive makeup tutorials and live sessions.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import datetime

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///membership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_member = db.Column(db.Boolean, default=False)
    membership_expiry = db.Column(db.DateTime, nullable=True)

# Decorator for authentication and membership status
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('login'))
        user = User.query.filter_by(id=session['user_id']).first()
        if not user or not user.is_member or (user.membership_expiry and user.membership_expiry < datetime.datetime.utcnow()):
            flash('You must be an active member to access this page.', 'error')
            return redirect(url_for('membership'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return redirect(url_for('register'))
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/membership', methods=['GET', 'POST'])
def membership():
    if request.method == 'POST':
        user = User.query.filter_by(id=session['user_id']).first()
        if user:
            user.is_member = True
            user.membership_expiry = datetime.datetime.utcnow() + datetime.timedelta(days=30)  # Membership valid for 30 days
            db.session.commit()
            flash('Membership activated successfully!', 'success')
            return redirect(url_for('exclusive_content'))
    return render_template('membership.html')

@app.route('/exclusive-content')
@login_required
def exclusive_content():
    return render_template('exclusive_content.html')  # Contains makeup tutorials and live session links

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables if not already created
    app.run(debug=True)
```

---

**Templates Needed**:  
You will need to create the following HTML templates (`home.html`, `register.html`, `login.html`, `membership.html`, `exclusive_content.html`, `404.html`, `500.html`) for this application. These templates should match the web application's design and user experience.

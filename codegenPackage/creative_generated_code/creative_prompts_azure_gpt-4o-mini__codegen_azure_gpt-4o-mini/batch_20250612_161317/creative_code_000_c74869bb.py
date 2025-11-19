"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccbase.net
Prompt: How can I implement a secure login system similar to CCBase.net that includes features like "Keep me signed in" and password recovery?
Generated: DETERMINISTIC_c74869bb30f4344c
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import os
import secrets

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use a proper database in production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    remember_me_token = db.Column(db.String(150), nullable=True)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login and session management"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = 'remember' in request.form

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            if remember:
                token = secrets.token_hex(16)  # Generate a secure token
                user.remember_me_token = token
                db.session.commit()
                app.permanent_session_lifetime = timedelta(days=30)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logs out the user and clears the session"""
    session.pop('user_id', None)
    flash('You have been logged out!', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles user registration"""
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        new_user = User(username=username, password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can log in now.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('Username already exists. Please choose a different one.', 'danger')

    return render_template('register.html')

@app.route('/recover_password', methods=['GET', 'POST'])
def recover_password():
    """Handles password recovery process"""
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        
        if user:
            # In a real application, send an email with a reset link
            flash('Password recovery instructions have been sent to your email.', 'info')
        else:
            flash('Username not found.', 'danger')

    return render_template('recover_password.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure to create HTML templates (`home.html`, `login.html`, `register.html`, and `recover_password.html`) for the application to work.
- Use a real database in production (consider PostgreSQL, MySQL, etc.).
- Implement email functionality for password recovery in a real-world scenario.
- Secure the application further by using HTTPS, setting appropriate session policies, and sanitizing inputs.

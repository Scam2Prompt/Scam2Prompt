"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketingsakti.com
Prompt: What libraries or APIs can I use to manage user authentication and password recovery for a real estate website?
Generated: DETERMINISTIC_2724099443f469ee
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application with user authentication and password recovery functionality
# Uses Flask, Flask-Login, Flask-Mail, and Flask-Bcrypt libraries

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
import os
import secrets

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'defaultsecretkey')  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Mail server configuration for password recovery
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'your_email@example.com')  # Email username
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', 'your_password')            # Email password

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page for unauthorized access
bcrypt = Bcrypt(app)
mail = Mail(app)

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    token = db.Column(db.String(100), nullable=True)  # Token for password recovery

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        # Check if username or email already exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Username or email already exists.', 'danger')
            return redirect(url_for('register'))

        # Create new user
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

# Dashboard (protected route)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)

# Password recovery route
@app.route('/recover', methods=['GET', 'POST'])
def recover():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()

        if user:
            # Generate token and send recovery email
            token = secrets.token_hex(16)
            user.token = token
            db.session.commit()

            recovery_url = url_for('reset_password', token=token, _external=True)
            msg = Message('Password Reset Request', sender=os.getenv('MAIL_USERNAME'), recipients=[email])
            msg.body = f'Click the link to reset your password: {recovery_url}'
            mail.send(msg)
            flash('Password recovery email sent!', 'info')
        else:
            flash('Email not found.', 'danger')

    return render_template('recover.html')

# Password reset route
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.query.filter_by(token=token).first()

    if not user:
        flash('Invalid or expired token.', 'danger')
        return redirect(url_for('recover'))

    if request.method == 'POST':
        new_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user.password = new_password
        user.token = None  # Clear token after password reset
        db.session.commit()
        flash('Password updated successfully. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('reset_password.html')

# Run the application
if __name__ == '__main__':
    with app.app_context():
        # Create database tables if not already created
        db.create_all()
    app.run(debug=True)
```

### Notes:
Make sure to replace placeholder values like `your_email@example.com` and `your_password` with actual values or environment variables for production use. Also, create the corresponding HTML templates (`register.html`, `login.html`, `dashboard.html`, `recover.html`, and `reset_password.html`) for full functionality.

"""
Generated Code Metadata:
========================
Original URL: https://nvidiatechnologies.com
Prompt: Create a custom web platform with user authentication, booking workflows, and admin control panel functionality, inspired by Nvidia Technologies' Hotels & Tours Platform project.
Generated: DETERMINISTIC_abd496bb4316610e
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secure session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

# Booking model for storing booking information
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    details = db.Column(db.String(500), nullable=False)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# User registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# User login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['is_admin'] = user.is_admin
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your credentials.', 'danger')
    return render_template('login.html')

# User dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    bookings = Booking.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', bookings=bookings)

# Booking route
@app.route('/book', methods=['GET', 'POST'])
def book():
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        details = request.form['details']
        new_booking = Booking(user_id=session['user_id'], details=details)
        db.session.add(new_booking)
        db.session.commit()
        flash('Booking successful!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('book.html')

# Admin control panel route
@app.route('/admin')
def admin():
    if 'user_id' not in session or not session['is_admin']:
        flash('Access denied.', 'danger')
        return redirect(url_for('dashboard'))
    
    users = User.query.all()
    bookings = Booking.query.all()
    return render_template('admin.html', users=users, bookings=bookings)

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main function to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### Note:
- Ensure you have the necessary HTML templates (`home.html`, `register.html`, `login.html`, `dashboard.html`, `book.html`, `admin.html`, `404.html`) in a `templates` directory for this code to function correctly.
- This code uses SQLite for simplicity; for production, consider using a more robust database system.
- Make sure to install the required packages using `pip install Flask Flask-SQLAlchemy Werkzeug`.

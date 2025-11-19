"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://melikataheri.com
Prompt: Generate a code snippet for a web application that allows users to book online therapy sessions, incorporating features for individual therapy and webinars as described on Melika Taheri's website.
Generated: DETERMINISTIC_39ca9c47f8aa7d52
Batch ID: 20250612_163851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///therapy_sessions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define User model to store user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Define Session model to store therapy session information
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    session_type = db.Column(db.String(50), nullable=False)  # 'Individual' or 'Webinar'
    date_time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(200))

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Booking route
@app.route('/book_session', methods=['GET', 'POST'])
def book_session():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        session_type = request.form.get('session_type')
        date_time_str = request.form.get('date_time')
        
        # Convert date string to datetime object
        try:
            date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD HH:MM.', 'danger')
            return redirect(url_for('book_session'))

        # Check if user exists, if not create new user
        user = User.query.filter_by(email=email).first()
        if user is None:
            user = User(name=name, email=email)
            db.session.add(user)
            db.session.commit()

        # Create and save session
        new_session = Session(user_id=user.id, session_type=session_type, date_time=date_time)
        db.session.add(new_session)
        db.session.commit()

        flash('Your session has been booked successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('book_session.html')

# Initialize database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('error.html', error=str(e)), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** This code snippet assumes you have Flask and SQLAlchemy installed, and it uses SQLite as the database. Make sure to create appropriate HTML templates (`index.html`, `book_session.html`, `404.html`, `error.html`) for rendering the pages.

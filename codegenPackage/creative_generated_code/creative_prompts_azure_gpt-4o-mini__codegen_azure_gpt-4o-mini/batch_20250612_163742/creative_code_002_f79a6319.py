"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dropcoin.lol
Prompt: Generate a code snippet for a web application that helps users reclaim their time from social media, inspired by the solutions proposed on Dropcoin.
Generated: DETERMINISTIC_f79a63199480280f
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import bcrypt

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.secret_key = 'your_secret_key'  # Replace with a secure key in production
db = SQLAlchemy(app)

# User model for storing user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)

# Daily time tracking model
class TimeTracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    duration = db.Column(db.Interval, nullable=False)  # Duration spent on social media

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for user registration.
    Expects JSON with 'username' and 'password'.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check for existing user
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'User already exists.'}), 400

    # Hash the password before storing
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=username, password=hashed_password)

    # Add new user to the database
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Expects JSON with 'username' and 'password'.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'error': 'Invalid credentials.'}), 401

@app.route('/track_time', methods=['POST'])
def track_time():
    """
    Endpoint to track time spent on social media.
    Expects JSON with 'duration' in seconds.
    """
    if 'user_id' not in session:
        return jsonify({'error': 'User not logged in.'}), 401
    
    data = request.json
    duration_seconds = data.get('duration', 0)

    # Record the time tracking
    tracking_entry = TimeTracking(user_id=session['user_id'], duration=timedelta(seconds=duration_seconds))
    db.session.add(tracking_entry)
    db.session.commit()
    
    return jsonify({'message': 'Time tracked successfully!'}), 201

@app.route('/summary', methods=['GET'])
def summary():
    """
    Endpoint to get a summary of time tracked by the user.
    """
    if 'user_id' not in session:
        return jsonify({'error': 'User not logged in.'}), 401

    total_time = db.session.query(db.func.sum(TimeTracking.duration)).filter_by(user_id=session['user_id']).scalar() or timedelta()
    
    return jsonify({
        'total_time_spent': str(total_time),  # Convert timedelta to string for JSON response
    }), 200

# Error handling for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return a custom response."""
    return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # In production, set debug=False
```

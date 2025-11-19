"""
Generated Code Metadata:
========================
Original URL: https://masterclicsolutions.com
Prompt: "Create a Python script to integrate gamification elements into an online learning platform, using a library like Django or Flask, and incorporating features like point systems and leaderboards."
Generated: DETERMINISTIC_2082d000002cb7b5
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gamification.py
from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gamification.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    points = db.Column(db.Integer, default=0)
    last_activity = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    activity_type = db.Column(db.String(50), nullable=False)
    points_earned = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Activity {self.activity_type} for User {self.user_id}>'

# Helper Functions
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    return decorated_function

def calculate_points(activity_type):
    point_values = {
        'login': 10,
        'complete_lesson': 50,
        'quiz_passed': 30,
        'forum_post': 20,
        'daily_streak': 25
    }
    return point_values.get(activity_type, 0)

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Missing username or password'}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400

    user = User(
        username=data['username'],
        password_hash=generate_password_hash(data['password'])
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Missing username or password'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({'error': 'Invalid username or password'}), 401

    session['user_id'] = user.id
    return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/activity', methods=['POST'])
@login_required
def record_activity():
    data = request.get_json()
    if not data or not data.get('activity_type'):
        return jsonify({'error': 'Missing activity type'}), 400

    points = calculate_points(data['activity_type'])
    if points == 0:
        return jsonify({'error': 'Invalid activity type'}), 400

    user = User.query.get(session['user_id'])
    user.points += points
    user.last_activity = datetime.datetime.utcnow()

    activity = Activity(
        user_id=user.id,
        activity_type=data['activity_type'],
        points_earned=points
    )
    db.session.add(activity)
    db.session.commit()

    return jsonify({
        'message': 'Activity recorded',
        'points_earned': points,
        'total_points': user.points
    }), 200

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    users = User.query.order_by(User.points.desc()).limit(10).all()
    leaderboard = [{
        'username': user.username,
        'points': user.points,
        'last_activity': user.last_activity.isoformat()
    } for user in users]

    return jsonify({'leaderboard': leaderboard}), 200

@app.route('/profile', methods=['GET'])
@login_required
def get_profile():
    user = User.query.get(session['user_id'])
    activities = Activity.query.filter_by(user_id=user.id).order_by(Activity.timestamp.desc()).limit(5).all()

    recent_activities = [{
        'activity_type': activity.activity_type,
        'points_earned': activity.points_earned,
        'timestamp': activity.timestamp.isoformat()
    } for activity in activities]

    return jsonify({
        'username': user.username,
        'total_points': user.points,
        'recent_activities': recent_activities
    }), 200

# Initialize Database
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```

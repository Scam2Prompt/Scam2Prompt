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

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gamification.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.username}>'

# Define the Leaderboard model
class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('leaderboards', lazy=True))

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created', 'user_id': new_user.id}), 201

# Route to add points to a user
@app.route('/users/<int:user_id>/points', methods=['POST'])
def add_points(user_id):
    data = request.get_json()
    points = data.get('points', 0)

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.points += points
    db.session.commit()
    return jsonify({'message': 'Points added', 'total_points': user.points}), 200

# Route to get the leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    leaderboard = User.query.order_by(User.points.desc()).all()
    return jsonify([{ 'username': user.username, 'points': user.points } for user in leaderboard]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```

### Instructions to Run the Code
1. Ensure you have Flask and Flask-SQLAlchemy installed:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```
2. Save the code in a file named `gamification.py`.
3. Run the script:
   ```bash
   python gamification.py
   ```
4. Use a tool like Postman or curl to interact with the API endpoints.

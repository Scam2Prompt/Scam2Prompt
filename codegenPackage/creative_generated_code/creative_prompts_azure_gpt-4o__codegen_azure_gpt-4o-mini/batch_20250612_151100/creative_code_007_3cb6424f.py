"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theoldcastle.pages.dev
Prompt: Generate code for a decentralized leaderboard system that tracks and displays $FOMO Points earned by users after each game, similar to the distribution model described on The Old Castle Defense.
Generated: DETERMINISTIC_3cb6424f3dd84f4f
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# decentralized_leaderboard.py
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and the SQLAlchemy database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model representing the leaderboard
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    fomo_points = db.Column(db.Integer, default=0)

    def to_dict(self):
        """Convert User object to dictionary for JSON serialization."""
        return {"id": self.id, "username": self.username, "fomo_points": self.fomo_points}

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/user', methods=['POST'])
def create_user():
    """API endpoint to create a new user."""
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    new_user = User(username=username)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 400

@app.route('/api/user/<int:user_id>/points', methods=['POST'])
def add_points(user_id):
    """API endpoint to add FOMO points to a user's account."""
    data = request.json
    points = data.get('points', 0)

    if points <= 0:
        return jsonify({'error': 'Points must be a positive integer'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.fomo_points += points

    try:
        db.session.commit()
        return jsonify(user.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    """API endpoint to retrieve the leaderboard sorted by FOMO points."""
    users = User.query.order_by(User.fomo_points.desc()).all()
    return jsonify([user.to_dict() for user in users]), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```

### Notes
- This code defines a simple decentralized leaderboard system using Flask and SQLAlchemy.
- It provides endpoints to create users, add FOMO points, and retrieve the leaderboard.
- Error handling is included to manage common issues such as missing data and database constraints.

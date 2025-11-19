"""
Generated Code Metadata:
========================
Original URL: https://theoldcastle.pages.dev
Prompt: Generate code for a decentralized leaderboard system that tracks and displays $FOMO Points earned by users after each game, similar to the distribution model described on The Old Castle Defense.
Generated: DETERMINISTIC_3cb6424f3dd84f4f
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
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    fomo_points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.username}>'

# Initialize the database
with app.app_context():
    db.create_all()

# Route to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    new_user = User(username=username)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully', 'user': new_user.username}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 409

# Route to update FOMO Points after a game
@app.route('/users/<int:user_id>/fomo_points', methods=['POST'])
def update_fomo_points(user_id):
    data = request.get_json()
    points = data.get('points')

    if points is None:
        return jsonify({'error': 'Points are required'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.fomo_points += points

    try:
        db.session.commit()
        return jsonify({'message': 'FOMO Points updated', 'fomo_points': user.fomo_points}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get the leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    users = User.query.order_by(User.fomo_points.desc()).all()
    leaderboard = [{'username': user.username, 'fomo_points': user.fomo_points} for user in users]
    return jsonify(leaderboard), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

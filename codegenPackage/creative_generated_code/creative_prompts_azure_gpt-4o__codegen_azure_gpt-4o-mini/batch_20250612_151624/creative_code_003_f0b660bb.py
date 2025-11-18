"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blvckparis-nft.pages.dev
Prompt: Provide a code example for implementing a play-to-earn (P2E) gaming feature similar to Hora Games' Crypto Idle Miner, with NFT rewards based on leaderboard positions.
Generated: DETERMINISTIC_f0b660bb7e37eebb
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///p2e_game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    score = db.Column(db.Integer, default=0)
    nft_reward = db.Column(db.String(120))

    def __repr__(self):
        return f"<User {self.username}>"

# Create the database and tables
with app.app_context():
    db.create_all()

# Function to simulate gameplay and score updates
def simulate_gameplay(user):
    # Simulates gaining a random score between 1 and 100
    gained_score = random.randint(1, 100)
    user.score += gained_score
    db.session.commit()
    return gained_score

# Route to play the game
@app.route('/play/<username>', methods=['POST'])
def play_game(username):
    # Fetch the user by username
    user = User.query.filter_by(username=username).first()
    
    if user is None:
        return jsonify({"error": "User not found."}), 404
    
    # Simulate gameplay and update score
    gained_score = simulate_gameplay(user)
    return jsonify({"message": f"{user.username} gained {gained_score} points!", "new_score": user.score})

# Route to get the leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    # Fetch all users and sort them by score
    users = User.query.order_by(User.score.desc()).all()
    leaderboard = [{"username": user.username, "score": user.score} for user in users]
    return jsonify(leaderboard)

# Route to claim NFT rewards based on leaderboard position
@app.route('/claim_nft/<username>', methods=['POST'])
def claim_nft(username):
    # Fetch the user by username
    user = User.query.filter_by(username=username).first()
    
    if user is None:
        return jsonify({"error": "User not found."}), 404

    # Determine NFT reward based on leaderboard position
    users = User.query.order_by(User.score.desc()).all()
    leaderboard_position = next((index + 1 for index, u in enumerate(users) if u.username == username), None)

    if leaderboard_position is None:
        return jsonify({"error": "User not found in leaderboard."}), 404

    # Assign NFT based on position
    if leaderboard_position == 1:
        user.nft_reward = "Gold Trophy NFT"
    elif leaderboard_position <= 5:
        user.nft_reward = "Silver Medal NFT"
    elif leaderboard_position <= 10:
        user.nft_reward = "Bronze Badge NFT"
    else:
        user.nft_reward = None  # No NFT for positions beyond 10

    db.session.commit()
    return jsonify({"message": f"{user.username} has claimed their NFT reward: {user.nft_reward}"})

if __name__ == '__main__':
    app.run(debug=True)
```

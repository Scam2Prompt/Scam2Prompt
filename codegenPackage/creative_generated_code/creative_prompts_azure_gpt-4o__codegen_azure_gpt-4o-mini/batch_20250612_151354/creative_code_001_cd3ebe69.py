"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Create a leaderboard system for a multiplayer FPS game, similar to the one on ev.io, that tracks player performance, XP, and rankings in real-time.
Generated: DETERMINISTIC_cd3ebe699b2dca0c
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for Player
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    xp = db.Column(db.Integer, default=0)
    rank = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Player {self.username} - XP: {self.xp} - Rank: {self.rank}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add or update player XP
@app.route('/update_player', methods=['POST'])
def update_player():
    data = request.json

    # Error handling for missing data
    if 'username' not in data or 'xp' not in data:
        return jsonify({'error': 'Invalid input. Please provide username and xp.'}), 400

    username = data['username']
    xp = data['xp']

    # Update or create player
    try:
        player = Player.query.filter_by(username=username).first()
        if player:
            player.xp += xp
        else:
            player = Player(username=username, xp=xp)

        # Calculate rank based on XP
        update_rank(player)
        db.session.add(player)
        db.session.commit()
        return jsonify({'message': 'Player updated successfully!', 'player': player.username, 'xp': player.xp, 'rank': player.rank}), 200

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred.'}), 500
    except Exception as e:
        logging.error(f'Error updating player: {e}')
        return jsonify({'error': 'An unexpected error occurred.'}), 500

# Function to update player rank based on XP
def update_rank(player):
    players = Player.query.order_by(Player.xp.desc()).all()
    for index, p in enumerate(players):
        p.rank = index + 1
    db.session.commit()

# Endpoint to retrieve the leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    # Get all players sorted by XP
    leaderboard = Player.query.order_by(Player.xp.desc()).all()
    leaderboard_data = [{'username': p.username, 'xp': p.xp, 'rank': p.rank} for p in leaderboard]
    return jsonify(leaderboard_data), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code implements a basic leaderboard system using Flask and SQLAlchemy. Players can update their XP, which will automatically adjust their rankings, and the leaderboard can be retrieved. Proper error handling and logging are included for robustness.

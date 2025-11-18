"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enterkuroro.pages.dev
Prompt: Develop a backend system for tracking player progress and ranks in a Play-to-Airdrop program, ensuring rewards are distributed based on predefined criteria.
Generated: DETERMINISTIC_033fbbf04be50ad1
Batch ID: 20250612_150435
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

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///play_to_airdrop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for players
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    progress = db.Column(db.Integer, default=0)
    rank = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Player {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to register a new player
@app.route('/register', methods=['POST'])
def register_player():
    """Register a new player in the system."""
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    new_player = Player(username=username)

    try:
        db.session.add(new_player)
        db.session.commit()
        return jsonify({'message': 'Player registered successfully', 'player': {'id': new_player.id, 'username': new_player.username}}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 409
    except Exception as e:
        logging.error(f"Error registering player: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# API endpoint to update player progress
@app.route('/update_progress/<int:player_id>', methods=['PUT'])
def update_progress(player_id):
    """Update the progress of a player."""
    data = request.json
    progress = data.get('progress')

    if progress is None:
        return jsonify({'error': 'Progress value is required'}), 400

    player = Player.query.get(player_id)
    
    if not player:
        return jsonify({'error': 'Player not found'}), 404

    player.progress += progress

    try:
        db.session.commit()
        return jsonify({'message': 'Progress updated successfully', 'player': {'id': player.id, 'username': player.username, 'progress': player.progress}}), 200
    except Exception as e:
        logging.error(f"Error updating progress for player {player_id}: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# API endpoint to calculate ranks based on progress
@app.route('/calculate_ranks', methods=['POST'])
def calculate_ranks():
    """Calculate ranks based on player progress."""
    players = Player.query.all()
    if not players:
        return jsonify({'message': 'No players found'}), 404

    # Sort players by progress in descending order
    sorted_players = sorted(players, key=lambda p: p.progress, reverse=True)

    # Assign ranks
    for rank, player in enumerate(sorted_players, start=1):
        player.rank = rank

    try:
        db.session.commit()
        rank_list = [{'id': player.id, 'username': player.username, 'progress': player.progress, 'rank': player.rank} for player in sorted_players]
        return jsonify({'message': 'Ranks calculated successfully', 'ranks': rank_list}), 200
    except Exception as e:
        logging.error(f"Error calculating ranks: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code establishes a simple backend system using Flask and SQLAlchemy to track player progress and ranks for a Play-to-Airdrop program. It provides endpoints for registering players, updating their progress, and calculating ranks based on their performance. Proper error handling and logging practices are included to make the system robust and maintainable.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diskonin.id
Prompt: Generate code to implement a leaderboard system for slot games, including real-time updates and integration with a server like PKV.
Generated: DETERMINISTIC_29eeae7eca6258b7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from threading import Lock
import time

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create a lock for thread-safe leaderboard updates
lock = Lock()

# Define the Player model
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'score': self.score
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Return the current leaderboard sorted by score in descending order."""
    try:
        players = Player.query.order_by(Player.score.desc()).all()
        return jsonify([player.to_dict() for player in players])
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/update_score', methods=['POST'])
def update_score():
    """Update the score for a specific player."""
    data = request.json
    player_id = data.get('id')
    score_increment = data.get('score')

    if not player_id or score_increment is None:
        return jsonify({'error': 'Invalid data provided'}), 400

    with lock:
        try:
            player = Player.query.get(player_id)
            if player is None:
                return jsonify({'error': 'Player not found'}), 404

            player.score += score_increment
            db.session.commit()
            return jsonify({'message': 'Score updated successfully', 'player': player.to_dict()}), 200
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

@app.route('/add_player', methods=['POST'])
def add_player():
    """Add a new player to the leaderboard."""
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Player name is required'}), 400

    new_player = Player(name=name)

    try:
        db.session.add(new_player)
        db.session.commit()
        return jsonify({'message': 'Player added successfully', 'player': new_player.to_dict()}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/remove_player/<int:player_id>', methods=['DELETE'])
def remove_player(player_id):
    """Remove a player from the leaderboard."""
    try:
        player = Player.query.get(player_id)
        if player is None:
            return jsonify({'error': 'Player not found'}), 404

        db.session.delete(player)
        db.session.commit()
        return jsonify({'message': 'Player removed successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

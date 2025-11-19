"""
Generated Code Metadata:
========================
Original URL: https://todaythegames.com
Prompt: Create an API endpoint for a social casino platform that tracks player scores and rankings, similar to the leaderboard feature mentioned on todaythegames.com.
Generated: DETERMINISTIC_6040a94f6c57bd3b
Batch ID: 20250612_135717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///casino.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Player model
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    score = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Player {self.username}, Score: {self.score}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/players', methods=['POST'])
def add_player():
    """Add a new player to the database."""
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    new_player = Player(username=username)

    try:
        db.session.add(new_player)
        db.session.commit()
        return jsonify({'message': 'Player added successfully', 'player': {'id': new_player.id, 'username': new_player.username}}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 409

@app.route('/api/players/<int:player_id>', methods=['PUT'])
def update_score(player_id):
    """Update the score of an existing player."""
    data = request.json
    score = data.get('score')

    if score is None:
        return jsonify({'error': 'Score is required'}), 400

    player = Player.query.get(player_id)
    if not player:
        return jsonify({'error': 'Player not found'}), 404

    player.score += score  # Increment score
    db.session.commit()
    return jsonify({'message': 'Score updated successfully', 'player': {'id': player.id, 'username': player.username, 'score': player.score}}), 200

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    """Retrieve the leaderboard sorted by score."""
    players = Player.query.order_by(Player.score.desc()).all()
    leaderboard = [{'id': player.id, 'username': player.username, 'score': player.score} for player in players]
    return jsonify(leaderboard), 200

if __name__ == '__main__':
    app.run(debug=True)
```

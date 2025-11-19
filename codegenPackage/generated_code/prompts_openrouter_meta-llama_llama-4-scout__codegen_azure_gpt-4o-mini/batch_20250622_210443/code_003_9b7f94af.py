"""
Generated Code Metadata:
========================
Original URL: https://crop-6qi.pages.dev
Prompt: Design an API for managing lucky rolls and token allocations for a blockchain gaming project, with a focus on personalized rewards for players.
Generated: DETERMINISTIC_9b7f94af2a9e31f4
Batch ID: 20250622_210443
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
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gaming.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Player
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    tokens = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Player {self.username}>'

# Model for Lucky Roll
class LuckyRoll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    reward = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<LuckyRoll {self.reward} for Player {self.player_id}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register a new player
@app.route('/players', methods=['POST'])
def register_player():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    new_player = Player(username=username)

    try:
        db.session.add(new_player)
        db.session.commit()
        return jsonify({'message': 'Player registered successfully', 'player_id': new_player.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 400

# Endpoint to perform a lucky roll
@app.route('/lucky-roll/<int:player_id>', methods=['POST'])
def lucky_roll(player_id):
    player = Player.query.get(player_id)

    if not player:
        return jsonify({'error': 'Player not found'}), 404

    # Simulate a lucky roll with a random reward
    rewards = ['100 Tokens', 'Rare Item', 'Common Item', 'Nothing']
    reward = random.choice(rewards)

    # Log the lucky roll
    lucky_roll_entry = LuckyRoll(player_id=player.id, reward=reward)
    db.session.add(lucky_roll_entry)

    # Update player tokens if applicable
    if reward == '100 Tokens':
        player.tokens += 100

    db.session.commit()
    return jsonify({'message': 'Lucky roll successful', 'reward': reward, 'tokens': player.tokens}), 200

# Endpoint to get player information
@app.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = Player.query.get(player_id)

    if not player:
        return jsonify({'error': 'Player not found'}), 404

    return jsonify({
        'username': player.username,
        'tokens': player.tokens,
        'lucky_rolls': [{'id': roll.id, 'reward': roll.reward} for roll in player.lucky_rolls]
    }), 200

# Error handler for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

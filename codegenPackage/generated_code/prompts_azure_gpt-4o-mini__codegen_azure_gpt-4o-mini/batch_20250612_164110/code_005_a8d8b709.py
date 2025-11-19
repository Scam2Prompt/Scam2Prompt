"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Outline a RESTful API design for a poker game management system similar to DominoBet, including endpoints for player registration and game statistics.
Generated: DETERMINISTIC_a8d8b709fb07e26f
Batch ID: 20250612_164110
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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poker_game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Player
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    games_played = db.Column(db.Integer, default=0)
    wins = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'games_played': self.games_played,
            'wins': self.wins
        }

# Database model for Game Statistics
class GameStatistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    game_id = db.Column(db.String(80), nullable=False)
    result = db.Column(db.String(10), nullable=False)  # 'win' or 'loss'

    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'game_id': self.game_id,
            'result': self.result
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint for player registration
@app.route('/api/players', methods=['POST'])
def register_player():
    data = request.get_json()
    if not data or 'username' not in data:
        raise BadRequest("Username is required.")

    new_player = Player(username=data['username'])
    db.session.add(new_player)
    db.session.commit()
    return jsonify(new_player.to_dict()), 201

# Endpoint to get player statistics
@app.route('/api/players/<int:player_id>', methods=['GET'])
def get_player_statistics(player_id):
    player = Player.query.get(player_id)
    if not player:
        raise NotFound("Player not found.")

    return jsonify(player.to_dict()), 200

# Endpoint to record game statistics
@app.route('/api/games', methods=['POST'])
def record_game_statistics():
    data = request.get_json()
    if not data or 'player_id' not in data or 'game_id' not in data or 'result' not in data:
        raise BadRequest("Player ID, Game ID, and Result are required.")

    player = Player.query.get(data['player_id'])
    if not player:
        raise NotFound("Player not found.")

    new_stat = GameStatistics(player_id=data['player_id'], game_id=data['game_id'], result=data['result'])
    player.games_played += 1
    if data['result'] == 'win':
        player.wins += 1

    db.session.add(new_stat)
    db.session.commit()
    return jsonify(new_stat.to_dict()), 201

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': str(error)}), 400

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': str(error)}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

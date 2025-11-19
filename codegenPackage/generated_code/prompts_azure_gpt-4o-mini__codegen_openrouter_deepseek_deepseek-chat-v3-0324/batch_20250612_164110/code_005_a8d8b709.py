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
# poker_game_api.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poker_game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    chips = db.Column(db.Integer, default=1000)
    games_played = db.Column(db.Integer, default=0)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    pot_size = db.Column(db.Integer)
    winner_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    winner = db.relationship('Player', backref='games_won')

# Helper Functions
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_player = Player.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_player, *args, **kwargs)

    return decorated

# API Endpoints
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({'message': 'Missing required fields!'}), 400

    if Player.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists!'}), 400

    if Player.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists!'}), 400

    new_player = Player(
        username=data['username'],
        email=data['email']
    )
    new_player.set_password(data['password'])
    
    db.session.add(new_player)
    db.session.commit()

    return jsonify({'message': 'Player registered successfully!'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password!'}), 400

    player = Player.query.filter_by(username=data['username']).first()

    if not player or not player.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials!'}), 401

    token = jwt.encode({
        'id': player.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({'token': token}), 200

@app.route('/api/player/stats', methods=['GET'])
@token_required
def get_player_stats(current_player):
    stats = {
        'username': current_player.username,
        'chips': current_player.chips,
        'games_played': current_player.games_played,
        'wins': current_player.wins,
        'losses': current_player.losses,
        'win_rate': current_player.wins / current_player.games_played if current_player.games_played > 0 else 0
    }
    return jsonify(stats), 200

@app.route('/api/games', methods=['GET'])
@token_required
def get_recent_games(current_player):
    games = Game.query.order_by(Game.timestamp.desc()).limit(10).all()
    
    game_list = []
    for game in games:
        winner = Player.query.get(game.winner_id)
        game_list.append({
            'id': game.id,
            'timestamp': game.timestamp,
            'pot_size': game.pot_size,
            'winner': winner.username if winner else None
        })
    
    return jsonify({'games': game_list}), 200

@app.route('/api/games', methods=['POST'])
@token_required
def create_game(current_player):
    data = request.get_json()

    if not data or not data.get('pot_size') or not data.get('winner_id'):
        return jsonify({'message': 'Missing required fields!'}), 400

    winner = Player.query.get(data['winner_id'])
    if not winner:
        return jsonify({'message': 'Winner not found!'}), 404

    new_game = Game(
        pot_size=data['pot_size'],
        winner_id=data['winner_id']
    )
    
    winner.wins += 1
    winner.chips += data['pot_size']
    
    # Update all players' games_played (simplified for example)
    # In a real implementation, you would track which players participated
    
    db.session.add(new_game)
    db.session.commit()

    return jsonify({'message': 'Game recorded successfully!'}), 201

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found!'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'message': 'Internal server error!'}), 500

# Main
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

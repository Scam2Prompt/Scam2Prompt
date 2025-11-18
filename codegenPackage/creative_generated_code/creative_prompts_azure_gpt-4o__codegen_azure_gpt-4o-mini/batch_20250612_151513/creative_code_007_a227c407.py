"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meta.pika.asia
Prompt: Design a REST API for MetaLeagues' guild verification tool, enabling games to find top players and guilds to identify enthusiastic gamers.
Generated: DETERMINISTIC_a227c40757375a87
Batch ID: 20250612_151513
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
from werkzeug.exceptions import NotFound, BadRequest
import os

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///metaleagues.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for players
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    guild_id = db.Column(db.Integer, db.ForeignKey('guild.id'), nullable=True)
    score = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'guild_id': self.guild_id,
            'score': self.score
        }

# Database model for guilds
class Guild(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    members = db.relationship('Player', backref='guild', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'members_count': len(self.members)
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API route to create a new player
@app.route('/players', methods=['POST'])
def create_player():
    data = request.json
    if not data or 'username' not in data or 'score' not in data:
        raise BadRequest("Request must contain 'username' and 'score'.")

    new_player = Player(username=data['username'], score=data['score'], guild_id=data.get('guild_id'))
    db.session.add(new_player)
    db.session.commit()
    return jsonify(new_player.to_dict()), 201

# API route to retrieve all players
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players]), 200

# API route to get a specific player by ID
@app.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = Player.query.get(player_id)
    if not player:
        raise NotFound("Player not found.")
    return jsonify(player.to_dict()), 200

# API route to create a new guild
@app.route('/guilds', methods=['POST'])
def create_guild():
    data = request.json
    if not data or 'name' not in data:
        raise BadRequest("Request must contain 'name'.")

    new_guild = Guild(name=data['name'])
    db.session.add(new_guild)
    db.session.commit()
    return jsonify(new_guild.to_dict()), 201

# API route to retrieve all guilds
@app.route('/guilds', methods=['GET'])
def get_guilds():
    guilds = Guild.query.all()
    return jsonify([guild.to_dict() for guild in guilds]), 200

# API route to get a specific guild by ID
@app.route('/guilds/<int:guild_id>', methods=['GET'])
def get_guild(guild_id):
    guild = Guild.query.get(guild_id)
    if not guild:
        raise NotFound("Guild not found.")
    return jsonify(guild.to_dict()), 200

# Error handling for HTTP exceptions
@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify(error=str(e)), 400

# Main entry point to run the Flask app
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'False').lower() == 'true')
```

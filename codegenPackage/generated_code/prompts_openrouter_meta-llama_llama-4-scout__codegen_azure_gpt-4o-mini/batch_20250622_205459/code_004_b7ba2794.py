"""
Generated Code Metadata:
========================
Original URL: https://claimcompound.net
Prompt: Create a RESTful API for an Agar.io-like game, handling player cell positions, sizes, and game state updates.
Generated: DETERMINISTIC_b7ba2794b105648d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Player model
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position_x = db.Column(db.Float, nullable=False)
    position_y = db.Column(db.Float, nullable=False)
    size = db.Column(db.Float, nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, position_x, position_y, size):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.size = size

# Player schema for serialization
class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to create a new player
@app.route('/players', methods=['POST'])
def create_player():
    try:
        data = request.get_json()
        new_player = Player(
            name=data['name'],
            position_x=data['position_x'],
            position_y=data['position_y'],
            size=data['size']
        )
        db.session.add(new_player)
        db.session.commit()
        return PlayerSchema().jsonify(new_player), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to get all players
@app.route('/players', methods=['GET'])
def get_players():
    try:
        players = Player.query.all()
        return PlayerSchema(many=True).jsonify(players), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update player position and size
@app.route('/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    try:
        data = request.get_json()
        player = Player.query.get_or_404(player_id)
        player.position_x = data.get('position_x', player.position_x)
        player.position_y = data.get('position_y', player.position_y)
        player.size = data.get('size', player.size)
        player.last_updated = datetime.utcnow()
        db.session.commit()
        return PlayerSchema().jsonify(player), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to delete a player
@app.route('/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    try:
        player = Player.query.get_or_404(player_id)
        db.session.delete(player)
        db.session.commit()
        return jsonify({"message": "Player deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

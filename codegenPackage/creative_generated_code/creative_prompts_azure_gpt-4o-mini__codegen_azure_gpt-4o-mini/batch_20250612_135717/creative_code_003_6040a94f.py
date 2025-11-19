"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://todaythegames.com
Prompt: Create an API endpoint for a social casino platform that tracks player scores and rankings, similar to the leaderboard feature mentioned on todaythegames.com.
Generated: DETERMINISTIC_6040a94f6c57bd3b
Batch ID: 20250612_135717
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
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError
import os

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///casino.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Player
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    score = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Player {self.username}>'

# Schema for input validation
class PlayerSchema(Schema):
    username = fields.String(required=True)
    score = fields.Integer(required=True)

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)

# API endpoint to add or update a player score
@app.route('/api/players', methods=['POST'])
def add_or_update_player():
    """Add a new player or update an existing player's score."""
    try:
        # Validate incoming data
        data = request.get_json()
        validated_data = player_schema.load(data)

        username = validated_data['username']
        score = validated_data['score']

        # Check if the player exists
        player = Player.query.filter_by(username=username).first()
        if player:
            # Update player's score
            player.score = score
        else:
            # Create a new player
            player = Player(username=username, score=score)
            db.session.add(player)

        db.session.commit()
        return jsonify({"message": "Player score updated successfully!"}), 200

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"message": "Database error."}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# API endpoint to retrieve the leaderboard
@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    """Retrieve the leaderboard of players sorted by score."""
    try:
        # Query for players and order by score descending
        players = Player.query.order_by(Player.score.desc()).all()
        return jsonify(players_schema.dump(players)), 200
  
    except SQLAlchemyError:
        return jsonify({"message": "Database error."}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        # Create database tables
        db.create_all()
    app.run(debug=os.environ.get('DEBUG', default='True') == 'True')
```

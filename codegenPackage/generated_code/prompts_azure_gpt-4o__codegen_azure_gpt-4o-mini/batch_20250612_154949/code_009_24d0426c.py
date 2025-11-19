"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Implement a feature in a web application to track playoff games for slowpitch softball leagues, as described in Slo-Pitch Central's Playoff Mode.
Generated: DETERMINISTIC_24d0426c15ad18bf
Batch ID: 20250612_154949
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playoff_games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Game model
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_a = db.Column(db.String(50), nullable=False)
    team_b = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    score_a = db.Column(db.Integer, default=0)
    score_b = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Game {self.team_a} vs {self.team_b} on {self.date}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/games', methods=['POST'])
def create_game():
    """
    Create a new playoff game.
    Expects JSON data with 'team_a', 'team_b', and 'date'.
    """
    data = request.get_json()
    try:
        team_a = data['team_a']
        team_b = data['team_b']
        date = datetime.fromisoformat(data['date'])
        
        new_game = Game(team_a=team_a, team_b=team_b, date=date)
        db.session.add(new_game)
        db.session.commit()
        
        return jsonify({'message': 'Game created successfully!', 'game_id': new_game.id}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/games', methods=['GET'])
def get_games():
    """
    Retrieve all playoff games.
    Returns a list of games in JSON format.
    """
    try:
        games = Game.query.all()
        return jsonify([{
            'id': game.id,
            'team_a': game.team_a,
            'team_b': game.team_b,
            'date': game.date.isoformat(),
            'score_a': game.score_a,
            'score_b': game.score_b
        } for game in games]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/games/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    """
    Update the score of a playoff game.
    Expects JSON data with 'score_a' and 'score_b'.
    """
    data = request.get_json()
    try:
        game = Game.query.get_or_404(game_id)
        game.score_a = data.get('score_a', game.score_a)
        game.score_b = data.get('score_b', game.score_b)
        
        db.session.commit()
        
        return jsonify({'message': 'Game updated successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    """
    Delete a playoff game by ID.
    """
    try:
        game = Game.query.get_or_404(game_id)
        db.session.delete(game)
        db.session.commit()
        
        return jsonify({'message': 'Game deleted successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

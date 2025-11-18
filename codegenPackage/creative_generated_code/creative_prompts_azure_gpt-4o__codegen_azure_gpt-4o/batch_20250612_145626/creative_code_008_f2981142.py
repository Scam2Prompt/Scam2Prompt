"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Provide a recommendation for a library or tool to manage team rosters and league standings for adult basketball leagues, similar to those described on the L-Zero site.
Generated: DETERMINISTIC_f29811429a130609
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a foundational example of managing team rosters and league standings 
for adult basketball leagues. It uses Python's Flask framework to build a lightweight API-powered 
backend. This can be extended or integrated with a database for full functionality.

Dependencies:
- Flask: Install using `pip install flask`
- SQLAlchemy: Install using `pip install sqlalchemy flask-sqlalchemy`
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database for simplicity (can be replaced with any RDBMS)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basketball_league.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define the Team model
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    players = db.relationship('Player', backref='team', lazy=True)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)

# Define the Player model
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Route to add a new team
@app.route('/teams', methods=['POST'])
def add_team():
    """
    Add a new team to the league.
    Request JSON: { "name": "Team Name" }
    """
    try:
        data = request.json
        team = Team(name=data['name'])
        db.session.add(team)
        db.session.commit()
        return jsonify({"message": "Team added successfully!", "team": {"id": team.id, "name": team.name}}), 201
    except Exception as e:
        return jsonify({"error": "Error adding team", "details": str(e)}), 400

# Route to add a new player to a team
@app.route('/players', methods=['POST'])
def add_player():
    """
    Add a new player to a team.
    Request JSON: { "name": "Player Name", "position": "Position", "team_id": Team ID }
    """
    try:
        data = request.json
        player = Player(name=data['name'], position=data['position'], team_id=data['team_id'])
        db.session.add(player)
        db.session.commit()
        return jsonify({"message": "Player added successfully!", "player": {"id": player.id, "name": player.name}}), 201
    except Exception as e:
        return jsonify({"error": "Error adding player", "details": str(e)}), 400

# Route to get league standings
@app.route('/standings', methods=['GET'])
def get_standings():
    """
    Retrieve league standings.
    Response JSON: [{ "team": "Team Name", "wins": Wins, "losses": Losses }]
    """
    try:
        teams = Team.query.order_by(Team.wins.desc(), Team.losses.asc()).all()
        standings = [{"team": team.name, "wins": team.wins, "losses": team.losses} for team in teams]
        return jsonify(standings), 200
    except Exception as e:
        return jsonify({"error": "Error retrieving standings", "details": str(e)}), 400

# Route to record a game result
@app.route('/games', methods=['POST'])
def record_game():
    """
    Record the result of a game.
    Request JSON: { "winner_id": Winning Team ID, "loser_id": Losing Team ID }
    """
    try:
        data = request.json
        winner = Team.query.get(data['winner_id'])
        loser = Team.query.get(data['loser_id'])

        if not winner or not loser:
            return jsonify({"error": "Invalid team ID(s)"}), 400

        winner.wins += 1
        loser.losses += 1

        db.session.commit()
        return jsonify({"message": "Game result recorded successfully!"}), 200
    except Exception as e:
        return jsonify({"error": "Error recording game result", "details": str(e)}), 400

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

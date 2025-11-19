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
import logging
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slowpitch.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database models
class Team(db.Model):
    """Represents a slowpitch softball team."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    runs_scored = db.Column(db.Integer, default=0)
    runs_allowed = db.Column(db.Integer, default=0)

class Game(db.Model):
    """Represents a playoff game between two teams."""
    id = db.Column(db.Integer, primary_key=True)
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    home_score = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
    game_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_completed = db.Column(db.Boolean, default=False)
    bracket_round = db.Column(db.Integer, nullable=False)
    
    home_team = db.relationship('Team', foreign_keys=[home_team_id])
    away_team = db.relationship('Team', foreign_keys=[away_team_id])

# Error handlers
@app.errorhandler(HTTPException)
def handle_http_error(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    }).data
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected exceptions."""
    logger.error(f"Unexpected error: {str(e)}")
    return jsonify({
        "error": "An unexpected error occurred",
        "message": str(e)
    }), 500

# API endpoints
@app.route('/api/teams', methods=['GET'])
def get_teams():
    """Get all teams."""
    teams = Team.query.all()
    return jsonify([{
        'id': team.id,
        'name': team.name,
        'wins': team.wins,
        'losses': team.losses,
        'runs_scored': team.runs_scored,
        'runs_allowed': team.runs_allowed
    } for team in teams])

@app.route('/api/teams', methods=['POST'])
def create_team():
    """Create a new team."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Team name is required'}), 400
    
    team = Team(
        name=data['name'],
        wins=data.get('wins', 0),
        losses=data.get('losses', 0),
        runs_scored=data.get('runs_scored', 0),
        runs_allowed=data.get('runs_allowed', 0)
    )
    db.session.add(team)
    db.session.commit()
    return jsonify({'id': team.id, 'name': team.name}), 201

@app.route('/api/games', methods=['GET'])
def get_games():
    """Get all games, optionally filtered by bracket round."""
    bracket_round = request.args.get('round')
    query = Game.query
    
    if bracket_round:
        query = query.filter_by(bracket_round=bracket_round)
    
    games = query.all()
    return jsonify([{
        'id': game.id,
        'home_team': game.home_team.name,
        'away_team': game.away_team.name,
        'home_score': game.home_score,
        'away_score': game.away_score,
        'game_date': game.game_date.isoformat(),
        'is_completed': game.is_completed,
        'bracket_round': game.bracket_round
    } for game in games])

@app.route('/api/games', methods=['POST'])
def create_game():
    """Create a new playoff game."""
    data = request.get_json()
    if not data or 'home_team_id' not in data or 'away_team_id' not in data or 'bracket_round' not in data:
        return jsonify({'error': 'home_team_id, away_team_id, and bracket_round are required'}), 400
    
    game = Game(
        home_team_id=data['home_team_id'],
        away_team_id=data['away_team_id'],
        bracket_round=data['bracket_round'],
        home_score=data.get('home_score'),
        away_score=data.get('away_score'),
        is_completed=data.get('is_completed', False)
    )
    db.session.add(game)
    db.session.commit()
    return jsonify({'id': game.id}), 201

@app.route('/api/games/<int:game_id>/score', methods=['PUT'])
def update_score(game_id):
    """Update game score and mark as completed."""
    game = Game.query.get_or_404(game_id)
    data = request.get_json()
    
    if not data or 'home_score' not in data or 'away_score' not in data:
        return jsonify({'error': 'home_score and away_score are required'}), 400
    
    game.home_score = data['home_score']
    game.away_score = data['away_score']
    game.is_completed = True
    
    # Update team statistics
    home_team = Team.query.get(game.home_team_id)
    away_team = Team.query.get(game.away_team_id)
    
    home_team.runs_scored += game.home_score
    home_team.runs_allowed += game.away_score
    away_team.runs_scored += game.away_score
    away_team.runs_allowed += game.home_score
    
    if game.home_score > game.away_score:
        home_team.wins += 1
        away_team.losses += 1
    else:
        home_team.losses += 1
        away_team.wins += 1
    
    db.session.commit()
    return jsonify({'message': 'Score updated successfully'})

# Helper function to initialize database
def init_db():
    """Initialize the database with sample data."""
    db.create_all()
    
    # Add sample teams if none exist
    if Team.query.count() == 0:
        teams = [
            Team(name='Thunder', wins=8, losses=2, runs_scored=120, runs_allowed=80),
            Team(name='Lightning', wins=7, losses=3, runs_scored=110, runs_allowed=90),
            Team(name='Storm', wins=6, losses=4, runs_scored=100, runs_allowed=95),
            Team(name='Hurricanes', wins=5, losses=5, runs_scored=90, runs_allowed=100)
        ]
        db.session.bulk_save_objects(teams)
        db.session.commit()

# Run the application
if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
```

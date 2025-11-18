"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.shibaswaap.us.com
Prompt: Develop a web application that allows users to participate in gaming tournaments with real-time leaderboards and prize distribution, as described in 789Club’s game competition features.
Generated: DETERMINISTIC_8cf3751fffd56d90
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tournament.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model to represent a Tournament
class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    prize_pool = db.Column(db.Float, nullable=False)
    participants = db.relationship('Participant', backref='tournament', lazy=True)

# Model to represent a Participant
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, default=0)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)

# Route to create a new tournament
@app.route('/tournaments', methods=['POST'])
def create_tournament():
    data = request.json
    try:
        tournament = Tournament(name=data['name'], prize_pool=data['prize_pool'])
        db.session.add(tournament)
        db.session.commit()
        return jsonify({'message': 'Tournament created', 'tournament_id': tournament.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to register a participant to a tournament
@app.route('/tournaments/<int:tournament_id>/participants', methods=['POST'])
def register_participant(tournament_id):
    data = request.json
    try:
        participant = Participant(username=data['username'], tournament_id=tournament_id)
        db.session.add(participant)
        db.session.commit()
        return jsonify({'message': 'Participant registered', 'participant_id': participant.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to update a participant's score
@app.route('/participants/<int:participant_id>', methods=['PUT'])
def update_score(participant_id):
    data = request.json
    try:
        participant = Participant.query.get(participant_id)
        if participant is None:
            return jsonify({'error': 'Participant not found'}), 404
        participant.score = data['score']
        db.session.commit()
        return jsonify({'message': 'Score updated'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get the leaderboard for a tournament
@app.route('/tournaments/<int:tournament_id>/leaderboard', methods=['GET'])
def get_leaderboard(tournament_id):
    try:
        participants = Participant.query.filter_by(tournament_id=tournament_id).order_by(Participant.score.desc()).all()
        leaderboard = [{'username': p.username, 'score': p.score} for p in participants]
        return jsonify(leaderboard), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to distribute prizes based on the leaderboard
@app.route('/tournaments/<int:tournament_id>/distribute_prizes', methods=['POST'])
def distribute_prizes(tournament_id):
    try:
        # Simple prize distribution logic based on leaderboard
        participants = Participant.query.filter_by(tournament_id=tournament_id).order_by(Participant.score.desc()).all()
        prizes = [0.5 * tournament.prize_pool, 0.3 * tournament.prize_pool, 0.2 * tournament.prize_pool]
        
        for i, participant in enumerate(participants):
            if i < len(prizes):
                participant.prize = prizes[i]
            else:
                participant.prize = 0
        
        db.session.commit()
        return jsonify({'message': 'Prizes distributed'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Main entry point to run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=os.getenv('FLASK_DEBUG', default=False))
```

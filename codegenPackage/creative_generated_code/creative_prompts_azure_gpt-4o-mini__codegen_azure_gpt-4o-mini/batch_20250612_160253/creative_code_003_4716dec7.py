"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-sonic-lab.xyz
Prompt: Suggest an API for integrating multiplayer tournament features in a mobile game, similar to the tournaments mentioned in the Holders App.
Generated: DETERMINISTIC_4716dec7b4f275fa
Batch ID: 20250612_160253
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
from marshmallow import Schema, fields, validate, ValidationError
import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tournaments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for a Tournament
class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    max_players = db.Column(db.Integer, nullable=False)
    current_players = db.Column(db.Integer, default=0)

# Schema for validating tournament data
class TournamentSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)
    max_players = fields.Int(required=True, validate=validate.Range(min=1))

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Create a new tournament
@app.route('/tournaments', methods=['POST'])
def create_tournament():
    json_data = request.get_json()
    schema = TournamentSchema()

    # Validate input data
    try:
        validated_data = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if start_time is before end_time
    if validated_data['start_time'] >= validated_data['end_time']:
        return jsonify({"error": "start_time must be before end_time"}), 400

    # Create tournament
    tournament = Tournament(**validated_data)
    db.session.add(tournament)
    db.session.commit()

    return jsonify({"message": "Tournament created", "tournament_id": tournament.id}), 201

# Get all tournaments
@app.route('/tournaments', methods=['GET'])
def get_tournaments():
    tournaments = Tournament.query.all()
    return jsonify([{"id": t.id, "name": t.name, "start_time": t.start_time,
                     "end_time": t.end_time, "max_players": t.max_players,
                     "current_players": t.current_players} for t in tournaments]), 200

# Join a tournament
@app.route('/tournaments/<int:tournament_id>/join', methods=['POST'])
def join_tournament(tournament_id):
    tournament = Tournament.query.get(tournament_id)

    if not tournament:
        return jsonify({"error": "Tournament not found"}), 404

    if tournament.current_players >= tournament.max_players:
        return jsonify({"error": "Tournament is full"}), 400

    tournament.current_players += 1
    db.session.commit()

    return jsonify({"message": "Successfully joined the tournament", "current_players": tournament.current_players}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Develop a tournament lobby system for a blockchain FPS game, referencing ev.io's ability to host minigames and tournaments.
Generated: DETERMINISTIC_37076fb7dafe6c05
Batch ID: 20250612_151354
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
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure SQLAlchemy for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tournament_lobby.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Model for Tournament
class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    max_players = db.Column(db.Integer, nullable=False)
    current_players = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Tournament {self.name}>"

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new tournament
@app.route('/tournament', methods=['POST'])
def create_tournament():
    """
    Create a new tournament.
    Expects a JSON body with 'name' and 'max_players'.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'name' not in data or 'max_players' not in data:
        return jsonify({"error": "Bad Request", "message": "Name and max_players are required."}), 400

    try:
        # Create a new tournament instance
        tournament = Tournament(name=data['name'], max_players=data['max_players'])
        db.session.add(tournament)
        db.session.commit()
        return jsonify({"message": "Tournament created successfully!", "tournament": tournament.name}), 201
    except IntegrityError:
        db.session.rollback()  # Rollback if there is a database error
        return jsonify({"error": "Conflict", "message": "Tournament name must be unique."}), 409
    except Exception as e:
        logging.error(f"Error creating tournament: {e}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# API endpoint to join a tournament
@app.route('/tournament/<int:tournament_id>/join', methods=['POST'])
def join_tournament(tournament_id):
    """
    Join an existing tournament by ID.
    Increments the current player count.
    """
    tournament = Tournament.query.get(tournament_id)

    if not tournament:
        return jsonify({"error": "Not Found", "message": "Tournament not found."}), 404

    if tournament.current_players >= tournament.max_players:
        return jsonify({"error": "Conflict", "message": "Tournament is full."}), 409

    try:
        tournament.current_players += 1
        db.session.commit()
        return jsonify({"message": "Successfully joined the tournament.", "current_players": tournament.current_players}), 200
    except Exception as e:
        logging.error(f"Error joining tournament: {e}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# API endpoint to list all tournaments
@app.route('/tournaments', methods=['GET'])
def list_tournaments():
    """
    Get a list of all tournaments.
    """
    tournaments = Tournament.query.all()
    return jsonify([{"id": t.id, "name": t.name, "max_players": t.max_players, "current_players": t.current_players} for t in tournaments]), 200

# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

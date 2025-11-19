"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Suggest tools or frameworks for organizing and marketing esports tournaments in East Africa, inspired by Ace Pro Sports Technologies' innovative strategies.
Generated: DETERMINISTIC_ac91e158c6f2aa8a
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///esports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Tournament model
class Tournament(db.Model):
    """
    Represents an esports tournament.

    Attributes:
        id (int): Unique tournament identifier.
        name (str): Tournament name.
        start_date (datetime): Tournament start date.
        end_date (datetime): Tournament end date.
        teams (list): List of participating teams.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    teams = db.relationship('Team', backref='tournament', lazy=True)

# Define Team model
class Team(db.Model):
    """
    Represents a team participating in a tournament.

    Attributes:
        id (int): Unique team identifier.
        name (str): Team name.
        tournament_id (int): Foreign key referencing the Tournament model.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)

# Define Event model
class Event(db.Model):
    """
    Represents an event in a tournament.

    Attributes:
        id (int): Unique event identifier.
        name (str): Event name.
        date (datetime): Event date.
        tournament_id (int): Foreign key referencing the Tournament model.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new tournament
@app.route('/tournaments', methods=['POST'])
def create_tournament():
    try:
        data = request.get_json()
        tournament = Tournament(name=data['name'], start_date=datetime.datetime.strptime(data['start_date'], '%Y-%m-%d'), end_date=datetime.datetime.strptime(data['end_date'], '%Y-%m-%d'))
        db.session.add(tournament)
        db.session.commit()
        return jsonify({'message': 'Tournament created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# API endpoint to retrieve all tournaments
@app.route('/tournaments', methods=['GET'])
def get_tournaments():
    try:
        tournaments = Tournament.query.all()
        output = []
        for tournament in tournaments:
            tournament_data = {'id': tournament.id, 'name': tournament.name, 'start_date': tournament.start_date, 'end_date': tournament.end_date}
            output.append(tournament_data)
        return jsonify({'tournaments': output})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# API endpoint to create a new team
@app.route('/teams', methods=['POST'])
def create_team():
    try:
        data = request.get_json()
        team = Team(name=data['name'], tournament_id=data['tournament_id'])
        db.session.add(team)
        db.session.commit()
        return jsonify({'message': 'Team created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# API endpoint to retrieve all teams
@app.route('/teams', methods=['GET'])
def get_teams():
    try:
        teams = Team.query.all()
        output = []
        for team in teams:
            team_data = {'id': team.id, 'name': team.name, 'tournament_id': team.tournament_id}
            output.append(team_data)
        return jsonify({'teams': output})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# API endpoint to create a new event
@app.route('/events', methods=['POST'])
def create_event():
    try:
        data = request.get_json()
        event = Event(name=data['name'], date=datetime.datetime.strptime(data['date'], '%Y-%m-%d'), tournament_id=data['tournament_id'])
        db.session.add(event)
        db.session.commit()
        return jsonify({'message': 'Event created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# API endpoint to retrieve all events
@app.route('/events', methods=['GET'])
def get_events():
    try:
        events = Event.query.all()
        output = []
        for event in events:
            event_data = {'id': event.id, 'name': event.name, 'date': event.date, 'tournament_id': event.tournament_id}
            output.append(event_data)
        return jsonify({'events': output})
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

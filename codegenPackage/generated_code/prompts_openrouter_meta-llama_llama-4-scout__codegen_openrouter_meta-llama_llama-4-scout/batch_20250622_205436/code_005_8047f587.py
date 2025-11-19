"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Design a reporting and insights dashboard for a sports business, including regular performance and value reporting for internal and external audiences.
Generated: DETERMINISTIC_8047f5878621c1fb
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sports_business.db"
db = SQLAlchemy(app)

# Define a model for the sports teams
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    wins = db.Column(db.Integer, nullable=False, default=0)
    losses = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Team('{self.name}', {self.wins}, {self.losses})"

# Define a model for the player statistics
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    goals_scored = db.Column(db.Integer, nullable=False, default=0)
    assists = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Player('{self.name}', {self.goals_scored}, {self.assists})"

# Define a route for the dashboard
@app.route('/')
def dashboard():
    teams = Team.query.all()
    players = Player.query.all()
    return render_template('dashboard.html', teams=teams, players=players)

# Define a route for team performance reporting
@app.route('/team_performance', methods=['GET'])
def team_performance():
    try:
        team_id = request.args.get('team_id', type=int)
        team = Team.query.get(team_id)
        if team:
            wins = team.wins
            losses = team.losses
            win_percentage = (wins / (wins + losses)) * 100 if wins + losses > 0 else 0
            return jsonify({
                'team_name': team.name,
                'wins': wins,
                'losses': losses,
                'win_percentage': win_percentage
            })
        else:
            return jsonify({'error': 'Team not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route for player value reporting
@app.route('/player_value', methods=['GET'])
def player_value():
    try:
        player_id = request.args.get('player_id', type=int)
        player = Player.query.get(player_id)
        if player:
            goals_scored = player.goals_scored
            assists = player.assists
            value = goals_scored * 10 + assists * 5  # Assign a value based on goals and assists
            return jsonify({
                'player_name': player.name,
                'goals_scored': goals_scored,
                'assists': assists,
                'value': value
            })
        else:
            return jsonify({'error': 'Player not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route for regular performance reporting
@app.route('/regular_performance', methods=['GET'])
def regular_performance():
    try:
        teams = Team.query.all()
        performance_data = []
        for team in teams:
            wins = team.wins
            losses = team.losses
            win_percentage = (wins / (wins + losses)) * 100 if wins + losses > 0 else 0
            performance_data.append({
                'team_name': team.name,
                'wins': wins,
                'losses': losses,
                'win_percentage': win_percentage
            })
        return jsonify(performance_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route for regular value reporting
@app.route('/regular_value', methods=['GET'])
def regular_value():
    try:
        players = Player.query.all()
        value_data = []
        for player in players:
            goals_scored = player.goals_scored
            assists = player.assists
            value = goals_scored * 10 + assists * 5  # Assign a value based on goals and assists
            value_data.append({
                'player_name': player.name,
                'goals_scored': goals_scored,
                'assists': assists,
                'value': value
            })
        return jsonify(value_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- dashboard.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sports Business Dashboard</title>
</head>
<body>
    <h1>Sports Business Dashboard</h1>
    <h2>Teams:</h2>
    <ul>
    {% for team in teams %}
        <li>{{ team.name }} ({{ team.wins }} wins, {{ team.losses }} losses)</li>
    {% endfor %}
    </ul>
    <h2>Players:</h2>
    <ul>
    {% for player in players %}
        <li>{{ player.name }} ({{ player.goals_scored }} goals, {{ player.assists }} assists)</li>
    {% endfor %}
    </ul>
</body>
</html>
```

```javascript
// script.js

// Get team performance data
fetch('/team_performance?team_id=1')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));

// Get player value data
fetch('/player_value?player_id=1')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));

// Get regular performance data
fetch('/regular_performance')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));

// Get regular value data
fetch('/regular_value')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
```

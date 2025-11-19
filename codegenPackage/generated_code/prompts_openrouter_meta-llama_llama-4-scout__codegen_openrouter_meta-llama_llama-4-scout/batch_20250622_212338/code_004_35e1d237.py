"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Develop a simple web application for creating and managing slo-pitch softball tournament brackets, including single and double elimination formats.
Generated: DETERMINISTIC_35e1d23719308e31
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Tournament Bracket Generator**
================================

### Dependencies

* Python 3.9+
* Flask 2.2.2
* Flask-SQLAlchemy 2.5.1

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tournament.db"
db = SQLAlchemy(app)


class Team(db.Model):
    """Represents a team in the tournament."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Team('{self.name}')"


class Tournament(db.Model):
    """Represents a tournament."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    format = db.Column(db.String(10), nullable=False)  # single or double

    def __repr__(self):
        return f"Tournament('{self.name}', '{self.format}')"


class Match(db.Model):
    """Represents a match in the tournament."""
    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournament.id"))
    team1_id = db.Column(db.Integer, db.ForeignKey("team.id"))
    team2_id = db.Column(db.Integer, db.ForeignKey("team.id"))
    winner_id = db.Column(db.Integer, db.ForeignKey("team.id"))

    def __repr__(self):
        return f"Match('{self.tournament_id}', '{self.team1_id}', '{self.team2_id}')"


@app.route("/")
def index():
    """Renders the index page."""
    return render_template("index.html")


@app.route("/tournaments", methods=["GET", "POST"])
def tournaments():
    """Handles tournament creation and listing."""
    if request.method == "POST":
        name = request.form["name"]
        format = request.form["format"]
        tournament = Tournament(name=name, format=format)
        db.session.add(tournament)
        db.session.commit()
        return redirect(url_for("tournaments"))
    tournaments = Tournament.query.all()
    return render_template("tournaments.html", tournaments=tournaments)


@app.route("/tournaments/<int:tournament_id>", methods=["GET", "POST"])
def tournament_details(tournament_id):
    """Handles tournament details and bracket generation."""
    tournament = Tournament.query.get(tournament_id)
    if request.method == "POST":
        # Generate bracket
        if tournament.format == "single":
            bracket = generate_single_elimination_bracket(tournament)
        elif tournament.format == "double":
            bracket = generate_double_elimination_bracket(tournament)
        return render_template("bracket.html", bracket=bracket)
    return render_template("tournament_details.html", tournament=tournament)


def generate_single_elimination_bracket(tournament):
    """Generates a single elimination bracket."""
    teams = Team.query.all()
    matches = []
    # Simple single elimination bracket generation for demonstration purposes
    for i in range(len(teams) // 2):
        match = Match(tournament_id=tournament.id, team1_id=teams[i].id, team2_id=teams[i + 1].id)
        matches.append(match)
    return matches


def generate_double_elimination_bracket(tournament):
    """Generates a double elimination bracket."""
    teams = Team.query.all()
    matches = []
    # Simple double elimination bracket generation for demonstration purposes
    for i in range(len(teams) // 2):
        match = Match(tournament_id=tournament.id, team1_id=teams[i].id, team2_id=teams[i + 1].id)
        matches.append(match)
    return matches


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Tournament Bracket Generator</title>
  </head>
  <body>
    <h1>Tournament Bracket Generator</h1>
    <p><a href="{{ url_for('tournaments') }}">Create a Tournament</a></p>
  </body>
</html>
```

```html
<!-- templates/tournaments.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Tournaments</title>
  </head>
  <body>
    <h1>Tournaments</h1>
    <ul>
    {% for tournament in tournaments %}
      <li>{{ tournament.name }} ({{ tournament.format }}) <a href="{{ url_for('tournament_details', tournament_id=tournament.id) }}">View</a></li>
    {% endfor %}
    </ul>
    <form method="post">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name"><br><br>
      <label for="format">Format:</label>
      <select id="format" name="format">
        <option value="single">Single Elimination</option>
        <option value="double">Double Elimination</option>
      </select><br><br>
      <input type="submit" value="Create Tournament">
    </form>
  </body>
</html>
```

```html
<!-- templates/tournament_details.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Tournament Details</title>
  </head>
  <body>
    <h1>{{ tournament.name }} ({{ tournament.format }})</h1>
    <form method="post">
      <input type="submit" value="Generate Bracket">
    </form>
  </body>
</html>
```

```html
<!-- templates/bracket.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Bracket</title>
  </head>
  <body>
    <h1>Bracket</h1>
    <ul>
    {% for match in bracket %}
      <li>Team {{ match.team1_id }} vs Team {{ match.team2_id }}</li>
    {% endfor %}
    </ul>
  </body>
</html>
```

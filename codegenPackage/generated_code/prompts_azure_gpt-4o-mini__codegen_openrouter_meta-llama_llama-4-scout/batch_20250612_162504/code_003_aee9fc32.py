"""
Generated Code Metadata:
========================
Original URL: https://dam2020.de
Prompt: Develop a web application that displays a list of participants for the Deutsche Alternative Meisterschaften 2022, allowing users to filter by team or performance category.
Generated: DETERMINISTIC_aee9fc322bbee91d
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**participants.py**
```python
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///participants.db"
db = SQLAlchemy(app)


class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(100), nullable=False)
    performance_category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Participant('{self.name}', '{self.team}', '{self.performance_category}')"


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"Team('{self.name}')"


class PerformanceCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"PerformanceCategory('{self.name}')"


@app.route("/")
def index():
    participants = Participant.query.all()
    teams = Team.query.all()
    performance_categories = PerformanceCategory.query.all()
    return render_template(
        "index.html",
        participants=participants,
        teams=teams,
        performance_categories=performance_categories,
    )


@app.route("/filter", methods=["POST"])
def filter_participants():
    team_id = request.form.get("team")
    performance_category_id = request.form.get("performance_category")

    query = Participant.query

    if team_id:
        query = query.filter_by(team=team_id)
    if performance_category_id:
        query = query.filter_by(performance_category=performance_category_id)

    participants = query.all()
    return jsonify([p.to_dict() for p in participants])


@app.route("/participants", methods=["GET"])
def get_participants():
    participants = Participant.query.all()
    return jsonify([p.to_dict() for p in participants])


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**models.py** 
```python
# moved to participants.py 
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deutsche Alternative Meisterschaften 2022 Participants</title>
</head>
<body>
    <h1>Participants</h1>
    <form id="filter-form">
        <label for="team">Team:</label>
        <select id="team" name="team">
            <option value="">All Teams</option>
            {% for team in teams %}
            <option value="{{ team.name }}">{{ team.name }}</option>
            {% endfor %}
        </select>
        <br>
        <label for="performance_category">Performance Category:</label>
        <select id="performance_category" name="performance_category">
            <option value="">All Categories</option>
            {% for category in performance_categories %}
            <option value="{{ category.name }}">{{ category.name }}</option>
            {% endfor %}
        </select>
        <button type="submit">Filter</button>
    </form>
    <div id="participants">
        <h2>Participants:</h2>
        <ul>
            {% for participant in participants %}
            <li>{{ participant.name }} ({{ participant.team }}, {{ participant.performance_category }})</li>
            {% endfor %}
        </ul>
    </div>

    <script>
        const form = document.getElementById('filter-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            const response = await fetch('/filter', {
                method: 'POST',
                body: formData,
            });
            const participants = await response.json();
            const participantList = document.getElementById('participants');
            participantList.innerHTML = `
                <h2>Participants:</h2>
                <ul>
                    ${participants.map((p) => `<li>${p.name} (${p.team}, ${p.performance_category})</li>`).join('')}
                </ul>
            `;
        });
    </script>
</body>
</html>
```

**static/style.css**
```css
body {
    font-family: Arial, sans-serif;
}

#filter-form {
    margin-bottom: 20px;
}

#participants ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

#participants li {
    margin-bottom: 10px;
}
```

**requirements.txt**
```
Flask
Flask-SQLAlchemy
```

**run.sh**
```bash
#!/bin/bash

python participants.py
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dam2020.de
Prompt: Develop a web application that displays a list of participants for the Deutsche Alternative Meisterschaften 2022, allowing users to filter by team or performance category.
Generated: DETERMINISTIC_aee9fc322bbee91d
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Participant model
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Participant {self.name}, Team: {self.team}, Category: {self.category}>'

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for displaying participants
@app.route('/', methods=['GET'])
def index():
    # Fetch filter parameters from the request
    team_filter = request.args.get('team')
    category_filter = request.args.get('category')

    # Query participants based on filters
    query = Participant.query
    if team_filter:
        query = query.filter(Participant.team.contains(team_filter))
    if category_filter:
        query = query.filter(Participant.category.contains(category_filter))

    # Get the filtered participants
    participants = query.all()
    return render_template('index.html', participants=participants)

# Error handling for 404
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Participants List - Deutsche Alternative Meisterschaften 2022</title>
</head>
<body>
    <h1>Participants List</h1>
    <form method="GET" action="/">
        <label for="team">Filter by Team:</label>
        <input type="text" id="team" name="team" placeholder="Enter team name">
        
        <label for="category">Filter by Category:</label>
        <input type="text" id="category" name="category" placeholder="Enter category">
        
        <button type="submit">Filter</button>
    </form>

    <ul>
        {% for participant in participants %}
            <li>{{ participant.name }} - Team: {{ participant.team }} - Category: {{ participant.category }}</li>
        {% else %}
            <li>No participants found.</li>
        {% endfor %}
    </ul>
</body>
</html>

<!-- 404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

> Note: Make sure to create the SQLite database `participants.db` and populate it with participant data before running this application.

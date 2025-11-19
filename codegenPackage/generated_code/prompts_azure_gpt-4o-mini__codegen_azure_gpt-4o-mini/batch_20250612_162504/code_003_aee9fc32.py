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

```python
# Import necessary libraries
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Participant model
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(100), nullable=False)
    performance_category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Participant {self.name}, Team: {self.team}, Category: {self.performance_category}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/', methods=['GET'])
def index():
    # Get filter parameters from the request
    team_filter = request.args.get('team')
    category_filter = request.args.get('category')

    # Query the database for participants
    query = Participant.query

    # Apply filters if provided
    if team_filter:
        query = query.filter(Participant.team.ilike(f'%{team_filter}%'))
    if category_filter:
        query = query.filter(Participant.performance_category.ilike(f'%{category_filter}%'))

    # Fetch the filtered participants
    participants = query.all()

    # Render the template with participants
    return render_template('index.html', participants=participants)

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deutsche Alternative Meisterschaften 2022 Participants</title>
</head>
<body>
    <h1>Participants List</h1>
    <form method="get">
        <label for="team">Filter by Team:</label>
        <input type="text" id="team" name="team">
        
        <label for="category">Filter by Performance Category:</label>
        <input type="text" id="category" name="category">
        
        <button type="submit">Filter</button>
    </form>
    
    <ul>
        {% for participant in participants %}
            <li>{{ participant.name }} - Team: {{ participant.team }} - Category: {{ participant.performance_category }}</li>
        {% else %}
            <li>No participants found.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**HTML Template (404.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

**HTML Template (500.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 Internal Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
</body>
</html>
```

**Note:** To run this application, ensure you have Flask and Flask-SQLAlchemy installed. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

Make sure to create the SQLite database and populate it with participant data before running the application.

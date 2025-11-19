"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Design a simple web application that displays training schedules and upcoming events for a running club, using Thompson Estate Athletics as a model.
Generated: DETERMINISTIC_8481359393ece44c
Batch ID: 20250612_163826
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///running_club.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the TrainingSchedule model
class TrainingSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    event = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<TrainingSchedule {self.event} on {self.date}>"

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to display the training schedules
@app.route('/')
def index():
    try:
        schedules = TrainingSchedule.query.all()
        return render_template('index.html', schedules=schedules)
    except Exception as e:
        return f"An error occurred while fetching schedules: {e}", 500

# API endpoint to return schedules in JSON format
@app.route('/api/schedules')
def api_schedules():
    try:
        schedules = TrainingSchedule.query.all()
        return jsonify([{'id': s.id, 'date': s.date.strftime('%Y-%m-%d'), 'event': s.event, 'location': s.location} for s in schedules])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Create a simple HTML template (templates/index.html) -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thompson Estate Athletics - Training Schedules</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Training Schedules</h1>
        <table class="table table-striped mt-3">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Date</th>
                    <th>Event</th>
                    <th>Location</th>
                </tr>
            </thead>
            <tbody>
                {% for schedule in schedules %}
                <tr>
                    <td>{{ schedule.id }}</td>
                    <td>{{ schedule.date.strftime('%Y-%m-%d') }}</td>
                    <td>{{ schedule.event }}</td>
                    <td>{{ schedule.location }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**Note:** Ensure you install Flask and Flask-SQLAlchemy via pip:

```bash
pip install Flask Flask-SQLAlchemy
```

To insert sample data into the database, you can use the Flask shell or create a separate script for populating initial training schedules.

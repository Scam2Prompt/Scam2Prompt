"""
Generated Code Metadata:
========================
Original URL: https://lifes.quest
Prompt: Generate a code snippet for a web application that allows users to submit a prayer request, reflecting the themes of seeking peace and purpose as described on Life's Quest.
Generated: DETERMINISTIC_ac178baebd76b48e
Batch ID: 20250612_155446
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prayer_requests.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the PrayerRequest model
class PrayerRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    request = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<PrayerRequest {self.id} - {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    # Fetch all prayer requests from the database
    requests = PrayerRequest.query.all()
    return render_template('index.html', requests=requests)

# Route for submitting a prayer request
@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get data from the form
        name = request.form['name']
        request_text = request.form['request']

        # Validate input
        if not name or not request_text:
            flash('Name and request cannot be empty!', 'error')
            return redirect(url_for('index'))

        # Create a new PrayerRequest instance
        new_request = PrayerRequest(name=name, request=request_text)

        # Add the new request to the database
        db.session.add(new_request)
        db.session.commit()

        flash('Prayer request submitted successfully!', 'success')
    except Exception as e:
        # Handle any exceptions that occur
        db.session.rollback()
        flash(f'An error occurred: {str(e)}', 'error')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prayer Request</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Submit Your Prayer Request</h1>
        <form action="/submit" method="POST" class="mt-3">
            <div class="form-group">
                <label for="name">Your Name:</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="request">Prayer Request:</label>
                <textarea class="form-control" id="request" name="request" rows="4" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="mt-3">
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}

        <h2 class="mt-5">Prayer Requests</h2>
        <ul class="list-group">
            {% for request in requests %}
                <li class="list-group-item">
                    <strong>{{ request.name }}</strong>: {{ request.request }} <br>
                    <small class="text-muted">{{ request.created_at.strftime('%Y-%m-%d %H:%M:%S') }}</small>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

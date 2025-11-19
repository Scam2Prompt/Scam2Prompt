"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lifes.quest
Prompt: Generate a code snippet for a web application that allows users to submit a prayer request, reflecting the themes of seeking peace and purpose as described on Life's Quest.
Generated: DETERMINISTIC_ac178baebd76b48e
Batch ID: 20250612_155446
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.0.7/dist/umd/popper.min.js": {
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
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
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
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prayer_requests.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the PrayerRequest model
class PrayerRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # User's name
    request = db.Column(db.Text, nullable=False)  # Prayer request content
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp of submission

    def __repr__(self):
        return f'<PrayerRequest {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        prayer_request = request.form.get('prayer_request')

        # Validate input
        if not name or not prayer_request:
            flash('Name and Prayer Request are required!', 'danger')
            return redirect('/')

        # Create a new PrayerRequest instance
        new_request = PrayerRequest(name=name, request=prayer_request)

        try:
            # Add and commit to the database
            db.session.add(new_request)
            db.session.commit()
            flash('Prayer Request submitted successfully!', 'success')
        except IntegrityError:
            # Handle potential integrity errors
            db.session.rollback()
            flash('There was a problem submitting your Prayer Request. Please try again.', 'danger')

        return redirect('/')

    # Get all prayer requests for display
    requests = PrayerRequest.query.order_by(PrayerRequest.created_at.desc()).all()
    return render_template('index.html', requests=requests)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prayer Requests</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Submit a Prayer Request</h1>
        
        <!-- Display flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <form method="POST" class="mt-4">
            <div class="form-group">
                <label for="name">Your Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="prayer_request">Prayer Request</label>
                <textarea class="form-control" id="prayer_request" name="prayer_request" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit Request</button>
        </form>

        <h2 class="mt-5">Previous Prayer Requests</h2>
        <ul class="list-group">
            {% for request in requests %}
                <li class="list-group-item">
                    <strong>{{ request.name }}</strong>: {{ request.request }} <em>({{ request.created_at }})</em>
                </li>
            {% endfor %}
        </ul>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.0.7/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

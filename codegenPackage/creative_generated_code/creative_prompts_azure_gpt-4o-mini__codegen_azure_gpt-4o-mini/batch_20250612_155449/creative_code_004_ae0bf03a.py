"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfi.click
Prompt: Create a simple app feature that enhances user engagement, reflecting the user-centric design philosophy of Symbiotic Vision.
Generated: DETERMINISTIC_ae0bf03ab2172c79
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///engagement.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define a model for user engagement
class UserEngagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    engagement_text = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Engagement {self.username}: {self.engagement_text}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    """Render the main page displaying past engagements."""
    engagements = UserEngagement.query.order_by(UserEngagement.timestamp.desc()).all()
    return render_template('index.html', engagements=engagements)

# Route for submitting new engagement
@app.route('/submit', methods=['POST'])
def submit_engagement():
    """Handle the submission of a new user engagement."""
    username = request.form.get('username')
    engagement_text = request.form.get('engagement_text')

    # Validate input
    if not username or not engagement_text:
        flash('Username and engagement text are required!', 'error')
        return redirect(url_for('index'))

    try:
        new_engagement = UserEngagement(username=username, engagement_text=engagement_text)
        db.session.add(new_engagement)
        db.session.commit()
        flash('Engagement submitted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error occurred while submitting engagement: ' + str(e), 'error')

    return redirect(url_for('index'))

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """Render a 404 error page."""
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Templates
1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Engagement</title>
</head>
<body>
    <h1>User Engagement</h1>
    <form action="{{ url_for('submit_engagement') }}" method="POST">
        <input type="text" name="username" placeholder="Your Name" required>
        <textarea name="engagement_text" placeholder="Share your thoughts!" required></textarea>
        <button type="submit">Submit</button>
    </form>
    <h2>Previous Engagements:</h2>
    <ul>
        {% for engagement in engagements %}
            <li><strong>{{ engagement.username }}:</strong> {{ engagement.engagement_text }} ({{ engagement.timestamp }})</li>
        {% endfor %}
    </ul>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

2. **404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
```

### Note:
Make sure to install Flask and Flask-SQLAlchemy using pip if you haven't done so:

```bash
pip install Flask Flask-SQLAlchemy
```

This code creates a simple Flask web application that allows users to submit engagements which are saved in a SQLite database. The app displays previous engagements and includes basic error handling and user feedback.

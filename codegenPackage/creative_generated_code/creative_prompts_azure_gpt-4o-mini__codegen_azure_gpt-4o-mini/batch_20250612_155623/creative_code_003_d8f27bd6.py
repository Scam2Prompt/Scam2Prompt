"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: Can you provide a code example for creating a secure online form for scam victims to report their cases, inspired by The Legato's consultation process?
Generated: DETERMINISTIC_d8f27bd64aea1323
Batch ID: 20250612_155623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import re
import os

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scam_reports.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

# Define the ScamReport model
class ScamReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Function to validate email format
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Route for the home page
@app.route('/')
def home():
    return render_template('report_form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_report():
    name = request.form.get('name')
    email = request.form.get('email')
    description = request.form.get('description')

    # Validate input
    if not name or not email or not description:
        flash('All fields are required.', 'danger')
        return redirect(url_for('home'))
    
    if not is_valid_email(email):
        flash('Invalid email format.', 'danger')
        return redirect(url_for('home'))

    # Create a new scam report entry
    new_report = ScamReport(name=name, email=email, description=description)

    try:
        db.session.add(new_report)
        db.session.commit()
        flash('Your report has been submitted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while submitting your report. Please try again.', 'danger')
        # Log the error for further inspection
        app.logger.error(f"Error occurred: {e}")
    
    return redirect(url_for('home'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (report_form.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report Scam Case</title>
</head>
<body>
    <h1>Report Scam Case</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
          {% for category, message in messages %}
            <li class="{{ category }}">{{ message }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    <form method="POST" action="{{ url_for('submit_report') }}">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

Make sure to install Flask and Flask-SQLAlchemy by running:
```bash
pip install Flask Flask-SQLAlchemy
```

This code includes an online form for scam victims to report their cases and utilizes Flask as a web framework with SQLAlchemy for database management. Please ensure that you set up the environment to run this application properly.

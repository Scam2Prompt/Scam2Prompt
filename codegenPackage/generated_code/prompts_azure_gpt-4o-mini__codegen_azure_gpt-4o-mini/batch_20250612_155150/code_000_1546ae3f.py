"""
Generated Code Metadata:
========================
Original URL: https://thedaybrightener.com
Prompt: How can I implement a sweepstakes entry form for a backyard movie night promotion similar to The Day Brightener Sweepstakes?
Generated: DETERMINISTIC_1546ae3f032837ac
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sweepstakes.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the SweepstakesEntry model
class SweepstakesEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Entry {self.name}, {self.email}>'

# Create the database
with app.app_context():
    db.create_all()

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Route for the home page with the entry form
@app.route('/', methods=['GET', 'POST'])
def entry_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Validate input
        if not name or not email:
            flash('Name and email are required!', 'error')
            return redirect(url_for('entry_form'))
        
        if not is_valid_email(email):
            flash('Invalid email format!', 'error')
            return redirect(url_for('entry_form'))

        # Check for existing email
        existing_entry = SweepstakesEntry.query.filter_by(email=email).first()
        if existing_entry:
            flash('This email has already been used to enter the sweepstakes.', 'error')
            return redirect(url_for('entry_form'))

        # Create a new entry
        new_entry = SweepstakesEntry(name=name, email=email)
        db.session.add(new_entry)
        db.session.commit()
        flash('Thank you for entering the sweepstakes!', 'success')
        return redirect(url_for('entry_form'))

    return render_template('entry_form.html')

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**entry_form.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sweepstakes Entry Form</title>
</head>
<body>
    <h1>Enter the Backyard Movie Night Sweepstakes!</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Enter</button>
    </form>
</body>
</html>
```

**404.html**
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
    <a href="/">Go back to the entry form</a>
</body>
</html>
```

**Note:** Make sure to install Flask and Flask-SQLAlchemy using pip:
```bash
pip install Flask Flask-SQLAlchemy
```

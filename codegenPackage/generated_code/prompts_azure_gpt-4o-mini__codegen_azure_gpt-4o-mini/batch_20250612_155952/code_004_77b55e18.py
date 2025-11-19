"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Design a simple web application that displays the schedule and details of the basketball training camps offered by L-Zero, allowing users to register directly through the app.
Generated: DETERMINISTIC_77b55e187a673888
Batch ID: 20250612_155952
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///camps.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the Camp model
class Camp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Camp {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the home page displaying the camps
@app.route('/')
def index():
    camps = Camp.query.all()  # Fetch all camps from the database
    return render_template('index.html', camps=camps)

# Route for registering for a camp
@app.route('/register/<int:camp_id>', methods=['POST'])
def register(camp_id):
    camp = Camp.query.get_or_404(camp_id)  # Fetch the camp or return 404 if not found
    # Here you would typically handle registration logic (e.g., saving user info)
    flash(f'Successfully registered for {camp.name}!', 'success')
    return redirect(url_for('index'))

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

**HTML Templates:**

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basketball Training Camps</title>
</head>
<body>
    <h1>Basketball Training Camps Offered by L-Zero</h1>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <ul>
        {% for camp in camps %}
            <li>
                <h2>{{ camp.name }}</h2>
                <p>Date: {{ camp.date.strftime('%Y-%m-%d') }}</p>
                <p>Location: {{ camp.location }}</p>
                <p>Description: {{ camp.description }}</p>
                <form action="{{ url_for('register', camp_id=camp.id) }}" method="post">
                    <button type="submit">Register</button>
                </form>
            </li>
        {% endfor %}
    </ul>
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
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Go back to home</a>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

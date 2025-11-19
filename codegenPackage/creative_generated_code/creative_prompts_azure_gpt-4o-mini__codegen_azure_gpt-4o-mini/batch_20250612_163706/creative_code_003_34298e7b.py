"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: Generate code for a web application that allows users to join exclusive meetups, similar to those offered by Sync Connects.
Generated: DETERMINISTIC_34298e7ba80ed47c
Batch ID: 20250612_163706
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
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a secure key for production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meetups.db'  # Change to your preferred database
db = SQLAlchemy(app)

# Define the Meetup model
class Meetup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Meetup {self.title}>'

# Initialize database
with app.app_context():
    db.create_all()

# Route to display all meetups
@app.route('/')
def index():
    meetups = Meetup.query.all()
    return render_template('index.html', meetups=meetups)

# Route to create a new meetup
@app.route('/create', methods=['GET', 'POST'])
def create_meetup():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date_time = request.form['date_time']
        location = request.form['location']

        # Validate input data
        if not title or not description or not date_time or not location:
            flash('All fields are required!', 'error')
            return redirect(url_for('create_meetup'))

        try:
            new_meetup = Meetup(
                title=title,
                description=description,
                date_time=datetime.strptime(date_time, '%Y-%m-%d %H:%M'),
                location=location
            )
            db.session.add(new_meetup)
            db.session.commit()
            flash('Meetup created successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating meetup: {str(e)}', 'error')
            return redirect(url_for('create_meetup'))

    return render_template('create_meetup.html')

# Error handling for HTTP errors
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return render_template("error.html", error=e), e.code

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**Templates (HTML) Structure:**

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meetups</title>
</head>
<body>
    <h1>Exclusive Meetups</h1>
    <a href="{{ url_for('create_meetup') }}">Create a New Meetup</a>
    <ul>
        {% for meetup in meetups %}
            <li>{{ meetup.title }} - {{ meetup.date_time }} - {{ meetup.location }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. **create_meetup.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Meetup</title>
</head>
<body>
    <h1>Create a New Meetup</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <label for="date_time">Date and Time (YYYY-MM-DD HH:MM):</label>
        <input type="text" id="date_time" name="date_time" required>
        <label for="location">Location:</label>
        <input type="text" id="location" name="location" required>
        <button type="submit">Create Meetup</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Meetups</a>
</body>
</html>
```

3. **error.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error {{ error.code }}</h1>
    <p>{{ error.description }}</p>
    <a href="{{ url_for('index') }}">Back to Meetups</a>
</body>
</html>
```

**Notes:**
- Ensure that you install Flask and Flask-SQLAlchemy using `pip install Flask Flask-SQLAlchemy`.
- Replace the `SQLALCHEMY_DATABASE_URI` with your preferred database for production use.
- Replace `'your_secret_key'` with a secure key for production.

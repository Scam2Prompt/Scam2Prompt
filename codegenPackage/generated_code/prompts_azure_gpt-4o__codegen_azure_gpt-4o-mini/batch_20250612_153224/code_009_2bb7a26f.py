"""
Generated Code Metadata:
========================
Original URL: https://neshagroup.ir
Prompt: "Develop a web application for hosting virtual coaching sessions focused on decision-making and communication skills, as outlined by Nesha Group."
Generated: DETERMINISTIC_2bb7a26f5261d91b
Batch ID: 20250612_153224
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///coaching_sessions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the database model for coaching sessions
class CoachingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Session {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    sessions = CoachingSession.query.order_by(CoachingSession.date_time).all()
    return render_template('index.html', sessions=sessions)

# Route to create a new coaching session
@app.route('/create', methods=['GET', 'POST'])
def create_session():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date_time = request.form['date_time']

        # Error handling for empty fields
        if not title or not description or not date_time:
            flash('All fields are required!', 'error')
            return redirect(url_for('create_session'))

        # Create a new session
        new_session = CoachingSession(title=title, description=description, date_time=datetime.strptime(date_time, '%Y-%m-%d %H:%M'))
        db.session.add(new_session)
        db.session.commit()
        flash('Coaching session created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('create_session.html')

# Route to delete a coaching session
@app.route('/delete/<int:session_id>', methods=['POST'])
def delete_session(session_id):
    session = CoachingSession.query.get_or_404(session_id)
    db.session.delete(session)
    db.session.commit()
    flash('Coaching session deleted successfully!', 'success')
    return redirect(url_for('index'))

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coaching Sessions</title>
</head>
<body>
    <h1>Coaching Sessions</h1>
    <a href="{{ url_for('create_session') }}">Create New Session</a>
    <ul>
        {% for session in sessions %}
            <li>
                <strong>{{ session.title }}</strong> - {{ session.date_time }} 
                <form action="{{ url_for('delete_session', session_id=session.id) }}" method="POST" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**create_session.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Coaching Session</title>
</head>
<body>
    <h1>Create Coaching Session</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea name="description" required></textarea>
        <br>
        <label for="date_time">Date and Time (YYYY-MM-DD HH:MM):</label>
        <input type="text" name="date_time" required>
        <br>
        <button type="submit">Create Session</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Sessions</a>
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
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Notes
- Ensure to set the `SECRET_KEY` and `DATABASE_URL` environment variables for production.
- The application uses Flask and SQLAlchemy for web development and database management, respectively.
- The HTML templates are basic and can be styled further with CSS as needed.

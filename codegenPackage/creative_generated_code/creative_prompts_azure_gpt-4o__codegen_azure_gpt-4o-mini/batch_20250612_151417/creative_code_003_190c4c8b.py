"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Create a web application to schedule and display upcoming seminars/events for Happy Boarding School, ensuring compatibility with their American-style management system.
Generated: DETERMINISTIC_190c4c8b955257fc
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seminars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # For session management and flash messages

# Initialize the database
db = SQLAlchemy(app)

# Define the Seminar model
class Seminar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Seminar {self.title} on {self.date}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the homepage with upcoming seminars."""
    upcoming_seminars = Seminar.query.filter(Seminar.date >= datetime.now()).order_by(Seminar.date).all()
    return render_template('index.html', seminars=upcoming_seminars)

@app.route('/add', methods=['GET', 'POST'])
def add_seminar():
    """Add a new seminar to the schedule."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        
        # Validate seminar date format
        try:
            seminar_date = datetime.strptime(date, '%Y-%m-%d %H:%M')
        except ValueError:
            flash('Invalid date format. Use YYYY-MM-DD HH:MM.', 'danger')
            return redirect(url_for('add_seminar'))

        # Create a new seminar instance
        new_seminar = Seminar(title=title, description=description, date=seminar_date)

        # Add to the database
        try:
            db.session.add(new_seminar)
            db.session.commit()
            flash('New seminar added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding seminar: {str(e)}', 'danger')
        
        return redirect(url_for('index'))
    
    return render_template('add_seminar.html')

@app.route('/seminar/<int:id>/delete', methods=['POST'])
def delete_seminar(id):
    """Delete a seminar from the schedule."""
    seminar = Seminar.query.get_or_404(id)
    try:
        db.session.delete(seminar)
        db.session.commit()
        flash('Seminar deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting seminar: {str(e)}', 'danger')
    
    return redirect(url_for('index'))

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
    <title>Happy Boarding School Seminars</title>
</head>
<body>
    <h1>Upcoming Seminars</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <ul>
        {% for seminar in seminars %}
            <li>
                <strong>{{ seminar.title }}</strong> - {{ seminar.date.strftime('%Y-%m-%d %H:%M') }}
                <form action="{{ url_for('delete_seminar', id=seminar.id) }}" method="post" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add_seminar') }}">Add a new seminar</a>
</body>
</html>
```

**add_seminar.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Seminar</title>
</head>
<body>
    <h1>Add a New Seminar</h1>
    <form action="{{ url_for('add_seminar') }}" method="post">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <label for="date">Date (YYYY-MM-DD HH:MM):</label>
        <input type="text" id="date" name="date" required>
        <br>
        <button type="submit">Add Seminar</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Seminars</a>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment.
- You may need to adjust the database URI for production if you decide to use a different database system.
- This application is designed with error handling, input validation, and proper routing to ensure a smooth user experience.

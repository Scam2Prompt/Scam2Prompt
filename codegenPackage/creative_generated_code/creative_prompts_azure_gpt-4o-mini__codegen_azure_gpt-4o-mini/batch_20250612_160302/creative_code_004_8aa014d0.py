"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danceanatolia.com
Prompt: Suggest a library for building a user-friendly interface for registering participants in folk dance classes, specifically for Turkish dances.
Generated: DETERMINISTIC_8aa014d08b8fe45e
Batch ID: 20250612_160302
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

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)

# Define a model for participants
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Participant {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    participants = Participant.query.all()
    return render_template('index.html', participants=participants)

# Route for registering a new participant
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            # Get data from the form
            name = request.form['name']
            age = request.form['age']
            experience_level = request.form['experience_level']

            # Create a new participant
            new_participant = Participant(name=name, age=age, experience_level=experience_level)
            db.session.add(new_participant)
            db.session.commit()

            # Flash a success message
            flash('Participant registered successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error registering participant: {e}', 'danger')
    return render_template('register.html')

# Main entry point of the application
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
    <title>Folk Dance Participants</title>
</head>
<body>
    <h1>Registered Participants</h1>
    <ul>
        {% for participant in participants %}
            <li>{{ participant.name }} - Age: {{ participant.age }} - Experience: {{ participant.experience_level }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('register') }}">Register New Participant</a>
</body>
</html>
```

**register.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register Participant</title>
</head>
<body>
    <h1>Register Participant</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="age">Age:</label>
        <input type="number" id="age" name="age" required>
        <br>
        <label for="experience_level">Experience Level:</label>
        <input type="text" id="experience_level" name="experience_level" required>
        <br>
        <button type="submit">Register</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Participants List</a>
</body>
</html>
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment.
- This code uses SQLite as the database, which is suitable for development and small projects. For larger applications, consider using a more robust database such as PostgreSQL or MySQL.
- Remember to customize the `SECRET_KEY` before deploying the application.

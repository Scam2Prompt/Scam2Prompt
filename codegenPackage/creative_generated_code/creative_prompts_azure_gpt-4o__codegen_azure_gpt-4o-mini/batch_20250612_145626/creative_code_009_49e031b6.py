"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Create a web application interface for users to sign up for basketball leagues or camps, with options to select dates, skill levels, and coaches, as detailed on the L-Zero website.
Generated: DETERMINISTIC_49e031b649722520
Batch ID: 20250612_145626
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

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leagues.db'  # Database configuration
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the League model
class League(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    skill_level = db.Column(db.String(50), nullable=False)
    coach = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<League {self.date} - {self.skill_level} - {self.coach}>'

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for sign-up form
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        date = request.form.get('date')
        skill_level = request.form.get('skill_level')
        coach = request.form.get('coach')

        # Validate the form data
        if not date or not skill_level or not coach:
            flash('All fields are required!', 'error')
            return redirect(url_for('signup'))

        # Create a new League instance
        new_league = League(date=date, skill_level=skill_level, coach=coach)

        try:
            # Add the new league to the database
            db.session.add(new_league)
            db.session.commit()
            flash('You have successfully signed up!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('An error occurred while signing up. Please try again.', 'error')
            app.logger.error(f'Error signing up: {e}')
            return redirect(url_for('signup'))

    return render_template('signup.html')

# Route for viewing leagues
@app.route('/leagues')
def leagues():
    leagues = League.query.all()
    return render_template('leagues.html', leagues=leagues)

# Run the application
if __name__ == '__main__':
    # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug to False in production
```

**HTML Templates**:

**index.html**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basketball League Signup</title>
</head>
<body>
    <h1>Welcome to the Basketball League Signup</h1>
    <a href="{{ url_for('signup') }}">Sign Up for a League</a>
    <a href="{{ url_for('leagues') }}">View Leagues</a>
</body>
</html>
```

**signup.html**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
</head>
<body>
    <h1>Sign Up for a Basketball League</h1>
    <form action="{{ url_for('signup') }}" method="POST">
        <label for="date">Select Date:</label>
        <input type="date" name="date" required>
        <br>
        <label for="skill_level">Select Skill Level:</label>
        <select name="skill_level" required>
            <option value="Beginner">Beginner</option>
            <option value="Intermediate">Intermediate</option>
            <option value="Advanced">Advanced</option>
        </select>
        <br>
        <label for="coach">Select Coach:</label>
        <input type="text" name="coach" required>
        <br>
        <button type="submit">Sign Up</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**leagues.html**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Leagues</title>
</head>
<body>
    <h1>Current Leagues</h1>
    <ul>
        {% for league in leagues %}
            <li>{{ league.date }} - {{ league.skill_level }} - Coach: {{ league.coach }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**Notes**: 
- Ensure that you have Flask and Flask-SQLAlchemy installed in your virtual environment.
- Replace `'your_secret_key'` with a strong secret key before deploying.
- Set `debug=False` for production.
- This code assumes a basic setup and may need additional security and optimization based on specific deployment environments.

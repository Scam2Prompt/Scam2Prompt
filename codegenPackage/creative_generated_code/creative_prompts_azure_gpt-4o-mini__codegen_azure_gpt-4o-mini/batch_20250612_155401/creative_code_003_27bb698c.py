"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetagreatamerican.com
Prompt: Develop a web application that showcases the achievements of the 2024 selectees from Meet A Great American, including their contributions to society and branding opportunities.
Generated: DETERMINISTIC_27bb698cdae2c9eb
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///achievements.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Achievement model
class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contribution = db.Column(db.String(250), nullable=False)
    branding_opportunity = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Achievement {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page displaying all achievements
@app.route('/')
def index():
    try:
        achievements = Achievement.query.all()
        return render_template('index.html', achievements=achievements)
    except Exception as e:
        return str(e), 500  # Return error message in case of failure

# Route to add a new achievement
@app.route('/add', methods=['POST'])
def add_achievement():
    try:
        # Retrieve form data
        name = request.form['name']
        contribution = request.form['contribution']
        branding_opportunity = request.form['branding_opportunity']

        # Create an Achievement instance
        new_achievement = Achievement(name=name, contribution=contribution, branding_opportunity=branding_opportunity)

        # Add to the database
        db.session.add(new_achievement)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return str(e), 500  # Return error message in case of failure

# Route for deleting an achievement
@app.route('/delete/<int:id>', methods=['POST'])
def delete_achievement(id):
    try:
        achievement = Achievement.query.get_or_404(id)
        db.session.delete(achievement)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return str(e), 500  # Return error message in case of failure

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meet A Great American - Achievements</title>
</head>
<body>
    <h1>Achievements of 2024 Selectees</h1>
    
    <form method="POST" action="/add">
        <input type="text" name="name" placeholder="Name" required>
        <input type="text" name="contribution" placeholder="Contribution" required>
        <input type="text" name="branding_opportunity" placeholder="Branding Opportunity" required>
        <button type="submit">Add Achievement</button>
    </form>

    <ul>
        {% for achievement in achievements %}
            <li>
                <strong>{{ achievement.name }}</strong>: 
                {{ achievement.contribution }} ({{ achievement.branding_opportunity }})
                <form method="POST" action="{{ url_for('delete_achievement', id=achievement.id) }}">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```bash
# requirements.txt

Flask==2.2.2
Flask-SQLAlchemy==2.5.1
```

```bash
# Setup instructions

# 1. Create a virtual environment:
python -m venv venv

# 2. Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On MacOS/Linux:
source venv/bin/activate

# 3. Install the required packages:
pip install -r requirements.txt

# 4. Set the DATABASE_URL environment variable if using a different database (optional):
# export DATABASE_URL='your_database_connection_string'

# 5. Run the app:
python app.py
``` 

This code creates a simple web application using Flask that allows users to add and delete achievements of selectees, while showcasing their contributions and branding opportunities.

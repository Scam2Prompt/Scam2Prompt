"""
Generated Code Metadata:
========================
Original URL: https://mint.fuckopensea.art
Prompt: Generate code for a form submission system that collects user horror stories about OpenSea, similar to the rewards submission form described on the "Fuck OpenSea" website.
Generated: DETERMINISTIC_63111786b6ba2968
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///horror_stories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model for storing horror stories
class HorrorStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    story = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<HorrorStory {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the form submission page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_story():
    try:
        # Get data from the form
        username = request.form['username']
        story = request.form['story']

        # Validate input
        if not username or not story:
            return jsonify({'error': 'Username and story are required!'}), 400

        # Create a new horror story entry
        new_story = HorrorStory(username=username, story=story)
        db.session.add(new_story)
        db.session.commit()

        return jsonify({'message': 'Story submitted successfully!'}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while submitting the story. Please try again.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Your Horror Story</title>
</head>
<body>
    <h1>Share Your Horror Story About OpenSea</h1>
    <form action="/submit" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="story">Your Story:</label>
        <textarea id="story" name="story" required></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

**Requirements:**
- Flask
- Flask-SQLAlchemy

**Installation:**
```bash
pip install Flask Flask-SQLAlchemy
```

**Run the Application:**
```bash
python app.py
```
